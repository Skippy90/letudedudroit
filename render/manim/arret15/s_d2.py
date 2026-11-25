from base import *


class D2(Sec15):
    L0, L1 = 26, 33

    def construct(self):
        self.debut(3)
        # 26 — premier indice : les résultats
        t = titre("Indice 1 : les résultats"); lp = loupe(1.1).move_to([-6.3, 2.9, 0])
        self.at(S(26, 1) - 0.2, FadeIn(t, shift=0.2 * DOWN), FadeIn(lp, scale=0.5), rt=0.5)
        ds = tas(16, 8, 1.1).move_to([0, 0.5, 0])
        self.at(S(26, 2) - 0.1, LaggedStart(*[FadeIn(d, shift=0.15 * UP) for d in ds], lag_ratio=0.04), rt=1.0)
        xs = VGroup(*[coche(False, 0.2).move_to(d.get_corner(UR)) for d in ds])
        self.at(W(26, 2, "rejet") - 0.5, LaggedStart(*[FadeIn(x, scale=2) for x in xs], lag_ratio=0.04), rt=0.9)
        s16 = puce("16 demandes sur 16 : rejetées", 28).move_to([0, -1.6, 0]); self.play(FadeIn(s16, scale=1.2), run_time=0.4)
        ph = bas("Pourtant : un groupe très varié", 26, -2.75); self.at(W(26, 3, "pourtant"), FadeIn(ph, shift=0.15 * UP), rt=0.5)
        # 27 — un groupe varié
        self.vider(S(27, 1) - 0.5, garder=[t, lp], rt=0.4)
        def case(titre_, ic, x, y):
            f = RoundedRectangle(corner_radius=0.2, width=6.2, height=2.5, fill_color=ROUGE_3, fill_opacity=1, stroke_width=0).move_to([x, y, 0])
            tt = bandeau(titre_, 22).move_to(f.get_top() + 0.4 * DOWN); ic.move_to(f.get_center() + 0.35 * DOWN)
            return VGroup(f, tt, ic)
        seul = VGroup(bonhomme(1.2), VGroup(bonhomme(1.2), bonhomme(1.2, femme=True), bonhomme(0.75)).arrange(RIGHT, buff=0.12, aligned_edge=DOWN)).arrange(RIGHT, buff=1.2, aligned_edge=DOWN)
        k1 = case("Seuls ou en famille", seul, -3.3, 1.0)
        met = VGroup(*[VGroup(bonhomme(1.1, femme=(k == 1)), Square(0.32, fill_color=ENCRE, fill_opacity=1, stroke_width=0).rotate(k * 0.5).shift(0.42 * RIGHT + 0.3 * UP)) for k in range(3)]).arrange(RIGHT, buff=0.7)
        k2 = case("Professions et revenus différents", met, 3.3, 1.0)
        ne = VGroup(carte(2.6, (0, 0)), bonhomme(0.8).shift(0.2 * DOWN)); k3 = case("Plusieurs sont nés en Suisse", ne, -3.3, -1.75)
        fr = frise(1968, 1994, -2.1, 1.7, 0, [(1971, "1971"), (1991, "1991")]); k4 = case("Les autres : arrivés entre 1971 et 1991", fr, 3.3, -1.75)
        self.at(S(27, 1), FadeIn(k1, shift=0.3 * UP), rt=0.5); self.at(S(27, 2), FadeIn(k2, shift=0.3 * UP), rt=0.5)
        self.at(S(27, 3) - 0.1, FadeIn(k3, shift=0.3 * UP), rt=0.5); self.at(S(27, 4) - 0.1, FadeIn(k4, shift=0.3 * UP), rt=0.5)
        # 28 — la comparaison
        self.vider(S(28, 1) - 0.5, garder=[lp], rt=0.4)
        t = titre("Une comparaison révélatrice"); self.at(S(28, 1), FadeIn(t, shift=0.2 * DOWN), rt=0.5)
        def fiche(l1, l2, x, eq):
            f = RoundedRectangle(corner_radius=0.2, width=4.5, height=4.2, fill_color=ROUGE_3, fill_opacity=1, stroke_width=0).move_to([x, -0.65, 0])
            b = acteur(1.6, eq, False, "neutre").move_to(f.get_center() + 0.8 * UP)
            tx = VGroup(T(l1, 19), T(l2, 20, CREME, False)).arrange(DOWN, buff=0.12).move_to(f.get_center() + 0.55 * DOWN)
            g = VGroup(f, b, tx); g.fond = f; g.b = b
            return g
        f1 = fiche("Ressortissant italien", "né en Suisse en 1980", -4.85, "it"); f2 = fiche("Originaire d'ex-Yougoslavie", "né à Lucerne en 1979", 0, "yu"); f3 = fiche("Originaire d'ex-Yougoslavie", "né à Lucerne en 1981", 4.85, "yu")
        self.at(S(28, 2), FadeIn(f1, shift=0.3 * UP), rt=0.5)
        o1 = VGroup(coche(True, 0.3), T("Naturalisé", 26)).arrange(RIGHT, buff=0.2).move_to(f1.fond.get_bottom() + 0.55 * UP)
        self.at(W(28, 2, "naturalisé") - 0.3, FadeIn(o1, scale=1.3), rt=0.4); visage(f1.b, 1.6, "content"); self.son("ding"); self.saut(f1.b, h=0.2)
        self.at(W(28, 3, "deux") - 0.2, FadeIn(f2, shift=0.3 * UP), FadeIn(f3, shift=0.3 * UP), rt=0.6)
        o2 = tampon("REFUSÉ", 26).move_to(f2.fond.get_bottom() + 0.55 * UP); o3 = tampon("REFUSÉ", 26).move_to(f3.fond.get_bottom() + 0.55 * UP)
        self.at(W(28, 3, "essuyé") - 0.2, FadeIn(o2, scale=2), FadeIn(o3, scale=2), rt=0.35); visage(f2.b, 1.6, "triste"); visage(f3.b, 1.6, "triste"); self.son("triste", dt=0.2)
        self.pop("Même âge. Même pays de naissance.", [0, 2.15, 0], 2.4, 22, 0.03)
        # 29 — aucune autre explication
        self.vider(S(29, 1) - 0.5, garder=[lp], rt=0.4)
        t = titre("Qu'est-ce qui explique l'écart ?"); self.at(S(29, 1) - 0.1, FadeIn(t, shift=0.2 * DOWN), rt=0.4)
        noms = ["Durée du séjour", "Profession", "Revenus", "Situation familiale"]; mots = ["durée", "profession", "revenus", "situation"]
        ps = VGroup(*[bandeau(n, 28) for n in noms]).arrange(DOWN, buff=0.3).move_to([-3.4, -0.3, 0])
        for k, m in enumerate(mots):
            self.at(W(29, 1, m) - 0.25, FadeIn(ps[k], shift=0.2 * RIGHT), rt=0.3)
        bs = VGroup(*[barre(p, CREME, 6) for p in ps])
        self.at(W(29, 1, "permettent") - 0.2, LaggedStart(*[Create(b) for b in bs], lag_ratio=0.15), ps.animate.set_opacity(0.55), rt=0.9)
        fl = Arrow([-0.6, -0.3, 0], [1.0, -0.3, 0], color=CREME, stroke_width=7, buff=0)
        orig = VGroup(RoundedRectangle(corner_radius=0.2, width=4.6, height=2.4, fill_color=CREME, fill_opacity=1, stroke_width=0), VGroup(T("Reste", 26, ENCRE, False), T("l'origine", 50, ROUGE)).arrange(DOWN, buff=0.15)).move_to([3.7, -0.3, 0])
        self.at(S(29, 2), GrowArrow(fl), rt=0.4); self.at(W(29, 2, "origine") - 0.6, FadeIn(orig, scale=1.3), rt=0.5)
        self.pop("Tiens, tiens…", [3.7, 1.75, 0], 2.2)
        # 30 — second indice : le climat du vote
        self.vider(S(30, 1) - 0.5, garder=[lp], rt=0.4)
        t = titre("Indice 2 : le climat du vote"); self.at(S(30, 1) - 0.1, FadeIn(t, shift=0.2 * DOWN), rt=0.5); self.play(Wiggle(lp), run_time=1.0)
        cal = bandeau("Les semaines avant le scrutin", 22).move_to([0, 2.2, 0]); self.at(S(30, 2), FadeIn(cal), rt=0.4)
        # des gens distribuent des tracts (contenu jamais montré), d'autres lisent le courrier des lecteurs
        SOLT = -1.75
        table = VGroup(Rectangle(width=1.3, height=0.12, fill_color=ENCRE, fill_opacity=1, stroke_width=0).move_to([-5.2, SOLT + 0.8, 0]), Rectangle(width=0.1, height=0.8, fill_color=ENCRE, fill_opacity=1, stroke_width=0).move_to([-5.2, SOLT + 0.4, 0]))
        pile = VGroup(*[dossier(0.55).move_to([-5.2, SOLT + 1.0 + 0.06 * k, 0]) for k in range(3)])
        dist = VGroup(au_sol(acteur(1.5, None, False, "neutre"), -6.6, SOLT), au_sol(acteur(1.5, None, True, "neutre"), -6.0, SOLT))
        pas_ = VGroup(*[au_sol(acteur(1.4, None, k % 2 == 1, "neutre"), 1.6 + 1.0 * k, SOLT) for k in range(4)])
        tl = puce("Tracts", 24).move_to([-3.4, SOLT - 0.5, 0])
        self.at(W(30, 2, "tracts") - 0.9, FadeIn(table), FadeIn(pile), FadeIn(dist, shift=0.3 * RIGHT), FadeIn(tl), rt=0.5)
        self.play(*self.marche(pas_, [p.get_center() + np.array([-5.6, 0, 0]) for p in pas_], 4), run_time=1.1)
        feuilles = VGroup(*[dossier(0.5).move_to(pile.get_center()) for _ in pas_])
        for k, p in enumerate(pas_):
            self.son("flic", 1.0, 0.0); self.play(feuilles[k].animate(path_arc=-1.2).move_to(p.get_center() + np.array([0.22, 0.05, 0])), run_time=0.28)
            visage(p, 1.4, "perplexe")
        journal = VGroup(RoundedRectangle(corner_radius=0.08, width=2.5, height=3.1, fill_color=CREME, fill_opacity=1, stroke_width=0), Rectangle(width=2.5, height=0.5, fill_color=ENCRE, fill_opacity=1, stroke_width=0).shift(1.3 * UP), T("Journal", 20).shift(1.3 * UP),
                         *[Line([-1.0, 0.75 - 0.28 * k, 0], [1.0 if k % 3 else 0.5, 0.75 - 0.28 * k, 0], color=ENCRE, stroke_width=3, stroke_opacity=0.55) for k in range(8)]).move_to([3.3, SOLT + 1.55, 0])
        lect = au_sol(acteur(1.4, None, True, "neutre"), 5.4, SOLT); ll = puce("Lettres de lecteurs", 24).move_to([3.9, SOLT - 0.5, 0])
        self.at(W(30, 2, "lettres") - 0.3, FadeIn(journal, shift=0.3 * DOWN), FadeIn(lect, shift=0.3 * LEFT), FadeIn(ll), rt=0.5)
        ck = cadre_autour(VGroup(*journal[3:7]), 0.1).set_color(ROUGE); self.play(Create(ck), run_time=0.5); visage(lect, 1.4, "perplexe")
        clim = VGroup(table, pile, dist, pas_, feuilles, tl, journal, ck, lect, ll)
        ho = bas("Des propos ouvertement hostiles", 26, -2.95); self.at(W(30, 2, "propos") - 0.2, FadeIn(ho, shift=0.15 * UP), rt=0.4)
        # 31 — des préjugés, un rôle décisif
        self.at(S(31, 1) - 0.4, FadeOut(ho), FadeOut(cal), clim.animate.scale(0.42).move_to([-4.3, -0.9, 0]), rt=0.5)
        ce = carton(["Certes : pas l'opinion", "de chaque électeur,", "ni même de la majorité"], 5.4, 2.2, 22).move_to([2.6, 1.2, 0])
        self.at(S(31, 1) + 0.3, FadeIn(ce, shift=0.3 * UP), rt=0.5)
        pj = puce("Mais : un climat de préjugés", 28).move_to([2.6, -0.75, 0]); self.at(S(31, 2), FadeIn(pj, scale=1.2), ce.animate.set_opacity(0.5), rt=0.5)
        u = urne(1.0).move_to([5.3, -2.3, 0]); fl = Arrow([1.0, -2.35, 0], [4.3, -2.35, 0], color=CREME, stroke_width=7, buff=0); rd = T("Rôle décisif", 24).next_to(fl, UP, buff=0.12)
        self.at(W(31, 3, "préjugés") - 0.2, FadeIn(u), rt=0.4); self.at(W(31, 3, "rôle") - 0.3, GrowArrow(fl), FadeIn(rd), rt=0.5)
        # 32 — discrimination établie
        self.vider(S(32, 1) - 0.5, rt=0.4)
        t = titre("La conclusion des juges"); self.at(S(32, 1) - 0.1, FadeIn(t, shift=0.2 * DOWN), rt=0.4)
        a = VGroup(coche(True, 0.36), T("Désavantagés en raison de leur origine", 28)).arrange(RIGHT, buff=0.3).move_to([0, 1.7, 0])
        b = VGroup(coche(True, 0.36), T("Aucune justification objective", 28)).arrange(RIGHT, buff=0.3).move_to([0, 0.7, 0]).align_to(a, LEFT)
        self.at(W(32, 1, "désavantagés") - 0.3, FadeIn(a, shift=0.3 * LEFT), rt=0.5); self.at(S(32, 2), FadeIn(b, shift=0.3 * LEFT), rt=0.5)
        p8 = page("Art. 8 al. 2 Cst.", ["Nul ne doit subir de discrimination", "du fait notamment de son origine […]"], taille=24).move_to([-1.2, -1.5, 0])
        self.at(S(32, 3), FadeIn(p8, shift=0.3 * UP), rt=0.5)
        vio = tampon("VIOLÉ", 44).move_to(p8.get_right() + 1.3 * RIGHT + 0.1 * UP)
        self.at(W(32, 3, "discrimination") - 0.2, FadeIn(vio, scale=2.4), rt=0.3)
        self.fin()
