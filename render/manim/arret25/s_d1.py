from base import *
from s_a import quatre
from s_c import bloc_art


def jauge(x0=-4.6, x1=4.6, y=0.0):
    """Jauge horizontale « intensité de l'atteinte », avec la zone du seuil."""
    f = RoundedRectangle(corner_radius=0.2, width=x1 - x0, height=0.5, fill_color=ROUGE_4, fill_opacity=1, stroke_color=CREME, stroke_width=3).move_to([(x0 + x1) / 2, y, 0])
    xs = x0 + 0.62 * (x1 - x0)
    seuil = VGroup(Line([xs, y - 0.55, 0], [xs, y + 0.55, 0], color=CREME, stroke_width=7), puce("Seuil", 22).move_to([xs, y + 0.95, 0]))
    g = VGroup(f, seuil, T("faible", 18, CREME, False).move_to([x0 + 0.5, y - 0.6, 0]), T("forte", 18, CREME, False).move_to([x1 - 0.5, y - 0.6, 0]))
    g.x0, g.x1, g.xs, g.y, g.seuil = x0, x1, xs, y, seuil
    return g


def curseur(couleur=AMBRE):
    return Triangle(fill_color=couleur, fill_opacity=1, stroke_color=ENCRE, stroke_width=2).scale(0.24).rotate(PI)


