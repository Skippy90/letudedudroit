"""Miniature YouTube d'une vidéo (1280 × 720), au gabarit de la chaîne.

Usage : python tools/miniature.py <matiere>/<numero-slug> <seconde> [sortie.png]

- La question du titre (scripts/<slug>/script.md, première ligne) en grand, en haut à gauche ;
  son dernier mot en ambre. La suite du titre et la matière en dessous, plus petit.
- En dessous, l'image des schémas à la seconde donnée (render/manim/media/<slug>/schemas.mp4) :
  choisir un moment où la scène du cas est lisible (personnages, décor).
- Le symbole de la chaîne en bas à gauche.
Sortie par défaut : scripts/<slug>/miniature.png. Rendu par Chromium (Playwright).
"""

import base64
import html
import re
import subprocess
import sys
import tempfile
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
MATIERES = {"droit-penal-general": "Droit pénal suisse", "procedure-penale": "Procédure pénale suisse"}


def decouper_titre(ligne: str) -> tuple[str, str]:
    """« Vidéo 1 — Qu'est-ce qu'une infraction ? Les trois étages » → (question, suite)."""
    titre = re.sub(r"^#\s*Vidéo\s+\d+\s*[—-]\s*", "", ligne).strip()
    if "?" in titre:
        question, suite = titre.split("?", 1)
        return question.strip() + " ?", suite.strip(" .:—-")
    return titre, ""


def main(slug: str, seconde: float, sortie: str | None = None) -> None:
    dossier = RACINE / "scripts" / slug
    question, suite = decouper_titre((dossier / "script.md").read_text(encoding="utf-8").splitlines()[0])
    # Espace insécable devant « ? » (le dernier mot garde son point d'interrogation) ; apostrophes typographiques.
    mots = question.replace(" ?", "\u00a0?").replace("'", "\u2019").split(" ")
    dernier = mots.pop()
    matiere = MATIERES.get(slug.split("/")[0], "Droit suisse")
    sous_titre = " · ".join(x for x in (suite.replace("'", "\u2019"), matiere) if x)

    with tempfile.TemporaryDirectory() as tmp:
        image = Path(tmp) / "scene.png"
        subprocess.run(["ffmpeg", "-y", "-v", "error", "-ss", str(seconde), "-i",
                        str(RACINE / "render/manim/media" / slug / "schemas.mp4"), "-frames:v", "1", str(image)],
                       check=True)
        scene = base64.b64encode(image.read_bytes()).decode()
        # Le fond reprend le noir exact de l'image (l'encodage vidéo le décale un peu) : pas de cadre visible.
        pixel = subprocess.run(["ffmpeg", "-v", "error", "-i", str(image), "-vf", "crop=1:1:4:4", "-f", "rawvideo",
                                "-pix_fmt", "rgb24", "-"], capture_output=True, check=True).stdout
        fond = "#" + pixel[:3].hex()
        symbole = (RACINE / "docs/marque/symbole.svg").read_text(encoding="utf-8")
        page = Path(tmp) / "miniature.html"
        page.write_text(f"""<!doctype html><meta charset="utf-8"><style>
body{{margin:0;width:1280px;height:720px;background:{fond};overflow:hidden;font-family:Inter,sans-serif;position:relative}}
.scene{{position:absolute;left:250px;top:250px;width:1030px;height:470px;background:url(data:image/png;base64,{scene}) center 62%/1030px auto no-repeat}}
.titre{{position:absolute;left:56px;top:34px;width:1100px;color:#F2EFE6;font-weight:800;font-size:92px;line-height:1.02;letter-spacing:-2px;text-wrap:balance}}
.titre b{{color:#E3A52F;font-weight:800}}
.sous{{position:absolute;left:60px;color:#F2EFE6;opacity:.75;font-weight:600;font-size:32px}}
.symbole{{position:absolute;left:44px;bottom:36px;width:120px;height:120px}}
.symbole svg{{width:120px;height:120px}}
</style><div class="scene"></div><div class="titre" id="t">{html.escape(' '.join(mots))} <b>{html.escape(dernier)}</b></div>
<div class="sous" id="s">{html.escape(sous_titre)}</div><div class="symbole">{symbole}</div>
<script>const t=document.getElementById('t');document.getElementById('s').style.top=(t.offsetTop+t.offsetHeight+14)+'px'</script>""",
                        encoding="utf-8")
        cible = Path(sortie) if sortie else dossier / "miniature.png"
        script = ("const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();"
                  "const p=await b.newPage({viewport:{width:1280,height:720}});await p.goto(process.argv[1]);"
                  "await p.screenshot({path:process.argv[2]});await b.close()})()")
        subprocess.run(["node", "-e", script, page.as_uri(), str(cible.resolve())], check=True)
    print(f"Miniature : {cible}")


if __name__ == "__main__":
    if len(sys.argv) not in (3, 4):
        sys.exit(__doc__)
    main(sys.argv[1], float(sys.argv[2]), sys.argv[3] if len(sys.argv) == 4 else None)
