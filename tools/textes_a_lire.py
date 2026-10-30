"""Textes à lire pour l'enregistrement des voix, en PDF.

Usage : python tools/textes_a_lire.py <sortie.pdf> <matiere>/<numero-slug> [<matiere>/<numero-slug> …]

Une section par vidéo : titre, puis chaque ligne de tts.txt numérotée comme dans le script
(les schémas sont calés sur ces numéros). Le PDF est produit par Chromium (Playwright,
déjà installé avec Remotion).
"""

import html
import re
import subprocess
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent

CSS = """@page{size:A4;margin:18mm 16mm}
body{font-family:Inter,Helvetica,Arial,sans-serif;font-size:15pt;line-height:1.45;color:#111}
section{page-break-after:always}h1{font-size:20pt;margin:0 0 4pt}.meta{color:#666;font-size:11pt;margin:0 0 14pt}
.bloc{display:flex;gap:12pt;padding:8pt 0;border-top:1px solid #ddd;break-inside:avoid}
.n{color:#b7791f;font-weight:700;min-width:22pt;text-align:right}.bloc p{margin:0 0 3pt}.intro li{margin-bottom:6pt}"""

CONSIGNES = """<section class=intro><h1>L'étude du droit — textes à lire</h1>
<ul><li>Chaque numéro correspond à une ligne du script : les schémas sont calés sur ces lignes.</li>
<li>Une phrase par ligne. Marquez une courte pause entre deux numéros.</li>
<li>Les articles sont écrits en toutes lettres : lisez-les tels quels.</li>
<li>Une phrase ratée ? Reprenez-la depuis son début : la dernière prise est gardée au montage.</li>
<li>Un fichier audio par vidéo. Le titre peut être lu au début : il est coupé au montage.</li>
<li>Si vous changez une phrase en lisant, notez-le : le texte de référence doit correspondre à l'audio.</li></ul></section>"""


def section(slug: str) -> str:
    dossier = RACINE / "scripts" / slug
    titre = (dossier / "script.md").read_text(encoding="utf-8").splitlines()[0].lstrip("# ")
    blocs = [b.strip().splitlines() for b in re.split(r"\n\s*\n", (dossier / "tts.txt").read_text(encoding="utf-8"))
             if b.strip()]
    mots = sum(len(l.split()) for b in blocs for l in b)
    s = f"<section><h1>{html.escape(titre)}</h1><p class=meta>{len(blocs)} lignes · {mots} mots · " \
        f"environ {round(mots / 150)} minutes</p>"
    for n, b in enumerate(blocs, 1):
        s += f"<div class=bloc><span class=n>{n}</span><div>" + "".join(f"<p>{html.escape(l)}</p>" for l in b) + "</div></div>"
    return s + "</section>"


def main(sortie: str, slugs: list[str]) -> None:
    page = Path(sortie).with_suffix(".html")
    page.write_text(f"<!doctype html><meta charset=utf-8><style>{CSS}</style>{CONSIGNES}"
                    + "".join(section(s) for s in slugs), encoding="utf-8")
    script = ("const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();"
              "const p=await b.newPage();await p.goto(process.argv[1]);"
              "await p.pdf({path:process.argv[2],format:'A4'});await b.close()})()")
    subprocess.run(["node", "-e", script, page.resolve().as_uri(), str(Path(sortie).resolve())], check=True)
    page.unlink()
    print(f"Textes à lire : {sortie}")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    main(sys.argv[1], sys.argv[2:])
