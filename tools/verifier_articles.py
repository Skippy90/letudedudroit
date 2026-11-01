"""Contrôle : le bloc d'article affiché correspond-il à l'article que la voix cite ?

Usage : python tools/verifier_articles.py <matiere>/<numero-slug>

Pour chaque « article … » prononcé (timings.json), on regarde quel bloc « Art. N … » est à l'écran une seconde plus
tard (visuals.md : actions article / article-retirer). Signale un écart, ou un article cité sans bloc à l'écran.
Né d'une erreur de la vidéo 3 : « Art. 109 CP » restait affiché pendant que la voix passait à l'article 97.
"""

import re
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RACINE / "render" / "manim"))
import os  # noqa: E402

os.environ.setdefault("APERCU", "1")
from video import lire_moments  # noqa: E402

UNITES = {"zéro": 0, "un": 1, "une": 1, "deux": 2, "trois": 3, "quatre": 4, "cinq": 5, "six": 6, "sept": 7, "huit": 8,
          "neuf": 9, "dix": 10, "onze": 11, "douze": 12, "treize": 13, "quatorze": 14, "quinze": 15, "seize": 16,
          "vingt": 20, "trente": 30, "quarante": 40, "cinquante": 50, "soixante": 60, "septante": 70,
          "huitante": 80, "octante": 80, "nonante": 90}
SUFFIXES = {"bis", "ter", "quater", "quinquies"}


def nombre(mots: list[str]) -> str | None:
    """« cent septante-deux ter » → « 172ter » ; s'arrête au premier mot qui n'est pas un nombre."""
    total, courant, suffixe, lu = 0, 0, "", False
    for m in mots:
        for p in m.lower().split("-"):
            if p == "et":
                if courant >= 20 and courant % 10 == 0:  # « vingt et un », pas « seize et dix-huit »
                    continue
                return f"{total + courant}{suffixe}" if lu else None
            if p in UNITES:
                courant += UNITES[p]
                lu = True
            elif p == "cent":
                courant = (courant or 1) * 100
                lu = True
            elif p == "mille":
                total += (courant or 1) * 1000
                courant, lu = 0, True
            elif p in SUFFIXES and lu:
                suffixe = p
                return f"{total + courant}{suffixe}"
            else:
                return f"{total + courant}" if lu else None
    return f"{total + courant}{suffixe}" if lu else None


def main(slug: str) -> int:
    import json
    timings = json.loads((RACINE / "voice" / slug / "timings.json").read_text(encoding="utf-8"))
    moments, _ = lire_moments(slug)
    affichages = []  # (instant, libellé ou None)
    for instant, actions, _ in moments:
        for a in actions:
            if a[0] == "article":
                affichages.append((instant, a[1]))
            elif a[0] == "article-retirer":
                affichages.append((instant, None))

    def affiche(t):
        courant = None
        for i, lib in affichages:
            if i <= t:
                courant = lib
        return courant

    ecarts = 0
    for l in timings["lignes"]:
        for p in l["phrases"]:
            mots = re.findall(r"[\w'-]+", p["texte"])
            for k, m in enumerate(mots):
                if m.lower() not in ("article", "l'article", "articles"):
                    continue
                n = nombre(mots[k + 1:k + 6])
                if n is None:
                    continue  # « cet article », « l'article suivant »
                rec = [w for w in p.get("mots", []) if w["mot"] == "article"]
                t = rec[0]["fin"] if rec else p["debut"]
                bloc = affiche(t + 1.0)
                num_bloc = re.match(r"Art\.\s*([\w]+)", bloc).group(1).lower() if bloc else None
                ok = num_bloc == n.lower()
                ecarts += not ok
                quand = f"{int(t // 60)}:{int(t % 60):02d}"
                print(f"{'ok ' if ok else 'ÉCART'} {quand}  voix : article {n:<8} écran : {bloc or '(aucun bloc)'}")
    print(f"\n{ecarts} écart(s)")
    return ecarts


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    sys.exit(1 if main(sys.argv[1]) else 0)
