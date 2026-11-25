"""Arrêt 12, lignes 5 à 8 (50,0 s à 99,6 s), même style que proto.py."""
from proto import *

T0 = 49.4


def tribunal(l=3.0):
    base = Rectangle(width=l, height=0.22, fill_color=CREME, fill_opacity=1, stroke_width=0)
    cols = VGroup(*[Rectangle(width=0.2, height=1.25, fill_color=CREME, fill_opacity=1, stroke_width=0) for _ in range(5)]).arrange(RIGHT, buff=(l - 0.5 - 1.0) / 4).next_to(base, UP, buff=0)
    linteau = Rectangle(width=l, height=0.2, fill_color=CREME, fill_opacity=1, stroke_width=0).next_to(cols, UP, buff=0)
    fronton = Polygon([-l/2 - 0.1, 0, 0], [l/2 + 0.1, 0, 0], [0, 0.75, 0], fill_color=ENCRE, fill_opacity=1, stroke_width=0).next_to(linteau, UP, buff=0)
    ombre = Rectangle(width=l - 0.5, height=1.25, fill_color=ROUGE_4, fill_opacity=0.9, stroke_width=0).move_to(cols)
    return VGroup(ombre, base, cols, linteau, fronton)


def dossier(e=1.0):
    f = RoundedRectangle(corner_radius=0.05 * e, width=0.62 * e, height=0.8 * e, fill_color=CREME, fill_opacity=1, stroke_width=0)
    lignes = VGroup(*[Line([-0.2 * e, y * e, 0], [0.2 * e, y * e, 0], color=ROUGE_3, stroke_width=3 * e) for y in (0.2, 0.05, -0.1)])
    return VGroup(f, lignes)


def calendrier(haut, bas):
    f = RoundedRectangle(corner_radius=0.14, width=2.5, height=1.9, fill_color=CREME, fill_opacity=1, stroke_width=0)
    tete = Rectangle(width=2.5, height=0.5, fill_color=ENCRE, fill_opacity=1, stroke_width=0).align_to(f, UP)
    return VGroup(f, tete, T(haut, 22).move_to(tete), T(bas, 44, ENCRE).move_to(f.get_center() + 0.25 * DOWN))


def fil(actif=0):
    noms = ["Les faits", "Les textes", "La question", "La réponse", "À retenir"]
    g = VGroup()
    for k, n in enumerate(noms):
        t = T(n, 20, CREME, k == actif).set_opacity(1 if k == actif else 0.45)
        g.add(t)
    g.arrange(RIGHT, buff=0.9).move_to([0, -3.72, 0])
    g.set_x(0)
    barre = Line(g[actif].get_corner(DL) + 0.1 * DOWN, g[actif].get_corner(DR) + 0.1 * DOWN, color=CREME, stroke_width=4)
    return VGroup(g, barre).set_x(0)


def groupe(n, femme, h=0.62, cols=11, larg=5.4):
    g = VGroup()
    for i in range(n):
        r, c = divmod(i, cols)
        g.add(bonhomme(h, CREME, femme=femme, chapeau=(not femme and (i * 7) % 3 == 0)).move_to([(c - (cols - 1) / 2) * larg / cols + (0.12 if r % 2 else 0), -r * 0.58, 0]))
    return g


