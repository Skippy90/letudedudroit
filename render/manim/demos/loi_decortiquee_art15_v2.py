import sys
sys.path.insert(0, str(__import__("pathlib").Path(__file__).resolve().parent.parent))
from manim import *
import charte as c


def noeud(t, couleur=c.TEXTE, taille=c.T_PETIT):
    lib = c.texte(t, taille)
    cadre = RoundedRectangle(corner_radius=0.14, width=max(lib.width + 0.6, 2.6), height=0.85, color=couleur,
                             stroke_width=3, fill_color=c.SURFACE, fill_opacity=1)
    return VGroup(cadre, lib.move_to(cadre))


def fleche(a, b, couleur=c.TEXTE):
    return Arrow(a.get_bottom(), b.get_top(), buff=0.08, color=couleur, stroke_width=4, max_tip_length_to_length_ratio=0.15)


class Demo2(MovingCameraScene):
    def construct(self):
        self.camera.background_color = c.FOND
        cam = self.camera.frame
        # ---------- 1. Le schéma global, d'emblée ----------
        titre = c.texte("Art. 15 CP : la carte", c.T_TITRE, gras=True).move_to([0, 3.3, 0])
        n1 = noeud("Attaque ou menace").move_to([-3.2, 1.8, 0])
        n2 = noeud("Imminente").move_to([3.2, 1.8, 0])
        n3 = noeud("Contraire au droit").move_to([0, 0.4, 0])
        n4 = noeud("Défense proportionnée").move_to([0, -1.0, 0])
        ok = noeud("Acte licite", c.VERT).move_to([-3.0, -2.6, 0])
        exces = noeud("Excès : art. 16", c.ACCENT).move_to([3.0, -2.6, 0])
        liens = VGroup(fleche(n1, n3), fleche(n2, n3), fleche(n3, n4), fleche(n4, ok, c.VERT), fleche(n4, exces, c.ACCENT))
        noeuds = [n1, n2, n3, n4]
        self.play(FadeIn(titre, shift=DOWN * 0.3), run_time=0.6)
        self.play(LaggedStart(*[GrowFromCenter(n) for n in noeuds], lag_ratio=0.25), run_time=1.6)
        self.play(LaggedStart(*[GrowArrow(l) for l in liens[:3]], lag_ratio=0.3), run_time=1.0)
        self.play(GrowArrow(liens[3]), FadeIn(ok, shift=DOWN * 0.2), GrowArrow(liens[4]), FadeIn(exces, shift=DOWN * 0.2), run_time=1.0)
        # Le schéma « respire » : une onde le parcourt de haut en bas.
        for n in noeuds + [ok]:
            self.play(n.animate.scale(1.08), run_time=0.15)
            self.play(n.animate.scale(1 / 1.08), run_time=0.15)
        carte = VGroup(titre, *noeuds, ok, exces, liens)
        self.wait(0.5)
        # ---------- 2. La bonne manière d'interpréter ----------
        self.play(carte.animate.scale(0.26).to_corner(UR, buff=0.3).set_opacity(0.55), run_time=1.0)
        t2 = c.texte("Comment lire un article ?", c.T_TITRE, gras=True).move_to([-6.6, 3.2, 0], aligned_edge=LEFT)
        mot = c.texte("« imminente »", c.T_TITRE, c.ACCENT, gras=True).move_to([0, -2.6, 0])
        methodes = VGroup(*[noeud(t) for t in ("Le texte", "Les autres articles", "Le but de la règle", "L'histoire de la loi")])
        methodes.arrange_in_grid(rows=2, cols=2, buff=(0.8, 0.6)).move_to([0, 0.7, 0])
        self.play(FadeIn(t2, shift=DOWN * 0.3), FadeIn(mot, scale=0.8), run_time=0.8)
        for m in methodes:
            rayon = Line(m.get_bottom(), mot.get_top(), color=c.ACCENT, stroke_width=3, stroke_opacity=0.6)
            self.play(GrowFromCenter(m), Create(rayon), run_time=0.55)
            self.play(Indicate(mot, color=c.ACCENT, scale_factor=1.06), FadeOut(rayon), run_time=0.45)
        sens = noeud("Le sens retenu", c.VERT).move_to(mot)
        self.play(*[m.animate.move_to(mot).scale(0.2).set_opacity(0) for m in methodes], ReplacementTransform(mot, sens), run_time=1.0)
        self.play(Circumscribe(sens, color=c.VERT), run_time=0.8)
        self.wait(0.3)
        # ---------- 3. Retour au schéma, puis zoom sur une condition ----------
        self.play(FadeOut(t2), FadeOut(sens), carte.animate.scale(1 / 0.26).move_to(ORIGIN).set_opacity(1), run_time=1.0)
        cible = n2
        autres = VGroup(titre, n1, n3, n4, ok, exces, liens)
        self.play(cam.animate.scale(0.5).move_to(cible.get_center() + DOWN * 0.7), autres.animate.set_opacity(0), run_time=1.4)
        # Dans la case : une frise du temps, un curseur.
        x0, x1, y = cible.get_left()[0] - 1.3, cible.get_right()[0] + 1.3, cible.get_bottom()[1] - 0.7
        ligne = Arrow([x0, y, 0], [x1 + 0.2, y, 0], buff=0, color=c.TEXTE, stroke_width=3, max_tip_length_to_length_ratio=0.06)
        zone = Rectangle(width=(x1 - x0) * 0.4, height=0.18, stroke_width=0, fill_color=c.VERT, fill_opacity=0.5).move_to([x0 + (x1 - x0) * 0.55, y, 0])
        etiquettes = VGroup(c.texte("trop tôt", 20, c.GRIS).move_to([x0 + (x1 - x0) * 0.15, y - 0.32, 0]),
                            c.texte("imminente", 20, c.VERT).move_to([x0 + (x1 - x0) * 0.55, y - 0.32, 0]),
                            c.texte("trop tard", 20, c.GRIS).move_to([x0 + (x1 - x0) * 0.92, y - 0.32, 0]))
        curseur = Triangle(color=c.ACCENT, fill_color=c.ACCENT, fill_opacity=1).scale(0.08).move_to([x0 + 0.1, y + 0.18, 0]).rotate(PI)
        self.play(Create(ligne), FadeIn(zone), FadeIn(etiquettes), FadeIn(curseur), run_time=0.8)
        self.play(curseur.animate.move_to([x0 + (x1 - x0) * 0.55, y + 0.18, 0]), run_time=1.0)
        self.play(cible[0].animate.set_fill(c.VERT, opacity=0.4).set_stroke(c.VERT), run_time=0.4)
        self.play(curseur.animate.move_to([x1 - 0.1, y + 0.18, 0]), cible[0].animate.set_fill(c.GRIS, opacity=1).set_stroke(c.GRIS), run_time=1.0)
        self.play(curseur.animate.move_to([x0 + (x1 - x0) * 0.55, y + 0.18, 0]), cible[0].animate.set_fill(c.VERT, opacity=0.4).set_stroke(c.VERT), run_time=0.8)
        # Dézoom : la case verte reprend sa place dans le schéma, et le courant passe jusqu'au bout.
        self.play(cam.animate.scale(2).move_to(ORIGIN), FadeOut(VGroup(ligne, zone, etiquettes, curseur)),
                  autres.animate.set_opacity(1), run_time=1.4)
        for n in (n1, n3, n4):
            self.play(n[0].animate.set_fill(c.VERT, opacity=0.4).set_stroke(c.VERT), run_time=0.3)
        self.play(liens[3].animate.set_stroke(width=8), Flash(ok, color=c.VERT, flash_radius=1.4), ok.animate.scale(1.15), run_time=0.9)
        self.wait(1.0)
