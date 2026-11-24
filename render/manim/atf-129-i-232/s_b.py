from base import *


class B_(Sec232):
    L0, L1 = 4, 12

    def construct(self):
        self.debut(0); self.chapitre(0, "Les faits", 1)
        # 4 — 5 octobre 1999 : l'UDC de la ville de Zurich dépose l'initiative
        cal = calendrier("5 OCTOBRE", "1999").scale(0.85).move_to([-5.8, 2.3, 0])
        vil = VGroup(maison(-0.9, 0, 1.1, 0.8, 0.9), maison(0.35, 0, 1.3, 1.25, 1.0), maison(1.6, 0, 1.0, 0.65, 0.8)).move_to([5.3, -0.1, 0])
        vl = bandeau("Ville de Zurich", 22).next_to(vil, DOWN, buff=0.2)
        self.at(S(4, 1) - 0.05, FadeIn(cal, shift=0.3 * DOWN), rt=0.4); self.son("ding", 0.6)
        au = puce("UDC de la ville de Zurich", 24).move_to([-4.2, -0.2, 0]); aul = bandeau("Auteur de l'initiative", 20).next_to(au, DOWN, buff=0.15)
        self.at(W(4, 1, "UDC") - 0.3, FadeIn(au, shift=0.2 * RIGHT), FadeIn(aul), FadeIn(vil, shift=0.3 * UP), FadeIn(vl), rt=0.5)
        ini = page("Initiative populaire", ["« Einbürgerungen", "vors Volk ! »"], taille=26).move_to([-4.2, -1.0, 0])
        self.at(W(4, 1, "dépose") - 0.3, FadeOut(aul), au.animate.move_to([-4.6, 0.95, 0]), FadeIn(ini, shift=0.3 * UP), rt=0.5); self.son("hop")
        self.at(W(4, 1, "intitulée") + 0.2, ini.animate.move_to([-0.1, -0.5, 0]), rt=0.9); self.son("plop")
        tr = bas("Les naturalisations devant le peuple", 28)
        self.at(W(4, 1, "naturalisations") - 0.3, FadeIn(tr, shift=0.15 * UP), rt=0.5)
        # 5 — qui est visé, qui déciderait
        self.vider(S(5, 1) - 0.45, rt=0.4)
        cs = VGroup(*[candidat(1.5, k) for k in range(3)]).arrange(RIGHT, buff=0.4).move_to([-4.3, -0.9, 0])
        ds = VGroup(*[dossier(0.7).next_to(c, RIGHT, buff=-0.1).shift(0.25 * DOWN) for c in cs])
        c1 = puce("Demandes de naturalisation", 24).move_to([-4.3, 2.2, 0])
        c2 = bandeau("Personnes étrangères nées à l'étranger", 22).next_to(cs, DOWN, buff=0.3)
        self.at(S(5, 1), FadeIn(c1, shift=0.2 * DOWN), LaggedStart(*[FadeIn(c, shift=0.2 * UP) for c in cs], lag_ratio=0.15), FadeIn(ds), rt=0.7)
        self.at(W(5, 1, "personnes") - 0.2, FadeIn(c2, shift=0.15 * UP), rt=0.4)
        self.at(W(5, 1, "nées") - 0.15, Indicate(c2, color=CREME, scale_factor=1.06), rt=0.6)
        el = VGroup(electeurs(5, 1.05), electeurs(5, 1.05)).arrange(DOWN, buff=0.2).move_to([4.2, -0.7, 0])
        fl = Arrow([-1.6, -0.6, 0], [1.3, -0.6, 0], color=CREME, stroke_width=8, buff=0); dl = T("la décision", 22).next_to(fl, UP, buff=0.12)
        self.at(W(5, 2, "transférer") - 0.3, GrowArrow(fl), FadeIn(dl), rt=0.6); self.son("souffle")
        e1 = puce("Électeurs domiciliés à Zurich", 24).move_to([4.2, 2.2, 0])
        self.at(W(5, 2, "électeurs") - 0.3, LaggedStart(*[FadeIn(b, shift=0.15 * UP) for r in el for b in r], lag_ratio=0.05), FadeIn(e1, shift=0.2 * DOWN), rt=0.8)
        e2 = bandeau("qui ont le droit de cité de la ville", 22).next_to(el, DOWN, buff=0.3)
        cit = VGroup(*[VGroup(RoundedRectangle(corner_radius=0.03, width=0.24, height=0.16, fill_color=ENCRE, fill_opacity=1, stroke_width=0)).move_to(b.get_center() + 0.05 * DOWN) for r in el for b in r])
        self.at(W(5, 2, "possèdent") - 0.3, FadeIn(e2, shift=0.15 * UP), LaggedStart(*[FadeIn(c, scale=2) for c in cit], lag_ratio=0.04), rt=0.8)
        # 6 — avant : organes communaux ; avec l'initiative : aux urnes, dossier par dossier
        self.vider(S(6, 1) - 0.45, rt=0.4)
        ta = puce("Avant", 28).move_to([-3.9, 2.6, 0]); tb = puce("Avec l'initiative", 28).move_to([3.7, 2.6, 0])
        sep = DashedLine([0, 2.9, 0], [0, -2.4, 0], color=CREME, stroke_width=3, dash_length=0.15).set_opacity(0.5)
        org = maison(0, 0, 2.4, 1.3, 1.1).move_to([-3.9, -0.2, 0]); ol = bandeau("Organes communaux", 22).next_to(org, DOWN, buff=0.2)
        d0 = dossier(0.8).move_to([-6.2, -0.2, 0])
        self.at(S(6, 1), FadeIn(ta, shift=0.2 * DOWN), FadeIn(org, shift=0.3 * UP), FadeIn(ol), FadeIn(d0), rt=0.5)
        self.play(d0.animate.move_to(org.get_center() + 0.25 * DOWN), run_time=0.7); self.son("plop")
        ck = coche(True, 0.3).next_to(org, RIGHT, buff=0.2); self.play(FadeIn(ck, scale=2), run_time=0.3)
        u = urne(1.6).move_to([3.7, -0.9, 0])
        self.at(S(6, 2), FadeIn(tb, shift=0.2 * DOWN), FadeIn(sep), FadeIn(u, shift=0.3 * UP), VGroup(ta, org, ol, d0, ck).animate.set_opacity(0.45), rt=0.6)
        au = maison(0, 0, 1.2, 0.7, 0.7).move_to([1.2, 1.2, 0]); al = T("Proposition", 20).next_to(au, DOWN, buff=0.1)
        self.at(W(6, 2, "urnes") - 0.2, Indicate(u[1], color=CREME, scale_factor=1.08), rt=0.5); self.son("ding", 0.6)
        self.at(W(6, 2, "proposition") - 0.3, FadeIn(au, shift=0.2 * DOWN), FadeIn(al), rt=0.4)
        t0 = W(6, 2, "dossier"); dd = bas("Dossier par dossier", 28).set_x(3.7)
        self.jusqua(t0 - 0.3); self.play(FadeIn(dd, shift=0.15 * UP), run_time=0.3)
        for k in range(3):
            d = dossier(0.7).move_to(au.get_center() + 0.6 * RIGHT)
            self.play(FadeIn(d, scale=0.4), run_time=0.15); self.play(d.animate.move_to(u[1].get_top() + 0.2 * UP).scale(0.6), run_time=0.4, path_arc=-0.8); self.son("plop", 0.7); self.remove(d)
        # 7 — des signatures ne suffisent pas : le droit supérieur
        self.vider(S(7, 1) - 0.45, rt=0.4)
        sg = page("Signatures", ["~~~~~~  ~~~~", "~~~~  ~~~~~~", "~~~~~~~  ~~~"], taille=20).move_to([-4.4, 0.3, 0]); ok = coche(True, 0.4).next_to(sg, RIGHT, buff=0.3)
        self.at(S(7, 1), FadeIn(sg, shift=0.3 * UP), rt=0.5); self.at(W(7, 1, "signatures") - 0.1, FadeIn(ok, scale=2), rt=0.3); self.son("plop")
        ns = bandeau("Cela ne suffit pas", 26).next_to(sg, DOWN, buff=0.35)
        self.at(W(7, 1, "valable") - 0.6, FadeIn(ns, shift=0.15 * UP), rt=0.4)
        cst = constit(None, 0.8).move_to([3.6, 1.4, 0]); dsup = puce("Droit supérieur", 26).next_to(cst, RIGHT, buff=0.3)
        ini = initiative(0.8).move_to([3.6, -1.6, 0]); fl = Arrow(ini.get_top() + 0.05 * UP, cst.get_bottom() + 0.15 * DOWN, color=CREME, stroke_width=7, buff=0)
        self.at(S(7, 2) - 0.1, FadeIn(ini, shift=0.3 * UP), VGroup(sg, ok, ns).animate.set_opacity(0.45), rt=0.5)
        self.at(W(7, 2, "droit") - 0.5, FadeIn(cst, shift=0.3 * DOWN), FadeIn(dsup), GrowArrow(fl), rt=0.6); self.son("ding", 0.6)
        cf = T("doit le respecter", 22).next_to(fl, RIGHT, buff=0.2); self.play(FadeIn(cf), run_time=0.3)
        # 8 à 11 — le parcours : quatre décisions
        self.vider(S(8, 1) - 0.45, rt=0.4)
        xs = [-5.25, -1.75, 1.75, 5.25]
        st = [station(["Parlement", "communal"], "17 janvier 2001"), station(["Conseil", "de district"], "30 août 2001"), station(["Gouvernement", "cantonal"], "13 novembre 2002"), station(["Tribunal", "fédéral"], "9 juillet 2003")]
        for s_, x in zip(st, xs): s_.move_to([x, -0.75, 0])
        fls = [Arrow(st[k].get_right() + 0.02 * RIGHT, st[k + 1].get_left() + 0.02 * LEFT, color=CREME, stroke_width=6, buff=0.05, max_tip_length_to_length_ratio=0.5) for k in range(3)]
        t = titre("Valable ou non ? Quatre décisions"); ini = initiative(0.62, True).move_to([xs[0], 1.6, 0])
        self.at(S(8, 1) - 0.05, FadeIn(t, shift=0.2 * DOWN), FadeIn(st[0], shift=0.3 * UP), FadeIn(ini, shift=0.2 * DOWN), rt=0.5)
        v0 = verdict("INVALIDE", False).move_to(st[0].get_center() + 0.25 * DOWN)
        self.at(W(8, 1, "invalide") - 0.3, FadeIn(v0, scale=2.2), rt=0.25); self.son("thud")
        jg = VGroup(Rectangle(width=2.4, height=0.3, fill_color=ROUGE_4, fill_opacity=1, stroke_width=0)); jg.move_to([xs[0], -2.45, 0])
        rp = Rectangle(width=1.6, height=0.3, fill_color=CREME, fill_opacity=1, stroke_width=0).align_to(jg, LEFT).set_y(-2.45)
        jl = T("Majorité des 2/3", 22).next_to(jg, RIGHT, buff=0.25)
        self.at(W(8, 1, "majorité") - 0.3, FadeIn(jg), GrowFromEdge(rp, LEFT), FadeIn(jl), rt=0.7)
        # 9
        self.at(S(9, 1) - 0.1, GrowArrow(fls[0]), FadeOut(jg), FadeOut(rp), FadeOut(jl), rt=0.5); self.son("souffle")
        self.at(S(9, 2) - 0.1, FadeIn(st[1], shift=0.3 * UP), ini.animate.set_x(xs[1]), rt=0.6)
        v1 = verdict("AU VOTE", True).move_to(st[1].get_center() + 0.25 * DOWN)
        self.at(W(9, 2, "raison") - 0.3, FadeIn(v1, scale=2.2), v0.animate.set_opacity(0.5), st[0].animate.set_opacity(0.6), rt=0.3); self.son("joie")
        # 10
        self.at(S(10, 1) - 0.1, GrowArrow(fls[1]), rt=0.5); self.son("souffle")
        self.at(S(10, 2) - 0.1, FadeIn(st[2], shift=0.3 * UP), ini.animate.set_x(xs[2]), rt=0.6)
        v2 = verdict("INVALIDE", False).move_to(st[2].get_center() + 0.25 * DOWN)
        self.at(W(10, 2, "confirme") - 0.3, FadeIn(v2, scale=2.2), v1.animate.set_opacity(0.5), st[1].animate.set_opacity(0.6), rt=0.3); self.son("thud")
        # 11
        self.at(S(11, 1) - 0.1, GrowArrow(fls[2]), rt=0.5); self.son("souffle")
        rc = bandeau("Recours : l'UDC zurichoise et 2 citoyens", 22).move_to([2.2, -2.6, 0])
        self.at(W(11, 1, "saisissent") - 0.3, FadeIn(st[3], shift=0.3 * UP), ini.animate.set_x(xs[3]), FadeIn(rc, shift=0.15 * UP), v2.animate.set_opacity(0.5), st[2].animate.set_opacity(0.6), rt=0.6)
        q = puce("?", 44).move_to(st[3].get_center() + 0.25 * DOWN)
        self.at(S(11, 2), FadeIn(q, scale=0.4), Indicate(st[3][-1], color=CREME, scale_factor=1.15), rt=0.6); self.son("ding", 0.7)
        self.fin()
