"""Fiche de cours de l'ATF 129 I 232 (Zurich), en PDF : même mise en page que tools/fiche.py.

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
SOURCES = [("ATF 129 I 232 (arrêt 1P.1/2003 du 9 juillet 2003, en allemand), consid. 3 à 5", "https://www.bger.ch/ext/eurospider/live/de/php/clir/http/index.php?highlight_docid=BGE-129-I-232&lang=de&type=show_document"),
           ("Art. 29 al. 2 Cst. : droit d'être entendu (d'où l'obligation de motiver, selon la jurisprudence)", "https://www.fedlex.admin.ch/eli/cc/1999/404/fr#art_29"),
           ("Art. 8 al. 2 Cst. : interdiction de la discrimination, notamment du fait de l'origine", "https://www.fedlex.admin.ch/eli/cc/1999/404/fr#art_8"),
           ("Art. 35 al. 2 Cst. : quiconque assume une tâche de l'État respecte les droits fondamentaux", "https://www.fedlex.admin.ch/eli/cc/1999/404/fr#art_35"),
           ("Art. 34 al. 2 Cst. : libre formation de l'opinion, expression fidèle et sûre de la volonté", "https://www.fedlex.admin.ch/eli/cc/1999/404/fr#art_34"),
           ("Art. 13 Cst. : protection de la sphère privée et des données personnelles", "https://www.fedlex.admin.ch/eli/cc/1999/404/fr#art_13"),
           ("Art. 15 à 17 LN : procédure cantonale, obligation de motiver, protection de la sphère privée", "https://www.fedlex.admin.ch/eli/cc/2016/404/fr#art_15")]
SLUG = "arrets/atf-129-i-232-zurich"
blocs = [b.split("\n") for b in (RACINE / "scripts" / SLUG / "tts.txt").read_text(encoding="utf-8").strip().split("\n\n")]


def L(n, phrases=None):
    """Texte de la ligne n du script (ou seulement certaines phrases, numérotées à partir de 1)."""
    t = " ".join(p for i, p in enumerate(blocs[n - 1], 1) if phrases is None or i in phrases)
    for a, b in REMPL: t = t.replace(a, b).replace(a.capitalize(), b)
    return t


def para(*ts): return "".join(f"<p>{e(t)}</p>" for t in ts)


reponse = "Parce que personne ne connaît les raisons réelles des votants : le vote est secret et aucun électeur ne s'explique. Une autorité qui écrirait des motifs après coup ne ferait que supposer. Le candidat ne pourrait pas comprendre le refus, et un juge ne pourrait pas vérifier qu'il n'est pas discriminatoire."
symbole = (RACINE / "docs/marque/symbole.svg").read_text(encoding="utf-8")
corps = f"""<div class="bandeau">{symbole}<div><p>L’étude du droit · Les arrêts du Tribunal fédéral · ATF 129 I 232 · 9 juillet 2003</p><h1>Zurich : le peuple peut-il choisir qui devient suisse ?</h1></div></div>
<div class="corps">
<h2>Les faits</h2>{para(L(4) + " " + L(5), L(6), L(8) + " " + L(9, [2]) + " " + L(10, [2]) + " " + L(11))}
<h2>La question</h2>{para(L(12) + " " + L(13))}
<h2>Premier problème : la motivation</h2>{para(L(16, [2]) + " " + L(17, [2]) + " " + L(18, [2]), L(19) + " " + L(22) + " " + L(23), L(25, [1]) + " " + L(26, [2]) + " " + L(28, [2, 3]), L(30))}
<h2>Second problème : l'information et la sphère privée</h2>{para(L(32) + " " + L(33), L(34) + " " + L(35), L(36, [2]) + " " + L(37, [1]) + " " + L(39))}
<h2>La décision et sa portée</h2>{para(L(40), L(42) + " " + L(43))}
<h2>Le piège</h2>{para(L(41))}
<h2>À retenir</h2>{para(L(44))}
<h2>À vous</h2><div class="question"><p>{e(L(45, [1]))}</p><p><b>Réponse :</b> {e(reponse)}</p></div>
<h2>Arrêt et articles cités</h2>
<ul>{"".join(f'<li>{e(t)}<br><span class="lien">{e(u)}</span></li>' for t, u in SOURCES)}</ul>
<p class="pied">Lois vérifiées sur Fedlex le 24 novembre 2026. L’arrêt est en allemand : les passages sont rapportés en substance. La procédure d’invalidation décrite relève du droit zurichois de l’époque. Introduction pédagogique, qui ne remplace pas un conseil juridique. Contenu sous licence CC BY-SA 4.0 · L’étude du droit · Le droit suisse, une notion à la fois.</p>
</div>"""
cible = Path(sys.argv[1]) if len(sys.argv) > 1 else RACINE / "out" / "arrets--atf-129-i-232-zurich--fiche.pdf"
with tempfile.TemporaryDirectory() as tmp:
    p = Path(tmp) / "fiche.html"; p.write_text(f"<!doctype html><meta charset=utf-8><style>{CSS}body{{font-size:9pt}}</style>{corps}", encoding="utf-8")
    js = ("const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();const p=await b.newPage();await p.goto(process.argv[1]);"
          "await p.pdf({path:process.argv[2],format:'A4',printBackground:true});await b.close()})()")
    subprocess.run(["node", "-e", js, p.as_uri(), str(cible.resolve())], check=True)
print("Fiche :", cible)
