"""Arrêt 15 : pauses ajoutées (ton de pièce), bruitages calculés, mixage. Pas de musique."""
import sys, numpy as np, soundfile as sf
import os
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
SORTIE = os.environ.get("A15_SORTIE", "/tmp/a15")
from temps import *
SR = 48000
v, sr = sf.read("voix.wav"); assert sr == SR
TOTAL = M(FIN) + 15.0   # 15 s d'écran de fin muet
# ton de pièce : le passage de 0,6 s le plus calme
# ton de pièce : le passage de 0,6 s le plus calme qui ne soit pas un silence numérique
w = int(0.6 * SR); pw = int(0.02 * SR)
def niv(x): return 20 * np.log10(np.sqrt((x ** 2).mean()) + 1e-9)
def vrai(i): return min(niv(v[j:j + pw]) for j in range(i, i + w, pw)) > -78
e = [(np.abs(v[i:i + w]).mean(), i) for i in range(0, len(v) - w, SR // 10) if vrai(i)]
q = v[min(e)[1]:min(e)[1] + w].copy(); print("ton de pièce", round(niv(q), 1), "dB"); f = int(0.05 * SR); r = np.linspace(0, 1, f); q[:f] *= r; q[-f:] *= r[::-1]
def ton(n):
    out = np.zeros(n + w); p = 0
    while p < n: out[p:p + w] += q; p += w - f
    return out[:n]
# Les trous de silence numérique laissés entre deux prises sont remplis par le ton de pièce (sinon le fond « tombe »)
nb = len(v) // pw; lv = 20 * np.log10(np.sqrt((v[:nb * pw].reshape(nb, pw) ** 2).mean(1)) + 1e-9); trou = lv < -78; k = 0; rempli = 0
while k < nb:
    if trou[k]:
        j = k
        while j < nb and trou[j]: j += 1
        a, b = max(0, k * pw - pw // 2), min(len(v), j * pw + pw // 2); seg = ton(b - a); r = min(pw // 2, (b - a) // 2)
        seg[:r] *= np.linspace(0, 1, r); seg[-r:] *= np.linspace(1, 0, r); v[a:b] += seg; rempli += b - a; k = j
    else: k += 1
print("trous remplis :", round(rempli / SR, 1), "s")
morceaux, p = [], 0
fd = int(0.02 * SR); rmp = np.linspace(1, 0, fd)
for x, s in sorted(AJOUTS):
    i = int(x * SR)
    if s >= 0: morceaux += [v[p:i], ton(int(s * SR))]; p = i
    else:
        hh = int(-s * SR / 2); a = v[p:i - hh].copy(); a[-fd:] *= rmp; morceaux.append(a); p = i + hh; v[p:p + fd] *= rmp[::-1]
morceaux.append(v[p:])
voix = np.concatenate(morceaux); voix = np.concatenate([voix, ton(max(0, int(TOTAL * SR) - len(voix)))])[:int(TOTAL * SR)]
k = int(0.6 * SR); voix[-k:] *= np.linspace(1, 0, k)
rng = np.random.default_rng(15); n = len(voix); fx = np.zeros((n, 2))
def pose(t0, s, g=1.0, pan=0.5, video=False):
    a = int((t0 if video else M(t0)) * SR); m = min(len(s), n - a)
    if a < 0 or m <= 0: return
    fx[a:a + m, 0] += s[:m] * g * (1 - pan) * 2; fx[a:a + m, 1] += s[:m] * g * pan * 2
def passe_bas(x, fc):
    a = 1 - np.exp(-2 * np.pi * fc / SR); y = np.zeros_like(x); z = 0.0
    for i in range(len(x)): z += a * (x[i] - z); y[i] = z
    return y
def tampon():
    tt = np.arange(int(0.45 * SR)) / SR
    return np.sin(2 * np.pi * (70 + 60 * np.exp(-tt * 30)) * tt) * np.exp(-tt * 11) + 0.35 * passe_bas(rng.normal(size=len(tt)), 1800) * np.exp(-tt * 45) * 3
def souffle(d=0.7):
    tt = np.arange(int(d * SR)) / SR
    return passe_bas(rng.normal(size=len(tt)), 1100) * np.sin(np.pi * tt / d) ** 2 * 2.2
def pop(fq=880):
    tt = np.arange(int(0.22 * SR)) / SR
    return (np.sin(2 * np.pi * fq * tt) + 0.5 * np.sin(2 * np.pi * fq * 1.5 * tt)) * np.exp(-tt * 22) * np.clip(tt / 0.004, 0, 1)
def tic():
    tt = np.arange(int(0.05 * SR)) / SR
    return np.sin(2 * np.pi * 1500 * tt) * np.exp(-tt * 90)
Tm, P, K = tampon(), pop(), tic()
for x in (W(2, 3, "rejet") - 0.1, W(12, 2, "tardif") - 0.3, W(12, 4, "rejette") - 0.2, W(28, 3, "essuyé") - 0.2, W(32, 3, "discrimination") - 0.2,
          W(35, 1, "décision") - 0.1, W(35, 2, "contraire") - 0.2, W(37, 2, "confirme") - 0.1, S(42, 1)): pose(x, Tm, 0.5)
for l in (4, 15, 18, 19, 37): pose(B(l), souffle(1.0), 0.2)
for x in (S(3, 1) - 0.55, S(2, 1) - 0.5, S(21, 1) - 0.5, S(28, 1) - 0.5, S(43, 1) - 0.5): pose(x, souffle(0.6), 0.14)
for x in (W(2, 2, "accept") - 0.15, W(8, 2, "toutes") - 0.1, S(20, 2), S(23, 2), W(28, 2, "naturalisé") - 0.3, W(32, 1, "désavantagés") - 0.3, S(32, 2),
          W(35, 1, "admet") - 0.2, S(43, 2), W(43, 3, "interdiction") - 0.3, W(43, 3, "obligation") - 0.3): pose(x, P, 0.15)
for x in (W(9, 1, "toutes") - 0.1, S(23, 3), W(36, 2, "ne") - 0.1): pose(x, pop(330), 0.2)
for x in np.linspace(S(7, 1), S(7, 1) + 2.0, 23): pose(x, K, 0.10)
# Bruitages des personnages, notés par les scènes (instant de la section + début de la section)
import json, glob
def note(fq, d, g=1.0, att=0.005):
    tt = np.arange(int(d * SR)) / SR
    return (np.sin(2 * np.pi * fq * tt) + 0.3 * np.sin(4 * np.pi * fq * tt)) * np.exp(-tt * 5 / d) * np.clip(tt / att, 0, 1) * g
def suite(notes, d=0.09):
    out = np.zeros(int((len(notes) * d + 0.3) * SR))
    for i, fq in enumerate(notes):
        s_ = note(fq, d * 2.2); a = int(i * d * SR); out[a:a + len(s_)] += s_
    return out
def glisse(f0, f1, d):
    tt = np.arange(int(d * SR)) / SR; ph = 2 * np.pi * np.cumsum(f0 + (f1 - f0) * tt / d) / SR
    return np.sin(ph) * np.sin(np.pi * tt / d) ** 0.5
def grelot():
    out = np.zeros(int(0.7 * SR))
    for i in range(6):
        a = int(i * 0.1 * SR); out[a:a + len(K)] += K * (1 - 0.1 * i)
    return out
def fermeture():
    tt = np.arange(int(0.16 * SR)) / SR
    return passe_bas(rng.normal(size=len(tt)), 2600) * np.sin(np.pi * tt / 0.16) * 2.5 * (0.6 + 0.4 * np.sign(np.sin(2 * np.pi * 70 * tt)))
SONS = {"plop": (glisse(520, 240, 0.09), 0.5), "ding": (note(1320, 0.5), 0.3), "joie": (suite([523, 659, 784]), 0.3),
        "triste": (np.concatenate([glisse(392, 370, 0.22), glisse(311, 277, 0.34)]), 0.28), "thud": (Tm, 0.45), "hop": (glisse(420, 760, 0.07), 0.35),
        "zip": (fermeture(), 0.3), "flic": (passe_bas(rng.normal(size=int(0.07 * SR)), 5000) * np.linspace(1, 0, int(0.07 * SR)) ** 2 * 2.5, 0.3), "grelot": (grelot(), 0.5), "souffle": (souffle(0.6), 0.16)}
nb_sons = 0
for fjs in sorted(glob.glob(SORTIE + "/sons-*.json")):
    dj = json.load(open(fjs))
    for t_, nom, g_ in dj["ev"]:
        w_, g0 = SONS[nom]; pose(dj["t0"] + t_, w_, g0 * g_, video=True); nb_sons += 1
print("bruitages des personnages :", nb_sons)
sf.write("voix_p.wav", voix, SR); sf.write("bruitages.wav", np.clip(fx, -1, 1), SR)
print("total", TOTAL, len(voix) / SR)
