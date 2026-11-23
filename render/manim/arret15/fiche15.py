"""Fiche de cours de l'arrêt 15, en PDF : même mise en page que tools/fiche.py.

Le texte enregistré ne suit pas le plan des scripts habituels (cas, piège, conclusion) ; l'outil général
assemble donc mal. Ici, on choisit les lignes du script à la main. Rien n'est rédigé : tout vient de tts.txt
(chiffres remis en chiffres) et de la réponse à la question finale, déjà audités.
Usage : python render/manim/arret15/fiche15.py [sortie.pdf]
"""
import html, subprocess, sys, tempfile
from pathlib import Path
RACINE = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(RACINE / "tools")); sys.path.insert(0, str(Path(__file__).resolve().parent))
from fiche import CSS
import ast
_src = (Path(__file__).resolve().parent / "srt.py").read_text(encoding="utf-8")   # srt.py s'exécute à l'import : on n'en lit que la table des chiffres
REMPL = next(ast.literal_eval(n.value) for n in ast.parse(_src).body if isinstance(n, ast.Assign) and n.targets[0].id == "REMPL")
e = html.escape
BGER = "https://search.bger.ch/ext/eurospider/live/fr/php/clir/http/index.php?lang=fr&type=show_document&highlight_docid=atf%3A%2F%2F"
SOURCES = [("ATF 129 I 217 (arrêt 1P.228/2002 du 9 juillet 2003), consid. 1.1, 2.2 à 2.4, 3 et 4", BGER + "129-I-217%3Afr"),
           ("ATF 129 I 232 (arrêt 1P.1/2003 du 9 juillet 2003), ville de Zurich : initiative invalidée", BGER + "129-I-232%3Afr"),
           ("Art. 8 al. 2 Cst. : nul ne doit subir de discrimination, notamment du fait de son origine", "https://www.fedlex.admin.ch/eli/cc/1999/404/fr#art_8"),
           ("Art. 29 al. 2 Cst. : les parties ont le droit d'être entendues", "https://www.fedlex.admin.ch/eli/cc/1999/404/fr#art_29"),
           ("Art. 34 al. 2 Cst. : libre formation de l'opinion des citoyens et expression fidèle et sûre de leur volonté", "https://www.fedlex.admin.ch/eli/cc/1999/404/fr#art_34"),
           ("Art. 35 al. 2 Cst. : quiconque assume une tâche de l'État est tenu de respecter les droits fondamentaux", "https://www.fedlex.admin.ch/eli/cc/1999/404/fr#art_35"),
           ("Art. 15 al. 2 et art. 16 LN : vote de l'assemblée communale possible ; tout rejet doit être motivé", "https://www.fedlex.admin.ch/eli/cc/2016/404/fr#art_15")]
SLUG = "arrets/15-atf-129-i-217"
blocs = [b.split("\n") for b in (RACINE / "scripts" / SLUG / "tts.txt").read_text(encoding="utf-8").strip().split("\n\n")]


def L(n, phrases=None):
    """Texte de la ligne n du script (ou seulement certaines phrases, numérotées à partir de 1)."""
    t = " ".join(p for i, p in enumerate(blocs[n - 1], 1) if phrases is None or i in phrases)
    for a, b in REMPL: t = t.replace(a, b).replace(a.capitalize(), b)
    return t


def para(*ts): return "".join(f"<p>{e(t)}</p>" for t in ts)


script = (RACINE / "scripts" / SLUG / "script.md").read_text(encoding="utf-8")
reponse = script.split("**Réponse attendue à la question finale**, pour la description : ")[1].strip().split("\n")[0]
symbole = (RACINE / "docs/marque/symbole.svg").read_text(encoding="utf-8")
corps = f"""<div class="bandeau">{symbole}<div><p>L’étude du droit · Les arrêts du Tribunal fédéral · Vidéo 15 · ATF 129 I 217</p><h1>Le peuple peut-il voter pour discriminer ?</h1></div></div>
<div class="corps">
<h2>Les faits</h2>{para(L(4), L(7) + " " + L(8, [2, 3]), L(9) + " " + L(10))}
<h2>Les deux questions</h2>{para(L(18, [2, 3]))}
<h2>La réponse du Tribunal fédéral</h2>{para(L(21, [2, 3]), L(22), L(23), L(24, [3, 4]) + " " + L(25, [1, 2]), L(32), L(33, [3, 4]) + " " + L(34, [1]), L(35))}
<h2>Le piège</h2>{para(L(41) + " " + L(42))}
<h2>À retenir</h2>{para(L(43, [2, 3, 4]), L(39, [2, 3]) + " " + L(40, [1, 2]))}
<h2>À vous</h2><div class="question"><p>{e(L(44, [2]))}</p><p><b>Réponse :</b> {e(reponse)}</p></div>
<h2>Articles et arrêts cités</h2>
<ul>{"".join(f'<li>{e(t)}<br><span class="lien">{e(u)}</span></li>' for t, u in SOURCES)}</ul>
<p class="pied">Lois vérifiées sur Fedlex, arrêts sur le site du Tribunal fédéral. Arrêt rendu en allemand : les passages sont rapportés en substance. Introduction pédagogique, qui ne remplace pas un conseil juridique. Contenu sous licence CC BY-SA 4.0 · L’étude du droit · Le droit suisse, une notion à la fois.</p>
</div>"""
cible = Path(sys.argv[1]) if len(sys.argv) > 1 else RACINE / "out" / "arrets--15-atf-129-i-217--fiche.pdf"
with tempfile.TemporaryDirectory() as tmp:
    p = Path(tmp) / "fiche.html"; p.write_text(f"<!doctype html><meta charset=utf-8><style>{CSS}body{{font-size:10pt}}</style>{corps}", encoding="utf-8")
    js = ("const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();const p=await b.newPage();await p.goto(process.argv[1]);"
          "await p.pdf({path:process.argv[2],format:'A4',printBackground:true});await b.close()})()")
    subprocess.run(["node", "-e", js, p.as_uri(), str(cible.resolve())], check=True)
print("Fiche :", cible)
