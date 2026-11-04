import sys
sys.path.insert(0, str(__import__("pathlib").Path(__file__).resolve().parent.parent))
from manim import *
import charte as c

ART15 = ["Quiconque, de manière contraire au droit,",
         "est attaqué ou menacé d’une attaque imminente",
         "a le droit de repousser l’attaque",
         "par des moyens proportionnés aux circonstances ;",
         "le même droit appartient aux tiers."]
CONDITIONS = [(1, "attaqué ou menacé", "Attaque ou menace"), (1, "imminente", "Imminente"),
              (0, "contraire au droit", "Contraire au droit"), (3, "proportionnés", "Proportionnée")]


def boite(t, couleur=c.TEXTE):
    lib = c.texte(t, c.T_PETIT)
    cadre = RoundedRectangle(corner_radius=0.12, width=lib.width + 0.6, height=0.8, color=couleur,
                             stroke_width=3, fill_color=c.SURFACE, fill_opacity=1)
    return VGroup(cadre, lib.move_to(cadre))


class Demo(Scene):
    def construct(self):
        self.camera.background_color = c.FOND
        # 1. L'article, morceau par morceau ; les mots-conditions s'allument et sortent du texte.
        loi = c.TexteLoi("Art. 15 CP", ART15, rang=0)
        self.play(FadeIn(loi.carte), FadeIn(loi.entete), FadeIn(loi.reglette), Write(loi.corps), run_time=1.6)
        extraits = {}
        for rang in range(len(ART15)):
            if rang:
                nouveau, reglette, anciens = loi.suivant(rang)
                self.play(FadeOut(loi.corps, shift=UP * 0.3), FadeOut(anciens), FadeIn(nouveau, shift=UP * 0.3),
                          Transform(loi.reglette, reglette), run_time=0.7)
                loi.corps = nouveau
            for r, frag, nom in CONDITIONS:
                if r == rang:
                    glyphes, marque = loi.souligner(frag)
                    self.play(glyphes.animate.set_color(c.ACCENT), Create(marque), run_time=0.5)
                    copie = c.texte(frag, c.T_PETIT, c.ACCENT).move_to(glyphes)
                    extraits[nom] = copie
                    self.add(copie)
                    cible = [-4.8, -1.6, 1.6, 4.8][len(extraits) - 1]
                    self.play(copie.animate.move_to([cible, -1.6, 0]),
                              run_time=0.6)
            self.wait(0.4)
        # 2. La loi se retire ; les extraits deviennent des cases de conditions qui s'alignent.
        self.play(FadeOut(VGroup(loi.carte, loi.entete, loi.corps, loi.reglette, loi.soulignes), shift=UP),
                  run_time=0.8)
        titre = c.texte("Quatre conditions", c.T_TITRE, gras=True).move_to([0, c.Y_TITRE, 0])
        boites = VGroup(*[boite(nom) for _, _, nom in CONDITIONS]).arrange(DOWN, buff=0.35).move_to([2.2, 0.2, 0])
        self.play(FadeIn(titre, shift=DOWN * 0.3),
                  *[ReplacementTransform(extraits[nom], boites[i]) for i, (_, _, nom) in enumerate(CONDITIONS)],
                  run_time=1.4)
        fleche = Arrow(boites.get_bottom() + DOWN * 0.1, boites.get_bottom() + DOWN * 0.9, color=c.TEXTE, buff=0)
        verdict = boite("Légitime défense", c.VERT).next_to(fleche, DOWN, buff=0.1)
        self.play(GrowArrow(fleche), FadeIn(verdict, shift=UP * 0.2), run_time=0.8)
        self.wait(0.6)
        # 3. Un cas teste les conditions : Yasmine et l'agresseur. Chaque case s'allume ou tombe.
        yasmine = c.Personnage("Yasmine", c.COULEURS_PERSONNAGES["turquoise"], "gauche").shift(LEFT * 0.6)
        self.play(FadeIn(yasmine, shift=UP * 0.2), run_time=0.6)
        for i in range(4):
            self.play(boites[i][0].animate.set_fill(c.VERT, opacity=0.35).set_stroke(c.VERT), run_time=0.35)
        self.play(verdict[0].animate.set_stroke(c.VERT, width=6), verdict.animate.scale(1.12), run_time=0.4)
        self.play(verdict.animate.scale(1 / 1.12), run_time=0.4)
        self.wait(0.4)
        # 4. On change un seul fait : l'agresseur est déjà parti. La case « Imminente » bascule, tout le bas tombe.
        cas = c.texte("Il s'en va. Elle le frappe dans le dos.", c.T_PETIT)
        cas.scale_to_fit_width(min(cas.width, 6.0)).move_to([-3.3, -2.5, 0])
        self.play(FadeIn(cas, shift=UP * 0.2), run_time=0.6)
        # La case se retourne comme une carte : elle s'écrase, change de couleur, se rouvre.
        self.play(boites[1].animate.stretch(0.02, 0), run_time=0.3)
        boites[1][0].set_fill(c.GRIS, opacity=1).set_stroke(c.GRIS)
        boites[1][1].set_opacity(0.6)
        self.play(boites[1].animate.stretch(50, 0), run_time=0.3)
        barre = Line(verdict.get_left(), verdict.get_right(), color=c.ACCENT, stroke_width=7)
        self.play(Create(barre), verdict.animate.set_opacity(0.4), boites[2:].animate.shift(DOWN * 0.15).set_opacity(0.5),
                  Wiggle(boites[1]), run_time=1.0)
        self.wait(0.6)
        # 5. Interpréter « imminente » : la case s'ouvre en frise ; un point se déplace dans le temps.
        self.play(*[FadeOut(m) for m in (titre, boites[0], boites[2], boites[3], fleche, verdict, barre, cas, yasmine, loi.soulignes)],
                  boites[1].animate.move_to([0, c.Y_TITRE, 0]).set_opacity(1), run_time=0.9)
        question = c.texte("« Imminente » : jusqu'à quand ?", c.T_TITRE, gras=True).move_to([0, c.Y_TITRE, 0])
        f = c.Frise()
        zone = f.zone(0.35, 0.72, "vert")
        self.play(ReplacementTransform(boites[1], question), Create(f.ligne), run_time=1.0)
        etiquettes = [f.point(0.15, "Menace lointaine"), f.point(0.35, "Attaque imminente"), f.point(0.72, "Attaque finie")]
        self.play(*[FadeIn(e, shift=UP * 0.2) for e in etiquettes], FadeIn(zone), run_time=0.9)
        curseur = Triangle(color=c.ACCENT, fill_color=c.ACCENT, fill_opacity=1).scale(0.22)
        curseur.move_to([f.x(0.05), f.y - 0.55, 0])
        etat = c.texte("Trop tôt", c.T_CORPS, c.GRIS, gras=True).move_to([0, -2.5, 0])
        self.play(FadeIn(curseur), FadeIn(etat), run_time=0.5)
        for x, t, coul in ((0.5, "Légitime défense possible", c.VERT), (0.9, "Trop tard", c.GRIS)):
            nouvel = c.texte(t, c.T_CORPS, coul, gras=True).move_to(etat)
            self.play(curseur.animate.move_to([f.x(x), f.y - 0.55, 0]), Transform(etat, nouvel), run_time=1.3)
            self.wait(0.5)
        arret = c.BlocArret("ATF 122 IV 1")
        self.play(FadeIn(arret.move_to([4.6, c.Y_ARTICLE, 0]), shift=UP * 0.2), run_time=0.6)
        self.wait(1.0)
