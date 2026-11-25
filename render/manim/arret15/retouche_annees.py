"""Ligne 28, phrase 3 : l'enregistrement dit « nés à Lucerne en 1979 et 1980 », l'arrêt dit 1981 et 1979 (consid. 2.3.1).
Les années sont retirées de la narration montée : « …, nés à Lucerne, ont essuyé un refus. »"""
import json, shutil, numpy as np, soundfile as sf
from pathlib import Path
D = Path(__file__).resolve().parents[3] / "voice/arrets/15-atf-129-i-217"
A, B = 407.545, 410.02
if not (D / "narration-brute.wav").exists():
    shutil.copy(D / "narration.wav", D / "narration-brute.wav"); shutil.copy(D / "timings.json", D / "timings-bruts.json")
s, fr = sf.read(D / "narration-brute.wav"); t = json.loads((D / "timings-bruts.json").read_text())
a, b, f = int(A * fr), int(B * fr), int(0.012 * fr)
r = np.linspace(1, 0, f)
g = s[:a].copy(); g[-f:] *= r if s.ndim == 1 else r[:, None]
d = s[b:].copy(); d[:f] *= r[::-1] if s.ndim == 1 else r[::-1, None]
sf.write(D / "narration.wav", np.concatenate([g, d]), fr, subtype="PCM_16")
dt = B - A
def dec(x): return round(x - dt, 3) if x >= B else (round(min(x, A), 3))
for l in t["lignes"]:
    for p in l["phrases"]:
        if l["ligne"] == 28 and p is l["phrases"][2]:
            p["texte"] = "À l'inverse, deux candidats originaires de l'ex-Yougoslavie, nés à Lucerne, ont essuyé un refus."
            p["mots"] = [m for m in p["mots"] if not (A - 0.05 <= m["debut"] < B - 0.4)]
        p["debut"], p["fin"] = dec(p["debut"]), dec(p["fin"])
        for m in p.get("mots", []): m["debut"], m["fin"] = dec(m["debut"]), dec(m["fin"])
    l["debut"], l["fin"] = l["phrases"][0]["debut"], l["phrases"][-1]["fin"]
t["duree"] = round(t["duree"] - dt, 3); t["retouche"] = "ligne 28, phrase 3 : années retirées (2,475 s), voir montage.txt"
(D / "timings.json").write_text(json.dumps(t, ensure_ascii=False, indent=1))
print("ok", t["duree"], [m["mot"] for m in t["lignes"][27]["phrases"][2]["mots"]])

# Ligne 2, phrase 3 : la coupe gardait l'attaque d'une prise écartée (« Le… ») juste après « rejetées ». Ce fragment est éteint.
s2, fr2 = sf.read(D / "narration.wav"); i0, i1 = int(23.70 * fr2), int(23.88 * fr2); k = int(0.02 * fr2)
env = np.ones(i1 - i0) * 0.004; env[:k] = np.linspace(1, 0.004, k)
s2[i0:i1] *= env if s2.ndim == 1 else env[:, None]
sf.write(D / "narration.wav", s2, fr2, subtype="PCM_16"); print("fragment éteint")

# Ligne 34, phrase 1 : même défaut, l'attaque d'une prise écartée (« Le… ») reste collée à la fin de la coupe. Elle est éteinte.
tt = json.loads((D / "timings.json").read_text()); f34 = tt["lignes"][33]["phrases"][0]["fin"]
s3, fr3 = sf.read(D / "narration.wav"); i0, i1 = int((f34 - 0.10) * fr3), int((f34 + 0.03) * fr3); k = int(0.015 * fr3)
env = np.ones(i1 - i0) * 0.004; env[:k] = np.linspace(1, 0.004, k)
s3[i0:i1] *= env if s3.ndim == 1 else env[:, None]
sf.write(D / "narration.wav", s3, fr3, subtype="PCM_16"); print("fragment 34.1 éteint à", round(f34, 2))
