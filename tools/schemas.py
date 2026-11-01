"""Schémas-résumés des vidéos : PDF A4 imprimable, image pour les fiches et l'application, carrousel carré.

Usage : python tools/schemas.py [<matiere>/<numero-slug> …]   (sans argument : toutes les vidéos qui ont un schema.json)
Entrée : scripts/<slug>/schema.json (contenu tiré du script audité, source à chaque élément ; voir docs/pedagogie).
Sorties : out/schemas/<numero-slug>.pdf (A4), out/schemas/<numero-slug>.png (aperçu pour la fiche et l'application),
out/schemas/carrousels/<numero-slug>-NN.png (1080 × 1080, réseaux sociaux).
Rendu par Chromium (Playwright). Formats de panneaux : arbre, echelle, etages, conditions, frise.
"""

import html
import re
import json
import subprocess
import sys
import tempfile
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
e = html.escape
COULEURS = {"vert": "#3E9C6C", "gris": "#6B7280", "ambre": "#D9951C", "rouge": "#DA291C"}
SYMBOLE = (RACINE / "docs/marque/symbole.svg").read_text(encoding="utf-8")

CSS = """
*{box-sizing:border-box}body{margin:0;font-family:Inter,Helvetica,Arial,sans-serif;-webkit-print-color-adjust:exact;print-color-adjust:exact}
.clair{--fond:#FFFFFF;--texte:#151515;--doux:#5C5C5C;--trait:#E2DED6;--surface:#F6F3EE}
.sombre{--fond:#0B0B0B;--texte:#F2EFE6;--doux:#A9A49A;--trait:#2E2E33;--surface:#18181B}
.page{background:var(--fond);color:var(--texte)}
.bandeau{background:#DA291C;color:#fff;display:flex;gap:14px;align-items:center}
.bandeau svg{flex:none}.bandeau p{margin:0;font-weight:700;opacity:.92}.bandeau h1{margin:2px 0 0;font-weight:800;line-height:1.08}
h2{margin:0 0 10px;font-size:15pt;font-weight:800}
.src{color:var(--doux);font-size:.72em;font-family:ui-monospace,Menlo,monospace}
.panneau{display:grid;gap:8px}
.q{border:2px solid var(--texte);border-radius:10px;padding:8px 12px;font-weight:700}
.branches{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin:6px 0 10px}
.branche{display:grid;gap:4px;align-content:start}.branche b{font-size:.78em;letter-spacing:.06em;text-transform:uppercase;color:var(--doux)}
.res{border-radius:10px;padding:7px 11px;color:#fff;font-weight:800}.res small{display:block;font-weight:500;opacity:.92}
.suite{color:var(--doux);font-weight:700}
.echelle{display:grid;gap:8px}.echelle .item,.etages .item,.frise .pt,.cond{border-left:8px solid var(--c);background:var(--surface);border-radius:8px;padding:8px 12px}
.item b,.pt b,.cond b{display:block}.sens{color:var(--doux);font-weight:700;font-size:.85em;text-transform:uppercase;letter-spacing:.05em}
.etages{display:flex;flex-direction:column-reverse;gap:6px}
.frise{display:grid;gap:8px;border-left:3px solid var(--trait);padding-left:12px;margin-left:6px}
.frise .pt{position:relative}.frise .pt::before{content:"";position:absolute;left:-23px;top:12px;width:13px;height:13px;border-radius:50%;background:var(--c)}
.conds{display:grid;gap:6px}.cond{--c:var(--texte)}.issues{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-top:6px}
.piege{border:2px solid #DA291C;border-radius:10px;padding:10px 14px;display:grid;gap:4px}
.piege s{color:var(--doux)}.piege strong{color:#DA291C;font-size:.78em;letter-spacing:.06em;text-transform:uppercase}
.retenir{background:var(--surface);border-radius:10px;padding:10px 14px;font-weight:700}
.pied{color:var(--doux);font-size:.72em;border-top:1px solid var(--trait);padding-top:6px}
.avert{border:1.5px solid #D9951C;color:#9A6A10;border-radius:8px;padding:6px 10px;font-size:.8em;font-weight:700}
.sombre .avert{color:#E3A52F}
"""


def pub(source):
    """Source affichée au public : les articles et arrêts, sans les renvois internes aux lignes du script."""
    t = re.sub(r"(?i)(r[ée]ponse attendue|lignes? [\d\s,età-]+)\s*(;|,)?\s*", "", source or "").strip(" ;,")
    return t


def coul(nom):
    return COULEURS.get(nom, COULEURS["gris"])


