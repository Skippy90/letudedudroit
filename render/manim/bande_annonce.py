"""Bande-annonce de la chaîne (10 s, 1920 × 1080), entièrement en code, aux couleurs de la marque.

Rendu : make bande-annonce (voir tools/bande_annonce.py, qui ajoute les bruitages et la sortie dans out/).

Scénario : un clic sur un bouton « lecture » en papier rouge ; la feuille se déchire sur les trois univers de la
chaîne (la rue et ses trois cas, le bâtiment de l'infraction, le Code pénal) ; le nom tombe en place ; un clic
sur « S'abonner » conclut. Chaque instant fort est noté dans media/bande-annonce-sons.json pour les bruitages.
"""

import json
import random
from pathlib import Path

import numpy as np
from manim import (
    DOWN, LEFT, ORIGIN, RIGHT, UP, AnimationGroup, Circle, Create, FadeIn, FadeOut, Line, Polygon,
    RoundedRectangle, Scene, VGroup, Write, config, there_and_back, rate_functions,
)

import charte as c

config.pixel_width, config.pixel_height, config.frame_rate = 1920, 1080, 30
config.background_color = c.FOND

L, H = config.frame_width, config.frame_height  # 14.22 × 8
PAPIER = c.ROUGE_MARQUE
CHAIR = "#F6E9E2"  # cœur blanc du papier, visible sur le bord déchiré


def bord_dechire(a, b, n=26, amplitude=0.22, graine=0):
    """Points d'une ligne déchirée de a à b (dents irrégulières)."""
    rnd = random.Random(graine)
    a, b = np.array(a, float), np.array(b, float)
    normale = np.array([-(b - a)[1], (b - a)[0], 0])
    normale /= np.linalg.norm(normale)
    pts = []
    for k in range(n + 1):
        t = k / n
        decal = 0 if k in (0, n) else rnd.uniform(-amplitude, amplitude)
        pts.append(a + (b - a) * t + normale * decal)
    return pts


class Feuille(VGroup):
    """Une feuille de papier rouge plein écran, prête à se déchirer en deux (verticalement ou horizontalement)."""

    def __init__(self, vertical=True, graine=0):
        m = 0.6  # marge hors cadre
        if vertical:
            dechirure = bord_dechire([0.3, H / 2 + m, 0], [-0.3, -H / 2 - m, 0], graine=graine)
            gauche = Polygon([-L / 2 - m, H / 2 + m, 0], *dechirure, [-L / 2 - m, -H / 2 - m, 0])
            droite = Polygon([L / 2 + m, H / 2 + m, 0], *dechirure, [L / 2 + m, -H / 2 - m, 0])
            self.sens = (LEFT, RIGHT)
        else:
            dechirure = bord_dechire([-L / 2 - m, -0.2, 0], [L / 2 + m, 0.25, 0], graine=graine)
            gauche = Polygon([-L / 2 - m, H / 2 + m, 0], *dechirure, [L / 2 + m, H / 2 + m, 0])
            droite = Polygon([-L / 2 - m, -H / 2 - m, 0], *dechirure, [L / 2 + m, -H / 2 - m, 0])
            self.sens = (UP, DOWN)
        for moitie in (gauche, droite):
            moitie.set_fill(PAPIER, 1).set_stroke(width=0)
        # Le cœur blanc du papier, sur chaque lèvre de la déchirure (décalé d'un cheveu, irrégulier).
        levres = []
        for moitie, signe in ((gauche, 1), (droite, -1)):
            decal = (np.array(self.sens[0]) if signe == 1 else np.array(self.sens[1])) * 0.05
            fibre = VGroup(*[Line(p + decal * random.Random(i).uniform(0.4, 1.4), q + decal, color=CHAIR,
                                  stroke_width=5) for i, (p, q) in enumerate(zip(dechirure, dechirure[1:]))])
            levres.append(fibre)
        super().__init__(VGroup(gauche, levres[0]), VGroup(droite, levres[1]))

    def ouvrir(self):
        return AnimationGroup(self[0].animate.shift(np.array(self.sens[0]) * 9),
                              self[1].animate.shift(np.array(self.sens[1]) * 9),
                              rate_func=rate_functions.ease_in_cubic)


