"""Site de L'étude du droit : pages statiques générées à partir du dépôt.

Usage : python tools/construire_site.py [dossier de sortie] [--apercu]

Sources : site/site.json (réglages, vidéos en ligne, identifiants YouTube), curriculum/*.yaml (parcours),
scripts/<matiere>/<numero-slug>/ (script.md, publication.md, miniature.png). Sortie par défaut : site/public/.
Chaque vidéo marquée « en_ligne » reçoit sa page : la vidéo (lecteur YouTube chargé seulement au clic),
le cas, le script complet, les articles et arrêts cités avec leurs liens, la réponse à la question finale,
et la fiche de cours en PDF (tools/fiche.py). Aucun texte juridique n'est écrit ici : tout vient des scripts
et des fiches de publication, déjà audités.

--apercu : la page d'accueil est écrite sans en-tête HTML, pour un aperçu publié comme Artifact.
"""

import html
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RACINE / "tools"))
MATIERES = {"droit-penal-general": "Droit pénal général", "procedure-penale": "Procédure pénale"}
e = html.escape


# ----- lecture du dépôt -----

def lire_script(slug: str) -> dict:
    """Titre, sections (nom, [(numéro, texte lu)]) et réponse attendue du script."""
    texte = (RACINE / "scripts" / slug / "script.md").read_text(encoding="utf-8")
    titre = re.sub(r"^#\s*Vidéo\s+\d+\s*[—-]\s*", "", texte.splitlines()[0]).strip()
    sections, courante = [], None
    for ligne in texte.splitlines():
        if ligne.startswith("## "):
            courante = (ligne[3:].strip(), [])
            sections.append(courante)
        m = re.match(r"\|\s*(\d+)\s*\|\s*(.+?)\s*\|", ligne)
        if m and courante:
            courante[1].append((int(m[1]), m[2]))
    reponse = re.search(r"\*\*Réponse attendue à la question finale\*\*[^:]*:\s*(.+)", texte)
    return {"titre": titre, "sections": [s for s in sections if s[1]],
            "reponse": reponse[1].strip() if reponse else ""}


def lire_sources(slug: str) -> list[tuple[str, str]]:
    """Articles et arrêts cités, avec leur lien, tels que dans la description de la fiche de publication."""
    pub = RACINE / "scripts" / slug / "publication.md"
    if not pub.exists():
        return []
    description = re.search(r"```text\n(.*?)```", pub.read_text(encoding="utf-8"), re.S)[1]
    return re.findall(r"• (.+)\n  (\S+)", description)


def lire_curriculum() -> list[dict]:
    """Les matières et leurs vidéos (lecture simple du YAML du curriculum : id, slug, titre, notion)."""
    matieres = []
    for f in sorted((RACINE / "curriculum").glob("*.yaml")):
        videos, courante = [], None
        for ligne in f.read_text(encoding="utf-8").splitlines():
            m = re.match(r"\s*-\s*id:\s*(\S+)", ligne)
            if m:
                courante = {"id": m[1].strip("\"'")}
                videos.append(courante)
                continue
            m = re.match(r"\s+(slug|titre|notion|module):\s*(.+)", ligne)
            if m and courante is not None:
                courante[m[1]] = m[2].strip().strip("\"'")
        matieres.append({"matiere": f.stem, "videos": videos})
    return matieres


# ----- gabarit -----

SYMBOLE = (RACINE / "docs/marque/symbole.svg").read_text(encoding="utf-8")


def page(titre: str, corps: str, prof: int, description: str, apercu: bool = False) -> str:
    """Une page du site ; « prof » : profondeur du dossier, pour les liens relatifs."""
    r = "../" * prof
    tete = f"""<title>{e(titre)}</title>
<meta name="description" content="{e(description)}">
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;800;900&display=swap">
<link rel="stylesheet" href="{r}assets/style.css">"""
    entete = f"""<header class="entete"><div class="cadre">
<a class="marque" href="{r}index.html"><span class="pastille">{SYMBOLE}</span><span>L’étude du droit</span></a>
<nav><a href="{r}index.html#videos">Vidéos</a><a href="{r}parcours/index.html">Parcours</a><a href="{r}a-propos/index.html">À propos</a></nav>
</div></header>"""
    pied = f"""<footer class="pied"><div class="cadre">
<p><b>L’étude du droit</b> · Le droit suisse, une notion à la fois.</p>
<p>Contenu sous licence <a href="https://creativecommons.org/licenses/by-sa/4.0/deed.fr">CC BY-SA 4.0</a>. Les vidéos sont des introductions pédagogiques et ne remplacent pas un conseil juridique.</p>
<p><a href="{r}confidentialite/index.html">Protection des données</a> · <a href="{r}mentions/index.html">Mentions légales</a></p>
</div></footer>"""
    contenu = f"{entete}<main>{corps}</main>{pied}"
    if apercu:
        return tete + "\n" + contenu
    return f"<!doctype html>\n<html lang=\"fr\"><head><meta charset=\"utf-8\"><meta name=\"viewport\" content=\"width=device-width, initial-scale=1, viewport-fit=cover\">\n{tete}\n</head><body>{contenu}</body></html>\n"