class Suite(MovingCameraScene):
    def jusqua(self, t):
        from temps import M
        d = (M(t) - M(T0)) - self.renderer.time
        if d > 1 / 30: self.wait(d)

    def construct(self):
        self.add(Rectangle(width=17, height=10, stroke_width=0).set_fill(color=[ROUGE, ROUGE_2], opacity=1).set_sheen_direction(DOWN).move_to([0, -0.45, 0]))
        self.camera.frame.scale(1.1125).move_to([0, -0.45, 0])
        f = fil(0); self.play(FadeIn(f), run_time=0.4)
        # ——— 5.1 : retour en arrière, Theresa Rohner ———
        cal = calendrier("AVRIL", "1990").move_to([-4.9, 2.4, 0])
        self.play(FadeIn(cal, shift=0.3 * DOWN), run_time=0.4)
        fleche = CurvedArrow([-3.4, 2.9, 0], [-3.4, 1.9, 0], angle=-2.2, color=CREME, stroke_width=5)
        cal2 = calendrier("AVRIL", "1989").move_to(cal)
        un_an = bandeau("Un an plus tôt").next_to(cal, RIGHT, buff=0.9)
        self.jusqua(50.1)
        self.play(Transform(cal, cal2), Create(fleche), FadeIn(un_an, shift=0.2 * LEFT), run_time=0.8)
        sol = Rectangle(width=16, height=3.0, fill_color=ROUGE_2, fill_opacity=1, stroke_width=0).move_to([0, -2.0, 0])
        m = montagnes(-0.5, ROUGE_3, [(-5.5, 1.5), (-2.0, 2.1), (1.5, 1.6), (5.0, 2.2)], 4)
        hommes = VGroup(*[bonhomme(1.9, CREME, chapeau=(i % 2 == 0), sabre=True) for i in range(4)])
        for i, b in enumerate(hommes): b.shift((2.7 + i * 1.3 - b.get_x()) * RIGHT + (-3.1 - b.get_bottom()[1]) * UP)
        poteaux = VGroup(*[Rectangle(width=0.09, height=1.0, fill_color=ENCRE, fill_opacity=1, stroke_width=0).move_to([x, -2.6, 0]) for x in (1.6,)])
        corde = Line([1.6, -2.3, 0], [7.2, -2.3, 0], color=ENCRE, stroke_width=7)
        rohner = bonhomme(2.3, CREME, femme=True); rohner.shift((-6.2 - rohner.get_x()) * RIGHT + (-3.1 - rohner.get_bottom()[1]) * UP)
        nom = puce("Theresa Rohner", 24)
        self.play(FadeIn(m, shift=0.3 * UP), FadeIn(sol), FadeIn(hommes), FadeIn(poteaux), Create(corde), FadeIn(rohner), run_time=0.7)
        nom.add_updater(lambda x: x.next_to(rohner, UP, buff=0.2))
        self.jusqua(52.6); self.add(nom)
        self.play(rohner.animate.shift(6.9 * RIGHT), run_time=2.6, rate_func=rate_functions.ease_out_sine)
        demande = bandeau("« Je veux participer »").next_to(rohner, UP, buff=0.85)
        self.play(FadeIn(demande, shift=0.15 * UP), run_time=0.4)
        # ——— 5.2 : le refus du gouvernement ———
        self.jusqua(57.4)
        gouv = VGroup(maison(0, 0, 2.6, 1.5, 1.2), ).move_to([-4.6, 0.3, 0])
        gl = bandeau("Gouvernement cantonal", 20).next_to(gouv, DOWN, buff=0.12)
        self.play(FadeOut(cal), FadeOut(fleche), FadeOut(un_an), FadeIn(gouv, shift=0.3 * UP), FadeIn(gl), run_time=0.6)
        lettre = dossier(0.9).move_to(gouv.get_right() + 0.3 * RIGHT)
        self.play(FadeIn(lettre, scale=0.4), run_time=0.3)
        self.play(lettre.animate.move_to(rohner.get_center() + 0.4 * UP + 1.3 * LEFT), FadeOut(demande), run_time=0.9, path_arc=-0.9)
        non = VGroup(RoundedRectangle(corner_radius=0.08, width=2.0, height=0.7, color=ROUGE, stroke_width=6, fill_color=CREME, fill_opacity=1), T("REFUS", 32, ROUGE)).rotate(-0.12).move_to(lettre.get_center() + 0.9 * RIGHT)
        self.play(FadeIn(non, scale=2.2), run_time=0.25)
        self.play(Rotate(rohner[1], 0.25, about_point=rohner[0].get_top()), run_time=0.4)
        # ——— 6.1 : elle porte l'affaire au Tribunal fédéral ———
        self.jusqua(61.5)
        nom.clear_updaters()
        self.play(*[FadeOut(x) for x in [m, sol, hommes, poteaux, corde, gouv, gl, non, lettre]], rohner.animate.scale(0.9).move_to([-5.2, -1.1, 0]), nom.animate.move_to([-5.2, 0.35, 0]), run_time=0.6)
        tf = tribunal(3.2).scale(1.3).move_to([4.0, -0.8, 0]); tfl = puce("Tribunal fédéral", 26).next_to(tf, UP, buff=0.25)
        chemin = DashedLine([-4.3, -1.2, 0], [1.6, -1.2, 0], color=CREME, stroke_width=4, dash_length=0.18)
        d1 = dossier(0.9).move_to([-4.3, -1.2, 0])
        self.play(FadeIn(tf, shift=0.4 * UP), FadeIn(tfl), Create(chemin), FadeIn(d1), run_time=0.7)
        rec = bandeau("Recours").next_to(chemin, UP, buff=0.5)
        self.play(d1.animate.move_to([1.4, -1.2, 0]), FadeIn(rec), run_time=1.5, rate_func=rate_functions.ease_in_out_sine)
        # ——— 6.2 : procédure suspendue ———
        self.jusqua(65.0)
        pause = VGroup(Circle(0.55, fill_color=ENCRE, fill_opacity=1, stroke_width=0), Rectangle(width=0.14, height=0.5, fill_color=CREME, fill_opacity=1, stroke_width=0).shift(0.14 * LEFT), Rectangle(width=0.14, height=0.5, fill_color=CREME, fill_opacity=1, stroke_width=0).shift(0.14 * RIGHT)).move_to([-5.6, 2.7, 0])
        susp = puce("Procédure suspendue", 28).next_to(pause, RIGHT, buff=0.3)
        self.play(FadeIn(pause, scale=1.6), FadeIn(susp, shift=0.2 * LEFT), FadeOut(rec), d1.animate.set_opacity(0.55), run_time=0.6)
        att = bandeau("En attendant le vote de 1990").next_to(susp, DOWN, buff=0.25).align_to(pause, LEFT)
        self.jusqua(67.6); self.play(FadeIn(att), run_time=0.5)
        # ——— 7.1 : après le refus de 1990, 53 femmes recourent ———
        self.jusqua(71.3)
        self.play(*[FadeOut(x) for x in [pause, susp, att, rohner, nom, chemin]], tf.animate.scale(0.8).move_to([0, 2.15, 0]), tfl.animate.scale(0.8).move_to([0, 3.45, 0]), d1.animate.set_opacity(1).scale(0.7).move_to([-0.5, 1.2, 0]), run_time=0.7)
        cal = calendrier("29 MAI", "1990").scale(0.8).move_to([-5.6, 2.6, 0])
        femmes = groupe(53, True).move_to([-3.7, -1.6, 0])
        n = ValueTracker(0)
        cpt = always_redraw(lambda: T(f"{int(n.get_value())} femme{'s' if n.get_value() >= 2 else ''}", 34).move_to([-3.4, 1.15, 0]))
        self.play(FadeIn(cal, shift=0.2 * DOWN), run_time=0.4)
        self.jusqua(73.6); self.add(cpt)
        self.play(LaggedStart(*[FadeIn(b, shift=0.15 * UP) for b in femmes], lag_ratio=0.025), n.animate.set_value(53), run_time=2.0, rate_func=linear)
        d2 = dossier(0.63).move_to([-3.7, 0.9, 0])
        self.play(FadeIn(d2, scale=0.4), run_time=0.3)
        self.play(d2.animate.move_to([0.0, 1.2, 0]), run_time=0.9, path_arc=-0.6)
        # ——— 7.2 : Ursula Baumann ———
        self.jusqua(79.4)
        ub = femmes[4]; nomb = puce("Ursula Baumann", 22)
        self.play(ub.animate.scale(1.35).shift(0.15 * UP), run_time=0.4); nomb.next_to(ub, UP, buff=0.12); self.play(FadeIn(nomb, shift=0.1 * UP), run_time=0.4)
        # ——— 8.1, 8.2 : et 49 hommes, neuf jours plus tôt ———
        self.jusqua(82.8)
        et = bandeau("Elles ne sont pas seules").move_to([3.7, -0.6, 0])
        self.play(FadeIn(et, shift=0.2 * UP), run_time=0.5)
        self.jusqua(86.1)
        cal3 = calendrier("20 MAI", "1990").scale(0.8).move_to([5.6, 2.6, 0])
        neuf = bandeau("9 jours plus tôt", 20).next_to(cal3, DOWN, buff=0.12)
        hommes = groupe(49, False).move_to([3.7, -1.6, 0])
        n2 = ValueTracker(0)
        cpt2 = always_redraw(lambda: T(f"{int(n2.get_value())} homme{'s' if n2.get_value() >= 2 else ''}", 34).move_to([3.4, 1.15, 0]))
        self.play(FadeOut(et), run_time=0.3); self.add(cpt2)
        self.play(LaggedStart(*[FadeIn(b, shift=0.15 * UP) for b in hommes], lag_ratio=0.025), n2.animate.set_value(49), run_time=1.8, rate_func=linear)
        ms = hommes[4]; nomm = puce("Mario Sonderegger", 22)
        self.play(ms.animate.scale(1.35).shift(0.15 * UP), run_time=0.4); nomm.next_to(ms, UP, buff=0.12); self.play(FadeIn(nomm, shift=0.1 * UP), run_time=0.4)
        d3 = dossier(0.63).move_to([3.7, 0.9, 0])
        self.play(FadeIn(d3, scale=0.4), run_time=0.3); self.play(d3.animate.move_to([0.5, 1.2, 0]), run_time=0.8, path_arc=0.6)
        # ——— 8.3 : eux votent déjà ———
        self.jusqua(91.5)
        cartes = VGroup(*[VGroup(RoundedRectangle(corner_radius=0.03, width=0.2, height=0.14, fill_color=ENCRE, fill_opacity=1, stroke_width=0)).move_to(b.get_center() + 0.02 * UP) for b in hommes])
        vote = puce("Ils votent déjà", 26).move_to([5.3, 2.5, 0])
        self.play(LaggedStart(*[FadeIn(c, scale=2) for c in cartes], lag_ratio=0.02), FadeIn(vote), femmes.animate.set_opacity(0.4), nomb.animate.set_opacity(0.4), run_time=1.2)
        # ——— 8.4 : pourquoi recourir ? ———
        self.jusqua(94.3)
        q = T("?", 150).move_to([-3.7, -0.9, 0])
        pq = puce("Pourquoi recourir ?", 30).move_to([-3.7, -2.5, 0])
        self.remove(cpt)
        self.play(FadeOut(femmes), FadeOut(nomb), FadeOut(cal), FadeIn(q, scale=0.3), run_time=0.5); self.play(FadeIn(pq, shift=0.2 * UP), Wiggle(q), run_time=1.0)
        # ——— 8.5 : on y reviendra (marque-page) ———
        self.jusqua(98.5)
        mp = VGroup(Polygon([-0.16, 0.3, 0], [0.16, 0.3, 0], [0.16, -0.3, 0], [0, -0.15, 0], [-0.16, -0.3, 0], fill_color=ENCRE, fill_opacity=1, stroke_width=0), T("Pourquoi les hommes ?", 17)).arrange(RIGHT, buff=0.15).to_corner(UR, buff=0.35)
        self.play(ReplacementTransform(VGroup(q, pq), mp), run_time=0.8)
        self.jusqua(99.9)
