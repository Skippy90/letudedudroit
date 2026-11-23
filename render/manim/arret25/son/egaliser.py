"""Arrêt 25 : l'enregistrement a été fait en trois temps (lignes 1-9, 10-35, 36-50), à des distances du micro différentes.
On rapproche le timbre des parties 1 et 3 de celui de la partie 2 (égalisation douce, ±6 dB au plus), puis on
ramène chaque ligne au même niveau de voix. Entrée et sortie : voix.wav (48 kHz, mono)."""
import sys, numpy as np, soundfile as sf
from scipy.signal import firwin2, fftconvolve
sys.path.insert(0, "/home/claude/a25")
from temps import S, E, B, DERNIERE, DUREE
v, sr = sf.read("voix.wav"); n = 4096; f = np.fft.rfftfreq(n, 1 / sr)
centres = 100 * 2 ** (np.arange(0, 20) / 3)          # tiers d'octave, 100 Hz à 8 kHz
def spectre(a, b):
    x = v[int(a * sr):int(b * sr)]; acc = np.zeros(len(centres)); k = 0
    for i in range(0, len(x) - n, n // 2):
        w = x[i:i + n]
        if np.sqrt((w ** 2).mean()) < 10 ** (-40 / 20): continue
        X = np.abs(np.fft.rfft(w * np.hanning(n))) ** 2
        acc += [X[(f >= c / 2 ** (1 / 6)) & (f < c * 2 ** (1 / 6))].mean() for c in centres]; k += 1
    return 10 * np.log10(acc / max(k, 1) + 1e-20)
def borne(l): return 0.0 if l == 1 else (B(l) if l <= DERNIERE else len(v) / sr)
PARTIES = [(1, 10), (10, 36), (36, DERNIERE + 1)]
ref = spectre(borne(10), borne(36)); ref -= ref.mean()
for l0, l1 in (PARTIES[0], PARTIES[2]):
    a, b = borne(l0), borne(l1); s = spectre(a, b); s -= s.mean()
    g = np.clip(ref - s, -6, 6); g = np.convolve(np.pad(g, 1, mode="edge"), [0.25, 0.5, 0.25], mode="valid")
    fr_ = np.concatenate([[0, 60], centres, [12000, sr / 2]]); gd = np.concatenate([[0, 0], g, [g[-1] / 2, 0]])
    h = firwin2(1025, fr_ / (sr / 2), 10 ** (gd / 20))
    i0, i1 = int(a * sr), int(b * sr); seg = fftconvolve(v[max(0, i0 - 512):i1 + 512], h, mode="same")
    seg = seg[i0 - max(0, i0 - 512):][:i1 - i0]; r = int(0.03 * sr); m = np.ones(i1 - i0); m[:r] = np.linspace(0, 1, r); m[-r:] = np.linspace(1, 0, r)
    v[i0:i1] = v[i0:i1] * (1 - m) + seg * m
    print("égalisation lignes", l0, "à", l1 - 1, ":", " ".join(f"{x:+.1f}" for x in g))
def niveau(a, b):
    x = v[int(a * sr):int(b * sr)]; p = int(0.05 * sr); k = len(x) // p; r = np.sqrt((x[:k * p].reshape(k, p) ** 2).mean(1)); r = r[r > 10 ** (-38 / 20)]
    return 20 * np.log10(np.sqrt((r ** 2).mean()) + 1e-9)
niv = {l: niveau(S(l), E(l)) for l in range(1, DERNIERE + 1)}; cible = float(np.median([niv[l] for l in range(10, 36)]))
gain = np.ones(len(v)); r = int(0.05 * sr)
for l in range(1, DERNIERE + 1):
    g = 10 ** (np.clip(cible - niv[l], -8, 8) / 20); i0, i1 = int(borne(l) * sr), int(borne(l + 1) * sr); gain[i0:i1] = g
k = np.ones(r) / r; gain = np.convolve(np.pad(gain, r // 2, mode="edge"), k, mode="valid")[:len(v)]
v *= gain; pic = np.abs(v).max()
# crêtes : limiteur doux (gain réduit autour des seules crêtes qui dépassent, lissé sur 10 ms)
p = int(0.005 * sr); k_ = len(v) // p; env = np.abs(v[:k_ * p]).reshape(k_, p).max(1); env = np.maximum(env, np.roll(env, 1)); env = np.maximum(env, np.roll(env, -1))
gl = np.repeat(np.minimum(1.0, 0.93 / np.maximum(env, 1e-9)), p); gl = np.concatenate([gl, np.ones(len(v) - len(gl))])
w_ = int(0.01 * sr); gl = np.minimum(gl, np.convolve(np.pad(gl, w_ // 2, mode="edge"), np.ones(w_) / w_, mode="valid")[:len(v)])
v *= gl
sf.write("voix.wav", v, sr)
print("niveau cible", round(cible, 1), "dB ; avant :", " ".join(f"{niv[l]:.0f}" for l in range(1, DERNIERE + 1)), "; pic avant limiteur", round(pic, 2), "après", round(float(np.abs(v).max()), 2), "; échantillons touchés", round(100 * float((gl < 0.999).mean()), 2), "%")
