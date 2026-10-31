"""Fiche de cours d'une vidéo, en PDF (une à deux pages A4), aux couleurs de la marque.

Usage : python tools/fiche.py <matiere>/<numero-slug> [sortie.pdf]

Rien n'est rédigé ici : la fiche assemble des passages du script (le cas de départ, le piège classique,
la conclusion, la question finale et sa réponse) et la liste des articles et arrêts de la fiche de publication,
tous déjà audités. Sortie par défaut : out/<matiere>--<numero-slug>--fiche.pdf. Rendu par Chromium (Playwright).
"""

import html
import subprocess
import sys
import tempfile
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RACINE / "tools"))
e = html.escape

CSS = """@page{size:A4;margin:0}
body{margin:0;font-family:Inter,Helvetica,Arial,sans-serif;color:#141414;font-size:10.5pt;line-height:1.5}
.bandeau{background:#DA291C;color:#fff;padding:14mm 16mm 10mm;display:flex;gap:14px;align-items:center}
.bandeau svg{width:46px;height:46px;flex:none}.bandeau p{margin:0;font-weight:600;opacity:.9}
.bandeau h1{margin:2px 0 0;font-size:21pt;line-height:1.1;font-weight:800}
.corps{padding:8mm 16mm 12mm}h2{font-size:12pt;margin:14pt 0 5pt;color:#DA291C;text-transform:uppercase;letter-spacing:.06em}
p{margin:0 0 6pt}.question{border:1.5px solid #DA291C;border-radius:6px;padding:8pt 10pt}
ul{margin:0;padding-left:14pt}li{margin:0 0 5pt}a{color:#141414}.lien{font-size:8pt;color:#555;word-break:break-all}
.pied{font-size:8pt;color:#666;border-top:1px solid #ddd;margin-top:14pt;padding-top:6pt}"""


def main(slug: str, sortie: str | None = None) -> None:
    from construire_site import lire_script, lire_sources, MATIERES
    s = lire_script(slug)
    sources = lire_sources(slug)
    sections = s["sections"]
    cas = sections[0][1] if sections else []
    piege = next((l for nom, l in sections if "piège" in nom.lower()), [])
    fin = sections[-1][1] if sections else []
    k = next((i for i, (_, t) in enumerate(fin) if "question pour finir" in t.lower()), len(fin))
    retenir = fin[:k]
    # La question : de « Une question pour finir » à l'invitation à répondre en commentaire (exclue).
    question = " ".join(t for _, t in fin[k:]).replace("Une question pour finir.", "").split("Écrivez")[0].strip()

    def para(lignes):
        return "".join(f"<p>{e(t)}</p>" for _, t in lignes)

    symbole = (RACINE / "docs/marque/symbole.svg").read_text(encoding="utf-8")
    matiere = MATIERES.get(slug.split("/")[0], "Droit suisse")
    numero = slug.split("/")[1][:2].lstrip("0")
    corps = f"""<div class="bandeau">{symbole}<div><p>L’étude du droit · {e(matiere)} · Vidéo {numero}</p><h1>{e(s["titre"])}</h1></div></div>
<div class="corps">
<h2>Le cas</h2>{para(cas)}
{f"<h2>Le piège classique</h2>{para(piege)}" if piege else ""}
{f"<h2>À retenir</h2>{para(retenir)}" if retenir else ""}
{f'<h2>À vous</h2><div class="question"><p>{e(question)}</p><p><b>Réponse :</b> {e(s["reponse"])}</p></div>' if question else ""}
<h2>Articles et arrêts cités</h2>
<ul>{"".join(f'<li>{e(t)}<br><span class="lien">{e(u)}</span></li>' for t, u in sources)}</ul>
<p class="pied">Lois vérifiées sur Fedlex, arrêts sur le site du Tribunal fédéral. Introduction pédagogique, qui ne remplace pas un conseil juridique. Contenu sous licence CC BY-SA 4.0 · L’étude du droit · Le droit suisse, une notion à la fois.</p>
</div>"""
    cible = Path(sortie) if sortie else RACINE / "out" / (slug.replace("/", "--") + "--fiche.pdf")
    cible.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory() as tmp:
        p = Path(tmp) / "fiche.html"
        p.write_text(f"<!doctype html><meta charset=utf-8><style>{CSS}</style>{corps}", encoding="utf-8")
        js = ("const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();"
              "const p=await b.newPage();await p.goto(process.argv[1]);"
              "await p.pdf({path:process.argv[2],format:'A4',printBackground:true});await b.close()})()")
        subprocess.run(["node", "-e", js, p.as_uri(), str(cible.resolve())], check=True)
    print(f"Fiche : {cible}")


if __name__ == "__main__":
    if len(sys.argv) not in (2, 3):
        sys.exit(__doc__)
    main(sys.argv[1], sys.argv[2] if len(sys.argv) == 3 else None)
