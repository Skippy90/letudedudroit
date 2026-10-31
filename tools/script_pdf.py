"""PDF de vérification d'une vidéo : le script, les sources citées et l'audit, pour une relecture juridique externe.

Usage : python tools/script_pdf.py <matiere>/<numero-slug> [sortie.pdf]

Contenu :
1. Le script (scripts/<slug>/script.md) : texte lu, ligne par ligne ; la colonne « À l'écran » est omise.
2. Les articles et arrêts cités, repris de la description (scripts/<slug>/publication.md).
3. L'audit (scripts/<slug>/audit.md) en annexe : ce que le script fait dire à chaque source, texte exact.
Sortie par défaut : out/<matiere>--<numero-slug>--verification.pdf. Rendu par Chromium (Playwright).
"""

import html
import re
import subprocess
import sys
import tempfile
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent

CSS = """@page{size:A4;margin:16mm 15mm}
body{font-family:Inter,Helvetica,Arial,sans-serif;font-size:10.5pt;line-height:1.45;color:#111}
h1{font-size:18pt;margin:0 0 4pt}h2{font-size:13pt;margin:16pt 0 6pt;border-bottom:1px solid #ccc;padding-bottom:3pt}
h3{font-size:11pt;margin:12pt 0 4pt}p{margin:0 0 6pt}.meta{color:#555;font-size:9.5pt}
.consigne{border:1px solid #b7791f;background:#fdf6e9;padding:8pt 10pt;margin:10pt 0;border-radius:4pt}
table{border-collapse:collapse;width:100%;margin:4pt 0 10pt;font-size:9.5pt}
th,td{border:1px solid #ddd;padding:4pt 6pt;vertical-align:top;text-align:left}th{background:#f3f3f3}
td.n{width:22pt;color:#b7791f;font-weight:700;text-align:right}
.sources p{margin:0 0 5pt}.sources a{color:#1a4f8b;word-break:break-all;font-size:8.5pt}
section{page-break-before:always}a{color:#1a4f8b}"""


def en_ligne(texte: str) -> str:
    """Markdown en ligne : liens, gras, italique, code."""
    t = html.escape(texte, quote=False)
    t = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', t)
    t = re.sub(r"\*\*([^*]+)\*\*", r"<b>\1</b>", t)
    t = re.sub(r"`([^`]+)`", r"<code>\1</code>", t)
    t = re.sub(r"(?<![\w*])\*([^*]+)\*(?![\w*])", r"<i>\1</i>", t)
    return t


def markdown_html(md: str, colonnes_omises=()) -> str:
    """Convertisseur minimal : titres, paragraphes, listes, tableaux (colonnes omises par leur en-tête)."""
    sortie, lignes, i = [], md.splitlines(), 0
    while i < len(lignes):
        l = lignes[i]
        if l.startswith("|"):
            bloc = []
            while i < len(lignes) and lignes[i].startswith("|"):
                bloc.append([c.strip() for c in lignes[i].strip().strip("|").split("|")])
                i += 1
            entete, corps = bloc[0], [r for r in bloc[2:]]
            garder = [k for k, c in enumerate(entete) if c not in colonnes_omises]
            s = "<table><tr>" + "".join(f"<th>{en_ligne(entete[k])}</th>" for k in garder) + "</tr>"
            for r in corps:
                s += "<tr>" + "".join(
                    f'<td class="n">{en_ligne(r[k])}</td>' if k == 0 and r[k].isdigit() else f"<td>{en_ligne(r[k]) if k < len(r) else ''}</td>"
                    for k in garder) + "</tr>"
            sortie.append(s + "</table>")
            continue
        if l.startswith("### "):
            sortie.append(f"<h3>{en_ligne(l[4:])}</h3>")
        elif l.startswith("## "):
            sortie.append(f"<h2>{en_ligne(l[3:])}</h2>")
        elif l.startswith("# "):
            sortie.append(f"<h1>{en_ligne(l[2:])}</h1>")
        elif re.match(r"\s*[-•] ", l):
            items = []
            while i < len(lignes) and re.match(r"\s*[-•] ", lignes[i]):
                items.append(f"<li>{en_ligne(re.sub(r'^\s*[-•] ', '', lignes[i]))}</li>")
                i += 1
            sortie.append("<ul>" + "".join(items) + "</ul>")
            continue
        elif l.strip():
            sortie.append(f"<p>{en_ligne(l)}</p>")
        i += 1
    return "\n".join(sortie)


def main(slug: str, sortie: str | None = None) -> None:
    dossier = RACINE / "scripts" / slug
    script = (dossier / "script.md").read_text(encoding="utf-8")
    audit = (dossier / "audit.md").read_text(encoding="utf-8")
    titre = script.splitlines()[0].lstrip("# ").strip()

    # Sources : la liste « Articles et arrêts cités » de la description, avec ses liens.
    sources = ""
    pub = dossier / "publication.md"
    if pub.exists():
        description = re.search(r"```text\n(.*?)```", pub.read_text(encoding="utf-8"), re.S)[1]
        bloc = description.split("\n\n")[1] if "\n\n" in description else ""
        items = re.findall(r"• (.+)\n  (\S+)", bloc)
        sources = "".join(f'<p>• {html.escape(t)}<br><a href="{u}">{html.escape(u)}</a></p>' for t, u in items)

    corps = f"""<h1>{html.escape(titre)}</h1>
<p class="meta">L'étude du droit · droit pénal suisse · document de vérification · {html.escape(slug)}</p>
<div class="consigne"><b>Objet du document.</b> Ce script est lu tel quel dans la vidéo. Merci de vérifier l'exactitude
juridique de chaque phrase au regard du droit suisse en vigueur : articles cités, arrêts du Tribunal fédéral, exemples et
réponse à la question finale. Signalez toute phrase inexacte, trop générale ou ambiguë, avec son numéro de ligne.
Les sources figurent en partie 2 ; l'audit en annexe donne, pour chaque source, ce que le script lui fait dire et le texte exact.</div>
<h2>1. Le script</h2>
{markdown_html("\n".join(script.splitlines()[1:]), colonnes_omises=("À l'écran",))}
<section><h2>2. Articles et arrêts cités</h2><div class="sources">{sources or "<p>Voir l'audit en annexe.</p>"}</div></section>
<section><h2>Annexe : audit des sources</h2>{markdown_html("\n".join(audit.splitlines()[1:]))}</section>"""

    cible = Path(sortie) if sortie else RACINE / "out" / (slug.replace("/", "--") + "--verification.pdf")
    cible.parent.mkdir(exist_ok=True)
    with tempfile.TemporaryDirectory() as tmp:
        page = Path(tmp) / "verification.html"
        page.write_text(f"<!doctype html><meta charset=utf-8><style>{CSS}</style>{corps}", encoding="utf-8")
        script_js = ("const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();"
                     "const p=await b.newPage();await p.goto(process.argv[1]);"
                     "await p.pdf({path:process.argv[2],format:'A4',printBackground:true});await b.close()})()")
        subprocess.run(["node", "-e", script_js, page.as_uri(), str(cible.resolve())], check=True)
    print(f"PDF de vérification : {cible}")


if __name__ == "__main__":
    if len(sys.argv) not in (2, 3):
        sys.exit(__doc__)
    main(sys.argv[1], sys.argv[2] if len(sys.argv) == 3 else None)
