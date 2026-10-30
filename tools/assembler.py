"""Assemble la vidéo finale : ouverture et fin (Remotion), schémas Manim et narration (ffmpeg).

Usage : python tools/assembler.py <matiere>/<numero-slug>

Entrées : render/manim/media/<slug>/schemas.mp4, voice/<slug>/narration.wav,
voice/<slug>/timings.json, le titre de scripts/<slug>/script.md et voice/config.json.
Sortie : out/<matiere>--<numero-slug>.mp4
"""

import json
import os
import re
import subprocess
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
REMOTION = RACINE / "render" / "remotion"
NAVIGATEUR = "/opt/pw-browsers/chromium_headless_shell-1243/chrome-headless-shell-linux64/chrome-headless-shell"
MATIERES = {"droit-penal-general": "Droit pénal général", "procedure-penale": "Procédure pénale"}
DUREE_OUVERTURE, DUREE_FIN = 4, 6  # secondes, comme dans render/remotion/src/Video.tsx


def main(slug: str) -> None:
    matiere, _ = slug.split("/")
    prefixe = slug.replace("/", "--")
    entete = (RACINE / "scripts" / slug / "script.md").read_text(encoding="utf-8").splitlines()[0]
    m = re.match(r"#\s*Vidéo\s+(\d+)\s*[—-]\s*(.+)", entete)
    if not m:
        sys.exit(f"Titre introuvable dans la première ligne de script.md : {entete!r}")

    voix = RACINE / "voice" / slug
    timings = json.loads((voix / "timings.json").read_text(encoding="utf-8"))
    config_voix = json.loads((RACINE / "voice" / "config.json").read_text(encoding="utf-8"))
    schemas = RACINE / "render" / "manim" / "media" / slug / "schemas.mp4"

    travail = RACINE / "render" / "remotion" / "public" / prefixe  # non versionné
    travail.mkdir(parents=True, exist_ok=True)
    props = travail / "props.json"
    props.write_text(json.dumps({
        "titre": m[2].strip(),
        "matiere": MATIERES.get(matiere, matiere),
        "numero": int(m[1]),
        "narrationSynthetique": timings.get("source", config_voix["source"]) == "synthese",
    }, ensure_ascii=False), encoding="utf-8")

    # 1. Habillage : ouverture et carte de fin, rendues par Remotion (muettes).
    for composition in ("Ouverture", "Fin"):
        subprocess.run(["npx", "remotion", "render", "src/index.ts", composition,
                        str(travail / f"{composition.lower()}.mp4"), f"--props={props}",
                        f"--browser-executable={NAVIGATEUR}", "--codec=h264", "--crf=16", "--muted",
                        "--log=error"], cwd=REMOTION, check=True)

    # 2. Montage : ouverture + schémas + fin à la suite ; la narration démarre après l'ouverture.
    duree = DUREE_OUVERTURE + timings["duree"] + DUREE_FIN
    sortie = RACINE / "out" / f"{prefixe}.mp4"
    delai = DUREE_OUVERTURE * 1000
    # Sous-titres incrustés, calés mot à mot, décalés de la durée de l'ouverture.
    # SOUS_TITRES=0 pour une version sans sous-titres.
    incruster = os.environ.get("SOUS_TITRES", "1") != "0"
    filtre_st = ""
    if incruster:
        ass = travail / "sous-titres.ass"
        subprocess.run([sys.executable, str(RACINE / "tools" / "sous_titres.py"), slug, str(ass),
                        str(DUREE_OUVERTURE)], check=True)
        filtre_st = f",subtitles={ass}"
    subprocess.run([
        "ffmpeg", "-y", "-v", "error",
        "-i", str(travail / "ouverture.mp4"), "-i", str(schemas), "-i", str(travail / "fin.mp4"),
        "-i", str(voix / "narration.wav"),
        "-filter_complex",
        "[0:v]setsar=1,fps=30[a];[1:v]setsar=1,fps=30[b];[2:v]setsar=1,fps=30[c];"
        f"[a][b][c]concat=n=3:v=1:a=0{filtre_st}[v];[3:a]adelay={delai}:all=1,apad[s]",
        "-map", "[v]", "-map", "[s]", "-t", f"{duree:.3f}",
        "-c:v", "libx264", "-crf", "18", "-preset", "medium", "-pix_fmt", "yuv420p",
        "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", str(sortie),
    ], check=True)
    print(f"Vidéo : {sortie} ({duree:.1f} s)")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    main(sys.argv[1])
