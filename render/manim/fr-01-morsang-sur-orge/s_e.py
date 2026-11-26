from base import *
from base import _bh, _vivant


class E1(Sec25):
    L0, L1 = 29, 34

    def construct(self):
        self.debut(3); self.chapitre(3, "La portée", 4)
        # 29.1 — l'arrêté du maire est jugé légal
        mr = maire(1.75, "neutre").move_to([-4.8, -0.85, 0])
        ar = decision("INTERDIT", False, "ARRÊTÉ DU MAIRE", 1.15).move_to([-1.6, 1.4, 0])
        self.at(S(29, 1), FadeIn(mr, shift=0.2 * UP), FadeIn(ar, scale=0.6), rt=0.4)
        lg = decision("LÉGAL", True, "CONSEIL D'ÉTAT", 0.9).move_to([1.6, 1.2, 0])
        self.at(W(29, 1, "légal") - 0.4, FadeIn(lg, scale=1.6), rt=0.35); self.son("thud", 0.7)
        visage(mr, 1.75, "content"); self.saut(mr, h=0.15)
        # 29.2 — la victoire obtenue devant le tribunal administratif est renversée
        st = station(["Tribunal", "administratif"], "25 février 1992", l=3.0, icone=palais(0.42)).move_to([4.7, -0.55, 0])
        vi = verdict("Victoire", True).move_to(st.f.get_bottom() + 0.95 * UP)
        og = organisateur(1.4, "content").move_to([0.2, -1.35, 0]); pa = participant(1.05, "content").move_to([1.5, -1.5, 0])
        self.at(S(29, 2), FadeIn(st, shift=0.2 * UP), FadeIn(vi), FadeIn(og), FadeIn(pa), rt=0.45)
        self.at(W(29, 2, "renversée") - 0.4, Rotate(VGroup(st, vi), PI, about_point=st.get_center()), rt=0.6); self.son("souffle", 0.7)
        humeur(VGroup(og, pa), "triste")
        # 30.1 — l'intérêt de l'arrêt dépasse largement ce litige
        self.vider(S(30, 1) - 0.4, rt=0.35)
        ca = carte_france(0.6); c0 = ca.get_center(); ca.move_to([-1.0, -0.4, 0]); dec = ca.get_center() - c0
        self.at(S(30, 1), FadeIn(ca, shift=0.2 * UP), rt=0.45)
        mairies = VGroup(*[Dot(projette(lon, lat, 0.6) + dec, radius=0.09, color=BLEU_FR) for lon, lat in
                           ((2.35, 48.66), (4.83, 45.76), (5.37, 43.30), (-1.55, 47.22), (1.44, 43.60), (7.75, 48.58), (3.06, 50.63), (-0.58, 44.84), (-1.68, 48.11), (3.88, 43.61), (0.69, 47.39), (5.04, 47.32))])
        self.at(W(30, 1, "dépasse") - 0.3, LaggedStart(*[FadeIn(m, scale=3) for m in mairies], lag_ratio=0.08), rt=0.9); self.son("joie", 0.5)
        lm = bandeau("Bien au-delà de Morsang-sur-Orge", 22).next_to(ca, RIGHT, buff=0.3)
        self.play(FadeIn(lm), run_time=0.3)
        # 30.2 — l'ordre public comprend aussi une dimension liée au respect de la personne
        self.vider(S(30, 2) - 0.35, rt=0.35)
        op = ordre_public(0.95).move_to([-2.8, 0.35, 0]); td = tuile_dignite(1.0).next_to(op, RIGHT, buff=0.5)
        pp = bandeau("Les pouvoirs de police", 22).next_to(op, DOWN, buff=0.25)
        self.at(S(30, 2), FadeIn(op, shift=0.2 * UP), rt=0.4)
        self.at(W(30, 2, "pouvoirs") - 0.4, FadeIn(pp), rt=0.35)
        plus = T("+", 60).move_to((op.get_right() + td.get_left()) / 2)
        self.at(W(30, 2, "dimension") - 0.4, FadeIn(plus), FadeIn(td, shift=0.3 * LEFT), rt=0.4); self.son("ding", 0.6)
        self.at(W(30, 2, "respect") - 0.2, Indicate(td, color=AMBRE, scale_factor=1.1), rt=0.5)
        # 31 — la jurisprudence tenait déjà compte de considérations immatérielles, avec des circonstances locales
        self.vider(S(31, 1) - 0.4, rt=0.35)
        f59 = VGroup(bobine(1.0), T("1959 · Films Lutetia", 22), T("Films à caractère immoral", 20, CREME, False)).arrange(DOWN, buff=0.18)
        c59 = VGroup(RoundedRectangle(corner_radius=0.2, width=4.6, height=3.6, fill_color=BLEU_3, fill_opacity=1, stroke_width=0), f59).move_to([-3.6, 0.1, 0]); f59.move_to(c59[0])
        self.at(S(31, 1), FadeIn(c59, shift=0.2 * RIGHT), rt=0.45); self.son("plop")
        im = bandeau("Des considérations immatérielles", 22).next_to(c59, DOWN, buff=0.2)
        self.at(W(31, 1, "immatérielles") - 0.5, FadeIn(im, shift=0.1 * UP), rt=0.35)
        lp_ = VGroup(quartier(0.75), loupe(0.6).shift(0.3 * RIGHT)).next_to(c59, UP, buff=0.15).shift(0.4 * RIGHT)
        ex = bandeau("+ circonstances locales exigées", 20).next_to(lp_, RIGHT, buff=0.2)
        self.at(W(31, 2, "circonstances") - 0.4, FadeIn(lp_, shift=0.2 * DOWN), FadeIn(ex), rt=0.4); self.son("thud", 0.5)
        c95 = VGroup(RoundedRectangle(corner_radius=0.2, width=4.6, height=3.6, fill_color=BLEU_3, fill_opacity=1, stroke_width=0), VGroup(tuile_dignite(0.9), T("1995 · Morsang-sur-Orge", 22), T("Un traitement propre", 20, CREME, False)).arrange(DOWN, buff=0.18)).move_to([3.6, 0.1, 0])
        fl = Arrow(c59.get_right(), c95.get_left(), color=CREME, buff=0.2, stroke_width=6)
        self.at(S(31, 3) - 0.05, GrowArrow(fl), FadeIn(c95, shift=0.2 * LEFT), rt=0.45); self.son("ding", 0.6)
        # 32.1 — attention : pas d'interdiction de n'importe quelle conduite jugée indigne
        self.vider(S(32, 1) - 0.4, rt=0.35)
        vA = vignette(-3.4, False, "N'importe quelle conduite", "jugée indigne")
        mA = maire(1.55, "decide").move_to([-4.7, -1.2, 0]); bA = bulle(["Indigne !"], 22).next_to(mA, RIGHT, buff=0.1).shift(0.6 * UP)
        dv = VGroup(habit(0.6, MENTHE), VGroup(Circle(0.12, fill_color=CIEL, fill_opacity=1, stroke_width=0), Line([0.12, 0, 0], [0.12, 0.45, 0], color=CIEL, stroke_width=5)), Star(5, outer_radius=0.25, inner_radius=0.11, fill_color=LILAS, fill_opacity=1, stroke_width=0)).arrange(RIGHT, buff=0.3).move_to([-1.9, -1.9, 0])
        self.at(S(32, 1), FadeIn(vA), FadeIn(mA, shift=0.2 * UP), rt=0.4)
        self.at(W(32, 1, "conduite") - 0.4, FadeIn(dv, shift=0.2 * LEFT), rt=0.35)
        self.at(W(32, 1, "indigne") - 0.35, FadeIn(bA, scale=0.5), rt=0.35); self.son("thud", 0.5)
        # 32.2 — une base juridique et une justification contrôlable
        vB = vignette(3.4, True, "Une base juridique,", "une justification contrôlable")
        bj = VGroup(code_fr("La loi", "", 0.65), T("Base juridique", 20)).arrange(DOWN, buff=0.15).move_to([2.0, -1.0, 0])
        jc = VGroup(juge(1.3, "decide"), loupe(0.7)).arrange(RIGHT, buff=0.1, aligned_edge=DOWN).move_to([4.7, -1.0, 0])
        ljc = T("Contrôle du juge", 20).next_to(jc, DOWN, buff=0.12)
        self.at(S(32, 2) - 0.05, FadeIn(vB), rt=0.35)
        self.at(W(32, 2, "base") - 0.35, FadeIn(bj, shift=0.2 * UP), rt=0.35); self.son("plop")
        self.at(W(32, 2, "contrôlable") - 0.5, FadeIn(jc, shift=0.2 * UP), FadeIn(ljc), rt=0.35); self.son("plop")
        # 33 — la dignité, composante de l'ordre public ; ici, l'interdiction est légalement justifiée
        self.vider(S(33, 1) - 0.4, rt=0.35)
        ad = page("Conseil d'État · 27 octobre 1995", ["La dignité de la personne humaine :", "une composante de l'ordre public", "Ici : interdiction légalement justifiée"], l=8.0, taille=24).move_to([0, 0.2, 0])
        self.at(S(33, 1), FadeIn(ad[0:4], shift=0.2 * UP), rt=0.4)
        self.at(W(33, 1, "dignité") - 0.3, FadeIn(VGroup(ad.corps[0], ad.corps[1]), shift=0.1 * RIGHT), rt=0.4); self.son("ding", 0.5)
        k1 = coche(True, 0.3).next_to(ad.corps[1], RIGHT, buff=0.2)
        self.play(FadeIn(k1, scale=2), run_time=0.25)
        self.at(W(33, 1, "interdiction") - 0.3, FadeIn(ad.corps[2], shift=0.1 * RIGHT), rt=0.4)
        k2 = coche(True, 0.3).next_to(ad.corps[2], RIGHT, buff=0.2)
        self.at(W(33, 1, "justifiée") - 0.3, FadeIn(k2, scale=2), rt=0.3); self.son("plop")
        self.fin()


