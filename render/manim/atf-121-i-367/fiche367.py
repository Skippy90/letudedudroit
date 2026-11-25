"""Fiche de cours de l'ATF 121 I 367 (minimum vital), en PDF : même mise en page que tools/fiche.py.

Le texte enregistré ne suit pas le plan des scripts habituels ; les lignes sont donc choisies à la main. Rien n'est
rédigé ici : tout vient de tts.txt (chiffres remis en chiffres) et de la réponse à la question finale, déjà audités.
Usage : python fiche25.py [sortie.pdf]
"""
import ast, html, subprocess, sys, tempfile
from pathlib import Path
ICI = Path(__file__).resolve().parent
RACINE = next((p for p in ICI.parents if (p / "tools" / "fiche.py").exists()), Path("/home/claude/letudedudroit"))
sys.path.insert(0, str(RACINE / "tools"))
from fiche import CSS
_src = (ICI / "srt.py").read_text(encoding="utf-8")   # srt.py s'exécute à l'import : on n'en lit que la table des chiffres
REMPL = next(ast.literal_eval(n.value) for n in ast.parse(_src).body if isinstance(n, ast.Assign) and n.targets[0].id == "REMPL")
e = html.escape
SOURCES = [("ATF 121 I 367 (arrêt du 27 octobre 1995, IIe Cour de droit public, en allemand), consid. 2 et 3", "https://www.servat.unibe.ch/Dfr/bge/c1121367.html"),
           ("Art. 12 Cst. : droit d'obtenir de l'aide dans des situations de détresse", "https://www.fedlex.admin.ch/eli/cc/1999/404/fr#art_12")]
SLUG = "arrets/atf-121-i-367-minimum-vital"
blocs = [b.split("\n") for b in (RACINE / "scripts" / SLUG / "tts.txt").read_text(encoding="utf-8").strip().split("\n\n")]


def L(n, phrases=None):
    """Texte de la ligne n du script (ou seulement certaines phrases, numérotées à partir de 1)."""
    t = " ".join(p for i, p in enumerate(blocs[n - 1], 1) if phrases is None or i in phrases)
    for a, b in REMPL: t = t.replace(a, b).replace(a.capitalize(), b)
    return t


def para(*ts): return "".join(f"<p>{e(t)}</p>" for t in ts)


reponse = "Se mettre soi-même dans le besoin, même par sa faute, ne suffit pas : l'aide indispensable reste due (la loi bernoise de l'époque le disait expressément). Il n'y a abus que si le comportement vise uniquement à obtenir l'aide, par exemple refuser sciemment un emploi pour être assisté."
symbole = (RACINE / "docs/marque/symbole.svg").read_text(encoding="utf-8")
corps = f"""<div class="bandeau">{symbole}<div><p>L’étude du droit · Les arrêts du Tribunal fédéral · ATF 121 I 367 · 27 octobre 1995</p><h1>Le droit de survivre : des conditions minimales d’existence</h1></div></div>
<div class="corps">
<h2>Les faits</h2>{para(L(4) + " " + L(5) + " " + L(6), L(7) + " " + L(8, [2, 3]) + " " + L(9, [2]), L(10, [2, 3]) + " " + L(11) + " " + L(12))}
<h2>La question</h2>{para(L(15) + " " + L(16, [2]), L(17))}
<h2>Le raisonnement</h2>{para(L(18, [2]) + " " + L(19), L(20, [1]) + " " + L(21), L(23, [1]))}
<h2>Ce que le droit garantit, et ce qu’il ne garantit pas</h2>{para(L(24) + " " + L(25), L(26), L(28, [2]) + " " + L(29))}
<h2>L’application à l’affaire</h2>{para(L(30), L(32) + " " + L(33) + " " + L(35, [1]), L(36) + " " + L(37), L(38))}
<h2>Le piège</h2>{para(L(39, [1]) + " " + L(42))}
<h2>À retenir</h2>{para(L(40) + " " + L(41), L(43, [2, 3]))}
<h2>À vous</h2><div class="question"><p>{e(L(44, [1]))}</p><p><b>Réponse :</b> {e(reponse)}</p></div>
<h2>Arrêt et article cités</h2>
<ul>{"".join(f'<li>{e(t)}<br><span class="lien">{e(u)}</span></li>' for t, u in SOURCES)}</ul>
<p class="pied">Article 12 vérifié sur Fedlex le 25 novembre 2026 (état le 3 mars 2024). L’arrêt est en allemand : les passages sont rapportés en substance. La procédure, la Constitution bernoise de 1993 et la loi bernoise de 1961 sur l’assistance relèvent du droit bernois de l’époque. Introduction pédagogique, qui ne remplace pas un conseil juridique. Contenu sous licence CC BY-SA 4.0 · L’étude du droit · Le droit suisse, une notion à la fois.</p>
</div>"""
cible = Path(sys.argv[1]) if len(sys.argv) > 1 else RACINE / "out" / "arrets--atf-121-i-367-minimum-vital--fiche.pdf"
with tempfile.TemporaryDirectory() as tmp:
    p = Path(tmp) / "fiche.html"; p.write_text(f"<!doctype html><meta charset=utf-8><style>{CSS}body{{font-size:9pt}}</style>{corps}", encoding="utf-8")
    js = ("const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();const p=await b.newPage();await p.goto(process.argv[1]);"
          "await p.pdf({path:process.argv[2],format:'A4',printBackground:true});await b.close()})()")
    subprocess.run(["node", "-e", js, p.as_uri(), str(cible.resolve())], check=True)
print("Fiche :", cible)
