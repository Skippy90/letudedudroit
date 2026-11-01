"""Bande-annonce de la chaîne : rendu Manim (render/manim/bande_annonce.py) + bruitages synthétisés + sortie MP4.

Usage : python tools/bande_annonce.py [--apercu]
Sortie : out/bande-annonce.mp4. Les bruitages sont fabriqués ici (bruit et sinus filtrés) : aucun son externe,
aucune licence à gérer.
"""

import json
import subprocess
import sys
from pathlib import Path

import numpy as np
import soundfile as sf

RACINE = Path(__file__).resolve().parent.parent
FR = 48000
rnd = np.random.default_rng(7)


def env(n, attaque=0.003, chute=0.05):
    t = np.arange(n) / FR
    return np.minimum(1, t / attaque) * np.exp(-t / chute)


def passe_bas(x, a):
    y = np.zeros_like(x)
    for i in range(1, len(x)):
        y[i] = y[i - 1] + a * (x[i] - y[i - 1])
    return y


def son(nom):
    if nom == "clic":
        n = int(0.06 * FR)
        t = np.arange(n) / FR
        return 0.5 * (rnd.normal(0, 1, n) * env(n, 0.0005, 0.004) + np.sin(2 * np.pi * 2300 * t) * env(n, 0.0005, 0.012))
    if nom == "glisse":
        n = int(0.32 * FR)
        b = passe_bas(rnd.normal(0, 1, n), 0.08)
        return 0.9 * b * np.sin(np.linspace(0, np.pi, n)) ** 2
    if nom == "dechire":
        n = int(0.42 * FR)
        b = rnd.normal(0, 1, n)
        b = b - passe_bas(b, 0.15)  # aigus : le grain du papier
        grains = (rnd.random(n // 240 + 1) > 0.35).repeat(240)[:n] * rnd.uniform(0.3, 1, n // 240 + 1).repeat(240)[:n]
        return 0.55 * b * grains * np.linspace(1, 0.2, n)
    if nom == "pop":
        n = int(0.11 * FR)
        t = np.arange(n) / FR
        return 0.45 * np.sin(2 * np.pi * (520 * t + 2200 * t * t)) * env(n, 0.002, 0.035)
    if nom == "page":
        n = int(0.3 * FR)
        b = passe_bas(rnd.normal(0, 1, n), 0.25)
        return 0.6 * b * np.sin(np.linspace(0, np.pi, n))
    if nom == "tombe":
        n = int(0.35 * FR)
        t = np.arange(n) / FR
        return 0.8 * np.sin(2 * np.pi * (95 * t - 60 * t * t)) * env(n, 0.002, 0.09)
    raise ValueError(nom)


def main(apercu: bool) -> None:
    manim = RACINE / "render" / "manim"
    media = manim / "media" / "bande-annonce"
    cmd = [str(RACINE / ".venv/bin/python"), "-m", "manim", "render", "--disable_caching", "--progress_bar", "none",
           "--media_dir", str(media), "-o", "bande-annonce", "bande_annonce.py", "BandeAnnonce"]
    if apercu:
        cmd.insert(5, "-ql")
    subprocess.run(cmd, cwd=manim, check=True)
    video = next(media.rglob("bande-annonce.mp4"))
    reperes = json.loads((media / "bande-annonce-sons.json").read_text(encoding="utf-8"))
    piste = np.zeros(int((reperes["duree"] + 0.5) * FR))
    for s in reperes["sons"]:
        x = son(s["son"])
        i = int(s["t"] * FR)
        piste[i:i + len(x)] += x[: len(piste) - i]
    piste = np.tanh(piste * 1.2) * 0.8
    wav = media / "sons.wav"
    sf.write(wav, piste, FR)
    sortie = RACINE / "out" / "bande-annonce.mp4"
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(video), "-i", str(wav), "-map", "0:v", "-map", "1:a",
                    "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "18", "-c:a", "aac", "-b:a", "192k",
                    "-af", "loudnorm=I=-16:TP=-1.5", "-shortest", str(sortie)], check=True)
    print(f"Bande-annonce : {sortie}")


if __name__ == "__main__":
    main("--apercu" in sys.argv)
