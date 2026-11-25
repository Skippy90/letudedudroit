"""ATF 121 I 367 (repris de Zurich) : rapproche le timbre de celui de la vidéo 25, ramène chaque ligne au même niveau de voix, puis limiteur doux. Entrée et sortie : voix.wav (48 kHz, mono)."""
import sys, numpy as np, soundfile as sf
from scipy.signal import firwin2, fftconvolve
sys.path.insert(0, "/home/claude/m367")
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
# Timbre : on rapproche la voix de celle de la vidéo 25 (voix traitée, référence validée à l'écoute), ±8 dB au plus.
def spectre_de(x):
    acc = np.zeros(len(centres)); k = 0; seuil = 10 ** (-40 / 20) * max(1e-9, float(np.sqrt((x ** 2).mean())) / 0.05)
    masques = [(f >= c / 2 ** (1 / 6)) & (f < c * 2 ** (1 / 6)) for c in centres]
    for i in range(0, len(x) - n, n // 2):
        w = x[i:i + n]
        if np.sqrt((w ** 2).mean()) < seuil: continue
        X = np.abs(np.fft.rfft(w * np.hanning(n))) ** 2
        acc += [X[m_].mean() for m_ in masques]; k += 1
    return 10 * np.log10(acc / max(k, 1) + 1e-20)
REF = "/home/claude/m367/son/ref25.npy"
import os
if not os.path.exists(REF):
    r_, sr_ = sf.read("/home/claude/a25/son/voix_pre.wav"); assert sr_ == sr; np.save(REF, spectre_de(r_ if r_.ndim == 1 else r_[:, 0]))
ref = np.load(REF); ref = ref - ref.mean(); s_ = spectre_de(v); s_ = s_ - s_.mean()
g_ = np.clip(ref - s_, -8, 8); g_ = np.convolve(np.pad(g_, 1, mode="edge"), [0.25, 0.5, 0.25], mode="valid")
fr_ = np.concatenate([[0, 60], centres, [12000, sr / 2]]); gd = np.concatenate([[0, 0], g_, [g_[-1] / 2, 0]])
v = fftconvolve(v, firwin2(1025, fr_ / (sr / 2), 10 ** (gd / 20)), mode="same")
s2 = spectre_de(v); s2 = s2 - s2.mean()
print("égalisation vers la vidéo 25 :", " ".join(f"{x:+.1f}" for x in g_), "; écart moyen avant", round(float(np.abs(ref - s_).mean()), 1), "dB, après", round(float(np.abs(ref - s2).mean()), 1), "dB")
def borne(l): return 0.0 if l == 1 else (B(l) if l <= DERNIERE else len(v) / sr)
def niveau(a, b):
    x = v[int(a * sr):int(b * sr)]; p = int(0.05 * sr); k = len(x) // p; r = np.sqrt((x[:k * p].reshape(k, p) ** 2).mean(1)); r = r[r > 10 ** (-38 / 20)]
    return 20 * np.log10(np.sqrt((r ** 2).mean()) + 1e-9)
niv = {l: niveau(S(l), E(l)) for l in range(1, DERNIERE + 1)}; PLUS = 5.8; cible = float(np.median(list(niv.values()))) + PLUS   # après égalisation du timbre ; la narration est montée bas (-22 LUFS) pour ne pas solliciter le limiteur du montage
gain = np.ones(len(v)); r = int(0.05 * sr)
for l in range(1, DERNIERE + 1):
    g = 10 ** ((np.clip(cible - PLUS - niv[l], -8, 8) + PLUS) / 20); i0, i1 = int(borne(l) * sr), int(borne(l + 1) * sr); gain[i0:i1] = g
k = np.ones(r) / r; gain = np.convolve(np.pad(gain, r // 2, mode="edge"), k, mode="valid")[:len(v)]
v *= gain; pic = np.abs(v).max()
# crêtes : limiteur doux (gain réduit autour des seules crêtes qui dépassent, lissé sur 10 ms)
p = int(0.005 * sr); k_ = len(v) // p; env = np.abs(v[:k_ * p]).reshape(k_, p).max(1); env = np.maximum(env, np.roll(env, 1)); env = np.maximum(env, np.roll(env, -1))
gl = np.repeat(np.minimum(1.0, 0.93 / np.maximum(env, 1e-9)), p); gl = np.concatenate([gl, np.ones(len(v) - len(gl))])
w_ = int(0.01 * sr); gl = np.minimum(gl, np.convolve(np.pad(gl, w_ // 2, mode="edge"), np.ones(w_) / w_, mode="valid")[:len(v)])
v *= gl
sf.write("voix.wav", v, sr)
print("niveau cible", round(cible, 1), "dB ; avant :", " ".join(f"{niv[l]:.0f}" for l in range(1, DERNIERE + 1)), "; pic avant limiteur", round(pic, 2), "après", round(float(np.abs(v).max()), 2), "; échantillons touchés", round(100 * float((gl < 0.999).mean()), 2), "%")
