from base import *


def fiche(lignes, titre_="Dossier du candidat", taille=24):
    return page(titre_, lignes, l=4.4, taille=taille)


class Es(Sec232):
    L0, L1 = 31, 40

    def construct(self):
        self.debut(2); self.chapitre(3, "L'information", 4)
        # 31 — une autre difficulté : les informations à communiquer
        t = titre("Une seconde difficulté")
        j = VGroup(*[juge(1.3) for _ in range(3)]).arrange(RIGHT, buff=0.25).move_to([-5.0, -1.0, 0])
        self.at(S(31, 1) - 0.05, FadeIn(t, shift=0.2 * DOWN), FadeIn(j, shift=0.3 * RIGHT), rt=0.5); self.son("ding", 0.6)
        mv = bandeau("Moins visible, tout aussi importante", 24).move_to([0.6, 2.2, 0])
        self.at(W(31, 1, "moins") - 0.3, FadeIn(mv, shift=0.15 * DOWN), rt=0.4)
        f = fiche(["Informations", "sur le candidat"]).move_to([-0.8, 0.3, 0])
        el = VGroup(electeurs(5, 0.95), electeurs(5, 0.95)).arrange(DOWN, buff=0.15).move_to([4.5, -0.6, 0]); ell = bandeau("Les votants", 22).next_to(el, DOWN, buff=0.2)
        self.at(W(31, 1, "informations") - 0.4, FadeIn(f, shift=0.3 * UP), rt=0.5); self.son("hop")
        fl = Arrow(f.get_right() + 0.1 * RIGHT, el.get_left() + 0.15 * LEFT, color=CREME, stroke_width=8, buff=0)
        self.at(W(31, 1, "communiquer") - 0.3, GrowArrow(fl), LaggedStart(*[FadeIn(b, shift=0.1 * UP) for r in el for b in r], lag_ratio=0.03), FadeIn(ell), rt=0.7)
        # 32 — art. 34 al. 2 Cst.
        self.vider(S(32, 1) - 0.45, rt=0.4)
        cst = constit("34", 0.9).move_to([-5.0, 0.2, 0])
        p = page("Art. 34 al. 2 Cst.", ["La libre formation", "de l'opinion", "L'expression fidèle et sûre", "de la volonté"], taille=26).move_to([1.2, 0.6, 0])
        self.at(S(32, 1) - 0.05, FadeIn(cst, shift=0.3 * RIGHT), FadeIn(p, shift=0.3 * UP), rt=0.5); self.son("hop")
        k1 = cadre_autour(VGroup(p.corps[0], p.corps[1]), 0.06); self.at(W(32, 1, "libre") - 0.2, Create(k1), rt=0.4)
        k2 = cadre_autour(VGroup(p.corps[2], p.corps[3]), 0.06); self.at(W(32, 1, "expression") - 0.2, ReplacementTransform(k1, k2), rt=0.4)
        inf = bas("Il faut une information suffisante et objective", 28)
        self.at(W(32, 2, "information") - 0.5, FadeOut(k2), FadeIn(inf, shift=0.15 * UP), rt=0.4); self.son("ding", 0.6)
        # 33 — ce que cela peut concerner
        self.vider(S(33, 1) - 0.45, rt=0.4)
        c = candidat(2.1, 2, "neutre").move_to([-4.6, -0.7, 0])
        mots = ["Origine", "Revenu", "Formation", "Travail", "Langues", "Situation familiale"]
        f = fiche(mots, taille=26).move_to([1.6, 0.0, 0])
        for x in f.corps: x.set_opacity(0)
        self.at(S(33, 1) - 0.05, FadeIn(c, shift=0.3 * RIGHT), FadeIn(f, shift=0.3 * UP), rt=0.5)
        cles = ["origine", "revenu", "formation", "travail", "connaissances", "situation"]
        for k, m in enumerate(cles):
            self.at(W(33, 1, m) - 0.2, f.corps[k].animate.set_opacity(1), rt=0.25); self.son("plop", 0.6)
        # 34 — mais c'est la sphère privée : art. 13 Cst.
        self.jusqua(S(34, 1) - 0.15)
        cdn = cadenas(1.6).move_to(f.get_center() + 0.2 * DOWN); sp = puce("Sphère privée", 28).next_to(f, UP, buff=0.25)
        self.play(FadeIn(cdn, scale=2.2), FadeIn(sp, shift=0.1 * UP), f.corps.animate.set_opacity(0.35), run_time=0.4); self.son("thud", 0.7); visage(c, 2.1, "surpris")
        p = page("Art. 13 Cst.", ["Vie privée et familiale", "Données personnelles"], l=4.6, taille=24).move_to([-3.7, 1.3, 0])
        self.at(S(34, 2) - 0.05, c.animate.scale(0.75).move_to([-5.6, -1.4, 0]), FadeIn(p, shift=0.3 * UP), rt=0.5); self.son("hop")
        k = cadre_autour(p.corps[0], 0.06); self.at(W(34, 2, "vie") - 0.2, Create(k), rt=0.35)
        k2 = cadre_autour(p.corps[1], 0.06); self.at(W(34, 2, "données") - 0.2, ReplacementTransform(k, k2), rt=0.35)
        # 35 — le dilemme
        self.vider(S(35, 1) - 0.45, rt=0.4)
        t = titre("Le dilemme")
        a = carton(["Informer", "suffisamment"], 4.8, 1.8, 28).move_to([-3.6, 1.0, 0]); b = carton(["Limiter", "l'information"], 4.8, 1.8, 28).move_to([3.6, 1.0, 0])
        ra = VGroup(coche(False, 0.34), T("Données privées exposées", 24)).arrange(RIGHT, buff=0.2).next_to(a, DOWN, buff=0.5)
        rb = VGroup(coche(False, 0.34), VGroup(T("Vote moins objectif,", 24), T("ou fondé sur des stéréotypes", 24)).arrange(DOWN, buff=0.08, aligned_edge=LEFT)).arrange(RIGHT, buff=0.2).next_to(b, DOWN, buff=0.4)
        fa = Arrow(a.get_bottom(), a.get_bottom() + 0.45 * DOWN, color=CREME, stroke_width=6, buff=0.03); fb = Arrow(b.get_bottom(), b.get_bottom() + 0.4 * DOWN, color=CREME, stroke_width=6, buff=0.03)
        self.at(S(35, 1) - 0.05, FadeIn(t, scale=1.2), rt=0.4)
        self.at(W(35, 1, "informer") - 0.3, FadeIn(a, shift=0.3 * UP), rt=0.4)
        self.at(W(35, 1, "exposer") - 0.4, GrowArrow(fa), FadeIn(ra, shift=0.1 * DOWN), rt=0.4); self.son("triste", 0.5)
        self.at(S(35, 2) - 0.05, FadeIn(b, shift=0.3 * UP), VGroup(a, ra, fa).animate.set_opacity(0.5), rt=0.4)
        self.at(W(35, 2, "moins") - 0.4, GrowArrow(fb), FadeIn(rb, shift=0.1 * DOWN), rt=0.4); self.son("triste", 0.5)
        self.play(VGroup(a, ra, fa).animate.set_opacity(1), run_time=0.4)
        # 36 — plus de 101 000 personnes
        self.vider(S(36, 1) - 0.45, rt=0.4)
        zl = puce("À Zurich", 28).move_to([-5.3, 2.6, 0])
        vil = VGroup(maison(-2.2, 0, 1.6, 1.1, 1.0), maison(-0.3, 0, 1.9, 1.9, 1.2), maison(1.6, 0, 1.5, 0.9, 0.9), maison(3.2, 0, 1.3, 1.4, 1.0)).move_to([0, -0.6, 0])
        self.at(S(36, 1) - 0.05, FadeIn(zl, shift=0.2 * DOWN), FadeIn(vil, shift=0.3 * UP), rt=0.5)
        self.at(W(36, 1, "impressionnante") - 0.3, vil.animate(rate_func=there_and_back).scale(1.12), rt=0.8)
        foule = groupe(88, False, 0.5, 22, 12.4).move_to([0, -1.2, 0])
        for i, b_ in enumerate(foule):
            if i % 2: b_.become(bonhomme(0.5, CREME, femme=True).move_to(b_))
        n = ValueTracker(0)
        cpt = always_redraw(lambda: T(f"{int(n.get_value()):,}".replace(",", " "), 86).move_to([0, 1.55, 0]))
        sous = bandeau("Plus de 101 000 électeurs, fin 2001", 26).move_to([0, 0.55, 0])
        self.jusqua(S(36, 2) - 0.4); self.play(FadeOut(vil), run_time=0.3); self.add(cpt); self.son("grelot", 0.6)
        self.play(n.animate.set_value(101000), LaggedStart(*[FadeIn(b_, shift=0.08 * UP) for b_ in foule], lag_ratio=0.01), run_time=2.2, rate_func=rate_functions.ease_out_cubic)
        self.at(W(36, 2, "plus") - 0.2, FadeIn(sous, shift=0.1 * UP), rt=0.4); self.son("ding", 0.6)
        # 37 — environ 450 dossiers par an
        self.jusqua(S(37, 1) - 0.3)
        self.remove(cpt); c0 = T("101 000", 86).move_to([0, 1.55, 0]); self.add(c0)
        self.play(FadeOut(sous), c0.animate.scale(0.45).move_to([3.9, 2.5, 0]), foule.animate.scale(0.42).move_to([3.9, 1.3, 0]), run_time=0.5)
        m = ValueTracker(0); cp2 = always_redraw(lambda: T(f"≈ {int(m.get_value())}", 80).move_to([-3.6, 1.6, 0]))
        tasd = tas(30, 10, 0.55).move_to([-3.6, -0.9, 0]); dl = bandeau("dossiers par an", 26).move_to([-3.6, 0.65, 0])
        self.jusqua(W(37, 1, "environ") - 0.3); self.add(cp2)
        self.play(m.animate.set_value(450), LaggedStart(*[FadeIn(d, scale=0.4) for d in tasd], lag_ratio=0.03), FadeIn(dl), run_time=1.6); self.son("grelot", 0.5)
        self.remove(cp2); cp2 = T("≈ 450", 80).move_to([-3.6, 1.6, 0]); self.add(cp2)
        fl = Arrow([-0.6, -0.4, 0], [1.7, 0.7, 0], color=CREME, stroke_width=8, buff=0)
        qi = bas("Une masse d'informations personnelles à diffuser", 26)
        self.at(S(37, 2) - 0.05, GrowArrow(fl), rt=0.5); self.son("souffle"); self.at(W(37, 2, "quantité") - 0.3, FadeIn(qi, shift=0.15 * UP), rt=0.4)
        # 38 — publier moins ? alors on vote sans éléments
        self.vider(S(38, 1) - 0.45, rt=0.4)
        t = titre("Publier moins de détails ?")
        f = fiche(["Origine", "Revenu", "Formation", "Travail", "Langues"], taille=24).move_to([-3.6, 0.0, 0])
        self.at(S(38, 1) - 0.05, FadeIn(t, shift=0.2 * DOWN), FadeIn(f, shift=0.3 * UP), rt=0.5)
        f2 = fiche(["Origine", " ", " ", " ", " "], taille=24).move_to([-3.6, 0.0, 0])
        barres = VGroup(*[Rectangle(width=2.6, height=0.26, fill_color=ENCRE, fill_opacity=1, stroke_width=0).move_to(f.corps[k]).align_to(f.corps[k], LEFT) for k in range(1, 5)])
        self.at(W(38, 1, "moins") - 0.2, LaggedStart(*[GrowFromEdge(b, LEFT) for b in barres], lag_ratio=0.15), rt=0.7); self.son("souffle")
        vs = electeurs(4, 1.4, "perplexe").move_to([3.6, -0.9, 0])
        qs = VGroup(*[T("?", 40).next_to(b, UP, buff=0.1) for b in vs])
        self.at(S(38, 2) - 0.05, LaggedStart(*[FadeIn(b, shift=0.15 * UP) for b in vs], lag_ratio=0.1), rt=0.5)
        self.at(W(38, 2, "approuver") - 0.2, LaggedStart(*[FadeIn(q, scale=0.4) for q in qs], lag_ratio=0.12), rt=0.5); self.son("triste", 0.5)
        ap = bas("Sans les éléments d'une appréciation individuelle sérieuse", 24); self.at(W(38, 2, "sans") - 0.3, FadeIn(ap, shift=0.15 * UP), rt=0.4)
        # 39 — second constat : pas d'équilibre possible à Zurich
        self.vider(S(39, 1) - 0.45, rt=0.4)
        n2 = VGroup(Circle(0.55, fill_color=CREME, fill_opacity=1, stroke_width=0), T("2", 50, ROUGE)).move_to([-5.6, 2.3, 0]); pc = puce("Second constat", 30).next_to(n2, RIGHT, buff=0.3)
        bal = balance(1.35).move_to([0, -0.5, 0]); pg, pd = bal.plats
        lg = puce("Liberté de vote", 24).next_to(pg, DOWN, buff=0.3); ld = puce("Sphère privée", 24).next_to(pd, DOWN, buff=0.3)
        ug = urne(0.75).next_to(pg[2], UP, buff=0); cd = cadenas(0.9).next_to(pd[2], UP, buff=0.05)
        self.at(S(39, 1) - 0.05, FadeIn(n2, scale=0.5), FadeIn(pc, shift=0.2 * LEFT), FadeIn(bal, shift=0.3 * UP), rt=0.5); self.son("ding", 0.7)
        self.at(W(39, 1, "liberté") - 0.3, FadeIn(ug, scale=0.5), FadeIn(lg), rt=0.4); self.at(W(39, 1, "protection") - 0.3, FadeIn(cd, scale=0.5), FadeIn(ld), rt=0.4)
        az = bas("À Zurich : aucun équilibre satisfaisant", 28); self.at(W(39, 1, "aucun") - 0.3, FadeIn(az, scale=1.15), rt=0.4)
        self.fin()
