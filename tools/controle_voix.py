"""Contrôles de la voix montée, à lancer après tools/alignement.py et avant tout rendu (docs/standards-grands-arrets.md, section 3).

usage : python tools/controle_voix.py arrets/atf-129-i-232-zurich

1. Coupes : aucune coupe de montage ne doit mordre sur un passage de voix voisin (fin d'une prise écartée, début de la phrase suivante).
2. Silences : aucun son à niveau de voix entre deux phrases de la narration.
3. Niveau : niveau de l'enregistrement brut et de la narration, échantillons au plafond (un limiteur qui pompe s'entend).
4. Timbre : écart au timbre de référence de la série (voix traitée de la vidéo 25), par tiers d'octave.

Le code de sortie est 1 si un contrôle 1 ou 2 échoue. Les points 3 et 4 sont des mesures : ils guident reglages.json et l'égalisation.
"""
import json
import re
import subprocess
import sys
from pathlib import Path

import numpy as np
import soundfile as sf

RACINE = Path(__file__).resolve().parents[1]
REF = RACINE / "render" / "manim" / "atf-129-i-232" / "son" / "ref25.npy"
CENTRES = 100 * 2 ** (np.arange(0, 20) / 3)


def zones(mots):
    z = {}
    for x in mots:
        a = z.setdefault(x["zone"], [x["start"], x["end"], []])
        a[1] = x["end"]
        a[2].append(x["text"])
    return sorted(z.values())


def coupes(dossier):
    zs = zones(json.loads((dossier / "transcription.json").read_text())["reponse"]["words"])
    fautes = []
    for ligne in (dossier / "montage.txt").read_text().splitlines():
        m = re.match(r"ligne (\d+), phrase (\d+) : prise gardée à ([\d.]+) s \(coupe ([\d.]+)–([\d.]+)\)", ligne)
        if not m:
            continue
        a, b = float(m.group(4)), float(m.group(5))
        for s, e, tx in zs:
            if s < a - 0.12 and a + 0.05 < e < b:
                fautes.append(f"{m.group(1)}.{m.group(2)} : le début de la coupe ({a:.2f} s) garde la fin d'un autre passage « {' '.join(tx)[-50:]} »")
            if a < s < b - 0.05 and e > b + 0.12:
                fautes.append(f"{m.group(1)}.{m.group(2)} : la fin de la coupe ({b:.2f} s) entame le passage suivant « {' '.join(tx)[:50]} »")
    return fautes


def silences(dossier, v, sr):
    t = json.loads((dossier / "timings.json").read_text())
    ph = [(l["ligne"], i, p) for l in t["lignes"] for i, p in enumerate(l["phrases"], 1)]
    pas = int(0.02 * sr)
    alertes = []
    for (la, ia, a), (lb, ib, b) in zip(ph, ph[1:]):
        x0, x1 = a["fin"] + 0.12, b["debut"] - 0.12
        s = v[int(x0 * sr):int(x1 * sr)]
        n = len(s) // pas
        if x1 - x0 < 0.06 or n < 1:
            continue
        d = 20 * np.log10(np.sqrt((s[:n * pas].reshape(n, pas) ** 2).mean(1)) + 1e-9)
        ref = 20 * np.log10(np.sqrt((v[int(a["debut"] * sr):int(a["fin"] * sr)] ** 2).mean()) + 1e-9)
        if d.max() > ref - 22:
            alertes.append(f"entre {la}.{ia} et {lb}.{ib} : son à {d.max():.0f} dB (voix à {ref:.0f} dB) vers {x0 + d.argmax() * 0.02:.2f} s de la narration — "
                           "mot en trop, ou premier mot de la phrase suivante mal daté : à écouter")
    return alertes


