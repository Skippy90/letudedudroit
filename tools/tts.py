"""Génère tts.txt à partir de la colonne « Texte à lire » de script.md.

Usage : python tools/tts.py <matiere>/<numero-slug>

- Une phrase par ligne, une ligne vide entre deux lignes du script (pause).
- Les numéros d'article et de vidéo sont écrits en toutes lettres
  (« article cent vingt-trois », « article premier », « vidéo quatre »).
- Le script s'arrête si un chiffre reste dans le texte : il faut alors l'écrire
  en toutes lettres dans script.md ou compléter les règles ci-dessous.
"""

import re
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
UNITES = ["zéro", "un", "deux", "trois", "quatre", "cinq", "six", "sept", "huit", "neuf", "dix", "onze",
          "douze", "treize", "quatorze", "quinze", "seize", "dix-sept", "dix-huit", "dix-neuf"]
DIZAINES = {2: "vingt", 3: "trente", 4: "quarante", 5: "cinquante", 6: "soixante"}


def en_lettres(n: int) -> str:
    """Nombres de 0 à 999, orthographe traditionnelle (traits d'union sous cent)."""
    if n < 20:
        return UNITES[n]
    if n < 100:
        d, u = divmod(n, 10)
        if d in (7, 9):  # soixante-dix, quatre-vingt-dix
            base = "soixante" if d == 7 else "quatre-vingt"
            reste = 10 + u
            lien = "-et-" if d == 7 and u == 1 else "-"
            return base + lien + UNITES[reste]
        if d == 8:
            return "quatre-vingts" if u == 0 else "quatre-vingt-" + UNITES[u]
        if u == 0:
            return DIZAINES[d]
        return DIZAINES[d] + ("-et-un" if u == 1 else "-" + UNITES[u])
    c, r = divmod(n, 100)
    tete = "cent" if c == 1 else UNITES[c] + " cent" + ("s" if r == 0 else "")
    return tete if r == 0 else f"{tete} {en_lettres(r)}"


def transformer(texte: str) -> str:
    # « l'article 1 » → « l'article premier » ; « articles 34 à 47 » → en lettres.
    texte = re.sub(r"\b(articles?|article premier) 1\b", r"\1 premier", texte)
    texte = re.sub(r"\barticle 1\b", "article premier", texte)
    texte = re.sub(r"\b(articles?|vidéos?|alinéas?|à|et|ou) (\d{1,3})\b",
                   lambda m: f"{m[1]} {en_lettres(int(m[2]))}", texte)
    # Une seconde passe pour les énumérations : « articles 15, 16 et 17 ».
    texte = re.sub(r"(?<=, )(\d{1,3})\b", lambda m: en_lettres(int(m[1])), texte)
    return texte


def phrases(texte: str) -> list[str]:
    """Découpe en phrases, sans jamais couper à l'intérieur d'une citation « … »."""
    morceaux = re.split(r"(?<=[.?!])\s+(?=[A-ZÀ-ÜÇÉ«])|(?<=[.?!] »)\s+(?=[A-ZÀ-ÜÇÉ])", texte)
    resultat = []
    for m in morceaux:
        if resultat and resultat[-1].count("«") > resultat[-1].count("»"):
            resultat[-1] += " " + m
        else:
            resultat.append(m)
    return resultat


def main(slug: str) -> None:
    dossier = RACINE / "scripts" / slug
    lignes = [l.split("|")[2].strip() for l in (dossier / "script.md").read_text(encoding="utf-8").splitlines()
              if re.match(r"\|\s*\d+\s*\|", l)]
    blocs = []
    for texte in lignes:
        texte = transformer(texte)
        if re.search(r"\d", texte):
            sys.exit(f"Chiffre restant, à écrire en toutes lettres dans script.md : {texte}")
        blocs.append("\n".join(phrases(texte)))
    (dossier / "tts.txt").write_text("\n\n".join(blocs) + "\n", encoding="utf-8")
    print(f"tts.txt : {len(blocs)} lignes, {sum(len(l.split()) for l in lignes)} mots")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    main(sys.argv[1])
