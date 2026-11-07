"""Planche des pictogrammes. Rendu : THEME=constitution python -m manim render -s -qh demos/pictos_planche.py Planche"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from manim import Scene  # noqa: E402
import charte as c  # noqa: E402
import pictos  # noqa: E402


class Planche(Scene):
    def construct(self):
        self.camera.background_color = c.FOND
        noms = sorted(pictos.FONCTIONS)
        par_rang = 13
        for k, n in enumerate(noms):
            i, j = k % par_rang, k // par_rang
            x, y = -6.5 + 1.08 * i, 3.4 - 1.12 * j
            p = c.Picto(n, [x, y + 0.12, 0], 0.62)
            t = c.texte(n, 13, c.TEXTE).move_to([x, y - 0.5, 0])
            self.add(p, t)
