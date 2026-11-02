"""Copie de lecture d'un tts.txt, avec les nombres en chiffres, pour enregistrer plus confortablement.

Usage : python tools/texte_lecture.py <matiere>/<numero-slug> [sortie.txt]

Le tts.txt reste la référence (alignement, sous-titres) : il n'est pas modifié. La copie convertit tous les nombres
en chiffres (« deux mille treize » → 2013, « vingt-deux heures trente » → 22 heures 30, « deux voitures » → 2 voitures).
« un » et « une » seuls restent en lettres (articles), sauf après « article », « alinéa » ou « vidéo ».
"""

import re
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RACINE / "tools"))
from verifier_articles import SUFFIXES, UNITES, nombre  # noqa: E402

MOTS_NOMBRE = set(UNITES) | {"cent", "cents", "mille", "et"} | SUFFIXES
DECLENCHEURS = {"article", "articles", "alinéa", "alinéas", "vidéo", "vidéos", "chiffre"}


def est_mot_nombre(mot: str) -> bool:
    return bool(mot) and all(p in MOTS_NOMBRE or p == "vingts" for p in mot.lower().split("-"))


def convertir(ligne: str) -> str:
    jetons = re.split(r"(\s+)", ligne)
    mots = [j for j in jetons if j and not j.isspace()]
    sortie, i = [], 0
    while i < len(mots):
        nu = mots[i].rstrip(".,;:?!»")
        if est_mot_nombre(nu) and nu.lower() != "et":
            j, groupe = i, []
            while j < len(mots):
                m = mots[j].rstrip(".,;:?!»")
                if not est_mot_nombre(m):
                    break
                if m.lower() == "et":  # « vingt et un » est un seul nombre ; « six et huit » en sont deux
                    v = nombre(groupe) if groupe else None
                    if not (v and v.isdigit() and int(v) >= 20 and int(v) % 10 == 0):
                        break
                groupe.append(m.replace("vingts", "vingt").replace("cents", "cent"))
                j += 1
                if m != mots[j - 1]:  # ponctuation : le nombre s'arrête là
                    break
            while groupe and groupe[-1].lower() == "et":  # « trois et » : le « et » n'appartient pas au nombre
                groupe.pop()
                j -= 1
            valeur = nombre(groupe)
            precedent = mots[i - 1].lower().rstrip(".,") if i else ""
            seul_article = len(groupe) == 1 and groupe[0].lower() in ("un", "une") and precedent not in DECLENCHEURS
            if valeur and not seul_article:
                n = re.sub(r"\D", "", valeur)
                if len(n) >= 5:  # 20000 → 20 000 (espace insécable fine), pas pour les années
                    valeur = f"{int(n):,}".replace(",", "\u202f") + valeur[len(n):]
                fin = mots[j - 1][len(mots[j - 1].rstrip(".,;:?!»")):]
                sortie.append(valeur + fin)
                i = j
                continue
        sortie.append(mots[i])
        i += 1
    return " ".join(sortie)


def main(slug: str, cible: str | None = None) -> None:
    source = RACINE / "scripts" / slug / "tts.txt"
    lignes = source.read_text(encoding="utf-8").splitlines()
    texte = "\n".join(convertir(l) if l.strip() else l for l in lignes) + "\n"
    sortie = Path(cible) if cible else RACINE / "out" / f"{slug.replace('/', '--')}--lecture.txt"
    sortie.write_text(texte, encoding="utf-8")
    print(f"Copie de lecture : {sortie}")


if __name__ == "__main__":
    main(*sys.argv[1:3])
