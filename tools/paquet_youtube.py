"""Paquet prêt pour l'upload YouTube (par une personne ou par un agent) : vidéo, miniature, description, réglages.

Usage : python tools/paquet_youtube.py <matiere>/<numero-slug>

Entrées : out/<matiere>--<numero-slug>.mp4, scripts/<slug>/miniature.png, scripts/<slug>/publication.md
(générée par tools/publication.py), scripts/<slug>/script.md (question finale pour le commentaire épinglé).
Sortie : out/upload/<numero-slug>.zip (dossier du même nom à côté). Rien n'est envoyé à YouTube.
"""

import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent

TAGS = ["droit suisse", "droit pénal", "code pénal suisse", "étudiant en droit", "Suisse romande", "L'étude du droit"]
# Séries nouvelles : mise en ligne non répertoriée, contrôle sur YouTube, puis publique.
NON_REPERTORIE = {"arrets"}
CONTROLE = ("0. Mise en ligne **non répertoriée**. Regarder la vidéo sur YouTube : voix, sous-titres, incrustations, "
            "chapitres et liens de la description. Si tout est conforme, passer la visibilité sur **Programmer**, "
            "à la date et à l'heure du tableau ci-dessus (heure suisse). Sinon, ne rien publier et signaler le défaut.\n")
PROGRAMMATION = RACINE / "docs" / "strategie" / "programmation.json"
JOURS = ["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche"]
MOIS = ["janvier", "février", "mars", "avril", "mai", "juin", "juillet", "août", "septembre", "octobre", "novembre",
        "décembre"]


def date_prevue(slug: str):
    """Date de publication prévue (docs/strategie/programmation.json), à l'heure suisse ; None si pas encore fixée."""
    from datetime import datetime
    from zoneinfo import ZoneInfo
    prog = json.loads(PROGRAMMATION.read_text(encoding="utf-8")) if PROGRAMMATION.exists() else {}
    quand = prog.get("videos", {}).get(slug)
    return datetime.fromisoformat(quand).replace(tzinfo=ZoneInfo("Europe/Zurich")) if quand else None


def en_toutes_lettres(d) -> str:
    return f"{JOURS[d.weekday()]} {d.day} {MOIS[d.month - 1]} {d.year} à {d.hour} h{d.minute:02d}".replace(" h00", " h")


PLAYLISTS = {"droit-penal-general": "Droit pénal général", "arrets": "Les arrêts du Tribunal fédéral", "procedure-penale": "Procédure pénale"}


