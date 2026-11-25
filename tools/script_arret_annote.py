"""Script d'un grand arrêt, d'une seule source : script.md, tts.txt, PDF annoté et Word modifiable.

Usage : python tools/script_arret_annote.py arrets/<slug> [dossier de sortie des PDF et Word]

Source : scripts/arrets/<slug>/sequences.py (voir ATF 121 I 367 pour le modèle).
- « ‿ » entre deux mots = liaison à faire. Elle est mise en évidence dans le PDF et le Word (rouge, lettres soulignées),
  et retirée de script.md et de tts.txt.
- tts.txt : une phrase par ligne, nombres en toutes lettres (table VOIX) ; le script s'arrête s'il reste un chiffre.
- PDF : Chrome sans écran ; Word : bibliothèque docx (Node), tools/script_arret_docx.js.
"""
import html, importlib.util, json, re, subprocess, sys
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
slug = sys.argv[1]; D = RACINE / "scripts" / slug
SORTIE = Path(sys.argv[2]) if len(sys.argv) > 2 else RACINE / "out"; SORTIE.mkdir(parents=True, exist_ok=True)
spec = importlib.util.spec_from_file_location("sequences", D / "sequences.py"); q = importlib.util.module_from_spec(spec); spec.loader.exec_module(q)
net = lambda t: t.replace("‿", " ")
nom = q.REF.replace(" ", "_")

# --- script.md : le tableau des séquences est remplacé entre les deux repères, le reste du fichier est conservé
tab = []
bornes = [p[0] for p in q.PARTIES] + [len(q.S) + 1]
for (deb, titre), fin in zip(q.PARTIES, bornes[1:]):
    tab += [f"## {titre}", "", "| N° | Direction de voix | Texte à enregistrer |", "| --- | --- | --- |"]
    tab += [f"| {n} | **{e}** — {ton}. {d} | {net(t)} |" for n, e, ton, d, t in q.S if deb <= n < fin] + [""]
f = D / "script.md"; s = f.read_text(encoding="utf-8")
a, b = "<!-- SEQUENCES -->", "<!-- FIN SEQUENCES -->"
f.write_text(s[: s.index(a) + len(a)] + "\n\n" + "\n".join(tab) + s[s.index(b):], encoding="utf-8")

# --- tts.txt
blocs = []
for n, e, ton, d, t in q.S:
    v = net(t)
    for x, y in q.VOIX: v = v.replace(x, y)
    assert not re.search(r"\d", v), f"séquence {n} : il reste un chiffre dans le texte de voix : {v}"
    blocs.append("\n".join(p.strip() for p in re.split(r"(?<=[.?!])\s+", v) if p.strip()))
(D / "tts.txt").write_text("\n\n".join(blocs) + "\n", encoding="utf-8")

# --- liaisons : découpe en morceaux (texte, est_liaison)
def morceaux(t):
    out = []
    for i, p in enumerate(t.split("‿")):
        if i: out.append(("‿", "tie"))
        g = p[:1] if i else ""; d_ = p[-1:] if i < t.count("‿") else ""
        mil = p[len(g): len(p) - len(d_)] if d_ else p[len(g):]
        if g: out.append((g, "l"))
        if mil: out.append((mil, ""))
        if d_: out.append((d_, "l"))
    return out

# --- PDF
def cellule(t):
    return "".join(f'<span class="{c}">{html.escape(x)}</span>' if c else html.escape(x) for x, c in morceaux(t))
lignes = "".join(
    f'<tr class="{"m" if n in q.TEXTE_MODIFIE else ""}"><td class="g"><b class="n">{n:02d}</b> <b>{html.escape(e)}</b> <span class="ton">| {html.escape(ton)}</span>'
    f'<div class="d{" dm" if n in q.DIRECTION_MODIFIEE else ""}">{html.escape(d)}</div></td><td class="t">{n}. {cellule(t)}</td></tr>'
    for n, e, ton, d, t in q.S)
