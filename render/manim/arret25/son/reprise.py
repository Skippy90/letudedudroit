"""Remplace une phrase de narration.wav par une prise réenregistrée, accordée en timbre et en niveau à ses voisines,
et décale timings.json. usage : reprise.py reprise.wav a_nouv b_nouv a_anc b_anc ref_a ref_b "début de la phrase"
(a/b_nouv : bornes de la voix dans la reprise ; a/b_anc : zone remplacée dans la narration ; ref : zone voisine de référence)"""
import sys, json, numpy as np, soundfile as sf
from pathlib import Path
from scipy.signal import firwin2, fftconvolve
N = Path("/home/claude/letudedudroit/voice/arrets/25-atf-146-i-145")
src, an, bn, aa, ba, ra, rb = sys.argv[1], *map(float, sys.argv[2:8]); debut_txt = sys.argv[8]
v, sr = sf.read(N / "narration.wav"); x, sr2 = sf.read(src); assert sr == sr2
n = 4096; f = np.fft.rfftfreq(n, 1 / sr); centres = 100 * 2 ** (np.arange(0, 20) / 3)
def spectre(s):
    acc = np.zeros(len(centres)); k = 0
    for i in range(0, len(s) - n, n // 2):
        w = s[i:i + n]
        if np.sqrt((w ** 2).mean()) < 10 ** (-40 / 20): continue
        X = np.abs(np.fft.rfft(w * np.hanning(n))) ** 2
        acc += [X[(f >= c / 2 ** (1 / 6)) & (f < c * 2 ** (1 / 6))].mean() for c in centres]; k += 1
    return 10 * np.log10(acc / max(k, 1) + 1e-20)
def niveau(s):
    p = int(0.05 * sr); k = len(s) // p; r = np.sqrt((s[:k * p].reshape(k, p) ** 2).mean(1)); r = r[r > 10 ** (-38 / 20)]
    return 20 * np.log10(np.sqrt((r ** 2).mean()) + 1e-9)
ref = np.concatenate([v[int(ra * sr):int(aa * sr)], v[int(ba * sr):int(rb * sr)]])
sr_, sx = spectre(ref), spectre(x); g = np.clip((sr_ - sr_.mean()) - (sx - sx.mean()), -10, 10)
g = np.convolve(np.pad(g, 1, mode="edge"), [0.25, 0.5, 0.25], mode="valid")
fr_ = np.concatenate([[0, 60], centres, [12000, sr / 2]]); gd = np.concatenate([[0, 0], g, [g[-1] / 2, 0]])
x = fftconvolve(x, firwin2(1025, fr_ / (sr / 2), 10 ** (gd / 20)), mode="same")
m0, m1 = 0.12, 0.15; seg = x[int((an - m0) * sr):int((bn + m1) * sr)].copy()
seg *= 10 ** ((niveau(ref) - niveau(seg)) / 20)
seg *= min(1.0, 0.97 / np.abs(seg).max())   # pas d'écrêtage
r = int(0.02 * sr); seg[:r] *= np.linspace(0, 1, r); seg[-r:] *= np.linspace(1, 0, r)
i0, i1 = int(aa * sr), int(ba * sr); delta = len(seg) / sr - (ba - aa)
sf.write(N / "narration.wav", np.concatenate([v[:i0], seg, v[i1:]]), sr, subtype=sf.info(N / "narration.wav").subtype)
print("égalisation", " ".join(f"{q:+.1f}" for q in g)); print("niveau réf", round(niveau(ref), 1), "prise", round(niveau(seg), 1), "écart de timbre restant",
      round(float(np.abs((spectre(seg) - spectre(seg).mean()) - (sr_ - sr_.mean()))[2:18].mean()), 1), "dB ; décalage", round(delta, 3), "s ; pic", round(float(np.abs(seg).max()), 2))
t = json.loads((N / "timings.json").read_text()); fait = False
def dec(o):
    if isinstance(o, dict):
        for k in ("debut", "fin", "duree"):
            if isinstance(o.get(k), (int, float)) and o[k] >= ba - 0.3: o[k] = round(o[k] + delta, 3)
        for q in o.values(): dec(q)
    elif isinstance(o, list):
        for q in o: dec(q)
for l in t["lignes"]:
    for p in l["phrases"]:
        if p["texte"].startswith(debut_txt):
            a, b = aa + m0, aa + m0 + (bn - an); tot = sum(len(w["mot"]) + 1 for w in p["mots"]); c = a
            for w in p["mots"]:
                e = c + (b - a) * (len(w["mot"]) + 1) / tot; w["debut"], w["fin"] = round(c, 3), round(e, 3); c = e
            p["debut"], p["fin"] = round(a, 3), round(b, 3); fait = True
        else: dec(p)
    for k in ("debut", "fin"):
        if l[k] >= ba - 0.3: l[k] = round(l[k] + delta, 3)
assert fait
if isinstance(t.get("duree"), (int, float)): t["duree"] = round(t["duree"] + delta, 3)
(N / "timings.json").write_text(json.dumps(t, ensure_ascii=False, indent=1), encoding="utf-8")