def curseur():
    fleche = Polygon([0, 0, 0], [0, -0.62, 0], [0.16, -0.48, 0], [0.3, -0.78, 0], [0.4, -0.73, 0],
                     [0.27, -0.44, 0], [0.47, -0.44, 0])
    return fleche.set_fill("#FFFFFF", 1).set_stroke(c.FOND, 3)


def symbole(taille=1.6):
    """Le logo (docs/marque/symbole.svg) redessiné : carré rouge arrondi, toit, trois étages."""
    k = taille / 512
    fond = RoundedRectangle(corner_radius=104 * k, width=taille, height=taille, stroke_width=0,
                            fill_color=c.ROUGE_MARQUE, fill_opacity=1)
    p = lambda x, y: [(x - 256) * k, (256 - y) * k, 0]
    toit = VGroup(Line(p(112, 200), p(256, 104)), Line(p(256, 104), p(400, 200))).set_stroke("#FFFFFF", 20 * taille * 135 / 512)
    etages = VGroup(*[RoundedRectangle(corner_radius=10 * k, width=212 * k, height=52 * k, stroke_width=0,
                                       fill_color="#FFFFFF", fill_opacity=o).move_to(p(256, y + 26))
                      for y, o in ((216, 1), (284, 0.85), (352, 0.7))])
    return VGroup(fond, toit, etages)


