"""Essai : personnages en bâtons, articulés, avec visage expressif.

Rendu : cd render/manim && python -m manim render -qh demos/bonhommes.py Essai
Un bonhomme est défini par des angles (tronc, bras, avant-bras, cuisses, jambes) ; une pose est un jeu d'angles,
et passer d'une pose à l'autre interpole les angles : les membres pivotent aux articulations au lieu de se déformer.
"""

import numpy as np
from manim import (Animation, Arc, Circle, Dot, Ellipse, Line, Scene, Text, UpdateFromAlphaFunc, ValueTracker, VGroup,
                   config, rate_functions, UP, DOWN, LEFT, RIGHT, PI)

FOND, TRAIT = "#0B0B0B", "#F2EFE6"
ROUGE = "#DA291C"

# Angles en degrés, 0 = vers le bas ; positif = vers l'avant (le sens où regarde le bonhomme).
POSES = {
    "debout":   dict(tronc=0,  bras_g=20,  av_g=12,  bras_d=-20, av_d=-12,  cuisse_g=6,   jambe_g=0,   cuisse_d=-6,  jambe_d=0),
    "marche_a": dict(tronc=4,  bras_g=-30, av_g=-10, bras_d=30,  av_d=45,  cuisse_g=28,  jambe_g=8,   cuisse_d=-22, jambe_d=-30),
    "marche_b": dict(tronc=4,  bras_g=30,  av_g=45,  bras_d=-30, av_d=-10, cuisse_g=-22, jambe_g=-30, cuisse_d=28,  jambe_d=8),
    "tend":     dict(tronc=28, bras_g=95,  av_g=92,  bras_d=82,  av_d=86,  cuisse_g=-40, jambe_g=-55, cuisse_d=35,  jambe_d=10),
    "pointe":   dict(tronc=0,  bras_g=-20, av_g=-12,   bras_d=95,  av_d=90,  cuisse_g=6,   jambe_g=0,   cuisse_d=-6,  jambe_d=0),
    "bras_ciel": dict(tronc=-4, bras_g=145, av_g=165, bras_d=-145, av_d=-165, cuisse_g=10, jambe_g=0, cuisse_d=-10, jambe_d=0),
    "assis":    dict(tronc=-6, bras_g=20,  av_g=70,  bras_d=10,  av_d=65,  cuisse_g=90,  jambe_g=0,   cuisse_d=85,  jambe_d=-5),
    "recule":   dict(tronc=-14, bras_g=60, av_g=120, bras_d=45,  av_d=110, cuisse_g=-25, jambe_g=-30, cuisse_d=20,  jambe_d=5),
}


def direction(deg, sens):
    a = np.radians(deg) * sens
    return np.array([np.sin(a), -np.cos(a), 0])


class Visage(VGroup):
    """Deux yeux, sourcils et bouche ; l'expression change la bouche et les sourcils."""

    def __init__(self, centre, r, sens, expression, couleur):
        self_ep = 7
        dx = 0.12 * r * sens  # le visage regarde un peu vers l'avant
        yeux = VGroup(*[Dot([centre[0] + dx + s * 0.32 * r, centre[1] + 0.08 * r, 0], radius=0.09 * r, color=couleur)
                        for s in (-1, 1)])
        bouche_y = centre[1] - 0.4 * r
        if expression == "content":
            bouche = Arc(radius=0.34 * r, start_angle=PI + 0.5, angle=PI - 1.0, color=couleur, stroke_width=self_ep)
            bouche.move_to([centre[0] + dx, bouche_y, 0])
        elif expression in ("triste", "inquiet"):
            bouche = Arc(radius=0.34 * r, start_angle=0.5, angle=PI - 1.0, color=couleur, stroke_width=self_ep)
            bouche.move_to([centre[0] + dx, bouche_y - 0.04 * r, 0])
        elif expression == "surpris":
            bouche = Circle(radius=0.11 * r, color=couleur, stroke_width=self_ep).move_to([centre[0] + dx, bouche_y, 0])
        else:
            bouche = Line([centre[0] + dx - 0.2 * r, bouche_y, 0], [centre[0] + dx + 0.2 * r, bouche_y, 0],
                          color=couleur, stroke_width=self_ep)
        parts = [yeux, bouche]
        visibles = expression in ("inquiet", "triste", "fache")
        pente = -1 if expression == "fache" else 1
        for s in (-1, 1):  # sourcils toujours présents (invisibles au besoin) : même structure d'une image à l'autre
            if True:
                x0 = centre[0] + dx + s * 0.32 * r
                y = centre[1] + 0.34 * r
                parts.append(Line([x0 - 0.14 * r, y + s * pente * 0.06 * r, 0], [x0 + 0.14 * r, y - s * pente * 0.06 * r, 0],
                                  color=couleur, stroke_width=self_ep, stroke_opacity=1 if visibles else 0))
        super().__init__(*parts)