def panneau(p):
    t = p.get("type")
    h = [f"<div class='panneau'><h2>{e(p.get('titre', ''))}</h2>"]
    if t == "arbre":
        res = p.get("resultats", {})
        def branche(nom, b):
            if "resultat" in b:
                r = res.get(b["resultat"], {})
                return (f"<div class='branche'><b>{nom}</b><div class='res' style='background:{coul(r.get('couleur'))}'>{e(b['resultat'])}"
                        f"<small>{e(r.get('detail', ''))}</small></div><span class='src'>{e(pub(r.get('source', '')))}</span></div>")
            return f"<div class='branche'><b>{nom}</b><span class='suite'>↓ question {b.get('suite', 0) + 1}</span></div>"
        for i, q in enumerate(p.get("questions", [])):
            h.append(f"<div class='q'>{i + 1}. {e(q['q'])} <span class='src'>{e(pub(q.get('source', '')))}</span></div>")
            h.append(f"<div class='branches'>{branche('Oui', q.get('oui', {}))}{branche('Non', q.get('non', {}))}</div>")
    elif t in ("echelle", "etages"):
        if p.get("sens"):
            h.append(f"<div class='sens'>{e(p['sens'])}</div>")
        h.append(f"<div class='{'echelle' if t == 'echelle' else 'etages'}'>")
        for it in p.get("items", []):
            h.append(f"<div class='item' style='--c:{coul(it.get('couleur'))}'><b>{e(it['label'])}</b>{e(it.get('detail', ''))} "
                     f"<span class='src'>{e(pub(it.get('source', '')))}</span></div>")
        h.append("</div>")
    elif t == "conditions":
        h.append("<div class='conds'>")
        for i, c in enumerate(p.get("conditions", [])):
            h.append(f"<div class='cond'><b>☐ {e(c['label'])}</b>{e(c.get('detail', ''))} <span class='src'>{e(pub(c.get('source', '')))}</span></div>")
        a, s = p.get("alors", {}), p.get("sinon", {})
        h.append(f"</div><div class='issues'><div class='branche'><b>Toutes réunies</b><div class='res' style='background:{coul(a.get('couleur', 'vert'))}'>{e(a.get('label', ''))}</div><span class='src'>{e(pub(a.get('source', '')))}</span></div>"
                 f"<div class='branche'><b>Une seule manque</b><div class='res' style='background:{coul(s.get('couleur', 'gris'))}'>{e(s.get('label', ''))}</div><span class='src'>{e(pub(s.get('source', '')))}</span></div></div>")
    elif t == "frise":
        h.append("<div class='frise'>")
        for pt in p.get("points", []):
            h.append(f"<div class='pt' style='--c:{coul(pt.get('couleur'))}'><b>{e(pt['label'])}</b>{e(pt.get('detail', ''))} "
                     f"<span class='src'>{e(pub(pt.get('source', '')))}</span></div>")
        h.append("</div>")
    h.append("</div>")
    return "".join(h)


def bandeau(s, taille):
    return (f"<div class='bandeau' style='padding:{taille[0]}'>{SYMBOLE.replace('<svg ', f'<svg width=\"{taille[1]}\" height=\"{taille[1]}\" ', 1)}"
            f"<div><p>L'étude du droit · Droit pénal général · Vidéo {s['video']}</p><h1 style='font-size:{taille[2]}'>{e(s['titre'])}</h1></div></div>")


def piege(s):
    p = s.get("piege")
    return (f"<div class='piege'><strong>Le piège classique</strong><s>{e(p['faux'])}</s><span>{e(p['vrai'])} <span class='src'>{e(pub(p.get('source', '')))}</span></span></div>"
            if p else "")


def avert(s):
    return "<div class='avert'>Version provisoire : contenu en attente de la relecture juridique.</div>" if s.get("a_relire") else ""


def page_a4(s):
    corps = "".join(panneau(p) for p in s.get("panneaux", []))
    return (f"<meta charset='utf-8'><style>{CSS}@page{{size:A4;margin:0}}.page{{width:210mm;min-height:297mm;display:grid;align-content:start}}"
            f".corps{{padding:9mm 14mm 10mm;display:grid;gap:12px;font-size:10.5pt;line-height:1.4}}</style>"
            f"<div class='page clair'>{bandeau(s, ('12mm 14mm 9mm', 44, '22pt'))}<div class='corps'>{avert(s)}{corps}{piege(s)}"
            f"<div class='retenir'>À retenir : {e(s.get('a_retenir', ''))}</div>"
            f"<div class='pied'>Sources : articles vérifiés sur Fedlex, arrêts du Tribunal fédéral ; script et audit en accès libre sur GitHub. "
            f"Licence CC BY-SA 4.0. Introduction pédagogique, ne remplace pas un conseil juridique.</div></div></div>")


