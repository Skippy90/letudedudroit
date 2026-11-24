"""Sous-titres de l'arrêt 25 : le texte lu, en morceaux courts, sur le temps de la vidéo."""
import sys
sys.path.insert(0, "/home/claude/z232")
from temps import *
REMPL = [("cinq octobre mille neuf cent nonante-neuf", "5 octobre 1999"), ("mille neuf cent nonante-neuf", "1999"), ("ATF cent vingt-neuf, un, deux cent trente-deux", "ATF 129 I 232"),
         ("dix-sept janvier deux mille un", "17 janvier 2001"), ("majorité des deux tiers", "majorité des 2 tiers"), ("trente août deux mille un", "30 août 2001"),
         ("treize novembre deux mille deux", "13 novembre 2002"), ("et deux citoyens", "et 2 citoyens"), ("neuf juillet deux mille trois", "9 juillet 2003"),
         ("article vingt-neuf, alinéa deux", "article 29, alinéa 2"), ("article huit, alinéa deux", "article 8, alinéa 2"), ("article trente-cinq", "article 35"),
         ("article trente-quatre", "article 34"), ("article treize", "article 13"), ("fin de deux mille un", "fin de 2001"), ("cent un mille personnes", "101 000 personnes"),
         ("quatre cent cinquante dossiers", "450 dossiers"), ("articles quinze à dix-sept", "articles 15 à 17")]
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