def lecteur(youtube: str, miniature: str, titre: str) -> str:
    """La vidéo : la miniature, et un lien vers YouTube (aucun contenu de YouTube n'est chargé avant le clic)."""
    if youtube:
        return (f'<a class="lecteur" href="https://www.youtube.com/watch?v={e(youtube)}" rel="noopener">'
                f'<img src="{miniature}" alt="Miniature : {e(titre)}" width="1280" height="720">'
                f'<span class="lire">Regarder sur YouTube</span></a>')
    return (f'<div class="lecteur"><img src="{miniature}" alt="Miniature : {e(titre)}" width="1280" height="720">'
            f'<span class="lire bientot">Bientôt en ligne</span></div>')


def inscription(reglages: dict, prof: int) -> str:
    action = reglages["inscription"]["action"]
    r = "../" * prof
    ferme = "" if action else " disabled"
    return f"""<section class="inscription" id="fiches"><div class="cadre">
<div><p class="sur">Fiches de cours</p><h2>Recevoir la fiche de chaque vidéo</h2>
<p>Une page par notion : le cas, la règle, le piège classique, les articles et arrêts cités. Par e-mail, à chaque nouvelle vidéo.</p></div>
<form{f' action="{e(action)}" method="post"' if action else ''} class="formulaire">
<label for="courriel">Adresse e-mail</label>
<input id="courriel" name="email" type="email" autocomplete="email" required placeholder="prenom@exemple.ch"{ferme}>
<label class="accord"><input id="accord" name="accord" type="checkbox" required{ferme}><span>J’accepte de recevoir les fiches et les nouvelles vidéos par e-mail. Désinscription en un clic, à tout moment (<a href="{r}confidentialite/index.html">protection des données</a>).</span></label>
<button type="submit"{ferme}>{'Recevoir les fiches' if action else 'Inscriptions bientôt ouvertes'}</button>
</form></div></section>"""


# ----- pages -----

def carte(slug: str, info: dict, prof: int, numero: str) -> str:
    s = lire_script(slug)
    r = "../" * prof
    etat = "" if info.get("en_ligne") else '<span class="etat">Bientôt</span>'
    lien = f'{r}{slug}/index.html' if info.get("en_ligne") else None
    image = f'<img src="{r}{slug}/miniature.png" alt="" width="1280" height="720" loading="lazy">'
    corps = f'{image}<span class="num">Vidéo {numero}</span><h3>{e(s["titre"])}</h3>{etat}'
    return f'<a class="carte" href="{lien}">{corps}</a>' if lien else f'<div class="carte inactive">{corps}</div>'


def accueil(reglages: dict, apercu: bool) -> str:
    cartes = "".join(carte(slug, info, 0, slug.split("/")[1][:2].lstrip("0"))
                     for slug, info in reglages["videos"].items())
    corps = f"""<section class="une"><div class="cadre">
<p class="nom"><span>L’étude du droit</span></p>
<h1>Le droit suisse, <em>une notion à la fois.</em></h1>
<p class="chapeau">Des vidéos courtes qui partent d’un cas concret, posent la règle, montrent le piège classique et finissent par une question. Chaque article est vérifié sur Fedlex, chaque arrêt sur le site du Tribunal fédéral, et le script complet est en accès libre.</p>
<p class="liens"><a class="bouton" href="#videos">Voir les vidéos</a><a class="bouton second" href="#fiches">Recevoir les fiches</a></p>
</div></section>
<section class="videos" id="videos"><div class="cadre">
<p class="sur">Droit pénal général</p><h2>Les vidéos</h2>
<div class="grille">{cartes}</div></div></section>
<section class="methode"><div class="cadre">
<p class="sur">La méthode</p><h2>Comment une vidéo est construite</h2>
<ol class="etapes">
<li><b>Un cas concret.</b> Une histoire courte, avec des personnes et un geste.</li>
<li><b>La règle.</b> L’article du Code, lu et expliqué, avec la jurisprudence du Tribunal fédéral quand elle compte.</li>
<li><b>Le piège classique.</b> L’erreur que tout le monde fait, et pourquoi c’est faux.</li>
<li><b>Une question pour vous.</b> La réponse est dans la description et sur la page de la vidéo.</li>
</ol></div></section>
{inscription(reglages, 0)}"""
    return page("L’étude du droit", corps, 0, "Le droit suisse, une notion à la fois : vidéos, scripts et fiches de cours.", apercu)