def diapos(s):
    """Carrousel 1080 × 1080 : couverture, un panneau par diapo, le piège, à retenir, invitation."""
    base = (f"<meta charset='utf-8'><style>{CSS}.page{{width:1080px;height:1080px;display:grid;align-content:start;overflow:hidden}}"
            ".corps{padding:56px 64px;display:grid;gap:18px;font-size:27px;line-height:1.35}h2{font-size:40px}"
            ".pied2{position:absolute;bottom:40px;left:64px;right:64px;display:flex;justify-content:space-between;color:var(--doux);font-size:22px;font-weight:700}</style>")
    n = s["video"]
    out = [base + f"<div class='page sombre' style='position:relative;background:#DA291C;color:#fff;align-content:center'>"
                  f"<div class='corps' style='gap:28px'>{SYMBOLE.replace('<svg ', '<svg width=\"110\" height=\"110\" ', 1)}"
                  f"<div style='font-size:76px;font-weight:900;line-height:1.05;letter-spacing:-1px'>{e(s.get('accroche', s['titre']))}</div>"
                  f"<div style='font-size:30px;font-weight:700;opacity:.9'>Le schéma en {len(s.get('panneaux', [])) + 2} images →</div></div></div>"]
    for p in s.get("panneaux", []):
        out.append(base + f"<div class='page sombre' style='position:relative'><div class='corps'>{avert(s)}{panneau(p)}</div>"
                          f"<div class='pied2'><span>L'étude du droit</span><span>Vidéo {n}</span></div></div>")
    out.append(base + f"<div class='page sombre' style='position:relative'><div class='corps'><h2>Attention</h2>{piege(s)}"
                      f"<div class='retenir'>À retenir : {e(s.get('a_retenir', ''))}</div></div>"
                      f"<div class='pied2'><span>L'étude du droit</span><span>Vidéo {n}</span></div></div>")
    out.append(base + f"<div class='page sombre' style='position:relative;align-content:center'><div class='corps' style='gap:26px;text-align:center;justify-items:center'>"
                      f"{SYMBOLE.replace('<svg ', '<svg width=\"120\" height=\"120\" ', 1)}"
                      f"<div style='font-size:52px;font-weight:900'>La vidéo complète</div>"
                      f"<div style='font-size:32px'>« {e(s['titre'])} »<br>sur la chaîne L'étude du droit</div>"
                      f"<div style='font-size:26px;color:var(--doux)'>Fiche du cours gratuite · articles vérifiés</div></div></div>")
    return out


def rendre(pages, cibles, pdf=None):
    with tempfile.TemporaryDirectory() as tmp:
        fichiers = []
        for i, h in enumerate(pages):
            f = Path(tmp) / f"p{i}.html"
            f.write_text(h, encoding="utf-8")
            fichiers.append(f.as_uri())
        js = ("const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();const a=JSON.parse(process.argv[1]);"
              "for(const [u,c,w,h,pdf] of a){const p=await b.newPage({viewport:{width:w,height:h}});await p.goto(u);await p.waitForTimeout(150);"
              "if(pdf){await p.pdf({path:pdf,format:'A4',printBackground:true});}"
              "await p.screenshot({path:c,fullPage:true});await p.close();}await b.close()})()")
        travaux = [[u, str(c), w, hh, str(pdf) if (pdf and i == 0) else ""] for i, (u, (c, w, hh)) in enumerate(zip(fichiers, cibles))]
        subprocess.run(["node", "-e", js, json.dumps(travaux)], check=True)


def main(slugs):
    sortie = RACINE / "out" / "schemas"
    (sortie / "carrousels").mkdir(parents=True, exist_ok=True)
    for slug in slugs:
        s = json.loads((RACINE / "scripts" / slug / "schema.json").read_text(encoding="utf-8"))
        nom = slug.split("/")[1]
        rendre([page_a4(s)], [(sortie / f"{nom}.png", 794, 1123)], pdf=sortie / f"{nom}.pdf")
        d = diapos(s)
        rendre(d, [(sortie / "carrousels" / f"{nom}-{i + 1:02d}.png", 1080, 1080) for i in range(len(d))])
        print(f"Schéma : {nom} (A4 + {len(d)} diapos)")


if __name__ == "__main__":
    args = sys.argv[1:] or sorted(str(p.parent.relative_to(RACINE / "scripts")) for p in (RACINE / "scripts").glob("*/*/schema.json"))
    main(args)
