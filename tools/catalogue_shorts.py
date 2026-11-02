"""Catalogue des shorts (YouTube Shorts, Instagram Reels, TikTok) tiré de tous les scripts/*/*/shorts.json.

Usage : python tools/catalogue_shorts.py

Sorties :
- docs/strategie/catalogue-shorts.md : tableau de tous les shorts (prêts ou à produire) et textes par plateforme ;
- out/shorts/catalogue.csv : une ligne par short, pour l'agent qui publie ;
- out/upload/shorts-catalogue.zip : les shorts déjà rendus, le CSV et un fichier texte par short.

Les textes ne disent rien de plus que l'accroche (validée par la relectrice) et le titre de la vidéo :
aucune affirmation juridique nouvelle. Rien n'est envoyé aux plateformes.
"""

import csv
import json
import re
import subprocess
import zipfile
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
SERIES = {"droit-penal-general": "Droit pénal général", "arrets": "Les arrêts du Tribunal fédéral"}
MOTS_PAR_SECONDE = 2.6  # débit moyen de la narration, pour estimer la durée d'un short pas encore rendu
MENTION = "Introduction pédagogique, pas un conseil juridique. Contenu sous licence CC BY-SA 4.0."
TAGS = {
    "youtube": "#Shorts #droitsuisse #droitpénal",
    "instagram": "#droitsuisse #droitpénal #étudiantendroit #suisseromande #apprendreledroit",
    "tiktok": "#droitsuisse #droit #étudiantendroit #suisseromande #apprendresurtiktok",
}


def duree_fichier(f: Path) -> float:
    r = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(f)],
                       capture_output=True, text=True)
    return float(r.stdout.strip() or 0)


def lignes_du_script(script: str) -> dict[int, str]:
    return {int(m[1]): m[2].strip() for m in re.finditer(r"^\|\s*(\d+)\s*\|([^|]+)\|", script, re.M)}


def textes(accroche: str, serie: str, numero: str, titre: str) -> dict[str, str]:
    video = f"« {titre} » ({serie}, vidéo {numero})"
    return {
        "youtube_titre": f"{accroche} #Shorts"[:100],
        "youtube_description": f"{accroche}\n\nExtrait de la vidéo {video}. La vidéo complète, avec les articles "
                               f"et les liens Fedlex, est sur la chaîne.\n\n{MENTION}\n{TAGS['youtube']}",
        "instagram": f"{accroche}\n\nExtrait de la vidéo {video}. Vidéo complète : lien en bio.\n"
                     f"Et vous, qu'auriez-vous répondu ? Dites-le en commentaire.\n\n{MENTION}\n\n{TAGS['instagram']}",
        "tiktok": f"{accroche} Vidéo complète sur YouTube : L'étude du droit (lien en bio). "
                  f"{MENTION} {TAGS['tiktok']}",
    }