page = f"""<!doctype html><meta charset="utf-8"><style>
@page{{size:A4 landscape;margin:13mm 14mm 14mm}}
body{{font-family:Inter,Helvetica,Arial,sans-serif;font-size:12.5pt;line-height:1.5;color:#161616}}
.h{{text-align:right;font-size:8pt;letter-spacing:1.5px;color:#888}}
h1{{font-size:21pt;margin:6pt 0 2pt}}.st{{color:#555;font-size:10.5pt;margin-bottom:8pt}}
.mode{{border-left:4px solid #DA291C;background:#fbf3f1;padding:7pt 10pt;font-size:10pt;margin:8pt 0 12pt}}
table{{border-collapse:collapse;width:100%}}thead th{{font-size:8pt;letter-spacing:1.5px;color:#888;text-align:left;padding:4pt 8pt;border-bottom:1.5px solid #161616}}
tr{{page-break-inside:avoid}}td{{vertical-align:top;padding:8pt 8pt;border-bottom:1px solid #e3e3e3}}
td.g{{width:27%;font-size:9.5pt;line-height:1.35;color:#333}}.n{{color:#DA291C}}.ton{{color:#777}}.d{{margin-top:3pt;font-style:italic;color:#555}}
.dm{{color:#8a5a00}}tr.m td.t{{border-left:3px solid #E0A526;padding-left:9pt}}
.tie{{color:#DA291C;font-weight:700}}.l{{color:#DA291C;text-decoration:underline;text-decoration-thickness:1.5px;text-underline-offset:3px}}
h2{{font-size:13pt;margin:0 0 8pt;page-break-before:always}}li{{font-size:10pt;line-height:1.45;margin-bottom:5pt}}.dg{{font-size:10pt;margin-top:10pt}}
</style><div class="h">L’ÉTUDE DU DROIT / SCRIPT DE VOIX OFF · VERSION DÉFINITIVE</div>
<h1>{html.escape(q.TITRE)}</h1><div class="st">{html.escape(q.SOUS_TITRE)}</div>
<div class="mode"><b>Mode d’emploi.</b> Lire uniquement la colonne de droite. Les consignes en marge dirigent l’intention, le débit et les silences. Les numéros restent fixes pour le montage.<br>
<b>Liaisons.</b> Le signe <span class="tie">‿</span> et les deux lettres <span class="l">soulignées en rouge</span> marquent une liaison à faire : « <span>le</span><span class="l">s</span><span class="tie">‿</span><span class="l">a</span>utorités » se lit « lé-z-autorités ». Seules les liaisons obligatoires ou attendues en lecture soignée sont marquées ; ailleurs, lire naturellement.<br>
<b>Repères.</b> Trait ambre à gauche du texte : séquence corrigée après l’audit. Consigne en brun : consigne ajustée.</div>
<table><thead><tr><th>MARGE · DIRECTION VOCALE</th><th>TEXTE À ENREGISTRER</th></tr></thead>{lignes}</table>
<h2>Notes juridiques · Ne pas lire à l’antenne</h2><ul>{"".join(f"<li>{html.escape(x)}</li>" for x in q.NOTES)}</ul>
<div class="dg">{html.escape(q.DIRECTION_GENERALE)}</div>"""
h = SORTIE / f"{nom}_script_definitif.html"; h.write_text(page, encoding="utf-8")
pdf = SORTIE / f"{nom}_script_definitif_annote.pdf"
subprocess.run(["google-chrome", "--headless=new", "--no-sandbox", "--disable-gpu", "--no-pdf-header-footer", f"--print-to-pdf={pdf}", h.as_uri()], check=True, capture_output=True)
h.unlink()

# --- Word
donnees = {"titre": q.TITRE, "sous_titre": q.SOUS_TITRE, "notes": q.NOTES, "direction_generale": q.DIRECTION_GENERALE,
           "sequences": [{"n": n, "etiquette": e, "ton": ton, "direction": d, "morceaux": morceaux(t), "m": n in q.TEXTE_MODIFIE, "dm": n in q.DIRECTION_MODIFIEE} for n, e, ton, d, t in q.S]}
j = SORTIE / "_script.json"; j.write_text(json.dumps(donnees, ensure_ascii=False), encoding="utf-8")
docx = SORTIE / f"{nom}_script_definitif.docx"
subprocess.run(["node", str(RACINE / "tools" / "script_arret_docx.js"), str(j), str(docx)], check=True); j.unlink()
print(pdf, docx, sum(len(net(s[4]).split()) for s in q.S), "mots", sep="\n")