def spectre(x, sr):
    n = 4096
    f = np.fft.rfftfreq(n, 1 / sr)
    masques = [(f >= c / 2 ** (1 / 6)) & (f < c * 2 ** (1 / 6)) for c in CENTRES]
    seuil = 10 ** (-40 / 20) * max(1e-9, float(np.sqrt((x ** 2).mean())) / 0.05)
    acc, k = np.zeros(len(CENTRES)), 0
    for i in range(0, len(x) - n, n // 2):
        w = x[i:i + n]
        if np.sqrt((w ** 2).mean()) < seuil:
            continue
        X = np.abs(np.fft.rfft(w * np.hanning(n))) ** 2
        acc += [X[m].mean() for m in masques]
        k += 1
    s = 10 * np.log10(acc / max(k, 1) + 1e-20)
    return s - s.mean()


def lufs(fichier):
    r = subprocess.run(["ffmpeg", "-hide_banner", "-nostats", "-i", str(fichier), "-af", "ebur128", "-f", "null", "-"], capture_output=True, text=True).stderr
    m = re.findall(r"I:\s+(-?[\d.]+) LUFS", r)
    return float(m[-1]) if m else None


def coupes_dans_la_voix(dossier):
    """Une coupe placée en pleine voix tranche une syllabe (« En effet, » coupé avant « -fet ») : chaque point de coupe
    de montage.txt doit tomber là où l'enregistrement brut est silencieux (moins de −45 dB sur ±20 ms)."""
    brut = next((p for p in dossier.glob("enregistrement.*")), None)
    if brut is None: return []
    r = subprocess.run(["ffmpeg", "-v", "error", "-i", str(brut), "-ac", "1", "-ar", "16000", "-f", "f32le", "-"], capture_output=True)
    x = np.frombuffer(r.stdout, dtype=np.float32); h = 160; nb = len(x) // h
    env = 20 * np.log10(np.sqrt((x[:nb * h].reshape(nb, h).astype(float) ** 2).mean(1)) + 1e-9)
    out = []
    for l in (dossier / "montage.txt").read_text(encoding="utf-8").splitlines():
        m = re.match(r"ligne (\d+), phrase (\d+) : .*?coupe ([\d.]+)–([\d.]+)", l)
        if not m: continue
        for nom, t in (("début", float(m[3])), ("fin", float(m[4]))):
            i = int(t / 0.01); v = float(env[max(0, i - 2):i + 3].max())
            if v > -45: out.append(f"{m[1]}.{m[2]} : le {nom} de la coupe ({t:.2f} s) tombe en pleine voix ({v:.0f} dB) : une syllabe est tranchée")
    return out


def main():
    dossier = RACINE / "voice" / sys.argv[1]
    v, sr = sf.read(dossier / "narration.wav")
    echec = False
    print("1. Coupes de montage")
    f = coupes(dossier)
    echec |= bool(f)
    print("\n".join("   ✗ " + x for x in f) or "   ✓ aucune coupe ne mord sur un passage voisin")
    print("1 bis. Coupes dans le silence")
    t = coupes_dans_la_voix(dossier)
    echec |= bool(t)
    print("\n".join("   ✗ " + x for x in t) or "   ✓ chaque coupe tombe dans un silence de l'enregistrement")
    print("2. Silences entre les phrases")
    a = silences(dossier, v, sr)
    print("\n".join("   ? " + x for x in a) or "   ✓ aucun son à niveau de voix dans les silences")
    print("3. Niveau")
    brut = next((p for p in dossier.glob("enregistrement.*")), None)
    pic = float(np.abs(v).max())
    print(f"   enregistrement brut : {lufs(brut) if brut else '—'} LUFS ; narration : {lufs(dossier / 'narration.wav')} LUFS, crête {pic:.2f}, "
          f"{int((np.abs(v) > 0.985 * pic).sum())} échantillons au plafond (au-delà de quelques dizaines, baisser « niveau » dans reglages.json)")
    print("4. Timbre")
    if REF.exists():
        ref = np.load(REF)
        ref = ref - ref.mean()
        s = spectre(v, sr)
        print(f"   écart moyen à la référence (vidéo 25) : {np.abs(ref - s).mean():.1f} dB ; par tiers d'octave, de 100 Hz à 8 kHz : " + " ".join(f"{x:+.0f}" for x in s - ref))
        print("   (positif : la voix a plus d'énergie que la référence dans cette bande ; l'égalisation de son/egaliser.py corrige jusqu'à ±8 dB)")
    else:
        print("   référence absente :", REF)
    sys.exit(1 if echec else 0)


if __name__ == "__main__":
    main()
