from base import *


class C(Sec232):
    L0, L1 = 12, 16

    def construct(self):
        self.debut(0); self.chapitre(1, "La question", 2)
        # 12 — ce n'est pas le mérite des candidats qui est jugé
        cs = VGroup(*[candidat(1.6, k) for k in range(3)]).arrange(RIGHT, buff=0.5).move_to([-3.6, -0.9, 0])
        mq = bulle_pensee("Méritent-ils la nationalité ?", 22).move_to([-3.6, 1.55, 0])
        self.at(S(12, 1) - 0.05, LaggedStart(*[FadeIn(c, shift=0.2 * UP) for c in cs], lag_ratio=0.12), rt=0.6)
        self.at(W(12, 1, "méritent") - 0.5, FadeIn(mq, shift=0.15 * UP), rt=0.4)
        x = VGroup(Line(mq.get_corner(UL), mq.get_corner(DR), color=ENCRE, stroke_width=9), Line(mq.get_corner(DL), mq.get_corner(UR), color=ENCRE, stroke_width=9))
        pq = puce("Pas la question", 26).move_to([3.6, 1.55, 0])
        self.play(Create(x), FadeIn(pq, shift=0.2 * LEFT), run_time=0.5); self.son("thud", 0.7)
        tf = tribunal(2.6).move_to([3.6, -0.7, 0]); ad = bandeau("Aucun dossier individuel jugé ici", 24).next_to(tf, DOWN, buff=0.3)
        self.at(S(12, 2) - 0.1, FadeIn(tf, shift=0.3 * UP), rt=0.5); self.at(W(12, 2, "dossier") - 0.3, FadeIn(ad, shift=0.15 * UP), cs.animate.set_opacity(0.5), rt=0.5)
        # 13 — la vraie question
        self.vider(S(13, 1) - 0.45, rt=0.4)
        t = titre("La vraie question")
        d = VGroup(dossier(1.3), puce("Décision individuelle", 22)).arrange(DOWN, buff=0.25).move_to([-4.9, 0.2, 0])
        u = urne(1.7).move_to([0, 0.1, 0]); cdn = cadenas(1.1).move_to(u[1].get_center() + 0.1 * DOWN); ul = puce("Vote secret", 22).next_to(u, DOWN, buff=0.25)
        el = VGroup(electeurs(6, 0.8), electeurs(6, 0.8)).arrange(DOWN, buff=0.12); ell = puce("Tous les électeurs concernés", 22)
        eg = VGroup(el, ell).arrange(DOWN, buff=0.25).move_to([4.7, 0.1, 0])
        self.at(S(13, 1) - 0.05, FadeIn(t, shift=0.2 * DOWN), rt=0.4)
        self.at(W(13, 1, "confier") - 0.3, FadeIn(d, shift=0.3 * RIGHT), rt=0.5); self.son("plop")
        self.at(W(13, 1, "vote") - 0.4, FadeIn(u, shift=0.3 * UP), FadeIn(ul), rt=0.4); self.play(FadeIn(cdn, scale=2), run_time=0.3); self.son("thud", 0.6)
        self.at(W(13, 1, "ensemble") - 0.4, LaggedStart(*[FadeIn(b, shift=0.15 * UP) for r in el for b in r], lag_ratio=0.03), FadeIn(ell), rt=0.7)
        q = bas("Est-ce possible sans violer la Constitution ?", 28)
        self.play(FadeIn(q, shift=0.15 * UP), run_time=0.4); self.son("ding", 0.7)
        # 14 — la thèse des auteurs
        self.vider(S(14, 1) - 0.45, rt=0.4)
        t = titre("La thèse des auteurs")
        au = parti(1.4).move_to([-4.9, -0.8, 0]); al = bandeau("Les auteurs de l'initiative", 20).next_to(au, DOWN, buff=0.2)
        b1 = bulle(["Souveraineté", "populaire !"], 26).move_to([-1.2, 1.1, 0])
        self.at(S(14, 1) - 0.05, FadeIn(t, shift=0.2 * DOWN), FadeIn(au, shift=0.3 * RIGHT), FadeIn(al), rt=0.5)
        self.at(W(14, 1, "souveraineté") - 0.3, FadeIn(b1, scale=0.6), rt=0.35); self.son("hop")
        cp = carton(["Naturaliser :", "un choix politique"], 5.2, 1.9, 28).move_to([3.5, 0.9, 0])
        el = electeurs(6, 1.0, "content").move_to([3.5, -1.4, 0]); ll = bandeau("que le peuple effectue librement", 22).next_to(el, DOWN, buff=0.2)
        self.at(W(14, 2, "choix") - 0.4, FadeIn(cp, shift=0.3 * UP), rt=0.5)
        self.at(W(14, 2, "peuple") - 0.3, LaggedStart(*[FadeIn(b, shift=0.15 * UP) for b in el], lag_ratio=0.08), FadeIn(ll), rt=0.6); self.son("joie", 0.7)
        # 15 — une procédure adaptée ; des motifs expliqués ensuite
        self.jusqua(S(15, 1) - 0.4)
        self.play(*[FadeOut(x_, shift=0.7 * LEFT) for x_ in (b1, cp, el, ll)], run_time=0.4)
        l1 = ligne_coche(True, "Une procédure adaptée", "informerait les citoyens").set_x(3.2).set_y(1.0)
        l2 = ligne_coche(True, "Une autorité expliquerait", "ensuite les motifs du refus").set_x(3.2).set_y(-0.9); l2.align_to(l1, LEFT)
        self.at(W(15, 1, "procédure") - 0.3, FadeIn(l1, shift=0.3 * LEFT), rt=0.5); self.son("plop")
        self.at(W(15, 2, "autorité") - 0.3, FadeIn(l2, shift=0.3 * LEFT), rt=0.5); self.son("plop")
        se = bas("Selon les auteurs de l'initiative", 24)
        self.play(FadeIn(se, shift=0.15 * UP), run_time=0.4)
        self.fin()
