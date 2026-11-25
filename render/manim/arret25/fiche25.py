"""Fiche de cours de l'arrêt 25, en PDF : même mise en page que tools/fiche.py.

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
BGER = "https://search.bger.ch/ext/eurospider/live/fr/php/clir/http/index.php?lang=fr&type=show_document&highlight_docid=atf%3A%2F%2F"
SOURCES = [("ATF 146 I 145 (arrêt 1C_37/2019 du 5 mai 2020, en allemand), consid. 4 à 6", BGER + "146-I-145%3Ade"),
           ("Cour européenne des droits de l'homme, Grande Chambre, Verein KlimaSeniorinnen Schweiz et autres c. Suisse, 9 avril 2024, requête n° 53600/20", "https://www.echr.coe.int/fr/w/grand-chamber-rulings-in-the-climate-change-cases"),
           ("Art. 25a PA : décision sur des actes matériels (intérêt digne de protection ; droits ou obligations touchés)", "https://www.fedlex.admin.ch/eli/cc/1969/737_757_755/fr#art_25_a"),
           ("Art. 10 al. 1 et art. 13 al. 1 Cst. : droit à la vie ; respect de la vie privée et familiale", "https://www.fedlex.admin.ch/eli/cc/1999/404/fr#art_10"),
           ("Art. 6 par. 1 et art. 8 CEDH : accès à un tribunal ; respect de la vie privée et familiale", "https://www.echr.coe.int/fr/european-convention-on-human-rights"),
           ("Art. 3 al. 1 LCl : objectif de zéro net d'ici à 2050", "https://www.fedlex.admin.ch/eli/cc/2023/655/fr#art_3")]
SLUG = "arrets/25-atf-146-i-145"
blocs = [b.split("\n") for b in (RACINE / "scripts" / SLUG / "tts.txt").read_text(encoding="utf-8").strip().split("\n\n")]


def L(n, phrases=None):
    """Texte de la ligne n du script (ou seulement certaines phrases, numérotées à partir de 1)."""
    t = " ".join(p for i, p in enumerate(blocs[n - 1], 1) if phrases is None or i in phrases)
    for a, b in REMPL: t = t.replace(a, b).replace(a.capitalize(), b)
    return t


def para(*ts): return "".join(f"<p>{e(t)}</p>" for t in ts)


script = (RACINE / "scripts" / SLUG / "script.md").read_text(encoding="utf-8")
reponse = script.split("**Réponse attendue à la question finale**, pour la description : ")[1].strip().split("\n")[0]
reponse = reponse[0].upper() + reponse[1:]
symbole = (RACINE / "docs/marque/symbole.svg").read_text(encoding="utf-8")
corps = f"""<div class="bandeau">{symbole}<div><p>L’étude du droit · Les arrêts du Tribunal fédéral · Vidéo 25 · ATF 146 I 145 et Cour européenne des droits de l’homme, 9 avril 2024</p><h1>Les Aînées pour le climat : du Tribunal fédéral à Strasbourg</h1></div></div>
<div class="corps">
<h2>Les faits</h2>{para(L(4) + " " + L(5), L(7) + " " + L(11, [2]), L(12, [2, 3]) + " " + L(13, [2, 3]))}
<h2>Le texte</h2>{para(L(15, [2, 3, 4]), L(16, [2, 3]) + " " + L(17, [2, 3, 4]))}
<h2>La réponse du Tribunal fédéral (5 mai 2020)</h2>{para(L(19, [3, 4]) + " " + L(20, [2]), L(21, [2, 3]) + " " + L(23, [1]), L(28, [2]) + " " + L(29, [2]), L(30) + " " + L(31, [2, 3]), L(33) + " " + L(34))}
<h2>La suite à Strasbourg (9 avril 2024)</h2>{para(L(38, [2, 3]) + " " + L(39, [2, 3]), L(40, [2]) + " " + L(41, [2, 3]), L(42, [2, 3]) + " " + L(43, [1, 3]))}
<h2>Le piège</h2>{para(L(46, [2]) + " " + L(47))}
<h2>À retenir</h2>{para(L(48, [2, 3]))}
<h2>À vous</h2><div class="question"><p>{e(L(49, [2, 3]))}</p><p><b>Réponse :</b> {e(reponse)}</p></div>
<h2>Arrêts et articles cités</h2>
<ul>{"".join(f'<li>{e(t)}<br><span class="lien">{e(u)}</span></li>' for t, u in SOURCES)}</ul>
<p class="pied">Lois vérifiées sur Fedlex, arrêt du Tribunal fédéral sur son site, arrêt de Strasbourg d’après les documents du greffe de la Cour. L’arrêt du Tribunal fédéral est en allemand : les passages sont rapportés en substance. Introduction pédagogique, qui ne remplace pas un conseil juridique. Contenu sous licence CC BY-SA 4.0 · L’étude du droit · Le droit suisse, une notion à la fois.</p>
</div>"""
cible = Path(sys.argv[1]) if len(sys.argv) > 1 else RACINE / "out" / "arrets--25-atf-146-i-145--fiche.pdf"
with tempfile.TemporaryDirectory() as tmp:
    p = Path(tmp) / "fiche.html"; p.write_text(f"<!doctype html><meta charset=utf-8><style>{CSS}body{{font-size:9pt}}</style>{corps}", encoding="utf-8")
    js = ("const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();const p=await b.newPage();await p.goto(process.argv[1]);"
          "await p.pdf({path:process.argv[2],format:'A4',printBackground:true});await b.close()})()")
    subprocess.run(["node", "-e", js, p.as_uri(), str(cible.resolve())], check=True)
print("Fiche :", cible)