def page_video(slug: str, info: dict, reglages: dict) -> str:
    s = lire_script(slug)
    sources = lire_sources(slug)
    matiere = MATIERES.get(slug.split("/")[0], "Droit suisse")
    numero = slug.split("/")[1][:2].lstrip("0")
    cas = s["sections"][0] if s["sections"] else ("", [])
    script = "".join(f'<h3>{e(nom)}</h3>' + "".join(f'<p><span class="n">{n}</span>{e(t)}</p>' for n, t in lignes)
                     for nom, lignes in s["sections"])
    liste = "".join(f'<li><a href="{e(u)}" rel="noopener">{e(t.split(" : ")[0])}</a>'
                    f'{" : " + e(t.split(" : ", 1)[1]) if " : " in t else ""}</li>' for t, u in sources)
    depot = f'{reglages["github"]}/tree/main/scripts/{slug}'
    corps = f"""<section class="video"><div class="cadre">
<p class="sur">{e(matiere)} · Vidéo {numero}</p><h1>{e(s["titre"])}</h1>
{lecteur(info.get("youtube", ""), "scene.jpg" if (RACINE / "render/manim/media" / slug / "schemas.mp4").exists() else "miniature.png", s["titre"])}
</div></section>
<section class="contenu"><div class="cadre colonnes">
<article>
<h2>{e(cas[0])}</h2>{"".join(f"<p>{e(t)}</p>" for _, t in cas[1])}
<details><summary>Lire le script complet</summary>{script}</details>
{f'<details class="reponse"><summary>Voir la réponse à la question finale</summary><p>{e(s["reponse"])}</p></details>' if s["reponse"] else ''}
</article>
<aside>
<div class="fiche"><p class="sur">Fiche de cours</p><p>Le cas, la règle, le piège et les sources sur une page.</p>
<a class="bouton" href="fiche.pdf">Télécharger la fiche (PDF)</a></div>
<h2>Articles et arrêts cités</h2><ul class="sources">{liste}</ul>
<p class="petit">Lois vérifiées sur Fedlex, arrêts sur le site du Tribunal fédéral. <a href="{e(depot)}" rel="noopener">Script, audit des sources et code</a>.</p>
</aside></div></section>
{inscription(reglages, 2)}"""
    return page(f"{s['titre']} · L’étude du droit", corps, 2, f"{s['titre']} : le cas, la règle, le piège, les articles cités.")


def page_parcours(reglages: dict) -> str:
    blocs = ""
    for m in lire_curriculum():
        lignes = ""
        for v in m["videos"]:
            slug = f'{m["matiere"]}/{v["id"].zfill(2)}-{v.get("slug", "")}'
            info = reglages["videos"].get(slug, {})
            titre = e(v.get("titre", ""))
            nom = f'<a href="../{slug}/index.html">{titre}</a>' if info.get("en_ligne") else titre
            etat = "En ligne" if info.get("en_ligne") else "En préparation"
            lignes += (f'<li><span class="num">{e(v["id"])}</span><div><b>{nom}</b><span>{e(v.get("notion", ""))}</span></div>'
                       f'<span class="etat{" actif" if info.get("en_ligne") else ""}">{etat}</span></li>')
        blocs += f'<h2>{e(MATIERES.get(m["matiere"], m["matiere"]))}</h2><ol class="parcours">{lignes}</ol>'
    corps = f"""<section class="contenu"><div class="cadre etroit">
<p class="sur">Parcours</p><h1>Les notions, dans l’ordre</h1>
<p class="chapeau">Chaque vidéo s’appuie sur les précédentes. Suivez-les dans l’ordre, ou reprenez une notion précise.</p>
{blocs}</div></section>"""
    return page("Parcours · L’étude du droit", corps, 1, "Les notions de droit pénal et de procédure pénale, dans l’ordre.")


def page_texte(titre: str, chapeau: str, html_corps: str, description: str) -> str:
    corps = f'<section class="contenu"><div class="cadre etroit"><h1>{e(titre)}</h1><p class="chapeau">{chapeau}</p>{html_corps}</div></section>'
    return page(f"{titre} · L’étude du droit", corps, 1, description)


A_PROPOS = """<h2>Le projet</h2>
<p>L’étude du droit explique le droit suisse une notion à la fois, pour les élèves, les apprentis, les étudiants de première année et toute personne curieuse. Les vidéos partent d’un cas, posent la règle, montrent le piège classique et finissent par une question.</p>
<h2>Des sources vérifiées</h2>
<p>Chaque article cité est vérifié dans sa version en vigueur sur Fedlex, et chaque arrêt sur le site du Tribunal fédéral. Pour chaque vidéo, un tableau d’audit relie chaque affirmation à sa source ; il est relu avant la publication. Le droit cantonal est signalé comme tel.</p>
<h2>Ouvert</h2>
<p>Les scripts, les audits et le code qui fabrique les vidéos sont publics. Les contenus sont sous licence CC BY-SA 4.0 : vous pouvez les réutiliser en citant « L’étude du droit » et en partageant dans les mêmes conditions. Le nom et le logo, eux, ne sont pas couverts par cette licence.</p>
<h2>Contact</h2>
<p>À VÉRIFIER : adresse de contact à indiquer.</p>"""

