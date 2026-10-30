"""Prépare la fiche de publication YouTube d'une vidéo (étape 7 du brief).

Usage : python tools/publication.py <matiere>/<numero-slug>

Écrit scripts/<slug>/publication.md : titre, description prête à coller (articles et
liens Fedlex repris de l'audit, jurisprudence, réponse à la question finale, chapitres,
lien vers le script, licence, mention de la narration synthétique).
Rien n'est envoyé à YouTube : l'upload se fait seulement sur instruction explicite.
"""

import json
import re
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
DEPOT = "https://github.com/Skippy90/letudedudroit"
DUREE_OUVERTURE = 4  # secondes, doit correspondre à render/remotion/src/Video.tsx


SUFFIXES = {"droit-penal-general": "Droit pénal suisse", "procedure-penale": "Procédure pénale suisse"}

def horodatage(secondes: float) -> str:
    s = int(secondes)
    return f"{s // 60}:{s % 60:02d}"


def sans_markdown(texte: str) -> str:
    texte = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", texte)
    return texte.replace("**", "").strip()


def main(slug: str) -> None:
    dossier = RACINE / "scripts" / slug
    script = (dossier / "script.md").read_text(encoding="utf-8")
    audit = (dossier / "audit.md").read_text(encoding="utf-8")
    config_voix = json.loads((RACINE / "voice/config.json").read_text(encoding="utf-8"))
    timings = json.loads((RACINE / "voice" / slug / "timings.json").read_text(encoding="utf-8"))
    debuts = {l["ligne"]: l["debut"] for l in timings["lignes"]}

    titre = re.match(r"#\s*Vidéo\s+\d+\s*[—-]\s*(.+)", script.splitlines()[0])[1].strip()

    # Chapitres : chaque section ## du script commence à sa première ligne numérotée.
    # YouTube exige un premier chapitre à 0:00 et au moins 10 s par chapitre :
    # l'ouverture (4 s) est donc rattachée au premier chapitre.
    chapitres, section = [], None
    for ligne in script.splitlines():
        if ligne.startswith("## "):
            section = ligne[3:].strip()
        m = re.match(r"\|\s*(\d+)\s*\|", ligne)
        if m and section:
            debut = 0 if not chapitres else DUREE_OUVERTURE + debuts[int(m[1])]
            chapitres.append((horodatage(debut), section))
            section = None

    # Articles : tableau « Articles cités » de l'audit (article avec lien, ce que le script lui fait dire).
    articles = []
    # Le tableau des articles est sous « ## Articles cités », ou seul dans l'audit (vidéo 1).
    bloc = audit.split("## Articles cités", 1)[-1].split("\n## ", 1)[0]
    for ligne in bloc.splitlines():
        m = re.match(r"\|\s*\[([^\]]+)\]\(([^)]+)\)([^|]*)\|([^|]+)\|", ligne)
        if m:
            # Les renvois internes aux lignes du script (« (ligne 19) ») restent dans l'audit.
            resume = re.sub(r"\s*\(lignes? [^)]*\)\s*$", "", sans_markdown(m[4]))
            articles.append(f"• {m[1]}{m[3].rstrip()} : {resume}\n  {m[2]}")

    # Jurisprudence citée dans l'audit, sans doublon.
    arrets = []
    for numero, lien in re.findall(r"\[(ATF [^\]]+)\]\(([^)]+)\)", audit):
        if numero not in [a[0] for a in arrets]:
            arrets.append((numero, lien))

    reponse = re.search(r"\*\*Réponse attendue à la question finale\*\*[^:]*:\s*(.+)", script)

    lignes = [
        f"{titre} — expliqué simplement, à partir d'un cas concret.",
        "",
        "Articles cités (texte en vigueur vérifié sur Fedlex) :",
        *articles,
    ]
    if arrets:
        lignes += ["", "Jurisprudence du Tribunal fédéral :", *[f"• {n}\n  {l}" for n, l in arrets]]
    if reponse:
        texte_reponse = sans_markdown(reponse[1])
        lignes += ["", "Réponse à la question finale :", texte_reponse[:1].upper() + texte_reponse[1:]]
    lignes += ["", "Chapitres :", *[f"{t} {nom}" for t, nom in chapitres]]
    lignes += [
        "",
        f"Script complet, audit des sources et code : {DEPOT}/tree/main/scripts/{slug}",
        "Contenu sous licence Creative Commons BY-SA 4.0 : vous pouvez le réutiliser en citant "
        "« L'étude du droit » et en partageant dans les mêmes conditions.",
    ]
    if timings.get("source", config_voix["source"]) == "synthese":
        lignes.append("Narration synthétique (voix générée par ElevenLabs).")
    lignes.append("Cette vidéo est une introduction pédagogique et ne remplace pas un conseil juridique.")
    description = "\n".join(lignes)

    sortie = dossier / "publication.md"
    sortie.write_text(
        f"# Publication — {titre}\n\n"
        "Fiche générée par `tools/publication.py`. À relire avant tout envoi ; "
        "l'upload YouTube se fait seulement sur instruction explicite.\n\n"
        f"## Titre\n\n{titre} | {SUFFIXES.get(slug.split('/')[0], 'Droit suisse')}\n\n"
        f"## Description ({len(description)} caractères sur 5 000)\n\n```text\n{description}\n```\n",
        encoding="utf-8")
    print(f"Fiche : {sortie} ({len(description)} caractères)")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    main(sys.argv[1])