class BandeAnnonce(Scene):
    def setup(self):
        self.sons = []

    def son(self, nom, decalage=0.0):
        self.sons.append({"son": nom, "t": round(self.time + decalage, 3)})
        print("REPERE", nom, round(self.time, 2))

    def dechirer(self, ancien, nouveau, vertical, graine):
        """La feuille rouge recouvre l'ancienne scène, puis se déchire sur la nouvelle."""
        feuille = Feuille(vertical, graine)
        feuille.shift(DOWN * 9 if vertical else LEFT * 15)
        self.add(feuille)
        self.son("glisse")
        self.play(feuille.animate.shift(UP * 9 if vertical else RIGHT * 15), run_time=0.3,
                  rate_func=rate_functions.ease_out_cubic)
        self.remove(*ancien)
        self.add(*nouveau)
        self.bring_to_front(feuille)
        self.son("dechire")
        self.play(feuille.ouvrir(), run_time=0.45)
        self.remove(feuille)

    def construct(self):
        # 1. Le bouton « lecture » en papier, et un clic.
        bouton = RoundedRectangle(corner_radius=0.35, width=3.0, height=2.1, stroke_width=0,
                                  fill_color=PAPIER, fill_opacity=1)
        triangle = Polygon([-0.35, 0.5, 0], [-0.35, -0.5, 0], [0.55, 0, 0]).set_fill("#FFFFFF", 1).set_stroke(width=0)
        lecture = VGroup(bouton, triangle)
        souris = curseur().move_to([4.2, -2.6, 0])
        self.play(FadeIn(lecture, scale=0.85), FadeIn(souris), run_time=0.4)
        self.play(souris.animate.move_to([0.45, -0.35, 0]), run_time=0.55, rate_func=rate_functions.ease_in_out_cubic)
        self.son("clic")
        self.play(lecture.animate(rate_func=there_and_back).scale(0.9), run_time=0.2)

        # 2. Déchirure → la rue : trois jeunes, trois actes, trois catégories.
        rue = c.Rue()
        noms = [("Inès", "rose", -3.6), ("Noah", "turquoise", 1.6), ("Yann", "bleu_clair", 4.6)]
        gens = []
        for nom, couleur, x in noms:
            p = c.Personnage(nom, c.COULEURS_PERSONNAGES[couleur], "centre")
            p.silhouette.scale(0.8, about_edge=DOWN)
            p.etiquette.next_to(p.silhouette, DOWN, buff=0.2)
            p.shift(np.array([x, c.Y_SOL, 0]) - p.silhouette.get_bottom())
            gens.append(p)
        self.dechirer([lecture, souris], [rue, *gens], vertical=True, graine=3)
        questions = [c.Etiquette(t, [x, 1.75, 0]) for t, x in
                     (("Crime ?", -3.6), ("Délit ?", 0.6), ("Contravention ?", 4.4))]
        for q in questions:
            self.son("pop")
            self.play(FadeIn(q, shift=DOWN * 0.25, scale=1.15), run_time=0.27)
        self.wait(0.25)

        # 3. Déchirure → le bâtiment de l'infraction, qui s'allume étage par étage.
        batiment = c.Batiment().shift(UP * 0.7)
        self.dechirer([rue, *gens, *questions], [batiment], vertical=False, graine=7)
        for n in (1, 2, 3):
            self.son("pop")
            self.play(batiment.colorer(n, "vert"), run_time=0.27)
        self.wait(0.2)

        # 4. Déchirure → le Code pénal qui s'ouvre, l'article en bas.
        livre = c.Livre().move_to([0, 0.5, 0])
        self.dechirer([batiment], [livre], vertical=True, graine=11)
        pages = livre.ouvert()
        article = c.BlocArticle("Art. 1 CP")
        self.son("page")
        self.play(FadeOut(livre), FadeIn(pages), FadeIn(article, shift=UP * 0.2), run_time=0.45)
        self.wait(0.25)

        # 5. Le nom tombe en place, avec le logo.
        logo = symbole(1.7).move_to([-4.05, 0.55, 0])
        haut = c.texte("L'étude", 96, gras=True)
        bas = c.pastille(c.texte("du droit", 96, "#FFFFFF", gras=True), buff=0.14)
        titre = VGroup(haut, bas).arrange(DOWN, aligned_edge=LEFT, buff=0.18).next_to(logo, RIGHT, buff=0.55)
        titre.align_to(logo, UP).shift(UP * 0.12)
        accroche = c.texte("Le droit suisse, une notion à la fois", c.T_SOUS_TITRE, c.GRIS)
        VGroup(logo, titre).move_to([0, 0.6, 0])
        accroche.next_to(VGroup(logo, titre), DOWN, buff=0.5)
        self.dechirer([pages, article], [], vertical=False, graine=19)
        self.son("tombe")
        self.play(FadeIn(logo, scale=1.4), FadeIn(haut, shift=DOWN * 0.8), run_time=0.3,
                  rate_func=rate_functions.ease_out_back)
        self.son("tombe")
        self.play(FadeIn(bas, shift=UP * 0.6), run_time=0.3, rate_func=rate_functions.ease_out_back)
        self.play(FadeIn(accroche, shift=UP * 0.15), run_time=0.35)

        # 6. « S'abonner », un clic, « Abonné ».
        abonner = c.pastille(c.texte("S'abonner", c.T_CORPS, "#FFFFFF", gras=True), buff=0.22)
        abonner.next_to(accroche, DOWN, buff=0.55)
        abonne = VGroup(RoundedRectangle(corner_radius=0.1, width=abonner.width, height=abonner.height,
                                         stroke_width=0, fill_color=c.SURFACE, fill_opacity=1),
                        c.texte("Abonné ✓", c.T_CORPS, c.TEXTE, gras=True)).move_to(abonner)
        abonne[1].move_to(abonne[0])
        souris = curseur().move_to([4.5, -3.4, 0])
        self.play(FadeIn(abonner, scale=0.9), FadeIn(souris), run_time=0.3)
        self.play(souris.animate.move_to(abonner.get_right() + np.array([0.05, -0.38, 0])), run_time=0.45,
                  rate_func=rate_functions.ease_in_out_cubic)
        self.son("clic")
        self.play(abonner.animate(rate_func=there_and_back).scale(0.92), run_time=0.18)
        self.remove(abonner)
        self.add(abonne)
        self.bring_to_front(souris)
        self.wait(max(0.5, 10.0 - self.time - 0.4))
        self.play(FadeOut(souris), run_time=0.4)

        sortie = Path(config.media_dir) / "bande-annonce-sons.json"
        sortie.write_text(json.dumps({"duree": round(self.time, 3), "sons": self.sons}, indent=1), encoding="utf-8")
