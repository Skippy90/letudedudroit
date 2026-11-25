"""Sous-titres de l'arrêt 15 : le texte lu, en morceaux courts, sur le temps de la vidéo."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from temps import *
REMPL = [("mille neuf cent septante et un et mille neuf cent nonante et un", "1971 et 1991"), ("mille neuf cent nonante-neuf", "1999"), ("mille neuf cent huitante", "1980"),
         ("neuf juillet deux mille trois", "9 juillet 2003"), ("mars deux mille deux", "mars 2002"), ("deux mille un", "2001"), ("douze mars deux mille", "12 mars 2000"), ("mars deux mille", "mars 2000"),
         ("article huit, alinéa deux", "article 8, alinéa 2"), ("article vingt-neuf, alinéa deux", "article 29, alinéa 2"), ("article trente-cinq, alinéa deux", "article 35, alinéa 2"),
         ("article trente-quatre", "article 34"), ("article quinze", "article 15"), ("article seize", "article 16"),
         ("vingt-trois", "23"), ("cinquante-six", "56"), ("seize demandes", "16 demandes"), ("trente-huit", "38"), ("huit personnes", "8 personnes"), ("quatre demandes", "4 demandes")]
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