def main(slug: str, tags_video: list[str]) -> None:
    matiere, nom = slug.split("/")
    dossier = RACINE / "scripts" / slug
    video = RACINE / "out" / f"{matiere}--{nom}.mp4"
    pub = (dossier / "publication.md").read_text(encoding="utf-8")
    titre = re.search(r"## Titre\s+(.+)", pub).group(1).strip()
    description = re.search(r"```text\n(.*?)```", pub, re.S).group(1).rstrip()
    # Garde-fous : rien d'interne ni d'illisible pour YouTube.
    for interdit in ("À VÉRIFIER", "(ligne", "le script dit", "relecture", "<", ">"):
        if interdit in description:
            sys.exit(f"Description refusée : contient « {interdit} »")
    if re.search(r"\blignes? \d", description):
        sys.exit("Description refusée : une note interne (« ligne N ») est restée")
    if len(description) > 5000 or len(titre) > 100:
        sys.exit("Titre ou description trop long pour YouTube")
    question = ""
    script = (dossier / "script.md").read_text(encoding="utf-8")
    for ligne in script.splitlines():
        cols = [c.strip() for c in ligne.split("|")]
        if len(cols) > 3 and "question pour finir" in cols[2].lower():
            question = re.sub(r"(?i)^une question pour finir\.\s*", "", cols[2])
            question = re.sub(r"\s*Écrivez votre réponse en commentaire\.?", "", question).strip()
    duree = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0",
                                  str(video)], capture_output=True, text=True, check=True).stdout)
    numero = nom[:2].lstrip("0")
    playlist = PLAYLISTS.get(matiere, matiere)
    quand = date_prevue(slug)

    sortie = RACINE / "out" / "upload" / nom
    if sortie.exists():
        shutil.rmtree(sortie)
    sortie.mkdir(parents=True)
    shutil.copy(video, sortie / "video.mp4")
    shutil.copy(dossier / "miniature.png", sortie / "miniature.png")
    (sortie / "description.txt").write_text(description + "\n", encoding="utf-8")
    from sous_titres_srt import srt
    srt(slug, sortie / "sous-titres.fr.srt")
    commentaire = (question + " Répondez en commentaire 👇 (réponse dans la description)").strip()
    reglages = {
        "video_file": "video.mp4",
        "thumbnail_file": "miniature.png",
        "title": titre,
        "description_file": "description.txt",
        "captions_file": "sous-titres.fr.srt (langue : français ; nom de la piste : Français)",
        "tags": tags_video + TAGS,
        "category": "Education (id 27)",
        "default_language": "fr",
        "default_audio_language": "fr",
        "made_for_kids": False,
        "altered_or_synthetic_content": False,
        "license": "youtube (licence standard ; la CC BY-SA 4.0 est indiquée dans la description, YouTube ne proposant que CC BY)",
        "embeddable": True,
        "privacy_status": ("unlisted, puis programmée après contrôle" if matiere in NON_REPERTORIE
                           else "programmée (privée jusqu'à publish_at)" if quand else "public"),
        "playlist": f"{playlist} (créer si absente ; vidéos dans l'ordre des numéros)",
        "pinned_comment": commentaire,
        "chapters": "dans la description (premier à 0:00)",
        "publish_at": quand.isoformat() if quand else "pas encore fixée (voir docs/strategie/programmation.json)",
    }
    (sortie / "youtube.json").write_text(json.dumps(reglages, ensure_ascii=False, indent=2), encoding="utf-8")
    minutes = f"{int(duree // 60)} min {int(duree % 60):02d}"
    (sortie / "LISEZMOI.md").write_text(f"""# Upload YouTube — {playlist}, vidéo {numero} : {titre}

Consignes pour l'agent qui publie. Tout est validé par la chaîne ; ne rien réécrire.

## Fichiers
- `video.mp4` : la vidéo (1920 × 1080, {minutes}, sous-titres incrustés).
- `miniature.png` : la miniature personnalisée.
- `description.txt` : la description, à coller telle quelle (chapitres compris).
- `sous-titres.fr.srt` : les sous-titres en fichier, à ajouter comme piste « Français » (Google et YouTube les lisent ; les sous-titres incrustés, non).
- `youtube.json` : les mêmes réglages, en format machine.

## Réglages
| Champ | Valeur |
|---|---|
| Titre | {titre} |
| Description | contenu de `description.txt`, sans modification |
| Miniature | `miniature.png` |
| Sous-titres | `sous-titres.fr.srt`, langue français (Sous-titres → Ajouter → Importer un fichier → « Avec minutage ») |
| Playlist | « {playlist} » (la créer si absente ; vidéos dans l'ordre des numéros) |
| Public cible | Non, cette vidéo n'est pas conçue pour les enfants |
| Contenu modifié ou synthétique | Non (narration enregistrée par une personne réelle) |
| Catégorie | Éducation |
| Langue de la vidéo et de l'audio | Français |
| Licence | Licence YouTube standard (la CC BY-SA 4.0 est mentionnée dans la description) |
| Intégration autorisée | Oui |
| Publication programmée | {en_toutes_lettres(quand) + " (heure suisse)" if quand else "pas encore fixée : ne pas publier"} |
| Visibilité | {"**Non répertoriée** d'abord ; programmée seulement après le contrôle ci-dessous" if matiere in NON_REPERTORIE else "**Programmer** à la date ci-dessus" if quand else "Public"} |
| Tags | {", ".join(reglages["tags"])} |

## Après la mise en ligne
{CONTROLE if matiere in NON_REPERTORIE else ""}1. Publier puis **épingler** ce commentaire :
   > {commentaire}
2. Vérifier que les chapitres apparaissent dans la barre de lecture.
3. Renvoyer le lien de la vidéo (pour le site et les vidéos suivantes).

## À ne pas faire
- Ne pas modifier le titre, la description ni les liens Fedlex.
- Ne pas activer la traduction ou le doublage automatiques.
- Ne pas ajouter de musique ni de son à la vidéo.
""", encoding="utf-8")
    archive = shutil.make_archive(str(sortie), "zip", sortie.parent, nom)
    print(f"Paquet : {archive}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    main(sys.argv[1], sys.argv[2:])
