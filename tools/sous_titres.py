"""Sous-titres d'une vidéo, calés mot à mot sur la narration.

Usage : python tools/sous_titres.py <matiere>/<numero-slug> <sortie.ass> [décalage en secondes]

Le texte affiché est le texte lu (tts.txt, articles en toutes lettres). Chaque phrase est découpée en morceaux de
MOTS_MAX mots au plus ; l'instant de chaque morceau vient des mots reconnus dans la narration
(voice/<slug>/timings.json, champ « mots »). Sans instant par mot, la phrase est répartie
à vitesse constante.

Format ASS (lu par ffmpeg / libass) : police Inter, blanc cassé sur un bandeau noir
semi-transparent, en bas de l'image, 54 px de haut sur 1080, à l'échelle des plus petits textes de la charte.
"""

import json
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))
from alignement import mots_texte  # noqa: E402
MOTS_MAX = 7

ENTETE = """[Script Info]
ScriptType: v4.00+
PlayResX: 1920
PlayResY: 1080
WrapStyle: 2

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Bas,Inter,54,&H00E6EFF2,&H00E6EFF2,&H400B0B0B,&H400B0B0B,0,0,0,0,100,100,0,0,3,8,0,2,80,80,18,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""


def horodatage(s: float) -> str:
    h, reste = divmod(max(0.0, s), 3600)
    m, sec = divmod(reste, 60)
    return f"{int(h)}:{int(m):02d}:{sec:05.2f}"


def morceaux(mots: list[str]) -> list[tuple[int, int]]:
    """Découpe en morceaux de MOTS_MAX mots au plus : (premier, après le dernier).

    On coupe de préférence après une ponctuation (« , ; : »), le plus près possible
    d'un découpage équilibré ; jamais après un petit mot (« un », « le », « de »…).
    """
    n = len(mots)
    k = -(-n // MOTS_MAX)
    coupes, debut = [], 0
    petits = {"un", "une", "le", "la", "les", "l'", "de", "du", "des", "d'", "à", "au", "et", "en", "son", "sa", "ses"}
    for i in range(1, k):
        ideal = round(i * n / k)
        candidats = range(max(debut + 1, ideal - 2), min(n, ideal + 3, debut + MOTS_MAX + 1))
        def score(c):
            return abs(c - ideal) - (2.5 if mots[c - 1][-1] in ",;:" else 0) + (3 if mots[c - 1].lower() in petits else 0)
        c = min(candidats, key=score, default=min(n, debut + MOTS_MAX))
        coupes.append(c)
        debut = c
    bornes = [0] + coupes + [n]
    resultat = [(a, b) for a, b in zip(bornes, bornes[1:]) if b > a]
    # Filet de sécurité : aucun morceau au-delà de MOTS_MAX mots.
    final = []
    for a, b in resultat:
        while b - a > MOTS_MAX:
            final.append((a, a + MOTS_MAX))
            a += MOTS_MAX
        final.append((a, b))
    return final


def main(slug: str, sortie: str, decalage: float = 0.0) -> None:
    timings = json.loads((RACINE / "voice" / slug / "timings.json").read_text(encoding="utf-8"))
    lignes, evenements = [ENTETE], []
    for ligne in timings["lignes"]:
        for phrase in ligne["phrases"]:
            mots = phrase["texte"].split()
            reconnus = phrase.get("mots") or []
            # Chaque mot du texte correspond à un ou plusieurs mots reconnus (« d'escalier » → d + escalier) :
            # on cumule ces nombres pour savoir où commence chaque mot dans la liste reconnue.
            pieces = [len(mots_texte(w)) for w in mots]
            exact = sum(pieces) == len(reconnus)
            rang = [sum(pieces[:i]) for i in range(len(mots) + 1)]
            for a, b in morceaux(mots):
                if reconnus:
                    m = len(reconnus)
                    if exact:
                        i, j = rang[a], max(rang[a], rang[b] - 1)
                    else:
                        i, j = round(a * m / len(mots)), round(b * m / len(mots)) - 1
                    debut = reconnus[min(m - 1, i)]["debut"]
                    fin = reconnus[min(m - 1, max(0, j))]["fin"]
                else:
                    duree = phrase["fin"] - phrase["debut"]
                    debut = phrase["debut"] + duree * a / len(mots)
                    fin = phrase["debut"] + duree * b / len(mots)
                texte = " ".join(mots[a:b]).replace("{", "(").replace("}", ")")
                evenements.append([debut + decalage, fin + decalage + 0.15, texte])
    # Un sous-titre s'efface au plus tard quand le suivant apparaît : jamais deux lignes à la fois.
    for e, suivant in zip(evenements, evenements[1:]):
        e[1] = min(e[1], suivant[0])
    for debut, fin, texte in evenements:
        lignes.append(f"Dialogue: 0,{horodatage(debut)},{horodatage(fin)},Bas,,0,0,0,,{texte}\n")
    Path(sortie).write_text("".join(lignes), encoding="utf-8")
    print(f"Sous-titres : {sortie} ({len(lignes) - 1} morceaux)")


if __name__ == "__main__":
    if len(sys.argv) not in (3, 4):
        sys.exit(__doc__)
    main(sys.argv[1], sys.argv[2], float(sys.argv[3]) if len(sys.argv) == 4 else 0.0)
