"""Essai des bonhommes. Rendu : cd render/manim && python -m manim render -qh demos/bonhommes.py Essai"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import numpy as np  # noqa: E402
from manim import Line, Scene, Text, VGroup, DOWN  # noqa: E402
from bonhomme import FOND, TRAIT, Bonhomme  # noqa: E402


class Essai(Scene):
    def construct(self):
        from manim import Succession, AnimationGroup, FadeIn, FadeOut, Write
        self.camera.background_color = FOND
        sol = Line([-7.2, -3.0, 0], [7.2, -3.0, 0], color=TRAIT, stroke_width=3, stroke_opacity=0.35)
        self.add(sol)
        y = -3.0 + (0.62 + 0.6) * 1.8 + 0.05  # hanche au-dessus du sol

        # 1. Mia attend, Léo arrive en marchant.
        mia = Bonhomme("#5EC8C0", (-3.5, y), sens=1, expression="neutre", nom="Mia")
        leo = Bonhomme("#E9A5C9", (7.5, y), sens=-1, expression="neutre", nom="Léo")
        self.play(FadeIn(mia))
        self.add(leo)
        self.play(Succession(*leo.marcher(-5.0, pas=6, duree=2.4)))
        self.play(leo.vers("debout", run_time=0.4))
        # 2. Il passe sans s'arrêter ; elle tend les bras, inquiète.
        self.play(mia.vers("tend", "inquiet", run_time=0.7))
        leo.sens = 1
        self.play(Succession(*leo.marcher(4.5, pas=6, duree=2.4)))
        self.play(mia.vers("debout", "triste", run_time=0.6))
        # 3. Elle montre quelque chose, surprise ; puis lève les bras, contente.
        self.play(mia.vers("pointe", "surpris", run_time=0.6))
        self.wait(0.6)
        self.play(mia.vers("bras_ciel", "content", run_time=0.7))
        self.wait(0.8)
        self.play(FadeOut(mia), FadeOut(leo))

        # 4. Planche des expressions.
        noms = ["neutre", "content", "triste", "inquiet", "surpris", "fache"]
        rang = VGroup(*[Bonhomme(TRAIT, (-5.5 + i * 2.2, -3.0 + 1.22 * 1.2 + 0.4), expression=e, echelle=1.2) for i, e in enumerate(noms)])
        legendes = VGroup(*[Text(e.replace("fache", "fâché"), font="Inter", font_size=24, color=TRAIT).move_to([-5.5 + i * 2.2, -3.25, 0])
                            for i, e in enumerate(noms)])
        self.play(FadeIn(rang), FadeIn(legendes))
        self.wait(1.5)
