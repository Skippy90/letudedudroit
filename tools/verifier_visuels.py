"""Vérifie visuals.md avant un rendu : actions connues du moteur, moments existants dans tts.txt,
et une animation au moins pour chaque ligne du script.

Usage : python tools/verifier_visuels.py <matiere>/<numero-slug>
"""

import json
import os
import re
import shlex
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RACINE / "render" / "manim"))


def main(slug: str) -> None:
    os.environ.setdefault("SLUG", slug)
    import video  # le moteur Manim : la liste des actions vient de ses méthodes a_*
    actions = {m[2:].replace("_", "-") for m in dir(video.Schemas) if m.startswith("a_")} | {"scene-vide"}
    dossier = RACINE / "scripts" / slug
    blocs = [b.split("\n") for b in (dossier / "tts.txt").read_text(encoding="utf-8").strip().split("\n\n")]
    erreurs, couvertes = [], set()
    fichier_t = RACINE / "voice" / slug / "timings.json"
    timings = json.loads(fichier_t.read_text(encoding="utf-8")) if fichier_t.exists() else None
    for ligne in (dossier / "visuals.md").read_text(encoding="utf-8").splitlines():
        m = re.match(r"\|\s*(\d+)\.(\d+)(?:\+[\d.]+|@([\w'-]+))?\s*\|(.*)\|\s*$", ligne)
        if not m:
            continue
        n, p, mot = int(m[1]), int(m[2]), m[3]
        # Un moment calé sur un mot : le mot doit avoir été prononcé (narration enregistrée).
        if mot and timings and n <= len(timings["lignes"]) and p <= len(timings["lignes"][n - 1]["phrases"]):
            reconnus = [w["mot"] for w in timings["lignes"][n - 1]["phrases"][p - 1].get("mots", [])]
            if reconnus and mot.lower() not in reconnus:
                erreurs.append(f"{n}.{p}@{mot} : ce mot n'est pas dans la narration ({' '.join(reconnus)})")
        couvertes.add(n)
        if n > len(blocs) or p > len(blocs[n - 1]):
            erreurs.append(f"{n}.{p} : cette phrase n'existe pas dans tts.txt")
        for action in filter(str.strip, m[4].split(";")):
            try:
                nom = shlex.split(action)[0]
            except ValueError:
                erreurs.append(f"{n}.{p} : guillemets mal fermés dans « {action.strip()} »")
                continue
            if nom not in actions:
                erreurs.append(f"{n}.{p} : action inconnue « {nom} »")
    erreurs += [f"ligne {i} du script : aucun visuel" for i in range(1, len(blocs) + 1) if i not in couvertes]
    if erreurs:
        sys.exit("visuals.md :\n" + "\n".join(erreurs))
    print("visuals.md : OK")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    main(sys.argv[1])
