from base import *
from s_a import quatre


def bloc_art(s="Art. 25a PA"):
    return puce(s, 30).move_to([0, -2.85, 0])


class C(Sec25):
    L0, L1 = 14, 19

    def construct(self):
        self.debut(fil_avant=0); self.chapitre(1, "Le texte", 2)
        # 14 — ouvrir la loi : l'article 25a PA
        q = quatre(1.1, "perplexe"); q.move_to([-5.3, -1.3, 0])
        self.at(S(14, 1) - 0.1, FadeIn(q, shift=0.2 * UP), rt=0.4)
        lv = livre("Procédure", "administrative", "25a").move_to([1.2, 0.3, 0])
        self.at(W(14, 1, "ouvrir") - 0.4, FadeIn(lv, shift=0.3 * UP), rt=0.5); self.son("plop")
        ba = bloc_art(); self.at(W(14, 2, "article") - 0.2, FadeIn(ba, scale=1.4), lv.animate(rate_func=there_and_back).scale(1.08), rt=0.5); self.son("ding", 0.7)
        pa = bandeau("PA : loi fédérale sur la procédure administrative", 20).move_to([1.2, -1.75, 0])
        self.at(W(14, 2, "loi") - 0.2, FadeIn(pa, shift=0.1 * UP), rt=0.4)
        # 15 — décisions et actes matériels
        self.at(S(15, 1) - 0.45, FadeOut(q), FadeOut(pa), lv.animate.scale(0.45).move_to([-6.0, 2.5, 0]), rt=0.4)
        pal = palais(2.4).move_to([0, 1.6, 0]); pl = bandeau("L'État", 22).next_to(pal, UP, buff=0.15)
        dec = page("Décision", ["Vu…", "Décide :", "…"], l=2.6, taille=18).move_to([-3.9, -0.7, 0]); dl = bandeau("Il décide", 22).next_to(dec, DOWN, buff=0.2)
        f1 = Arrow(pal.get_bottom() + 0.6 * LEFT, dec.get_top() + 0.8 * RIGHT + 0.1 * UP, color=CREME, stroke_width=6, buff=0.15)
        self.at(S(15, 1) - 0.05, FadeIn(pal, shift=0.2 * DOWN), FadeIn(pl), rt=0.4)
        da = puce("En droit administratif", 24).move_to([0, 0.35, 0]); self.at(W(15, 2, "droit") - 0.3, FadeIn(da, scale=1.2), rt=0.35)
        self.at(W(15, 2, "seulement") - 0.2, FadeOut(da), rt=0.25)
        self.at(W(15, 2, "décisions") - 0.4, GrowArrow(f1), FadeIn(dec, shift=0.2 * UP), FadeIn(dl), rt=0.5); self.son("plop")
        ouv = acteur(1.3, None, False, "content"); ouv.move_to([3.2, -1.05, 0])
        casque = AnnularSector(inner_radius=0, outer_radius=0.2, angle=PI, fill_color=AMBRE, fill_opacity=1, stroke_width=0).move_arc_center_to(ouv[1].get_center() + 0.08 * UP); ouv.add(casque)
        mur = VGroup(*[Rectangle(width=0.5, height=0.24, fill_color=CREME, fill_opacity=1, stroke_color=ENCRE, stroke_width=2).move_to([4.4 + 0.5 * c + (0.25 if r % 2 else 0), -1.58 + 0.24 * r, 0]) for r in range(4) for c in range(3)])
        f2 = Arrow(pal.get_bottom() + 0.6 * RIGHT, [3.4, 0.2, 0], color=CREME, stroke_width=6, buff=0.15)
        self.at(S(15, 3) - 0.1, GrowArrow(f2), FadeIn(ouv, shift=0.2 * UP), rt=0.4)
        am = puce("Actes matériels", 30).move_to([4.6, 0.75, 0])
        self.at(W(15, 3, "actes") - 0.2, FadeIn(am, scale=1.4), rt=0.4); self.son("ding", 0.7)
        self.jusqua(W(15, 4, "effets") - 0.9)
        for k in range(0, 12, 3):
            self.son("flic", 0.7); self.play(*[FadeIn(mur[j], shift=0.15 * DOWN) for j in range(k, k + 3)], run_time=0.18)
        al = bandeau("Des effets concrets", 22).move_to([4.2, -2.2, 0]); self.play(FadeIn(al), run_time=0.3)
        sj = bandeau("sans régler une situation juridique", 20).move_to([4.2, -2.75, 0])
        self.at(W(15, 4, "sans") - 0.2, FadeIn(sj, shift=0.1 * UP), FadeOut(f2), rt=0.4)
        # 16 — ce que permet l'article
        self.vider(S(16, 1) - 0.5, garder=[lv], rt=0.4)
        ba = bloc_art(); q = quatre(1.0, "decide"); q.move_to([-5.0, -1.3, 0])
        aut = palais(2.2).move_to([4.6, -0.9, 0]); aul = bandeau("L'autorité", 20).next_to(aut, DOWN, buff=0.15)
        self.at(S(16, 1) - 0.1, FadeIn(ba), FadeIn(q, shift=0.2 * UP), FadeIn(aut, shift=0.2 * UP), FadeIn(aul), rt=0.5)
        ds = VGroup(bulle(["Renoncez à l'acte illicite"], 22), bulle(["Faites-en cesser les effets"], 22), bulle(["Ou constatez qu'il est illicite"], 22)).arrange(DOWN, buff=0.22, aligned_edge=LEFT).move_to([-0.6, 0.6, 0])
        for k, mot in enumerate(("renoncer", "cesser", "constater")):
            self.at(W(16, 2, mot) - 0.4, FadeIn(ds[k], shift=0.2 * RIGHT), rt=0.35); self.son("hop", 0.8)
        dd = page("Décision", ["…", "…"], l=1.9, taille=16).scale(0.8).move_to(aut.get_top() + 1.0 * UP)
        self.at(W(16, 3, "décision") - 0.5, FadeIn(dd, shift=0.3 * DOWN), rt=0.4); self.son("plop")
        for x in q: visage(x, 1.0, "content")
        # 17 — pas pour tout le monde : deux conditions
        self.vider(S(17, 1) - 0.5, garder=[ba, lv], rt=0.4)
        t = titre("Pas pour tout le monde")
        foule = VGroup(*[acteur(0.7, None, k % 2 == 0, "neutre") for k in range(9)]).arrange(RIGHT, buff=0.2).move_to([0, -0.5, 0])
        self.at(S(17, 1) - 0.05, FadeIn(t, shift=0.2 * DOWN), LaggedStart(*[FadeIn(x, shift=0.15 * UP) for x in foule], lag_ratio=0.04), rt=0.6)
        bar = Line([-4.4, -0.5, 0], [4.4, -0.5, 0], color=ENCRE, stroke_width=10)
        self.at(W(17, 1, "pas") - 0.1, Create(bar), foule.animate.set_opacity(0.5), rt=0.4); self.son("thud", 0.6)
        def cond(n, a, x):
            f = RoundedRectangle(corner_radius=0.22, width=5.6, height=2.6, fill_color=ROUGE_3, fill_opacity=1, stroke_width=0).move_to([x, -0.3, 0])
            c = VGroup(Circle(0.4, fill_color=CREME, fill_opacity=1, stroke_width=0), T(str(n), 32, ROUGE)).move_to(f.get_top() + 0.1 * DOWN)
            tx = VGroup(*[T(s, 28) for s in a]).arrange(DOWN, buff=0.14).move_to(f.get_center() + 0.15 * DOWN)
            return VGroup(f, c, tx)
        k1 = cond(1, ["Un intérêt digne", "de protection"], -3.2); k2 = cond(2, ["Être touché dans ses", "droits ou ses obligations"], 3.2)
        t2 = titre("Deux conditions")
        self.at(S(17, 2) - 0.2, FadeOut(foule), FadeOut(bar), FadeOut(t), FadeIn(t2, scale=1.2), rt=0.4)
        self.at(S(17, 3) - 0.1, FadeIn(k1, shift=0.3 * UP), rt=0.45); self.son("plop")
        self.at(S(17, 4) - 0.1, FadeIn(k2, shift=0.3 * UP), rt=0.45); self.son("plop")
        # 18 — toute la difficulté
        self.vider(S(18, 1) - 0.5, garder=[ba], rt=0.4)
        t = titre("Toute la difficulté", 36); self.at(S(18, 1) - 0.1, FadeIn(t, scale=1.3), rt=0.4)
        f = RoundedRectangle(corner_radius=0.3, width=11.6, height=2.9, fill_color=ROUGE_3, fill_opacity=1, stroke_width=0).move_to([0, 0.75, 0])
        qt = VGroup(T("Les Aînées sont-elles assez touchées", 34), T("pour exiger une réponse", 34), T("sur le climat ?", 34)).arrange(DOWN, buff=0.22).move_to(f)
        q = quatre(0.95, "perplexe"); q.move_to([-4.3, -1.75, 0]); pal = palais(1.8).scale(0.8).move_to([4.3, -1.6, 0])
        self.at(S(18, 2) - 0.1, FadeIn(f), FadeIn(qt[0], shift=0.15 * UP), FadeIn(q, shift=0.2 * UP), rt=0.5)
        self.at(W(18, 2, "exiger") - 0.3, FadeIn(qt[1], shift=0.15 * UP), FadeIn(pal, shift=0.2 * UP), rt=0.4)
        self.at(W(18, 2, "omissions") - 0.3, FadeIn(qt[2], shift=0.15 * UP), rt=0.4)
        sb = sablier(0.9).move_to([0, -1.7, 0])
        self.at(F_(18) + 0.2, FadeIn(sb, scale=0.5), rt=0.3); self.son("grelot", 0.6)
        self.play(Rotate(sb, PI), run_time=1.0)
        self.fin()
