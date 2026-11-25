"""Sous-titres de l'arrêt 25 : le texte lu, en morceaux courts, sur le temps de la vidéo."""
import sys
sys.path.insert(0, "/home/claude/a25")
from temps import *
REMPL = [("vingt-cinq novembre deux mille seize", "25 novembre 2016"), ("deux mille seize", "2016"), ("neuf avril deux mille vingt-quatre", "9 avril 2024"), ("deux mille vingt-quatre", "2024"),
         ("entre septante-six et huitante-sept ans", "entre 76 et 87 ans"), ("en dessous de deux degrés", "en dessous de 2 degrés"), ("un virgule cinq degré", "1,5 degré"), ("deux mille trente", "2030"),
         ("cinquante pour cent", "50 pour cent"), ("mille neuf cent nonante", "1990"), ("septante-cinq ans", "75 ans"), ("vingt-cinq avril deux mille dix-sept", "25 avril 2017"),
         ("vingt-sept novembre deux mille dix-huit", "27 novembre 2018"), ("deux mille dix-huit", "2018"), ("article vingt-cinq a", "article 25a"), ("cinq mai deux mille vingt", "5 mai 2020"),
         ("vingt-six novembre deux mille vingt", "26 novembre 2020"), ("deux mille quarante", "2040"), ("deux mille cinquante-deux", "2052"), ("deux mille cinquante", "2050"),
         ("article six, paragraphe un", "article 6, paragraphe 1"), ("articles huit et six", "articles 8 et 6"), ("article huit", "article 8"), ("seize voix contre une", "16 voix contre une"),
         ("deux mille vingt-deux", "2022"), ("deux mille vingt-trois", "2023"), ("premier janvier deux mille vingt-cinq", "1er janvier 2025"), ("deux mille vingt", "2020")]
MAXC = 60
def h(t):
    ms = int(round(t * 1000)); return f"{ms // 3600000:02d}:{ms // 60000 % 60:02d}:{ms // 1000 % 60:02d},{ms % 1000:03d}"
cles = sorted(PH); out = []; n = 0
for i, c in enumerate(cles):
    p = PH[c]; brut = p["texte"]; d, f = p["debut"], p["fin"]
    txt = brut
    for a, b in REMPL: txt = txt.replace(a, b).replace(a.capitalize(), b)
    mots = txt.split(); k = -(-len(txt) // MAXC); blocs = []
    while k > 1:
        reste = " ".join(mots); cible = len(reste) / k; best = None; c = 0
        for j, m in enumerate(mots[:-1]):
            c += len(m) + 1
            score = abs(c - cible) - (10 if m[-1] in ",;:" else 0)
            if c <= MAXC + 6 and (best is None or score < best[0]): best = (score, j + 1)
        blocs.append(mots[:best[1]]); mots = mots[best[1]:]; k -= 1
    blocs.append(mots)
    tot = sum(len(" ".join(b)) + 1 for b in blocs); t = d
    suiv = PH[cles[i + 1]]["debut"] if i + 1 < len(cles) else f + 1
    for k, b in enumerate(blocs):
        e = t + (f - d) * (len(" ".join(b)) + 1) / tot
        vf = M(e) if k < len(blocs) - 1 else min(M(f) + 0.4, M(suiv) - 0.05)
        vf = max(vf, M(t) + 0.3)
        n += 1; out.append(f"{n}\n{h(M(t))} --> {h(vf)}\n{' '.join(b)}\n"); t = e
open(sys.argv[1], "w").write("\n".join(out)); print(n, max(len(x.split(chr(10))[2]) for x in out))
