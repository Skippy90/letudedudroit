from base import *
from s_a import quatre


def asso(n=18, h=0.6):
    """L'association : un groupe d'aînées derrière une banderole."""
    cols = [CREME, MENTHE, LILAS, AMBRE, CIEL]
    g = VGroup(*[ainee(h, cols[k % 5], "neutre", canne=(k % 3 == 0)) for k in range(n)]).arrange_in_grid(2, n // 2, buff=(0.12, 0.05))
    ban = puce("Aînées pour le climat", 20).next_to(g, UP, buff=0.12)
    r = VGroup(g, ban); r.membres, r.ban = g, ban
    return r


def batiment(nom, l=2.2, taille=20):
    m = maison(0, 0, l, 1.25, 1.0); m.move_to(ORIGIN)
    return VGroup(m, bandeau(nom, taille).next_to(m, DOWN, buff=0.15))


class Bf(Sec25):
    L0, L1 = 4, 14

    def construct(self):
        self.debut(); self.chapitre(0, "Les faits", 1)
        # 4 — 25 novembre 2016 : l'association adresse une demande au Conseil fédéral
        cal = calendrier("25 NOV.", "2016").scale(0.85).move_to([-5.9, 2.6, 0])
        self.at(S(4, 1) - 0.2, FadeIn(cal, shift=0.3 * DOWN), rt=0.5)
        a = asso(); a.move_to([-3.2, -1.0, 0])
        pal = palais(3.0).move_to([4.3, -1.1, 0]); pl = bandeau("Conseil fédéral", 22).next_to(pal, DOWN, buff=0.2)
        self.at(S(4, 2) - 0.1, LaggedStart(*[FadeIn(x, shift=0.2 * UP) for x in a.membres], lag_ratio=0.03), rt=0.7)
        self.at(W(4, 2, "Aînées") - 0.3, FadeIn(a.ban, scale=1.5), rt=0.4); self.son("ding", 0.7)
        self.at(W(4, 2, "adresse") - 0.3, FadeIn(pal, shift=0.3 * UP), FadeIn(pl), rt=0.5)
        env = enveloppe(0.9).move_to(a.get_right() + 0.5 * RIGHT + 0.3 * UP)
        self.son("hop"); self.play(FadeIn(env, scale=0.4), run_time=0.2)
        self.play(env.animate.move_to(pal.get_left() + 0.7 * LEFT + 0.2 * UP), run_time=0.8, path_arc=-0.7); self.son("plop")
        nom = bandeau("En allemand : KlimaSeniorinnen Schweiz", 20).next_to(a, DOWN, buff=0.25)
        self.play(FadeIn(nom, shift=0.1 * UP), run_time=0.4)
        # 5 — quatre femmes agissent à ses côtés
        self.at(S(5, 1) - 0.45, FadeOut(nom), a.animate.scale(0.7).move_to([-4.6, 1.0, 0]), rt=0.4)
        q = quatre(1.5); q.move_to([-2.2, -1.6, 0])
        self.at(S(5, 1), LaggedStart(*[FadeIn(x, shift=0.3 * UP) for x in q], lag_ratio=0.15), rt=0.7)
        let = page("Demande", ["Au Conseil fédéral", "…", "…"], l=2.6, taille=18).move_to([1.6, 0.9, 0])
        self.at(W(5, 1, "agissent") - 0.3, FadeIn(let, shift=0.2 * DOWN), rt=0.4)
        for k in range(4):
            sg = VMobject(color=[MENTHE, AMBRE, LILAS, CIEL][k], stroke_width=5).set_points_smoothly([let.get_bottom() + np.array([-0.9 + 0.5 * k + dx, 0.25 + dy, 0]) for dx, dy in ((0, 0), (0.1, 0.12), (0.2, -0.04), (0.3, 0.1), (0.4, 0))])
            self.son("flic", 0.8); self.play(Create(sg), q[k].animate(rate_func=there_and_back).shift(0.15 * UP), run_time=0.22)
        age = puce("76 à 87 ans", 34).move_to([-2.2, 1.4, 0]); ar = bandeau("au moment de la procédure", 22).next_to(age, DOWN, buff=0.15)
        self.at(S(5, 2) - 0.05, FadeOut(a), FadeIn(ar, shift=0.1 * UP), rt=0.3)
        self.at(W(5, 2, "septante") - 0.3, FadeIn(age, scale=1.4), rt=0.4); self.son("plop")
        # 6 — la requête vise aussi un département et deux offices
        self.vider(S(6, 1) - 0.5, garder=[cal], rt=0.4)
        t = titre("Quatre destinataires")
        bs = VGroup(batiment("Conseil fédéral"), batiment("Département (DETEC)"), batiment("Office de l'environnement"), batiment("Office de l'énergie")).arrange(RIGHT, buff=0.45).move_to([0, 0.2, 0])
        q = quatre(0.9, "decide"); q.move_to([0, -2.45, 0])
        self.at(S(6, 1) - 0.05, FadeIn(t, shift=0.2 * DOWN), FadeIn(bs[0], shift=0.2 * UP), FadeIn(q, shift=0.2 * UP), rt=0.5)
        for k, tt in ((1, W(6, 1, "Département")), (2, W(6, 1, "celui")), (3, W(6, 1, "celui", 2))):
            e = enveloppe(0.6).move_to(q.get_top() + 0.3 * UP)
            self.jusqua(tt - 0.3); self.son("hop", 0.8)
            self.play(FadeIn(bs[k], shift=0.2 * UP), e.animate.move_to(bs[k][0].get_top() + 0.4 * UP), run_time=0.45); self.son("plop", 0.7)
            if k == 1:
                dl = bandeau("Environnement, transports, énergie, communication", 20).move_to([0, -1.45, 0]); self.play(FadeIn(dl, shift=0.1 * UP), run_time=0.3)
        # 7 — le reproche
        self.vider(S(7, 1) - 0.5, garder=[cal], rt=0.4)
        t = titre("Le reproche"); q = quatre(1.5, "decide"); q.move_to([-3.4, -1.4, 0])
        te = terre(1.3, "inquiet").move_to([3.0, 0.2, 0]); th = thermometre(1.1, 0.35).move_to([5.4, 0.2, 0])
        self.at(S(7, 1) - 0.1, FadeIn(t, shift=0.2 * DOWN), FadeIn(q, shift=0.2 * UP), rt=0.5)
        self.at(S(7, 2) - 0.1, FadeIn(te, scale=0.6), FadeIn(th, shift=0.2 * UP), rt=0.4)
        bu = bulle(["Pas assez de mesures", "contre le réchauffement"], 24); bu.next_to(q, UP, buff=0.3).shift(1.2 * RIGHT)
        self.at(W(7, 2, "mesures") - 0.3, FadeIn(bu, shift=0.15 * UP), rt=0.4)
        self.at(W(7, 2, "réchauffement") - 0.4, th.niv.animate.set_value(0.85), rt=1.0); terre_visage(te, "chaud"); self.son("triste", 0.6)
        self.saut(*q, h=0.14, rt=0.35)
        # 8 — l'Accord de Paris
        self.vider(S(8, 1) - 0.5, garder=[cal], rt=0.4)
        acc = page("Accord de Paris", ["Objectif", "de température"], l=3.6, taille=22).move_to([-3.4, 0.2, 0])
        self.at(S(8, 1) + 0.3, FadeIn(acc, shift=0.3 * UP), rt=0.5); self.son("plop")
        th = thermometre(1.5, 0.15).move_to([2.6, -0.2, 0])
        Y = lambda v: th.boule.get_center()[1] + 1.5 * (0.5 + 1.75 * v)
        self.at(S(8, 2) - 0.1, FadeIn(th, shift=0.2 * UP), rt=0.4)
        self.at(W(8, 2, "élévation") - 0.2, th.niv.animate.set_value(0.5), rt=1.2)
        lim = DashedLine([1.5, Y(0.8), 0], [4.2, Y(0.8), 0], color=CREME, stroke_width=5); l2 = puce("+ 2 °C", 28).next_to(lim, RIGHT, buff=0.15)
        self.at(W(8, 2, "deux") - 0.5, Create(lim), FadeIn(l2, scale=1.4), rt=0.4); self.son("ding", 0.7)
        nd = bandeau("nettement en dessous", 20).next_to(l2, DOWN, buff=0.12); self.play(FadeIn(nd, shift=0.1 * UP), run_time=0.3)
        lim2 = DashedLine([1.5, Y(0.56), 0], [4.2, Y(0.56), 0], color=AMBRE, stroke_width=5); l15 = puce("+ 1,5 °C", 24).next_to(lim2, RIGHT, buff=0.15).shift(0.25 * DOWN)
        ef = bandeau("Efforts pour limiter à 1,5 °C", 20).next_to(l15, DOWN, buff=0.12)
        self.at(W(8, 2, "limiter") - 0.4, Create(lim2), FadeIn(l15, scale=1.4), FadeIn(ef), FadeOut(nd), rt=0.4); self.son("ding", 0.6)
        # 9 — ce qu'elles demandent : au moins 50 % d'ici à 2030
        self.vider(S(9, 1) - 0.5, garder=[cal], rt=0.4)
        t = titre("Ce qu'elles demandent")
        sol = Line([-4.6, -2.3, 0], [4.6, -2.3, 0], color=CREME, stroke_width=4)
        def colonne(x, hh, nomb):
            r = Rectangle(width=1.5, height=hh, fill_color=GRIS, fill_opacity=1, stroke_width=0).move_to([x, -2.3 + hh / 2, 0])
            return r, T(nomb, 26).move_to([x, -2.75, 0])
        r1, n1 = colonne(-2.4, 3.6, "1990"); r2, n2 = colonne(2.4, 3.6, "2030")
        em = bandeau("Gaz à effet de serre", 22).move_to([-2.4, 1.75, 0])
        self.at(S(9, 1) - 0.05, FadeIn(t, shift=0.2 * DOWN), Create(sol), rt=0.4)
        self.at(W(9, 1, "trente") - 0.6, FadeIn(r2, shift=0.2 * UP), FadeIn(n2), rt=0.4)
        self.at(W(9, 1, "réduction") - 0.4, FadeIn(r1, shift=0.2 * UP), FadeIn(n1), rt=0.4)
        m50 = puce("au moins − 50 %", 34).move_to([2.4, 1.2, 0])
        self.jusqua(W(9, 1, "cinquante") - 0.4)
        self.son("souffle"); self.play(r2.animate.stretch_to_fit_height(1.8).move_to([2.4, -2.3 + 0.9, 0]), FadeIn(m50, scale=1.4), run_time=0.7)
        self.at(W(9, 1, "émissions") - 0.2, FadeIn(em), rt=0.3)
        pr = bandeau("par rapport à 1990", 22).next_to(m50, DOWN, buff=0.15); self.at(W(9, 1, "rapport") - 0.2, FadeIn(pr), rt=0.3)
        # 10 — pourquoi ces femmes ? les fortes chaleurs
        self.vider(S(10, 1) - 0.5, garder=[cal], rt=0.4)
        t = titre("Pourquoi ces femmes ?", 34); q = quatre(1.5, "perplexe"); q.move_to([-3.4, -1.5, 0])
        self.at(S(10, 1) - 0.1, FadeIn(t, scale=1.3), FadeIn(q, shift=0.2 * UP), rt=0.4)
        et = VGroup(*[page("Étude", ["…", "…"], l=1.7, taille=16).scale(0.8).rotate(0.06 * (k - 1)) for k in range(3)]).arrange(RIGHT, buff=0.12).move_to([3.2, 0.4, 0])
        self.at(W(10, 2, "études") - 0.4, LaggedStart(*[FadeIn(x, shift=0.2 * DOWN) for x in et], lag_ratio=0.2), rt=0.6)
        so = soleil(1.3).move_to([4.6, 1.8, 0]); th = thermometre(1.0, 0.3).move_to([1.4, 0.3, 0])
        self.at(W(10, 2, "épisodes") - 0.3, FadeOut(et), FadeIn(so, scale=0.4), FadeIn(th, shift=0.2 * UP), rt=0.5)
        self.play(th.niv.animate.set_value(0.95), run_time=0.9)
        for x in q: visage(x, 1.5, "surpris")
        rk = VGroup(T("Risques particulièrement élevés", 24, AMBRE), T("pour la santé et la vie, selon les études citées", 20, CREME, False)).arrange(DOWN, buff=0.1).move_to([3.3, -2.5, 0])
        self.at(W(10, 2, "risques") - 0.3, FadeIn(rk[0], shift=0.1 * UP), rt=0.4); self.son("triste", 0.7)
        self.at(W(10, 2, "santé") - 0.3, FadeIn(rk[1]), rt=0.3)
        for x in q: visage(x, 1.5, "triste")
        f75 = puce("Femmes de plus de 75 ans", 28).move_to([3.3, -1.5, 0])
        self.at(W(10, 2, "femmes") - 0.2, FadeIn(f75, scale=1.3), rt=0.4)
        # 11 — les droits invoqués
        self.vider(S(11, 1) - 0.5, garder=[cal], rt=0.4)
        t = titre("Leur argumentation juridique")
        q = quatre(0.9, "decide"); q.move_to([0, -2.4, 0])
        c1 = carton(["Droit à la vie", "art. 10 Cst. · art. 2 CEDH"], 5.4, 1.9, 26).move_to([-3.1, 0.6, 0]); c1[1][1].scale(0.78)
        c2 = carton(["Vie privée et familiale", "art. 8 CEDH"], 5.4, 1.9, 26).move_to([3.1, 0.6, 0]); c2[1][1].scale(0.78)
        self.at(S(11, 1) - 0.05, FadeIn(t, shift=0.2 * DOWN), FadeIn(q, shift=0.2 * UP), rt=0.4)
        so = soleil(0.7).move_to([5.6, 2.4, 0]); vu = puce("Une vulnérabilité particulière", 24).move_to([0, 2.15, 0])
        self.at(W(11, 1, "vulnérabilité") - 0.3, FadeIn(so, scale=0.4), FadeIn(vu, scale=1.2), rt=0.4); self.son("plop", 0.7)
        self.saut(*q, h=0.12, rt=0.35)
        self.at(W(11, 2, "droit") - 0.25, FadeIn(c1, shift=0.3 * RIGHT), rt=0.45); self.son("plop")
        self.at(W(11, 2, "droit", 2) - 0.25, FadeIn(c2, shift=0.3 * LEFT), rt=0.45); self.son("plop")
        mn = bandeau("déjà menacés, selon elles, par des mesures insuffisantes", 22).move_to([0, -0.95, 0])
        self.at(W(11, 2, "insuffisance") - 0.3, FadeIn(mn, shift=0.15 * UP), rt=0.4)
        # 12 — le département n'entre pas en matière
        self.vider(S(12, 1) - 0.5, rt=0.4)
        dep = batiment("Département (DETEC)", 3.0, 22).move_to([3.4, -0.5, 0])
        q = quatre(1.2, "decide"); q.move_to([-3.6, -1.6, 0])
        env = enveloppe(0.8).move_to([-1.5, -0.6, 0])
        self.at(S(12, 1) - 0.1, FadeIn(dep, shift=0.3 * UP), FadeIn(q), FadeIn(env), rt=0.5)
        self.play(env.animate.move_to(dep[0].get_left() + 0.6 * LEFT), run_time=0.7)
        cal = calendrier("25 AVRIL", "2017").scale(0.85).move_to([-5.9, 2.6, 0])
        self.at(S(12, 2) - 0.1, FadeIn(cal, shift=0.3 * DOWN), rt=0.4)
        nem = tampon("N'ENTRE PAS EN MATIÈRE", 26).move_to(dep[0].get_top() + 0.7 * UP)
        self.at(W(12, 2, "refuse") - 0.15, FadeIn(nem, scale=2.2), rt=0.3); self.son("thud")
        self.play(env.animate.move_to([-1.5, -0.6, 0]).rotate(-0.4), run_time=0.45, rate_func=rate_functions.ease_out_bounce)
        for x in q: visage(x, 1.2, "triste")
        self.son("triste", 0.8)
        pf = bas("Les mesures demandées ne sont même pas examinées", 24); self.at(W(12, 3, "examine") - 0.4, FadeIn(pf, shift=0.15 * UP), rt=0.4)
        # 13 — le Tribunal administratif fédéral, puis le Tribunal fédéral
        self.vider(S(13, 1) - 0.5, rt=0.4)
        t = titre("Deux recours")
        q = quatre(0.9, "decide"); q.move_to([-5.6, -1.5, 0])
        taf = tribunal(2.5).scale(0.9).move_to([-0.6, -0.8, 0]); tal = bandeau("Tribunal administratif fédéral", 20).next_to(taf, DOWN, buff=0.15)
        tf = tribunal(3.0).scale(0.95).move_to([4.6, -0.7, 0]); tfl = bandeau("Tribunal fédéral", 20).next_to(tf, DOWN, buff=0.15)
        d = dossier(0.8).move_to(q.get_right() + 0.45 * RIGHT + 0.2 * UP)
        self.at(S(13, 1) - 0.1, FadeIn(t, shift=0.2 * DOWN), FadeIn(q), FadeIn(d, scale=0.4), rt=0.5); self.son("hop")
        self.at(S(13, 2) - 0.2, FadeIn(taf, shift=0.3 * UP), FadeIn(tal), rt=0.4)
        self.play(d.animate.move_to(taf.get_left() + 0.5 * LEFT + 0.2 * UP), run_time=0.7)
        rej = tampon("REJETÉ", 28).move_to(taf.get_top() + 0.55 * UP); nv = bandeau("27 novembre 2018", 20).next_to(rej, UP, buff=0.12)
        self.at(W(13, 2, "rejette") - 0.15, FadeIn(rej, scale=2.2), FadeIn(nv), rt=0.3); self.son("thud")
        for x in q: visage(x, 0.9, "triste")
        self.at(S(13, 3) - 0.1, FadeIn(tf, shift=0.3 * UP), FadeIn(tfl), rt=0.5)
        for x in q: visage(x, 0.9, "decide")
        self.jusqua(W(13, 3, "tournent") - 0.2)
        self.son("hop"); self.play(d.animate.move_to(tf.get_left() + 0.5 * LEFT + 0.2 * UP), *[x.animate(rate_func=there_and_back).shift(0.15 * UP) for x in q], run_time=1.0, path_arc=-0.5)
        self.fin()
