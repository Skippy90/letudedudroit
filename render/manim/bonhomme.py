"""Personnages en bâtons, articulés, avec visage expressif (charte depuis novembre 2026).

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
    # Actions : tendre un objet, se pencher pour prendre, porter à bout de bras, gestes de la parole.
    "donne":    dict(tronc=6,  bras_g=15,  av_g=10,  bras_d=70,  av_d=78,  cuisse_g=12,  jambe_g=0,   cuisse_d=-8,  jambe_d=0),
    "prend":    dict(tronc=34, bras_g=40,  av_g=30,  bras_d=55,  av_d=25,  cuisse_g=20,  jambe_g=-25, cuisse_d=-10, jambe_d=-5),
    "porte":    dict(tronc=0,  bras_g=20,  av_g=12,  bras_d=36,  av_d=40,  cuisse_g=6,   jambe_g=0,   cuisse_d=-6,  jambe_d=0),
    "parle_a":  dict(tronc=2,  bras_g=20,  av_g=12,  bras_d=40,  av_d=120, cuisse_g=6,   jambe_g=0,   cuisse_d=-6,  jambe_d=0),
    "parle_b":  dict(tronc=0,  bras_g=35,  av_g=95,  bras_d=25,  av_d=70,  cuisse_g=6,   jambe_g=0,   cuisse_d=-6,  jambe_d=0),
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
        self.mains = {}
        for cote in ("g", "d"):
            coude = epaule + direction(a[f"bras_{cote}"], s) * t["bras"] * k
            main = coude + direction(a[f"av_{cote}"], s) * t["av"] * k
            genou = h + direction(a[f"cuisse_{cote}"], s) * t["cuisse"] * k
            pied = genou + direction(a[f"jambe_{cote}"], s) * t["jambe"] * k
            self.mains[cote] = main + direction(a[f"av_{cote}"], s) * 0.06 * k
            membres += [Line(epaule, coude, **trait), Line(coude, main, **trait),
                        Line(h, genou, **trait), Line(genou, pied, **trait)]
            # main et pied : petites ellipses, comme un trait de feutre
            membres.append(Ellipse(width=0.16 * k, height=0.1 * k, **trait).move_to(main + direction(a[f"av_{cote}"], s) * 0.06 * k))
            membres.append(Ellipse(width=0.24 * k, height=0.09 * k, **trait).move_to(pied + np.array([0.08 * k * s, 0, 0])))
        tronc = Line(h, cou, **trait)  # toujours en premier : synchroniser() le relit
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

    def main(self, cote="d"):
        """Position de la main, calculée sur le dessin tel qu'il est (même après un shift ou un scale extérieur)."""
        tronc = self.submobjects[0]
        h = np.array(tronc.get_start())
        k = np.linalg.norm(tronc.get_end() - tronc.get_start()) / (self.TAILLE["tronc"] + 0.12)
        t, s, a = self.TAILLE, self.sens, self.angles
        epaule = h + direction(a["tronc"] + 180, s) * t["tronc"] * k
        coude = epaule + direction(a[f"bras_{cote}"], s) * t["bras"] * k
        return coude + direction(a[f"av_{cote}"], s) * (t["av"] + 0.06) * k

    def synchroniser(self):
        """Relit la hanche et l'échelle sur le dessin : un déplacement ou une mise à l'échelle faits de l'extérieur
        (animate.shift, scale) sont conservés à la pose suivante."""
        tronc = self.submobjects[0]
        self.hanche = np.array(tronc.get_start())
        longueur = np.linalg.norm(tronc.get_end() - tronc.get_start())
        self.echelle = longueur / ((self.TAILLE["tronc"] + 0.12))
        self.epaisseur = tronc.get_stroke_width()

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
        b.synchroniser()
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


class Marche(Animation):
    """Marche sur une distance : les jambes et les bras alternent, puis le bonhomme se remet debout."""

    def __init__(self, bonhomme, deplacement, pas=None, sens_final=None, **reglages):
        self.depl = np.array([deplacement[0], deplacement[1], 0.0])
        self.sens_final = sens_final  # arrivé, il se tourne (vers celui à qui il a affaire)
        self.pas = pas or max(2, round(abs(deplacement[0]) / 0.7))
        super().__init__(bonhomme, **reglages)

    def begin(self):
        b = self.mobject
        b.synchroniser()
        if self.depl[0]:
            b.sens = 1 if self.depl[0] > 0 else -1
        self.h0, self.depart = b.hanche.copy(), dict(b.angles)
        super().begin()

    def interpolate_mobject(self, alpha):
        b = self.mobject
        a, bb, debout = POSES["marche_a"], POSES["marche_b"], POSES["debout"]
        phase = np.sin(alpha * self.pas * np.pi / 2) ** 2 if self.pas % 2 else (1 - np.cos(alpha * self.pas * np.pi)) / 2
        fin = max(0.0, (alpha - 0.85) / 0.15)  # les derniers 15 % : retour à la pose debout
        debut = min(1.0, alpha / 0.1)
        for c in a:
            marche = a[c] + (bb[c] - a[c]) * phase
            v = self.depart[c] + (marche - self.depart[c]) * debut
            b.angles[c] = v + (debout[c] - v) * fin
        b.hanche = self.h0 + self.depl * alpha
        if alpha >= 1 and self.sens_final:
            b.sens = self.sens_final
        b.dessiner()
