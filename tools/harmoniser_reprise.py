"""Harmonise une reprise enregistrée à part avec l'enregistrement principal : même timbre, même niveau de voix.

Usage : python tools/harmoniser_reprise.py <reprise.m4a> <principal.m4a> <debut_s> <duree_s> <sortie.wav>

<debut_s> et <duree_s> désignent, dans l'enregistrement principal, la première prise de la même phrase (même texte :
la comparaison ne dépend alors que du micro et de la pièce, pas des sons prononcés). L'outil mesure l'écart de
spectre par tiers d'octave sur les passages parlés, le corrige par un égaliseur (firequalizer), puis aligne le niveau
moyen de la voix. Il affiche l'écart restant.
"""

import subprocess
import sys
import tempfile
from pathlib import Path

import numpy as np
import soundfile as sf

SR = 44100
CENTRES = [100 * 2 ** (k / 3) for k in range(0, 22)]  # 100 Hz à ~12,7 kHz


def lire(fichier, debut=None, duree=None) -> np.ndarray:
    cmd = ["ffmpeg", "-nostdin", "-v", "error"] + (["-ss", str(debut), "-t", str(duree)] if debut is not None else [])
    cmd += ["-i", str(fichier), "-ac", "1", "-ar", str(SR), "-f", "f32le", "-"]
    return np.frombuffer(subprocess.run(cmd, capture_output=True, check=True).stdout, dtype=np.float32)


def mesure(x: np.ndarray):
    """Spectre moyen (par bande) et niveau moyen des trames parlées."""
    n, hop = 4096, 1024
    tr = np.lib.stride_tricks.sliding_window_view(x, n)[::hop] * np.hanning(n)
    db = 20 * np.log10(np.sqrt((tr ** 2).mean(1)) + 1e-9)
    voix = db > np.percentile(db, 40)
    sp = (np.abs(np.fft.rfft(tr[voix], axis=1)) ** 2).mean(0)
    fq = np.fft.rfftfreq(n, 1 / SR)
    bandes = np.array([10 * np.log10(sp[(fq >= c / 2 ** (1 / 6)) & (fq < c * 2 ** (1 / 6))].sum() + 1e-20) for c in CENTRES])
    return bandes, db[voix].mean()


def main(reprise, principal, debut, duree, sortie, passes=3):
    """Plusieurs passes : chaque passe corrige ce que la précédente a laissé (l'égaliseur n'est pas exact)."""
    ref_b, ref_v = mesure(lire(principal, float(debut), float(duree)))
    _, v_avant = mesure(lire(reprise))
    source = reprise
    for k in range(passes):
        passe(source, ref_b, ref_v, sortie)
        source = sortie
    b3, v3 = mesure(sf.read(sortie)[0].astype(np.float32))
    reste = (ref_b - ref_b.mean()) - (b3 - b3.mean())
    print(f"Niveau de voix : principal {ref_v:.1f} dB, reprise {v_avant:.1f} → {v3:.1f} dB")
    print("Écart de timbre restant par bande (dB) :")
    for c, z in zip(CENTRES[::3], reste[::3]):
        print(f"  {c:6.0f} Hz : {z:+5.1f}")
    print(f"Reprise harmonisée : {sortie}")


def passe(reprise, ref_b, ref_v, sortie):
    rep = lire(reprise)
    b, v = mesure(rep)
    # Écart de timbre (spectres ramenés à la même énergie), lissé et borné : on corrige une couleur, pas un mot.
    ecart = (ref_b - ref_b.mean()) - (b - b.mean())
    ecart = np.convolve(np.pad(ecart, 1, mode="edge"), [0.25, 0.5, 0.25], mode="valid").clip(-9, 9)
    entrees = ";".join(f"entry({c:.0f},{g:.2f})" for c, g in zip(CENTRES, ecart))
    with tempfile.TemporaryDirectory() as tmp:
        brut, egal = Path(tmp) / "brut.wav", Path(tmp) / "egal.wav"
        sf.write(brut, rep, SR)
        subprocess.run(["ffmpeg", "-nostdin", "-v", "error", "-y", "-i", str(brut), "-af",
                        f"firequalizer=gain_entry='{entrees}'", str(egal)], check=True)
        y, _ = sf.read(egal)
        _, v2 = mesure(y.astype(np.float32))
        y = y * 10 ** ((ref_v - v2) / 20)
        crete = np.abs(y).max()
        if crete > 0.98:
            y *= 0.98 / crete
        sf.write(sortie, y, SR)


if __name__ == "__main__":
    main(*sys.argv[1:6])
