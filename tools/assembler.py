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
MATIERES = {"droit-penal-general": "Droit pénal général", "procedure-penale": "Procédure pénale", "arrets": "Les arrêts du Tribunal fédéral"}
DUREE_OUVERTURE, DUREE_FIN = 4, 6  # secondes, comme dans render/remotion/src/Video.tsx


# Texture de l'image (adoptée le 1er novembre 2026), sur les schémas seulement (l'ouverture et la fin gardent le
# rouge exact de la marque), avant les sous-titres pour qu'ils restent nets :
# halo doux autour des éléments clairs (blanc, rouge de la marque), vignette légère, grain fin animé.
# Les couleurs de la charte ne bougent pas (mélange en RVB). Grain à 3 : au-delà, le fichier explose (6 → 3,5 Go
# pour 7 min, le grain animé ne se compresse pas). TEXTURE=0 rend sans.
TEXTURE = (",format=gbrp,split[t1][t2];[t2]curves=all='0/0 0.6/0.03 1/1',gblur=sigma=16[t3];"
           "[t1][t3]blend=all_mode=screen:all_opacity=0.35,vignette=angle=PI/8,noise=alls=3:allf=t,format=yuv420p")

# Bruitages de l'ouverture, calés sur l'animation de render/remotion/src/Video.tsx : les trois barres
# traversent l'écran (0 s), les étages du logo s'empilent (0,55 s, puis toutes les 0,15 s), le titre arrive (1,3 s).
# Fabriqués en code (tools/bande_annonce.py) : aucune licence à gérer.
# Carte de fin : les étages du logo (0,2 s), le clic sur « S'abonner » (2,7 s).
REPERES_FIN = [("pop", 0.25), ("pop", 0.4), ("pop", 0.55), ("clic", 2.7)]
REPERES_OUVERTURE = [("glisse", 0.0), ("pop", 0.6), ("pop", 0.75), ("pop", 0.9), ("tombe", 1.35)]


def bruitages(travail: Path, debut_fin: float) -> Path:
    """Piste des bruitages : ouverture à 0 s, carte de fin à debut_fin."""
    import numpy as np
    import soundfile as sf
    from bande_annonce import FR, son
    piste = np.zeros(int((debut_fin + DUREE_FIN) * FR))
    for nom, t in REPERES_OUVERTURE + [(n, debut_fin + t) for n, t in REPERES_FIN]:
        x = son(nom)
        i = int(t * FR)
        piste[i:i + len(x)] += x[: len(piste) - i]
    sortie = travail / "bruitages.wav"
    sf.write(sortie, np.tanh(piste), FR)
    return sortie


def video_suivante(matiere: str, numero: int) -> str:
    """Titre de la vidéo suivante du curriculum, annoncé sur la carte de fin, si son script existe déjà."""
    fichier = RACINE / "curriculum" / f"{matiere}.yaml"
    if not fichier.exists():
        return ""
    entrees = re.findall(r'id:\s*"?(\d+)"?[^\n]*?(?:\n[^\n]*?)*?titre:\s*"([^"]+)"', fichier.read_text(encoding="utf-8"))
    for ident, titre in entrees:
        if int(ident) == numero + 1 and list((RACINE / "scripts" / matiere).glob(f"{ident}-*/script.md")):
            return titre
    return ""


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
        "suivante": video_suivante(matiere, int(m[1])),
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
    texture = os.environ.get("TEXTURE", "1") != "0"
    filtre_st = ""
    if incruster:
        ass = travail / "sous-titres.ass"
        subprocess.run([sys.executable, str(RACINE / "tools" / "sous_titres.py"), slug, str(ass),
                        str(DUREE_OUVERTURE)], check=True)
        filtre_st = f",subtitles={ass}"
    subprocess.run([
        "ffmpeg", "-y", "-v", "error",
        "-i", str(travail / "ouverture.mp4"), "-i", str(schemas), "-i", str(travail / "fin.mp4"),
        "-i", str(voix / "narration.wav"), "-i", str(bruitages(travail, DUREE_OUVERTURE + timings["duree"])),
        "-filter_complex",
        "[0:v]setsar=1,fps=30[a];"
        f"[1:v]setsar=1,fps=30{TEXTURE if texture else ''}[b];[2:v]setsar=1,fps=30[c];"
        f"[a][b][c]concat=n=3:v=1:a=0{filtre_st}[v];[3:a]adelay={delai}:all=1,apad[n];"
        "[4:a]volume=0.45,apad[o];[n][o]amix=inputs=2:normalize=0[s]",
        "-map", "[v]", "-map", "[s]", "-t", f"{duree:.3f}",
        "-c:v", "libx264", "-crf", "18", "-preset", "medium", "-pix_fmt", "yuv420p",
        "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", str(sortie),
    ], check=True)
    print(f"Vidéo : {sortie} ({duree:.1f} s)")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    main(sys.argv[1])