class E2(Sec25):
    L0, L1 = 34, 39

    def construct(self):
        self.debut(3)
        # 34.1 — retour à la question d'ouverture
        pa = participant(1.6, "neutre").move_to([-1.0, -0.95, 0]); pp = parapluie(1.15, AMBRE, "?").move_to(pa.get_center() + 2.05 * UP)
        af = affiche(0.9).move_to([3.2, 1.2, 0]); tq = tampon("INTERDIT", 26).rotate(-0.1).move_to(af.get_center() + 0.1 * DOWN)
        rp = bandeau("La question du début", 22).move_to([-5.0, 2.4, 0])
        ml = mallette(1.0).move_to(main_de(pa, 1) + [0.45, -0.1, 0])
        self.at(S(34, 1), FadeIn(rp), FadeIn(pa, shift=0.2 * UP), FadeIn(ml, shift=0.2 * UP), FadeIn(af), FadeIn(tq), rt=0.45)
        self.at(W(34, 1, "question") - 0.3, FadeIn(pp, shift=0.3 * DOWN), rt=0.4); self.son("ding", 0.5)
        # 34.2 — protéger quelqu'un en lui retirant un travail qu'il revendique ?
        bu = bulle(["Mon travail"], 22).next_to(pa, LEFT, buff=0.2).shift(0.9 * UP)
        mr = maire(1.75, "decide").move_to([4.8, -0.85, 0])
        self.at(W(34, 2, "protéger") - 0.3, FadeIn(mr, shift=0.2 * LEFT), rt=0.35)
        self.at(W(34, 2, "retire") - 0.3, donner(ml, main_de(mr, -1) + [-0.3, -0.1, 0], -0.4, 0.6), rt=0.6); self.son("hop", 0.5)
        self.at(W(34, 2, "revendique") - 0.4, FadeIn(bu, scale=0.5), rt=0.35)
        humeur(pa, "triste")
        # 35 — deux lectures, sans trancher : une valeur commune / l'autonomie et la parole de la personne
        self.vider(S(35, 1) - 0.4, rt=0.35)
        vA = vignette(-3.4, None, "Une valeur commune,", "indépendante du consentement")
        gA = VGroup(*[_bh(1.15, c) for c in (MENTHE, CIEL, LILAS, CREME)]).arrange(RIGHT, buff=0.15, aligned_edge=DOWN)
        for b in gA: b.h = 1.15; _vivant(b, 0.03); visage(b, 1.15, "content")
        tdA = tuile_dignite(0.7)
        VGroup(tdA, gA).arrange(DOWN, buff=0.25).move_to(vA.f.get_center() + 0.4 * DOWN)
        self.at(S(35, 1), FadeIn(vA), rt=0.35)
        self.at(W(35, 1, "valeur") - 0.3, FadeIn(gA, shift=0.2 * UP), FadeIn(tdA, scale=0.6), rt=0.4); self.son("plop")
        vB = vignette(3.4, None, "L'autonomie et la parole", "de la personne concernée")
        pB = participant(1.35, "decide").move_to([2.5, -1.25, 0]); bB = bulle(["C'est mon choix"], 22).next_to(pB, RIGHT, buff=0.1).shift(0.7 * UP)
        self.at(S(35, 2) - 0.05, FadeIn(vB), rt=0.35)
        self.at(W(35, 2, "autonomie") - 0.3, FadeIn(pB, shift=0.2 * UP), rt=0.35)
        self.at(W(35, 2, "parole") - 0.3, FadeIn(bB, scale=0.5), rt=0.35); self.son("plop")
        # 36.1 — la vidéo ne tranche pas la controverse à la place du spectateur
        self.vider(S(36, 1) - 0.4, rt=0.35)
        bal = balance(1.2, VGroup(tuile_dignite(0.55)), VGroup(participant(0.8, "decide"), bulle(["Mon choix"], 16)).arrange(RIGHT, buff=0.05)).move_to([-2.2, -0.3, 0])
        ec = ecran(1.3).move_to([4.0, 0.3, 0]); lv = bandeau("À vous de juger", 22).next_to(ec, DOWN, buff=0.25)
        self.at(S(36, 1), FadeIn(bal, shift=0.2 * UP), rt=0.45)
        self.at(W(36, 1, "trancher") - 0.3, Wiggle(bal, scale_value=1.02, rotation_angle=0.02 * TAU), rt=0.6)
        self.at(W(36, 1, "spectateur") - 0.35, FadeIn(ec, shift=0.2 * LEFT), FadeIn(lv), rt=0.4); self.son("plop")
        # 36.2 — montrer le choix juridique du Conseil d'État en 1995
        self.vider(S(36, 2) - 0.35, rt=0.35)
        ce = conseil_etat(0.95).move_to([-3.2, 0.8, 0]); cal = date_fr("Année", "1995").scale(0.7).move_to([-6.3, 2.3, 0])
        ad = page("Le choix juridique", ["La dignité fait partie", "de l'ordre public"], l=5.0, taille=24).move_to([3.0, 0.3, 0])
        lp_ = loupe(1.0).move_to(ad.get_left() + 0.4 * LEFT)
        self.at(S(36, 2), FadeIn(ce, shift=0.2 * UP), FadeIn(cal), rt=0.4)
        self.at(W(36, 2, "choix") - 0.35, FadeIn(ad, shift=0.2 * LEFT), rt=0.4); self.son("ding", 0.5)
        self.play(FadeIn(lp_), run_time=0.25); self.play(lp_.animate.move_to(ad.corps.get_center()), run_time=0.6)
        # 37 — trois éléments
        self.vider(S(37, 1) - 0.4, rt=0.35)
        tt = puce("Ce choix repose sur 3 éléments", 30).move_to([0, 2.5, 0])
        self.at(S(37, 1), FadeIn(tt, scale=1.2), rt=0.4)
        def carte(ic, a, b, x):
            f = RoundedRectangle(corner_radius=0.2, width=4.3, height=3.9, fill_color=BLEU_3, fill_opacity=1, stroke_width=0).move_to([x, -0.5, 0])
            ic.move_to(f.get_center() + 0.6 * UP)
            t = VGroup(T(a, 22), T(b, 20, CREME, False)).arrange(DOWN, buff=0.1).move_to(f.get_center() + 1.2 * DOWN)
            return VGroup(f, ic, t)
        k1 = carte(maire(1.35, "decide"), "Une autorité de police", "compétente", -4.6)
        k2 = carte(VGroup(affiche(0.75), tuile_dignite(0.6)).arrange(RIGHT, buff=0.15), "Une atteinte à la dignité", "par l'objet de l'attraction", 0)
        k3 = carte(VGroup(contrat(0.75), piece_fr(0.6), coche(False, 0.3)).arrange(RIGHT, buff=0.15), "Ni consentement", "ni rémunération décisifs", 4.6)
        self.at(W(37, 1, "autorité") - 0.4, FadeIn(k1, shift=0.3 * UP), rt=0.4); self.son("plop")
        self.at(W(37, 1, "atteinte") - 0.4, FadeIn(k2, shift=0.3 * UP), rt=0.4); self.son("plop")
        self.at(W(37, 1, "absence") - 0.4, FadeIn(k3, shift=0.3 * UP), rt=0.4); self.son("plop")
        # 38 — un grand arrêt : ordre public, liberté individuelle, dignité, ensemble
        self.vider(S(38, 1) - 0.4, rt=0.35)
        lv = livres(1.6).move_to([-4.4, 0.6, 0]); ld = bandeau("Étudié en droit administratif", 20).next_to(lv, DOWN, buff=0.25)
        self.at(S(38, 1), FadeIn(lv, shift=0.2 * UP), rt=0.4)
        sig = VGroup(RoundedRectangle(corner_radius=0.06, width=3.1, height=0.5, fill_color=CREME, fill_opacity=1, stroke_color=ENCRE, stroke_width=2), T("Morsang-sur-Orge, 1995", 18, ENCRE)).move_to(lv.get_right() + 2.5 * RIGHT + 0.6 * UP)
        self.at(W(38, 1, "figure") - 0.3, FadeIn(sig, shift=0.2 * LEFT), rt=0.3)
        self.play(sig.animate.move_to(lv[0][1].get_center()).scale(0.7), run_time=0.5); self.son("hop", 0.5)
        self.at(W(38, 1, "administratif") - 0.4, FadeIn(ld, shift=0.1 * UP), rt=0.35)
        t1 = tuile("Ordre public", CREME, 2.6, 0.85, 22).move_to([2.6, 1.8, 0])
        t2 = tuile("Liberté individuelle", MENTHE, 3.0, 0.85, 22).move_to([0.6, -1.2, 0])
        t3 = tuile("Dignité humaine", AMBRE, 2.8, 0.85, 22).move_to([4.6, -1.2, 0])
        liens = VGroup(Line(t1.get_bottom(), t2.get_top(), color=CREME, stroke_width=4), Line(t1.get_bottom(), t3.get_top(), color=CREME, stroke_width=4), Line(t2.get_right(), t3.get_left(), color=CREME, stroke_width=4))
        self.at(W(38, 1, "ordre") - 0.3, FadeIn(t1, scale=0.6), rt=0.3)
        self.at(W(38, 1, "liberté") - 0.3, FadeIn(t2, scale=0.6), rt=0.3)
        self.at(W(38, 1, "dignité") - 0.3, FadeIn(t3, scale=0.6), rt=0.3); self.son("ding", 0.5)
        self.play(Create(liens), run_time=0.5)
        self.fin()
