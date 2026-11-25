"""Planche des décors (avant/après les détails) : python -m manim render -s demos/decors.py <Classe>"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import charte as c  # noqa: E402
from manim import Scene  # noqa: E402

DECORS = {"Rue": lambda: c.Rue("Électronique"), "Escalier": c.Escalier, "Appartement": c.Appartement,
          "Parc": c.Parc, "Piscine": c.Piscine, "Tribunal": c.Tribunal, "Festival": lambda: c.Festival("Festival")}


def scene_de(nom):
    class S(Scene):
        def construct(self):
            self.camera.background_color = c.FOND
            d = DECORS[nom]()
            a = c.Personnage("Mia", c.COULEURS_PERSONNAGES["turquoise"], "centre-gauche")
            b = c.Personnage("Léo", c.COULEURS_PERSONNAGES["rose"], "centre-droite")
            for p, n in ((a, -1), (b, 1)):
                p.silhouette.scale(0.8, about_edge=c.DOWN)
                p.etiquette.next_to(p.silhouette, c.DOWN, buff=0.2)
                p.shift(d.pied(n) - p.silhouette.get_bottom())
            self.add(d, a, b)
    S.__name__ = nom
    return S


for _n in DECORS:
    globals()[_n] = scene_de(_n)