class Bonhomme(VGroup):
    """Bonhomme en bâtons : trait d'une seule couleur, articulé par des angles."""

    TAILLE = dict(tronc=1.0, bras=0.55, av=0.5, cuisse=0.62, jambe=0.6, tete=0.42)

    def __init__(self, couleur=TRAIT, position=(0, 0), sens=1, pose="debout", expression="neutre",
                 epaisseur=9, echelle=1.8, nom=None):
        super().__init__()
        self.couleur, self.sens, self.epaisseur, self.echelle = couleur, sens, epaisseur, echelle
        self.hanche = np.array([position[0], position[1], 0.0])
        self.angles = dict(POSES[pose])
        self.expression = expression
        self.nom = nom
        self.dessiner()

    def dessiner(self):
        t, k, s, a = self.TAILLE, self.echelle, self.sens, self.angles
        trait = dict(color=self.couleur, stroke_width=self.epaisseur)
        h = self.hanche
        epaule = h + direction(a["tronc"] + 180, s) * t["tronc"] * k
        cou = epaule + direction(a["tronc"] + 180, s) * 0.12 * k
        tete_c = cou + direction(a["tronc"] + 180, s) * t["tete"] * k
        membres = []
        for cote in ("g", "d"):
            coude = epaule + direction(a[f"bras_{cote}"], s) * t["bras"] * k
            main = coude + direction(a[f"av_{cote}"], s) * t["av"] * k
            genou = h + direction(a[f"cuisse_{cote}"], s) * t["cuisse"] * k
            pied = genou + direction(a[f"jambe_{cote}"], s) * t["jambe"] * k
            membres += [Line(epaule, coude, **trait), Line(coude, main, **trait),
                        Line(h, genou, **trait), Line(genou, pied, **trait)]
            # main et pied : petites ellipses, comme un trait de feutre
            membres.append(Ellipse(width=0.16 * k, height=0.1 * k, **trait).move_to(main + direction(a[f"av_{cote}"], s) * 0.06 * k))
            membres.append(Ellipse(width=0.24 * k, height=0.09 * k, **trait).move_to(pied + np.array([0.08 * k * s, 0, 0])))
        tronc = Line(h, cou, **trait)
        tete = Circle(radius=t["tete"] * k, **trait).move_to(tete_c)
        visage = Visage(tete_c, t["tete"] * k, s, self.expression, self.couleur)
        neufs = [tronc, *membres, tete, visage]
        if self.nom:
            etiquette = Text(self.nom, font="Inter", font_size=26, color=TRAIT)
            etiquette.next_to(VGroup(*neufs), DOWN, buff=0.18)
            neufs.append(etiquette)
        if len(self.submobjects) == len(neufs):  # mise à jour sur place : pas de restes d'images précédentes
            for ancien, neuf in zip(self.submobjects, neufs):
                ancien.become(neuf)
        else:
            self.submobjects = neufs

    def vers(self, pose=None, expression=None, deplacement=(0, 0), **reglages):
        """Animation : passe à une pose (angles interpolés) et, au besoin, se déplace.
        L'état de départ est lu au début de l'animation, pas à sa création : les pas s'enchaînent."""
        return ChangerPose(self, pose, expression, deplacement, **reglages)

    def marcher(self, distance, pas=4, duree=2.0):
        """Plusieurs animations de pas, à jouer en Succession."""
        d = distance / pas
        return [self.vers("marche_a" if i % 2 == 0 else "marche_b", deplacement=(d, 0), run_time=duree / pas,
                          rate_func=rate_functions.linear) for i in range(pas)]


class ChangerPose(Animation):
    def __init__(self, bonhomme, pose, expression, deplacement, **reglages):
        self.pose, self.expr, self.depl = pose, expression, np.array([deplacement[0], deplacement[1], 0.0])
        super().__init__(bonhomme, **reglages)

    def begin(self):
        b = self.mobject
        self.depart = dict(b.angles)
        self.arrivee = dict(POSES[self.pose]) if self.pose else dict(b.angles)
        self.h0 = b.hanche.copy()
        self.expr = self.expr or b.expression
        super().begin()

    def interpolate_mobject(self, alpha):
        b, a = self.mobject, self.rate_func(alpha)
        b.angles = {c: self.depart[c] + (self.arrivee[c] - self.depart[c]) * a for c in self.depart}
        b.hanche = self.h0 + self.depl * a
        if a > 0.3:
            b.expression = self.expr
        b.dessiner()


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
