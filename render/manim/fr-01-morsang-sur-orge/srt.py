"""Sous-titres de FR-01 Morsang-sur-Orge : le texte lu, en morceaux courts, sur le temps de la vidéo."""
import sys
sys.path.insert(0, "/home/claude/fr01")
from temps import *
REMPL = [("vingt-cinq octobre mille neuf cent nonante et un", "25 octobre 1991"), ("vingt-cinq février mille neuf cent nonante-deux", "25 février 1992"),
         ("vingt-sept octobre mille neuf cent nonante-cinq", "27 octobre 1995"), ("mille neuf cent nonante et un", "1991"),
         ("mille neuf cent nonante-cinq", "1995"), ("L cent trente et un-deux", "L. 131-2"), ("dix mille francs", "10 000 francs"), ("trois éléments", "3 éléments")]
MAXC = 42          # standard : une ligne courte, lisible sur téléphone
PETITS = {"l", "à", "de", "du", "des", "le", "la", "les", "un", "une", "et", "ou", "en", "au", "aux", "que", "qui", "ne", "se", "sa", "son", "ses", "leur", "leurs", "ce", "cette", "ces", "par", "pour", "sur", "dans", "avec", "sans", "est", "a", "il", "elle", "ils", "elles", "on", "y", "plus", "très", "d'un", "d'une", "qu'il", "qu'elle", "qu'une", "qu'un"}
import difflib, re as _re
def h(t):
    ms = int(round(t * 1000)); return f"{ms // 3600000:02d}:{ms // 60000 % 60:02d}:{ms // 1000 % 60:02d},{ms % 1000:03d}"
def _n(x): return _re.sub(r"[^\w]", "", x.lower())
def mots_affiches(p):
    """Les mots affichés (chiffres arabes) avec leurs instants, repris des mots lus (nombres en lettres)."""
    brut = p["texte"]; txt = brut
    for a, b in REMPL: txt = txt.replace(a, b).replace(a.capitalize(), b)
    D = txt.split(); Sx = p.get("mots") or []
    if not Sx:
        tot = sum(len(m) + 1 for m in D); t = p["debut"]; out = []
        for m in D:
            e = t + (p["fin"] - p["debut"]) * (len(m) + 1) / tot; out.append([m, t, e]); t = e
        return out
    out = [None] * len(D)
    for tag, i1, i2, j1, j2 in difflib.SequenceMatcher(None, [_n(w["mot"]) for w in Sx], [_n(m) for m in D], autojunk=False).get_opcodes():
        if tag == "equal":
            for k in range(i2 - i1): out[j1 + k] = [D[j1 + k], Sx[i1 + k]["debut"], Sx[i1 + k]["fin"]]
        elif j2 > j1:
            a = Sx[i1]["debut"] if i2 > i1 else (Sx[i1 - 1]["fin"] if i1 else p["debut"]); b = Sx[i2 - 1]["fin"] if i2 > i1 else a
            tot = sum(len(m) + 1 for m in D[j1:j2]); t = a
            for k in range(j1, j2):
                e = t + (b - a) * (len(D[k]) + 1) / tot; out[k] = [D[k], t, e]; t = e
    return out
def decoupe(ms):
    """Coupe en lignes de MAXC caractères au plus : de préférence après une ponctuation, jamais sur un petit mot."""
    n = len(ms); INF = 1e9; best = [INF] * (n + 1); prev = [0] * (n + 1); best[0] = 0
    for j in range(1, n + 1):
        for i in range(max(0, j - 12), j):
            L = len(" ".join(m[0] for m in ms[i:j]))
            if L > MAXC and j - i > 1: continue
            if i > 0 and ms[i][0] in (":", "?", "!", ";", "»"): continue
            dernier = ms[j - 1][0]; c = 0.04 * (L - 32) ** 2 + (14 if L < 14 and (i > 0 or j < n) else 0)
            if j < n:
                if dernier[-1] in ",;:.?!": c -= 7
                if _n(dernier) in PETITS or dernier in (":", "«"): c += 12
            if best[i] + c + 3 < best[j]: best[j] = best[i] + c + 3; prev[j] = i
    cp = []; j = n
    while j > 0: cp.append((prev[j], j)); j = prev[j]
    return [ms[a:b] for a, b in reversed(cp)]
def blocs():
    """[(début vidéo, fin vidéo, [(mot, début vidéo, fin vidéo)])] pour tout le texte."""
    cles = sorted(PH); out = []
    for i, c in enumerate(cles):
        p = PH[c]; suiv = PH[cles[i + 1]]["debut"] if i + 1 < len(cles) else p["fin"] + 1
        lignes = decoupe(mots_affiches(p))
        for k, L in enumerate(lignes):
            d = M(L[0][1]) if k else M(min(p["debut"], L[0][1]))
            f = M(lignes[k + 1][0][1]) if k < len(lignes) - 1 else min(M(p["fin"]) + 0.4, M(suiv) - 0.05)
            f = max(f, d + 0.3); out.append((d, f, [(m, M(a), M(b)) for m, a, b in L]))
    for k in range(len(out) - 1):            # jamais deux lignes à l'écran en même temps
        if out[k][1] > out[k + 1][0]: out[k] = (out[k][0], out[k + 1][0], out[k][2])
    return out
if __name__ == "__main__":
    B_ = blocs()
    open(sys.argv[1], "w").write("\n".join(f"{n}\n{h(d)} --> {h(f)}\n{' '.join(m[0] for m in L)}\n" for n, (d, f, L) in enumerate(B_, 1)))
    print(len(B_), max(len(" ".join(m[0] for m in L)) for _, _, L in B_))