def main() -> None:
    sortie_shorts = RACINE / "out" / "shorts"
    sortie_shorts.mkdir(parents=True, exist_ok=True)
    rangs = []
    for config in sorted((RACINE / "scripts").glob("*/*/shorts.json")):
        dossier = config.parent
        matiere, video = dossier.parent.name, dossier.name
        script = (dossier / "script.md").read_text(encoding="utf-8")
        titre = script.splitlines()[0].split("—", 1)[-1].strip()
        numero = video[:2].lstrip("0")
        lignes = lignes_du_script(script)
        for s in json.loads(config.read_text(encoding="utf-8"))["shorts"]:
            fichier = sortie_shorts / f"{matiere}--{video}--{s['id']}.mp4"
            if fichier.exists():
                statut, duree = "prêt", duree_fichier(fichier)
            else:
                mots = sum(len(lignes.get(n, "").split()) for n in range(s["de"], s["a"] + 1))
                statut, duree = "après enregistrement", mots / MOTS_PAR_SECONDE + 4
            rangs.append({
                "serie": SERIES.get(matiere, matiere), "video": numero, "titre_video": titre, "id": s["id"],
                "accroche": s["accroche"], "lignes": f"{s['de']}–{s['a']}", "duree_s": round(duree),
                "statut": statut, "fichier": fichier.name if fichier.exists() else "",
                **textes(s["accroche"], SERIES.get(matiere, matiere), numero, titre),
            })

    with open(sortie_shorts / "catalogue.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rangs[0]))
        w.writeheader()
        w.writerows(rangs)

    prets = [r for r in rangs if r["statut"] == "prêt"]
    md = ["# Catalogue des shorts", "",
          "Généré par `tools/catalogue_shorts.py` à partir des `shorts.json` de chaque vidéo. Un short reprend tel quel "
          "un extrait audité de la vidéo ; seule l'accroche lui est propre (à valider par la relectrice). "
          "Les textes par plateforme sont dans `out/shorts/catalogue.csv` et dans le paquet `out/upload/shorts-catalogue.zip`.",
          "", f"**{len(rangs)} shorts : {len(prets)} prêts, {len(rangs) - len(prets)} à produire après l'enregistrement.**",
          "", "## Réglages communs", "",
          "- Format : 1080 × 1920, 25 à 60 s, sous-titres incrustés, même fichier pour les trois plateformes.",
          "- YouTube Shorts : titre = accroche + #Shorts ; relier le short à la vidéo complète (« vidéo associée »).",
          "- Instagram Reels et TikTok : lien de la chaîne YouTube dans la bio ; légende ci-dessous.",
          "- Musique : aucune (la narration seule ; pas de son sous licence à gérer).",
          "- Rythme proposé : un short par jour, en alternant les vidéos ; toujours après la publication de la vidéo complète.",
          "", "## Tous les shorts", "",
          "| Série | Vidéo | Short | Accroche | Lignes | Durée | Statut |", "| --- | --- | --- | --- | --- | --- | --- |"]
    for r in rangs:
        md.append(f"| {r['serie']} | {r['video']} — {r['titre_video']} | `{r['id']}` | {r['accroche']} | "
                  f"{r['lignes']} | {'' if r['statut'] == 'prêt' else '≈ '}{r['duree_s']} s | {r['statut']} |")
    md += ["", "## Textes par plateforme (shorts prêts)", ""]
    for r in prets:
        md += [f"### {r['serie']}, vidéo {r['video']} — {r['accroche']}", "", f"Fichier : `out/shorts/{r['fichier']}`", "",
               f"**YouTube** — titre : {r['youtube_titre']}", "", "```text", r["youtube_description"], "```", "",
               "**Instagram**", "", "```text", r["instagram"], "```", "", "**TikTok**", "", "```text", r["tiktok"], "```", ""]
    (RACINE / "docs" / "strategie" / "catalogue-shorts.md").write_text("\n".join(md), encoding="utf-8")

    paquet = RACINE / "out" / "upload" / "shorts-catalogue.zip"
    paquet.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(paquet, "w") as z:
        z.write(sortie_shorts / "catalogue.csv", "shorts/catalogue.csv")
        z.write(RACINE / "docs" / "strategie" / "catalogue-shorts.md", "shorts/LISEZMOI.md")
        for r in prets:
            base = Path(r["fichier"]).stem
            z.write(sortie_shorts / r["fichier"], f"shorts/{r['fichier']}", compress_type=zipfile.ZIP_STORED)
            z.writestr(f"shorts/textes/{base}.txt",
                       f"YOUTUBE — TITRE\n{r['youtube_titre']}\n\nYOUTUBE — DESCRIPTION\n{r['youtube_description']}\n\n"
                       f"INSTAGRAM\n{r['instagram']}\n\nTIKTOK\n{r['tiktok']}\n")
    print(f"Catalogue : {len(rangs)} shorts ({len(prets)} prêts) → {paquet}")


if __name__ == "__main__":
    main()