class D1(Sec25):
    L0, L1 = 19, 27

    def construct(self):
        self.debut(fil_avant=1); self.chapitre(2, "Le Tribunal fédéral", 3)
        ba = bloc_art(); self.add(ba)
        # 19 — 5 mai 2020 : une précision favorable
        cal = calendrier("5 MAI", "2020").scale(0.85).move_to([-5.9, 2.6, 0])
        tf = tribunal(3.2).move_to([-2.6, -0.3, 0]); atf = puce("ATF 146 I 145", 32).move_to([-2.6, 2.1, 0])
        self.at(S(19, 1) - 0.2, FadeIn(cal, shift=0.3 * DOWN), FadeIn(tf, shift=0.3 * UP), rt=0.5)
        self.at(W(19, 1, "Tribunal") - 0.2, FadeIn(atf, scale=1.4), rt=0.4); self.son("ding", 0.7)
        porte = Rectangle(width=0.9, height=1.2, fill_color=ENCRE, fill_opacity=1, stroke_color=CREME, stroke_width=3).move_to(tf[2].get_center() + 0.02 * DOWN)
        self.add(porte)
        ouv = bandeau("Une précision favorable", 24).next_to(tf, DOWN, buff=0.2)
        self.at(W(19, 2, "précision") - 0.3, porte.animate.stretch_to_fit_width(0.14).align_to(porte, LEFT), FadeIn(ouv), rt=0.6); self.son("zip")
        ac = VGroup(coche(True, 0.3), T("Les actes", 30)).arrange(RIGHT, buff=0.25).move_to([3.6, 0.6, 0])
        om = VGroup(coche(True, 0.3), T("Certaines omissions", 30)).arrange(RIGHT, buff=0.25); om.move_to([3.6, -0.5, 0]).align_to(ac, LEFT)
        self.at(W(19, 3, "actes") - 0.3, FadeIn(ac, shift=0.3 * LEFT), rt=0.4); self.son("plop")
        self.at(W(19, 4, "omissions") - 0.3, FadeIn(om, shift=0.3 * LEFT), rt=0.4); self.son("plop")
        # 20 — une limite : une obligation juridique précise d'agir
        self.at(S(20, 1) - 0.3, FadeOut(ac), FadeOut(ouv), om.animate.move_to([3.6, 2.0, 0]), rt=0.4)
        j = juge(1.9, "decide"); j.move_to([0.3, -1.3, 0])
        cd = carton(["Illicite seulement si l'autorité", "avait l'obligation précise d'agir"], 5.8, 1.7, 22).move_to([4.3, 0.3, 0])
        self.at(S(20, 1), FadeIn(j, shift=0.2 * UP), rt=0.35)
        self.at(S(20, 2) - 0.05, FadeIn(cd, shift=0.2 * UP), rt=0.5)
        dv = cadre_autour(cd[1][1], 0.1).set_color(CREME); self.at(W(20, 2, "obligation") - 0.2, Create(dv), rt=0.4); self.son("ding", 0.6)
        ms = bandeau("Une mesure simplement souhaitable ne suffit pas", 20).move_to([4.4, -1.5, 0])
        self.at(S(20, 3) - 0.05, FadeIn(ms, shift=0.15 * UP), rt=0.4)
        # 21 — un second obstacle : des positions individuelles, pas la politique générale
        self.vider(S(21, 1) - 0.5, garder=[cal], rt=0.4)
        t = titre("Un second obstacle")
        un = ainee(1.7, MENTHE, "content"); un.move_to([-3.9, -0.6, 0])
        bo = Polygon([-0.5, 0.55, 0], [0.5, 0.55, 0], [0.5, -0.1, 0], [0, -0.6, 0], [-0.5, -0.1, 0], fill_color=CREME, fill_opacity=1, stroke_color=ENCRE, stroke_width=4).scale(0.9).move_to(un.get_right() + 0.75 * RIGHT + 0.1 * UP)
        l1 = VGroup(coche(True, 0.28), T("Des positions individuelles", 24)).arrange(RIGHT, buff=0.2).next_to(VGroup(un, bo), DOWN, buff=0.35)
        self.at(S(21, 1) - 0.05, FadeIn(t, shift=0.2 * DOWN), rt=0.3); self.son("grelot", 0.5)
        self.at(S(21, 2) - 0.05, FadeIn(un, shift=0.2 * UP), rt=0.4)
        self.at(W(21, 2, "protéger") - 0.2, FadeIn(bo, scale=0.4), FadeIn(l1), rt=0.4); self.son("plop")
        mes = page("Politique climatique", ["Objectifs", "Moyens", "Délais"], l=3.6, taille=20).scale(0.9).move_to([3.4, 0.0, 0])
        l2 = VGroup(coche(False, 0.28), T("La réorienter en général", 24)).arrange(RIGHT, buff=0.2).next_to(mes, DOWN, buff=0.35)
        self.at(S(21, 3) - 0.05, FadeIn(mes, shift=0.2 * UP), rt=0.4)
        self.at(W(21, 3, "réorientation") - 0.4, FadeIn(l2, scale=1.2), mes.animate.set_opacity(0.6), rt=0.35); self.son("thud", 0.7)
        # 22 — l'action populaire
        self.vider(S(22, 1) - 0.45, garder=[cal], rt=0.4)
        foule = VGroup(*[acteur(0.75, None, k % 2 == 0, "neutre") for k in range(21)]).arrange_in_grid(3, 7, buff=(0.17, 0.1)).move_to([0, -1.5, 0])
        ap = puce("Action populaire", 34).move_to([0, 3.0, 0])
        self.at(S(22, 1) - 0.05, LaggedStart(*[FadeIn(x, shift=0.15 * UP) for x in foule], lag_ratio=0.02), rt=0.6)
        self.at(W(22, 1, "action") - 0.3, FadeIn(ap, scale=1.3), rt=0.4); self.son("ding", 0.7)
        ds = VGroup(bandeau("Chacun pourrait saisir le juge", 24), bandeau("pour défendre l'intérêt général", 24), bandeau("sans être assez touché soi-même", 24)).arrange(DOWN, buff=0.14).move_to([0, 1.35, 0])
        self.at(W(22, 2, "chacun") - 0.3, FadeIn(ds[0], shift=0.15 * UP), rt=0.4); self.saut(*foule, h=0.1, rt=0.35)
        self.at(W(22, 2, "défendre") - 0.3, FadeIn(ds[1], shift=0.15 * UP), rt=0.4)
        self.at(W(22, 2, "sans") - 0.3, FadeIn(ds[2], shift=0.15 * UP), rt=0.4)
        # 23 — une atteinte personnelle d'une intensité suffisante ; le seuil
        self.vider(S(23, 1) - 0.5, garder=[cal], rt=0.4)
        t = titre("Une atteinte personnelle, assez intense").shift(1.4 * RIGHT)
        jg = jauge(y=-0.4); jt = bandeau("Intensité de l'atteinte", 22).move_to([-3.2, 1.7, 0])
        cu = curseur().move_to([jg.x0 + 1.2, -0.4 + 0.5, 0])
        j = juge(1.3, "decide"); j.move_to([5.9, -1.6, 0])
        self.at(S(23, 1) - 0.05, FadeIn(t, shift=0.2 * DOWN), FadeIn(j, shift=0.2 * UP), rt=0.4)
        self.at(W(23, 1, "atteinte") - 0.4, FadeIn(jg[0]), FadeIn(jg[2]), FadeIn(jg[3]), FadeIn(jt), FadeIn(cu, shift=0.2 * DOWN), rt=0.5)
        self.at(W(23, 1, "intensité") - 0.3, cu.animate.set_x(jg.x1 - 1.0), rt=0.9)
        self.at(S(23, 2) - 0.1, FadeIn(jg.seuil, scale=1.3), rt=0.35); self.son("ding", 0.6)
        self.at(W(23, 3, "élevé") - 0.5, jg.seuil.animate.shift(2.2 * RIGHT), rt=0.4)
        self.at(W(23, 3, "faible") - 0.5, jg.seuil.animate.shift(5.6 * LEFT), rt=0.5)
        self.at(W(23, 3, "toute") - 0.1, jg.seuil.animate.shift(3.4 * RIGHT), rt=0.5); self.son("plop")
        # 24 — appliquer le critère aux requérantes
        self.at(S(24, 1) - 0.4, FadeOut(t), FadeOut(j), cu.animate.set_x(jg.x0 + 2.2), rt=0.4)
        q = quatre(0.95, "perplexe"); q.move_to([0, -2.0, 0])
        self.at(S(24, 1), FadeIn(q, shift=0.2 * UP), rt=0.4)
        pq = T("?", 54).next_to(cu, UP, buff=0.1)
        self.at(S(24, 2) - 0.05, FadeIn(pq, scale=0.5), rt=0.3)
        self.play(cu.animate(rate_func=there_and_back).shift(1.6 * RIGHT), pq.animate(rate_func=there_and_back).shift(1.6 * RIGHT), run_time=1.6)
        # 24.3 à 25 — les projections de l'époque : le rapport du GIEC de 2018
        self.vider(S(24, 3) - 0.45, garder=[cal], rt=0.4)
        t = titre("Les projections de l'époque")
        fr = frise(2015, 2065, -5.4, 4.8, -1.4, [(2018, "2018"), (2040, "vers 2040")])
        j = juge(1.1, "neutre"); j.move_to([-5.9, -0.3, 0]); lp = loupe(0.6).move_to(j.get_right() + 0.45 * RIGHT + 0.25 * UP)
        self.at(S(24, 3) - 0.05, FadeIn(t, shift=0.2 * DOWN), FadeIn(j, shift=0.2 * UP), rt=0.4)
        self.at(W(24, 3, "projections") - 0.4, FadeIn(fr[0]), FadeIn(lp, scale=0.5), rt=0.5)
        rp = page("Rapport spécial du GIEC", ["Experts du climat", "2018"], l=4.6, taille=18).scale(0.8).move_to([fr.X(2018) + 2.0, 1.2, 0])
        self.at(S(25, 1) + 0.3, FadeIn(fr[1], scale=1.4), FadeIn(rp, shift=0.2 * DOWN), rt=0.5); self.son("plop")
        tr = Line([fr.X(2018), -1.4, 0], [fr.X(2040), -1.4, 0], color=AMBRE, stroke_width=10)
        p15 = puce("+ 1,5 °C", 30).move_to([fr.X(2040), 0.1, 0])
        self.at(W(25, 2, "réchauffement") - 0.3, Create(tr), rt=1.4)
        self.at(W(25, 2, "virgule") - 0.4, FadeIn(p15, scale=1.4), rt=0.4); self.son("ding", 0.7)
        self.at(W(25, 2, "quarante") - 0.6, FadeIn(fr[2], scale=1.4), rt=0.4)
        acc = VGroup(Line([fr.X(2030), -1.95, 0], [fr.X(2052), -1.95, 0], color=CREME, stroke_width=5), Line([fr.X(2030), -1.8, 0], [fr.X(2030), -2.1, 0], color=CREME, stroke_width=5), Line([fr.X(2052), -1.8, 0], [fr.X(2052), -2.1, 0], color=CREME, stroke_width=5))
        fo = bandeau("Fourchette : 2030 à 2052", 20).next_to(acc, DOWN, buff=0.15)
        self.at(W(25, 2, "fourchette") - 0.3, Create(acc), FadeIn(fo, shift=0.1 * UP), rt=0.5); self.son("plop", 0.7)
        # 26 — le seuil de l'Accord de Paris ne serait pas franchi à brève échéance
        tr2 = DashedLine([fr.X(2040), -1.4, 0], [fr.X(2062), -1.4, 0], color=AMBRE, stroke_width=8)
        p2 = VGroup(puce("Seuil de l'Accord de Paris", 22), T("pas franchi à brève échéance", 22)).arrange(DOWN, buff=0.12).move_to([fr.X(2060) - 0.9, 2.0, 0])
        self.at(S(26, 1) - 0.05, FadeOut(rp), rt=0.3)
        self.at(W(26, 1, "seuil") - 0.3, Create(tr2), FadeIn(p2[0], shift=0.15 * DOWN), rt=0.8)
        self.at(W(26, 1, "franchi") - 0.6, FadeIn(p2[1], shift=0.1 * DOWN), rt=0.4)
        sb = sablier(0.8).move_to([fr.X(2029), 0.1, 0]); st = puce("Il reste encore du temps", 24).move_to([-2.4, 1.3, 0])
        self.at(S(26, 2) - 0.05, FadeIn(sb, scale=0.5), FadeIn(st, shift=0.15 * UP), rt=0.4); self.son("grelot", 0.6)
        self.play(Rotate(sb, PI), run_time=0.9)
        self.fin()
