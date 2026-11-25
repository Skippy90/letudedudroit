from base import *


class A(Sec232):
    L0, L1 = 1, 4

    def construct(self):
        self.debut()
        # 1 — 1999, Zurich : confier au peuple le choix, personne par personne
        cal = calendrier("ANNÉE", "1999").scale(0.85).move_to([-5.8, 2.3, 0])
        vil = VGroup(maison(-0.9, 0, 1.1, 0.8, 0.9), maison(0.35, 0, 1.3, 1.25, 1.0), maison(1.6, 0, 1.0, 0.65, 0.8)).move_to([-5.3, -0.1, 0])
        zl = puce("Zurich", 26).next_to(vil, DOWN, buff=0.2)
        self.at(S(1, 1) - 0.05, FadeIn(cal, shift=0.3 * DOWN), rt=0.4)
        self.at(W(1, 1, "Zurich") - 0.3, FadeIn(vil, shift=0.3 * UP), FadeIn(zl), rt=0.5); self.son("ding", 0.6)
        ini = initiative(0.9).move_to([-1.7, 2.0, 0])
        self.at(W(1, 1, "initiative") - 0.3, FadeIn(ini, shift=0.3 * DOWN), rt=0.5); self.son("hop")
        u = urne(1.5).move_to([0.2, -1.55, 0]); el = electeurs(5, 1.2, "neutre", drapeaux=True).next_to(u, LEFT, buff=0.4).align_to(u, DOWN)
        self.at(W(1, 1, "peuple") - 0.4, FadeIn(u, shift=0.2 * UP), LaggedStart(*[FadeIn(b, shift=0.2 * UP) for b in el], lag_ratio=0.1), zl.animate.set_opacity(0.0), vil.animate.set_opacity(0.0), rt=0.8)
        self.remove(vil, zl)
        cs = VGroup(*[candidat(1.45, k) for k in range(3)]).arrange(RIGHT, buff=0.45).move_to([4.6, -1.3, 0])
        qs = VGroup(*[puce("?", 34).next_to(c, UP, buff=0.18) for c in cs])
        t0 = W(1, 1, "personne"); t1 = W(1, 1, "qui")
        for k in range(3):
            self.at(t0 - 0.2 + k * (t1 - t0) / 3, FadeIn(cs[k], shift=0.25 * LEFT), FadeIn(qs[k], scale=0.4), rt=0.35); self.son("plop", 0.7)
        pp = passeport(0.75).move_to([4.6, 2.45, 0]); ds = bandeau("Qui pourra devenir suisse ?", 26).next_to(pp, DOWN, buff=0.2)
        self.at(W(1, 1, "devenir") - 0.4, FadeIn(pp, scale=0.5), FadeIn(ds, shift=0.15 * DOWN), rt=0.5)
        # 2 — démocratique en apparence ; pourtant déclaré invalide
        self.jusqua(S(2, 1) - 0.25)
        dm = VGroup(coche(True, 0.36), T("Démocratique ?", 28)).arrange(RIGHT, buff=0.25).move_to([-4.3, 0.45, 0])
        humeur(el, "content")
        self.play(FadeOut(cal, shift=0.3 * LEFT), FadeIn(dm, shift=0.2 * DOWN), *[b.animate(rate_func=there_and_back).shift(0.15 * UP) for b in personnes(el)], run_time=0.6)
        self.jusqua(S(2, 2) - 0.2)
        self.play(*[FadeOut(x) for x in (dm, ds, pp, qs)], ini.animate.scale(1.25).move_to([0, 1.35, 0]), el.animate.set_opacity(0.6), cs.animate.set_opacity(0.6), u.animate.set_opacity(0.6), run_time=0.6)
        av = bandeau("Avant même le vote", 24).next_to(ini, LEFT, buff=0.4)
        self.at(W(2, 2, "avant") - 0.2, FadeIn(av, shift=0.15 * RIGHT), rt=0.4)
        humeur(el, "surpris"); [visage(c, 1.45, "surpris") for c in cs]
        tp = tampon("INVALIDE", 44).move_to(ini.get_center() + 0.15 * DOWN)
        self.at(W(2, 2, "invalide") - 0.35, FadeIn(tp, scale=2.4), rt=0.25); self.son("thud")
        self.play(Wiggle(ini, scale_value=1.04), run_time=0.5)
        self.vider(S(2, 3) - 0.45, rt=0.4)
        cst = constit(None, 1.05).move_to([4.3, 0.1, 0]); ini2 = initiative(1.1).move_to([-4.3, 0.2, 0])
        vs = T("contre", 30).move_to([0, 0.2, 0]); eclair = T("?", 150).move_to([0, 1.2, 0])
        self.at(S(2, 3), FadeIn(ini2, shift=0.3 * RIGHT), rt=0.5)
        self.at(W(2, 3, "contraire") - 0.3, FadeIn(cst, shift=0.3 * LEFT), FadeIn(eclair, scale=0.4), rt=0.5); self.son("ding", 0.7)
        q = bas("Une initiative populaire peut-elle être contraire à la Constitution ?", 26)
        self.play(FadeIn(q, shift=0.15 * UP), run_time=0.4)
        # 3 — bienvenue, l'arrêt, la tension
        self.vider(S(3, 1) - 0.4, rt=0.35)
        logo = T("L'étude du droit", 78).move_to([0, 0.3, 0])
        self.at(S(3, 1) - 0.05, FadeIn(logo, scale=0.8), rt=0.4); self.son("joie")
        self.jusqua(S(3, 2) - 0.2)
        ref = puce("ATF 129 I 232", 44).move_to([0, 2.5, 0]); sous = bandeau("Tribunal fédéral · 9 juillet 2003", 24).next_to(ref, DOWN, buff=0.2)
        self.play(logo.animate.scale(0.35).move_to([-5.0, 2.95, 0]).set_opacity(0.8), run_time=0.5)
        self.at(W(3, 2, "ATF") - 0.3, FadeIn(ref, scale=1.3), rt=0.4); self.play(FadeIn(sous, shift=0.1 * UP), run_time=0.3)
        bal = balance(1.35).move_to([0, -1.0, 0]); pg, pd = bal.plats
        ug = urne(0.8).next_to(pg[2], UP, buff=0); cd = constit(None, 0.36).next_to(pd[2], UP, buff=0)
        lg = puce("Démocratie directe", 24).next_to(pg, DOWN, buff=0.3); ld = puce("Droits fondamentaux", 24).next_to(pd, DOWN, buff=0.3)
        self.at(W(3, 2, "affaire") - 0.3, FadeIn(bal, shift=0.3 * UP), rt=0.5)
        self.at(W(3, 2, "démocratie") - 0.3, FadeIn(ug, scale=0.5), FadeIn(lg, shift=0.1 * UP), rt=0.4); self.son("plop")
        self.at(W(3, 2, "droits") - 0.3, FadeIn(cd, scale=0.5), FadeIn(ld, shift=0.1 * UP), rt=0.4); self.son("plop")
        self.play(Rotate(bal.fleau, 0.05), run_time=0.5, rate_func=there_and_back)
        self.fin()