CONFIDENTIALITE = """<p class="alerte">Projet à relire et à compléter avant la mise en ligne (À VÉRIFIER : responsable du traitement, adresse, service d’envoi choisi).</p>
<h2>Qui traite vos données</h2>
<p>À VÉRIFIER : nom et adresse de la personne responsable du site L’étude du droit.</p>
<h2>Ce qui est collecté</h2>
<p>Si vous vous inscrivez pour recevoir les fiches : votre adresse e-mail et la date de votre consentement. Rien d’autre n’est demandé.</p>
<h2>Pourquoi</h2>
<p>Pour vous envoyer les fiches de cours et l’annonce des nouvelles vidéos. Votre adresse n’est ni vendue ni utilisée à d’autres fins.</p>
<h2>Où et combien de temps</h2>
<p>À VÉRIFIER : service d’envoi utilisé et pays où les données sont hébergées. Les données sont conservées jusqu’à votre désinscription.</p>
<h2>Vidéos YouTube</h2>
<p>Les pages du site n’intègrent pas de lecteur YouTube : un clic sur une vidéo vous emmène sur YouTube, qui applique alors ses propres règles.</p>
<h2>Vos droits</h2>
<p>Vous pouvez vous désinscrire en un clic depuis chaque e-mail, et demander l’accès à vos données, leur rectification ou leur effacement. À VÉRIFIER : adresse à laquelle écrire, et renvoi exact aux dispositions applicables (loi fédérale sur la protection des données ; règlement européen pour les personnes dans l’Union européenne).</p>"""

MENTIONS = """<p class="alerte">Projet à compléter avant la mise en ligne.</p>
<h2>Éditrice du site</h2>
<p>À VÉRIFIER : nom, adresse, adresse de contact.</p>
<h2>Contenus</h2>
<p>Les vidéos, scripts et fiches sont des introductions pédagogiques. Ils ne remplacent pas un conseil juridique adapté à une situation particulière.</p>
<h2>Licence</h2>
<p>Contenus sous licence Creative Commons BY-SA 4.0. Le nom « L’étude du droit » et le logo ne sont pas couverts par cette licence.</p>"""


def main(sortie: str | None, apercu: bool) -> None:
    import fiche
    reglages = json.loads((RACINE / "site/site.json").read_text(encoding="utf-8"))
    dossier = Path(sortie) if sortie else RACINE / "site/public"
    if dossier.exists():
        shutil.rmtree(dossier)
    (dossier / "assets").mkdir(parents=True)
    shutil.copy(RACINE / "site/style.css", dossier / "assets/style.css")
    (dossier / "index.html").write_text(accueil(reglages, apercu), encoding="utf-8")
    for slug, info in reglages["videos"].items():
        cible = dossier / slug
        cible.mkdir(parents=True)
        shutil.copy(RACINE / "scripts" / slug / "miniature.png", cible / "miniature.png")
        if info.get("en_ligne"):
            # Image de la page : la scène du cas, tirée des schémas (sans titre ni sous-titres).
            schemas = RACINE / "render/manim/media" / slug / "schemas.mp4"
            if schemas.exists():
                subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", str(info.get("scene", 10)), "-i", str(schemas),
                                "-frames:v", "1", "-q:v", "3", "-vf", "scale=1280:-2", str(cible / "scene.jpg")], check=True)
            (cible / "index.html").write_text(page_video(slug, info, reglages), encoding="utf-8")
            fiche.main(slug, str(cible / "fiche.pdf"))
    for nom, contenu in [("parcours", page_parcours(reglages)),
                         ("a-propos", page_texte("À propos", "Pourquoi ce projet, et comment il est fait.", A_PROPOS,
                                                 "Le projet L’étude du droit : méthode, sources, licence.")),
                         ("confidentialite", page_texte("Protection des données", "Ce que le site collecte, et pourquoi.",
                                                        CONFIDENTIALITE, "Protection des données sur L’étude du droit.")),
                         ("mentions", page_texte("Mentions légales", "Qui publie ce site.", MENTIONS, "Mentions légales."))]:
        (dossier / nom).mkdir()
        (dossier / nom / "index.html").write_text(contenu, encoding="utf-8")
    print(f"Site : {dossier}")


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if a != "--apercu"]
    main(args[0] if args else None, "--apercu" in sys.argv)
