from base import *


class C(Sec15):
    L0, L1 = 15, 19

    def construct(self):
        self.debut(0); self.chapitre(1, "Les textes", 2)
        # 15 — art. 8 al. 2
        cst = livre("Constitution", "fédérale").move_to([-5.3, -0.3, 0])
        self.at(S(15, 1) - 0.3, FadeIn(cst, shift=0.4 * RIGHT), rt=0.6)
        p8 = page("Art. 8 al. 2 Cst.", ["Nul ne doit subir de discrimination", "du fait notamment de son origine […]"], taille=28).move_to([1.6, 0.5, 0])
        self.at(W(15, 1, "article") - 0.3, FadeIn(p8, shift=0.4 * UP), rt=0.6)
        t = titre("Interdiction de discriminer"); self.at(S(15, 2), FadeIn(t, shift=0.2 * DOWN), rt=0.5)
        cad = cadre_autour(p8.corps[1], 0.1); o = bas("L'origine : un critère interdit", 26, -2.3)
        self.at(W(15, 2, "origine") - 0.4, Create(cad), FadeIn(o, shift=0.15 * UP), rt=0.6)
        # 16 — art. 29 al. 2
        self.jusqua(S(16, 1) - 0.5)
        self.play(FadeOut(t, shift=0.7 * LEFT), FadeOut(o, shift=0.7 * LEFT), FadeOut(cad), VGroup(p8).animate.scale(0.5).move_to([-5.2, 1.9, 0]), cst.animate.scale(0.6).move_to([-6.3, -1.6, 0]), run_time=0.5)
        p29 = page("Art. 29 al. 2 Cst.", ["Les parties ont le droit", "d'être entendues."], taille=30).move_to([-2.2, -0.5, 0])
        self.at(W(16, 1, "article") - 0.3, FadeIn(p29, shift=0.4 * UP), rt=0.6)
        t = titre("Le droit d'être entendu"); self.at(W(16, 1, "garantit") - 0.2, FadeIn(t, shift=0.2 * DOWN), rt=0.5)
        fl = Arrow(p29.get_right() + 0.1 * RIGHT, p29.get_right() + 1.3 * RIGHT, color=CREME, stroke_width=7, buff=0)
        mo = puce("Motiver les décisions", 26).next_to(fl, RIGHT, buff=0.2)
        self.at(W(16, 2, "découle") - 0.2, GrowArrow(fl), rt=0.5); self.at(W(16, 2, "motiver") - 0.5, FadeIn(mo, scale=1.3), rt=0.5)
        au = bandeau("Une obligation pour toute autorité", 22).next_to(mo, DOWN, buff=0.25)
        self.play(FadeIn(au, shift=0.15 * UP), run_time=0.4)
        # 17 — en face : art. 34
        self.jusqua(S(17, 1) - 0.5)
        p29b = page("Art. 29 al. 2 Cst.", ["Les parties ont le droit", "d'être entendues."], taille=30).scale(0.5).move_to([-5.2, 0.2, 0])
        self.play(*[FadeOut(x, shift=0.7 * LEFT) for x in (t, fl, mo, au)], Transform(p29, p29b), FadeOut(cst), run_time=0.5)
        t = titre("Mais en face…"); self.at(S(17, 1), FadeIn(t, shift=0.2 * DOWN), rt=0.4)
        p34 = page("Art. 34 al. 2 Cst. · Droits politiques", ["La garantie des droits politiques protège", "la libre formation de l'opinion […]", "et l'expression fidèle et sûre de leur volonté."], taille=22).move_to([3.1, 0.9, 0])
        self.at(W(17, 1, "article") - 0.3, FadeIn(p34, shift=0.4 * UP), rt=0.6)
        vs = VGroup(Line([-2.6, 1.0, 0], [-1.5, 1.0, 0], color=CREME, stroke_width=6).add_tip(tip_length=0.2).add_tip(at_start=True, tip_length=0.2))
        self.at(W(17, 1, "consacré") - 0.2, Create(vs), rt=0.5)
        u = urne(1.2).move_to([3.3, -1.6, 0]); vv = votants(3, 1.0).next_to(u, LEFT, buff=0.4).align_to(u, DOWN); vd = votants(3, 1.0).next_to(u, RIGHT, buff=0.4).align_to(u, DOWN)
        self.at(S(17, 2), FadeIn(u, shift=0.2 * UP), FadeIn(vv), FadeIn(vd), rt=0.6)
        c1 = cadre_autour(p34.corps[1], 0.08); c2 = cadre_autour(p34.corps[2], 0.08)
        self.at(W(17, 2, "libre") - 0.2, Create(c1), rt=0.5); self.at(W(17, 2, "expression") - 0.2, Create(c2), rt=0.5)
        # 18 — les deux questions
        self.vider(B(18) - 0.35, rt=0.35)
        self.jusqua(B(18)); self.chapitre(2, "La question", 3)
        t = titre("Deux questions"); self.at(S(18, 1), FadeIn(t, shift=0.2 * DOWN), rt=0.4)
        def q(num, lignes, x):
            f = RoundedRectangle(corner_radius=0.25, width=6.3, height=3.9, fill_color=ROUGE_3, fill_opacity=1, stroke_width=0).move_to([x, -0.5, 0])
            n = VGroup(Circle(0.42, fill_color=CREME, fill_opacity=1, stroke_width=0), T(str(num), 34, ROUGE)).move_to(f.get_top() + 0.1 * DOWN)
            tx = VGroup(*[T(l, 28) for l in lignes]).arrange(DOWN, buff=0.2).move_to(f.get_center() + 0.1 * DOWN)
            return VGroup(f, n, tx)
        q1 = q(1, ["Un vote populaire", "peut-il être", "une discrimination interdite ?"], -3.5)
        q2 = q(2, ["Peut-on refuser", "une naturalisation", "sans donner de raisons ?"], 3.5)
        self.at(S(18, 2) - 0.1, FadeIn(q1, shift=0.3 * UP), rt=0.6)
        self.at(S(18, 3) - 0.1, FadeIn(q2, shift=0.3 * UP), rt=0.6)
        qp = bas("Qu'en pensez-vous ?", 28, -2.95)
        self.at(F_(18) + 0.4, FadeIn(qp, shift=0.15 * UP), rt=0.5)
        self.fin()
