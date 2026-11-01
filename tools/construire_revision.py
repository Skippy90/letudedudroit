"""Application de révision « L'étude du droit » : les sept formats pédagogiques, pour toutes les vidéos.

Usage : python tools/construire_revision.py
Entrées : scripts/<matiere>/<slug>/revision.json (contenu tiré des scripts audités, avec la ligne source),
curriculum/<matiere>.yaml (prérequis, pour le graphe des notions).
Sortie : revision/index.html, un seul fichier autonome (données incluses), prêt à publier.

Formats (docs/pedagogie/nouvelles-facons-d-etudier.md) :
1. « À vous d'abord » : la question à se poser avant de regarder ; 2. fiche vivante (cartes et rappels espacés) ;
3. machine à variantes ; 4. cas pratique en fondu ; 5. trouvez l'erreur ; 6. révision mélangée ; 7. graphe des notions.
"""

import json
import re
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
MATIERE = "droit-penal-general"


def prerequis() -> dict[str, list[str]]:
    texte = (RACINE / "curriculum" / f"{MATIERE}.yaml").read_text(encoding="utf-8")
    graphe = {}
    for ident, req in re.findall(r"- id: \"?(\d+)\"?.*?requiert: \[(.*?)\]", texte, re.S):
        graphe[f"{int(ident):02d}"] = [f"{int(x):02d}" for x in re.findall(r"\d+", req)]
    return graphe


def main() -> None:
    videos = []
    for f in sorted((RACINE / "scripts" / MATIERE).glob("*/revision.json")):
        d = json.loads(f.read_text(encoding="utf-8"))
        d["num"] = f.parent.name[:2]
        videos.append(d)
    donnees = {"videos": videos, "graphe": prerequis()}
    modele = (RACINE / "tools" / "revision_modele.html").read_text(encoding="utf-8")
    page = modele.replace("/*DONNEES*/null", json.dumps(donnees, ensure_ascii=False))
    sortie = RACINE / "revision" / "index.html"
    sortie.parent.mkdir(exist_ok=True)
    sortie.write_text(page, encoding="utf-8")
    n = sum(len(v.get("cartes", [])) for v in videos)
    print(f"Révision : {sortie} ({len(videos)} vidéos, {n} cartes)")


if __name__ == "__main__":
    main()
