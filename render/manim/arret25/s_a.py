from base import *


def quatre(h=1.3, humeur="neutre", buff=0.28):
    return VGroup(*[ainee(h, ROBES[k], humeur) for k in range(4)]).arrange(RIGHT, buff=buff * h, aligned_edge=DOWN)


class A(Sec25):
    L0, L1 = 1, 4

    def construct(self):
        self.debut()
        # 1 — 2016 : des femmes âgées demandent à la Confédération de mieux protéger le climat
        cal = calendrier("ANNÉE", "2016").scale(0.85).move_to([-5.9, 2.6, 0])
        q = quatre(1.5); q.move_to([-3.6, -1.35, 0])
        pal = palais(3.0).move_to([4.2, -1.2, 0]); pl = bandeau("La Confédération", 22).next_to(pal, DOWN, buff=0.2)
        self.at(S(1, 1) - 0.05, FadeIn(cal, shift=0.3 * DOWN), LaggedStart(*[FadeIn(a, shift=0.3 * RIGHT) for a in q], lag_ratio=0.12), rt=0.7)
        self.at(W(1, 1, "demandent") - 0.3, FadeIn(pal, shift=0.3 * UP), FadeIn(pl), rt=0.5)
        env = enveloppe(0.9).move_to(q.get_right() + 0.5 * RIGHT + 0.5 * UP)
        self.son("hop"); self.play(FadeIn(env, scale=0.4), run_time=0.25)
        self.play(env.animate.move_to(pal.get_left() + 0.7 * LEFT + 0.3 * UP), run_time=0.9, path_arc=-0.7); self.son("plop")
        th = thermometre(1.0, 0.3).move_to([2.1, 1.75, 0]); te = terre(1.4).move_to([-0.1, 1.7, 0])
        self.at(W(1, 1, "protéger") - 0.4, FadeIn(te, scale=0.5), FadeIn(th, shift=0.2 * UP), rt=0.5); self.son("ding", 0.6)
        for a in q: visage(a, 1.5, "decide")
        bu = bulle(["Protégez mieux", "le climat !"], 24); bu.next_to(q, UP, buff=0.25).shift(0.4 * LEFT)
        self.play(FadeIn(bu, shift=0.15 * UP), th.niv.animate.set_value(0.6), run_time=0.8); terre_visage(te, "inquiet")
        bal = balance(0.5).move_to([5.0, 1.4, 0]); dj = puce("Une démarche juridique", 24).next_to(bal, UP, buff=0.2)
        self.at(S(1, 2) - 0.05, FadeIn(bal, scale=0.6), FadeIn(dj, shift=0.15 * DOWN), rt=0.4); self.son("ding", 0.7)
        dg = VGroup(T("Droits fondamentaux en danger,", 24, AMBRE), T("selon elles", 20, CREME, False)).arrange(DOWN, buff=0.1).move_to([-2.6, -2.85, 0])
        self.at(W(1, 3, "inaction") - 0.3, th.niv.animate.set_value(0.92), te.animate(rate_func=there_and_back).scale(1.08), rt=0.7); terre_visage(te, "chaud"); self.son("triste", 0.6)
        self.at(W(1, 3, "droits") - 0.4, FadeIn(dg, shift=0.15 * UP), rt=0.5)
        self.saut(*q, h=0.14, rt=0.35)
        # 2 — le Tribunal fédéral refuse ; Strasbourg condamne la Suisse
        self.vider(S(2, 1) - 0.5, rt=0.4)
        tf = tribunal(2.8).move_to([-3.9, -0.4, 0]); tl = bandeau("Tribunal fédéral · 2020", 22).next_to(tf, DOWN, buff=0.18)
        q2 = quatre(0.95, "decide"); q2.move_to([0, -2.1, 0])
        self.at(S(2, 1) - 0.05, FadeIn(tf, shift=0.3 * UP), FadeIn(tl), FadeIn(q2, shift=0.2 * UP), rt=0.5)
        non = tampon("PAS D'EXAMEN SUR LE FOND", 24).move_to(tf.get_top() + 0.6 * UP)
        self.at(W(2, 1, "refuse") - 0.1, FadeIn(non, scale=2.2), rt=0.3); self.son("thud")
        for a in q2: visage(a, 0.95, "triste")
        self.son("triste", dt=0.25)
        st = cour(2.8).move_to([3.9, -0.55, 0]); sl = bandeau("Strasbourg · 2024", 22).next_to(st, DOWN, buff=0.18)
        self.at(W(2, 2, "Strasbourg") - 0.9, FadeIn(st, shift=0.3 * UP), FadeIn(sl), tf.animate.set_opacity(0.45), non.animate.set_opacity(0.6), rt=0.6)
        ok = VGroup(coche(True, 0.36), T("Un arrêt contre la Suisse", 24)).arrange(RIGHT, buff=0.2).move_to([3.6, 2.35, 0])
        self.at(W(2, 2, "obtient") - 0.2, FadeIn(ok, scale=1.3), rt=0.35); self.son("joie")
        for a in q2: visage(a, 0.95, "surpris")
        self.saut(*q2, h=0.16, rt=0.4)
        pq = T("?", 150).move_to([0, 0.7, 0])
        self.at(S(2, 3) - 0.05, FadeIn(pq, scale=0.4), rt=0.4)
        for a in q2: visage(a, 0.95, "perplexe")
        self.play(pq.animate(rate_func=there_and_back).scale(1.15), run_time=0.6)
        self.at(W(2, 3, "conclusions") - 0.2, tf.animate.set_opacity(1), rt=0.4)
        # 3 — bienvenue ; le parcours ; la question centrale
        self.vider(S(3, 1) - 0.5, rt=0.4)
        logo = T("L'étude du droit", 64).move_to([0, 0.2, 0])
        self.at(S(3, 1) - 0.1, FadeIn(logo, scale=1.15), rt=0.5)
        ti = puce("Les Aînées pour le climat", 38).move_to([0, 2.6, 0])
        self.at(S(3, 2) - 0.1, logo.animate.scale(0.4).move_to([0, 3.45, 0]).set_opacity(0.8), FadeIn(ti, shift=0.2 * DOWN), rt=0.6)
        t1 = palais(2.2).move_to([-4.2, -0.55, 0]); b1 = bandeau("Administration fédérale", 20).next_to(t1, DOWN, buff=0.2)
        t2 = cour(2.2).move_to([4.2, -0.45, 0]); b2 = bandeau("Cour européenne des droits de l'homme", 20).next_to(t2, DOWN, buff=0.2)
        fl = Arrow([-2.6, -0.3, 0], [2.6, -0.3, 0], color=CREME, stroke_width=7, buff=0)
        qq = quatre(0.8, "decide"); qq.move_to([-2.3, 0.25, 0])
        self.at(W(3, 2, "administration") - 0.4, FadeIn(t1, shift=0.3 * UP), FadeIn(b1), FadeIn(qq, shift=0.2 * UP), rt=0.5)
        self.at(W(3, 2, "Cour") - 0.5, GrowArrow(fl), FadeIn(t2, shift=0.3 * UP), FadeIn(b2), rt=0.5); self.son("hop")
        self.play(*self.marche([qq], [[1.9, 0.25, 0]], 4), run_time=1.2)
        self.vider(S(3, 3) - 0.45, garder=[ti, logo], rt=0.35)
        ch = VGroup(*[VGroup(puce(n, 40), T(s, 26)).arrange(DOWN, buff=0.2) for n, s in (("2", "arrêts"), ("2", "raisonnements"), ("1", "question centrale"))]).arrange(RIGHT, buff=1.1).move_to([0, 0.9, 0])
        for k, mot in enumerate(("arrêts", "raisonnements", "question")):
            self.at(W(3, 3, mot) - 0.3, FadeIn(ch[k], shift=0.2 * UP), rt=0.3); self.son("plop", 0.7)
        f = RoundedRectangle(corner_radius=0.3, width=11.0, height=2.2, fill_color=ROUGE_3, fill_opacity=1, stroke_width=0).move_to([0, -1.5, 0])
        qt = VGroup(T("Qui peut faire contrôler par un juge", 32), T("l'action climatique de l'État ?", 32)).arrange(DOWN, buff=0.2).move_to(f)
        self.at(S(3, 4) - 0.1, ch.animate.scale(0.75).move_to([0, 1.2, 0]), FadeIn(f), FadeIn(qt[0], shift=0.15 * UP), rt=0.45)
        self.at(W(3, 4, "contrôler") + 0.2, FadeIn(qt[1], shift=0.15 * UP), rt=0.4)
        self.fin()
