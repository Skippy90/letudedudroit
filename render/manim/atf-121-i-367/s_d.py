from base import *
from base import _bh


def carte_lib(icone, l1, l2, l=3.3, h=2.5):
    f = RoundedRectangle(corner_radius=0.2, width=l, height=h, fill_color=ROUGE_3, fill_opacity=1, stroke_width=0)
    icone.move_to(f.get_center() + 0.4 * UP)
    tx = VGroup(T(l1, 20), T(l2, 20)).arrange(DOWN, buff=0.06).move_to(f.get_bottom() + 0.5 * UP)
    return VGroup(f, icone, tx)


# Les trois icônes sont en couleur, comme les autres (demande du 25 nov., 3:40 : seule la réunion l'était)
def ic_personnelle(e=1.0):
    b = _bh(1.0 * e, CIEL); b.add(Line(b[1].get_center() + [-0.16 * e, -0.22 * e, 0], b[1].get_center() + [-0.42 * e, 0.12 * e, 0], color=CIEL, stroke_width=7 * e), Line(b[1].get_center() + [0.16 * e, -0.22 * e, 0], b[1].get_center() + [0.42 * e, 0.12 * e, 0], color=CIEL, stroke_width=7 * e))
    visage(b, 1.0 * e, "content"); return b


def ic_langue(e=1.0):
    b1 = bulle(["Bonjour"], int(18 * e)); b2 = bulle(["Grüezi"], int(18 * e))
    for b_, c_ in ((b1, MENTHE), (b2, AMBRE)): b_[0].set_fill(c_, 1); b_[1].set_fill(c_, 1)
    return VGroup(b1.scale(0.9).shift(0.25 * e * UP + 0.2 * e * LEFT), b2.scale(0.9).shift(0.3 * e * DOWN + 0.25 * e * RIGHT))


def ic_reunion(e=1.0):
    g = VGroup(*[_bh(0.75 * e, c, femme=(k == 1)) for k, c in enumerate((MENTHE, LILAS, AMBRE))]).arrange(RIGHT, buff=0.08 * e, aligned_edge=DOWN)
    for b in g: visage(b, 0.75 * e, "content")
    return g


class D1(Sec367):
    L0, L1 = 18, 24

    def construct(self):
        self.debut(1); self.chapitre(2, "Le raisonnement", 3)
        # 18 — pas évident ; des droits non écrits déjà reconnus
        jg = juge(1.5, "perplexe").move_to([0, -0.85, 0]); bp = bulle_pensee("?", 34).next_to(jg, UP, buff=0.15).shift(0.4 * RIGHT)
        self.at(S(18, 1) - 0.05, FadeIn(jg, shift=0.2 * UP), FadeIn(bp, scale=0.5), rt=0.45)
        self.jusqua(S(18, 2) - 0.2)
        hd = puce("Déjà reconnus, sans être écrits", 24).move_to([0, 2.8, 0])
        self.play(jg.animate.move_to([-5.7, -0.9, 0]), FadeOut(bp), FadeIn(hd, shift=0.15 * DOWN), run_time=0.5)
        visage(jg, 1.5, "decide")
        cs = [carte_lib(ic_personnelle(0.95), "Liberté", "personnelle"), carte_lib(ic_langue(1.0), "Liberté", "de la langue"), carte_lib(ic_reunion(1.0), "Liberté", "de réunion")]
        for k, c in enumerate(cs): c.move_to([-2.0 + 3.6 * k, 0.4, 0])
        for k, mot in enumerate(("personnelle", "langue", "réunion")):
            tg = cs[k].get_center(); cs[k].scale(0.2).move_to(main_de(jg, 1))
            self.at(W(18, 2, mot) - 0.6, FadeIn(cs[k]), rt=0.15)
            self.play(cs[k].animate(path_arc=-0.5).scale(5).move_to(tg), run_time=0.45); self.son("plop")
        # 19 — les critères : indispensable aux autres libertés ou à l'État démocratique ; consensus
        self.vider(S(19, 1) - 0.4, rt=0.4)
        js = juges(3, 1.15, "neutre").move_to([-4.7, -1.05, 0]); lp = loupe(0.8).move_to([-3.2, 1.0, 0])
        self.at(S(19, 1), FadeIn(js, shift=0.2 * UP), FadeIn(lp, scale=0.5), rt=0.45)
        l1 = ligne_coche(None, "Indispensable aux autres libertés ?", None, 24).move_to([1.4, 1.6, 0]).align_to([-1.6, 0, 0], LEFT)
        l2 = ligne_coche(None, "Ou à l'État démocratique", "fondé sur le droit ?", 24).next_to(l1, DOWN, buff=0.35, aligned_edge=LEFT)
        l3 = ligne_coche(None, "Un consensus solide ?", None, 24).next_to(l2, DOWN, buff=0.35, aligned_edge=LEFT)
        self.at(W(19, 1, "indispensable") - 0.3, FadeIn(l1, shift=0.2 * LEFT), lp.animate.move_to(l1.get_left() + 0.5 * LEFT), rt=0.4); self.son("plop")
        self.at(W(19, 1, "fonctionnement") - 0.3, FadeIn(l2, shift=0.2 * LEFT), lp.animate.move_to(l2.get_left() + 0.5 * LEFT), rt=0.4); self.son("plop")
        self.at(W(19, 2, "consensus") - 0.3, FadeIn(l3, shift=0.2 * LEFT), lp.animate.move_to(l3.get_left() + 0.5 * LEFT), *[b.animate(rate_func=there_and_back).shift(0.1 * UP) for b in js], rt=0.45); self.son("plop")
        # 20 — avant de débattre, de voter, de vivre : se nourrir, se vêtir, un abri
        self.vider(S(20, 1) - 0.4, rt=0.4)
        hauts = VGroup(bulle(["Débattre"], 20), urne(0.75), ic_personnelle(1.1)).arrange(RIGHT, buff=1.4, aligned_edge=DOWN).move_to([0, 1.85, 0])
        lh = VGroup(T("", 18), T("Voter", 20), T("Mener sa vie", 20))
        lh[1].next_to(hauts[1], DOWN, buff=0.12); lh[2].next_to(hauts[2], DOWN, buff=0.12)
        for k, mot in enumerate(("débattre", "voter", "mener")):
            self.at(W(20, 1, mot) - 0.3, FadeIn(hauts[k], shift=0.2 * DOWN), FadeIn(lh[k]), rt=0.35); self.son("plop", 0.6)
        socle = RoundedRectangle(corner_radius=0.15, width=9.4, height=1.75, fill_color=ROUGE_3, fill_opacity=1, stroke_width=0).move_to([0, -1.2, 0])
        bs = besoins(1.0).move_to(socle.get_center() + 0.12 * UP)
        # pas de personnage isolé sur le socle (demande du 25 nov., 4:07) : la personne est celle de « Mener sa vie »
        self.at(W(20, 1, "encore") - 0.2, FadeIn(socle, shift=0.2 * UP), rt=0.35)
        for k, mot in enumerate(("nourrir", "vêtir", "abri")):
            self.at(W(20, 1, mot) - 0.35, FadeIn(bs[k], scale=0.5), rt=0.35); self.son("ding", 0.45)
        lb = puce("Les besoins élémentaires", 24).move_to(socle.get_bottom() + 0.05 * DOWN)
        self.at(W(20, 2, "besoins") - 0.3, FadeIn(lb, shift=0.1 * UP), rt=0.35)
        fl = VGroup(*[Arrow(socle.get_top() + x * RIGHT, socle.get_top() + x * RIGHT + 0.9 * UP, color=CREME, buff=0.05, stroke_width=6) for x in (-2.7, 0, 2.7)])
        self.at(W(20, 2, "conditionnent") - 0.3, LaggedStart(*[GrowArrow(f) for f in fl], lag_ratio=0.15), VGroup(hauts, lh).animate.shift(0.12 * UP), rt=0.5)
        self.at(W(20, 2, "existence") - 0.2, Indicate(socle, color=ROUGE_4, scale_factor=1.03), hauts[2].animate(rate_func=there_and_back).shift(0.25 * UP), rt=0.5)
        # 21 — sans ce socle, les libertés perdent leur portée ; la dignité humaine
        self.vider(S(21, 1) - 0.4, rt=0.4)
        cs = VGroup(carte_lib(ic_personnelle(0.8), "Liberté", "personnelle", 2.8, 2.1), carte_lib(ic_langue(0.85), "Liberté", "de la langue", 2.8, 2.1), carte_lib(ic_reunion(0.85), "Liberté", "de réunion", 2.8, 2.1)).arrange(RIGHT, buff=0.35).move_to([0, 1.55, 0])
        lc = puce("Les libertés fondamentales", 22).next_to(cs, UP, buff=0.15)
        socle = RoundedRectangle(corner_radius=0.15, width=9.2, height=0.45, fill_color=CREME, fill_opacity=1, stroke_width=0).next_to(cs, DOWN, buff=0.08)
        self.at(S(21, 1) - 0.05, FadeIn(cs, shift=0.2 * DOWN), FadeIn(lc), FadeIn(socle), rt=0.5)
        pe = frere(1.35, 2, "triste").move_to([0, -1.6, 0])
        self.at(W(21, 1, "abandonnée") - 0.4, FadeOut(socle, shift=0.5 * DOWN), *[c.animate.rotate((-1) ** k * 0.12).shift(0.25 * DOWN).set_opacity(0.45) for k, c in enumerate(cs)], FadeIn(pe, shift=0.2 * UP), rt=0.6); self.son("souffle")
        ld = bandeau("Une détresse matérielle", 20).next_to(pe, RIGHT, buff=0.3)
        self.at(W(21, 1, "détresse") - 0.3, FadeIn(ld, shift=0.1 * LEFT), rt=0.35)
        di = VGroup(coeur(1.6), T("Dignité humaine", 22)).arrange(RIGHT, buff=0.2).next_to(pe, LEFT, buff=0.4)
        self.at(W(21, 1, "dignité") - 0.3, FadeIn(di, scale=0.5), rt=0.4); self.son("ding", 0.6)
        # 22 — législations cantonales ; constitutions cantonales ; doctrine
        self.vider(S(22, 1) - 0.4, rt=0.4)
        ca = carte(5.2).move_to([-3.2, 0.5, 0]); js = juges(2, 1.1, "neutre").move_to([3.2, -1.05, 0]); lp = loupe(0.6).next_to(js, LEFT, buff=0.1).shift(0.6 * UP)
        self.at(S(22, 1), FadeIn(ca), FadeIn(js, shift=0.2 * UP), FadeIn(lp, scale=0.5), rt=0.45)
        lc = puce("Les législations cantonales", 22).next_to(ca, DOWN, buff=0.25)
        self.at(W(22, 1, "législations") - 0.4, LaggedStart(*[c.animate.set_fill(CREME, 0.45) for c in ca.cantons.values()], lag_ratio=0.04), FadeIn(lc), lp.animate(path_arc=0.5).move_to(ca.get_center() + 0.3 * UP).scale(1.6), rt=1.0); self.son("ding", 0.5)
        self.play(lp.animate.shift(1.4 * RIGHT), run_time=0.6, rate_func=there_and_back)
        sl = VGroup(*[texte_cantonal("Constitution", "cantonale", None, "Canton").scale(0.38) for _ in range(3)]).arrange(RIGHT, buff=0.15).move_to([2.6, 1.9, 0])
        self.at(W(22, 2, "constitutions") - 0.3, LaggedStart(*[FadeIn(x, shift=0.2 * DOWN) for x in sl], lag_ratio=0.15), rt=0.6); self.son("plop")
        dc = VGroup(*[livre("Doctrine", "", None).scale(0.32) for _ in range(3)]).arrange(RIGHT, buff=-0.35).move_to([5.6, 0.25, 0])
        ldc = T("La doctrine", 20).next_to(dc, UP, buff=0.12)
        self.at(W(22, 2, "doctrine") - 0.3, FadeIn(dc, shift=0.2 * LEFT), FadeIn(ldc), rt=0.4); self.son("plop")
        humeur(js, "content")
        # 23 — le droit est reconnu ; que peut-on exiger ?
        self.vider(S(23, 1) - 0.4, rt=0.4)
        js = juges(3, 1.2, "decide").move_to([-4.7, -1.05, 0]); ltf = bandeau("Tribunal fédéral", 20).next_to(js, DOWN, buff=0.2)
        self.at(S(23, 1), FadeIn(js, shift=0.2 * UP), FadeIn(ltf), rt=0.4)
        cd = carte_droit(besoins(0.42), "Conditions minimales", "d'existence", l=6.0, h=2.2).move_to([1.6, 1.4, 0])
        ar = arret_tf("DROIT RECONNU", True, 1.0).move_to([1.6, -0.9, 0])
        ba23 = bras_tendu(js[2], 1); self.at(W(23, 1, "reconnaît") - 0.5, Create(ba23), rt=0.2)
        self.play(FadeIn(ar, scale=1.6), js[2].animate(rate_func=there_and_back).shift(0.1 * DOWN), run_time=0.35); self.son("thud", 0.6)
        self.play(FadeOut(ba23), run_time=0.2)
        lnc = bandeau("Droit constitutionnel non écrit", 20).next_to(ar, DOWN, buff=0.2)
        self.at(W(23, 1, "écrit") - 0.3, FadeIn(lnc, shift=0.1 * UP), rt=0.35)
        self.at(W(23, 1, "conditions") - 0.3, FadeIn(cd, shift=0.3 * DOWN), rt=0.45); self.son("joie", 0.6)
        humeur(js, "content"); self.saut(*js)
        self.jusqua(S(23, 2) - 0.25)
        self.play(*[FadeOut(x) for x in (ar, lnc)], cd.animate.scale(0.75).move_to([-3.6, 2.2, 0]), run_time=0.45)
        st = VGroup(ic_gouvernement(1.0), puce("L'État", 22)).arrange(DOWN, buff=0.2).move_to([4.9, 0.4, 0])
        q = ligne_coche(None, "Exiger quoi, exactement ?", None, 26).move_to([-0.3, -0.85, 0])
        self.at(W(23, 2, "question") - 0.3, FadeIn(st, shift=0.2 * LEFT), rt=0.4)
        self.at(W(23, 2, "exiger") - 0.35, FadeIn(q, shift=0.15 * UP), rt=0.4); self.son("ding", 0.6)
        humeur(js, "perplexe")
        self.fin()


class D2(Sec367):
    L0, L1 = 24, 30

    def construct(self):
        self.debut(2)
        # 24 — ni revenu garanti, ni toutes les prestations ; seulement le minimum indispensable
        c1 = VGroup(VGroup(*[piece(0.6).shift(0.12 * k * UP) for k in range(4)]), T("Un revenu garanti", 22)).arrange(DOWN, buff=0.3).move_to([-3.8, 1.0, 0])
        c2 = VGroup(VGroup(colis(0.7), colis(0.6).shift(0.75 * RIGHT + 0.05 * DOWN), colis(0.55).shift(0.35 * RIGHT + 0.55 * UP)), T("Toutes les prestations", 22), T("de l'aide sociale", 22)).arrange(DOWN, buff=0.15).move_to([3.6, 1.0, 0])
        self.at(W(24, 1, "revenu") - 0.4, FadeIn(c1, shift=0.2 * UP), rt=0.4)
        x1 = coche(False, 0.45).move_to(c1[0].get_center())
        self.at(W(24, 1, "garanti") - 0.1, FadeIn(x1, scale=2), rt=0.3); self.son("thud", 0.5)
        self.at(W(24, 1, "prestations") - 0.4, FadeIn(c2, shift=0.2 * UP), rt=0.4)
        x2 = coche(False, 0.45).move_to(c2[0].get_center())
        self.at(W(24, 1, "sociale") - 0.2, FadeIn(x2, scale=2), rt=0.3); self.son("thud", 0.5)
        self.jusqua(S(24, 2) - 0.25)
        self.play(c1.animate.scale(0.6).move_to([-5.4, 2.2, 0]).set_opacity(0.4), x1.animate.scale(0.6).move_to([-5.4, 2.5, 0]).set_opacity(0.4),
                  c2.animate.scale(0.6).move_to([5.3, 2.2, 0]).set_opacity(0.4), x2.animate.scale(0.6).move_to([5.3, 2.5, 0]).set_opacity(0.4), run_time=0.5)
        cst = constit(None, 0.7).move_to([-3.3, -0.6, 0])
        bc = parapluie(1.45).move_to([1.4, 0.0, 0]); tl = bc[0].get_bottom()[1]
        bs = VGroup(VGroup(assiette(0.42), habit(0.34)).arrange(RIGHT, buff=0.15, aligned_edge=DOWN), abri(0.42)); bs[0].next_to([1.4 - 0.12, tl - 0.75, 0], LEFT, buff=0); bs[1].next_to([1.4 + 0.12, tl - 0.75, 0], RIGHT, buff=0)
        au_sol(bs[0], bs[0].get_x(), tl - 0.95); au_sol(bs[1], bs[1].get_x(), tl - 0.95)
        lm = puce("Le minimum indispensable", 24).next_to(bc, UP, buff=0.2)
        self.at(W(24, 2, "Constitution") - 0.3, FadeIn(cst, shift=0.2 * UP), rt=0.4)
        self.at(W(24, 2, "protège") - 0.2, FadeIn(bc, scale=0.5), FadeIn(bs, scale=0.5), rt=0.45); self.son("ding", 0.6)
        self.at(W(24, 2, "minimum") - 0.3, FadeIn(lm, shift=0.1 * DOWN), rt=0.35)
        vd = bandeau("Une vie digne", 22).next_to(bc, DOWN, buff=0.2)
        self.at(W(24, 2, "digne") - 0.4, FadeIn(vd, shift=0.1 * UP), rt=0.35)
        # 25 — manger, se vêtir, un abri ; argent ou nature
        self.vider(S(25, 1) - 0.4, rt=0.4)
        pe = frere(1.45, 1, "neutre").move_to([-5.2, -0.8, 0]); lpe = bandeau("Une personne en détresse", 18).next_to(pe, DOWN, buff=0.15)
        self.at(S(25, 1), FadeIn(pe, shift=0.2 * UP), FadeIn(lpe), rt=0.4)
        bs = VGroup(assiette(1.2), habit(1.0), abri(1.25)).arrange(RIGHT, buff=1.1, aligned_edge=DOWN).move_to([1.2, 1.0, 0])
        lb = VGroup(T("Manger", 22), T("Se vêtir", 22), T("Un abri", 22))
        ag25 = agent(1.4, "content").move_to([5.9, -0.8, 0]); lag25 = bandeau("L'État", 18).next_to(ag25, DOWN, buff=0.15)
        hd25 = puce("Ce minimum comprend…", 24).move_to([0.3, 2.75, 0])
        self.play(FadeIn(ag25, shift=0.2 * LEFT), FadeIn(lag25), FadeIn(hd25, shift=0.1 * DOWN), run_time=0.3)
        for k, mot in enumerate(("manger", "vêtir", "abri")):
            lb[k].next_to(bs[k], DOWN, buff=0.2); tg = bs[k].get_center(); bs[k].scale(0.3).move_to(main_de(ag25, -1))
            self.at(W(25, 1, mot) - 0.55, FadeIn(bs[k]), rt=0.12)
            self.play(bs[k].animate(path_arc=0.6).scale(1 / 0.3).move_to(tg), FadeIn(lb[k]), run_time=0.4); self.son("ding", 0.45)
        visage(pe, 1.45, "content")
        ar = VGroup(piece(0.85), T("En argent", 22)).arrange(DOWN, buff=0.2).move_to([-0.6, -1.3, 0])
        na = VGroup(colis(1.0), T("En nature", 22)).arrange(DOWN, buff=0.2).move_to([3.4, -1.3, 0])
        for g_, mot in ((ar, "argent"), (na, "nature")):
            tg = g_[0].get_center(); g_[0].scale(0.4).move_to(main_de(ag25, -1))
            self.at(W(25, 2, mot) - 0.5, FadeIn(g_[0]), rt=0.12)
            self.play(g_[0].animate(path_arc=0.6).scale(2.5).move_to(tg), FadeIn(g_[1]), run_time=0.4); self.son("plop")
        # 26 — le législateur organise ; le juge veille au seuil
        self.vider(S(26, 1) - 0.4, rt=0.4)
        pa = ic_parlement(1.0).move_to([-5.1, 1.5, 0]); lpa = puce("Le législateur", 22).next_to(pa, DOWN, buff=0.2)
        ag = agent(1.3, "neutre").move_to([-2.1, -0.95, 0]); lag = bandeau("Les autorités", 18).next_to(ag, DOWN, buff=0.15)
        # l'étagère de l'aide sociale : en haut, les autres prestations ; en bas, le minimum indispensable
        cadre = Rectangle(width=4.0, height=3.0, color=BOIS, stroke_width=9).move_to([1.7, 0.35, 0])
        planche = Line(cadre.get_left(), cadre.get_right(), color=BOIS, stroke_width=9).move_to(cadre.get_center())
        fond_et = Rectangle(width=4.0, height=3.0, fill_color=ROUGE_3, fill_opacity=1, stroke_width=0).move_to(cadre)
        haut = VGroup(piece(0.62), colis(0.75), dossier(0.85)).arrange(RIGHT, buff=0.35, aligned_edge=DOWN)
        au_sol(haut, 1.7, planche.get_y() + 0.08)
        bas_ = VGroup(assiette(0.85), habit(0.62), abri(0.8)).arrange(RIGHT, buff=0.35, aligned_edge=DOWN)
        au_sol(bas_, 1.7, cadre.get_bottom()[1] + 0.08)
        lpi = T("Les prestations sociales", 20).next_to(cadre, UP, buff=0.15)
        self.at(W(26, 1, "législateur") - 0.3, FadeIn(pa, shift=0.2 * UP), FadeIn(lpa), rt=0.4)
        lo = page("Loi", ["sur l'aide sociale"], l=2.4, taille=16).scale(0.6).move_to(pa.get_center())
        self.play(FadeIn(lo, scale=0.4), run_time=0.2)
        self.play(lo.animate(path_arc=-0.5).move_to(cadre.get_left() + np.array([-0.85, 0.9, 0])), FadeIn(fond_et), Create(cadre), Create(planche), FadeIn(lpi), run_time=0.6); self.son("plop")
        self.at(W(26, 1, "autorités") - 0.3, FadeIn(ag, shift=0.2 * UP), FadeIn(lag), rt=0.4)
        objets = [*haut, *bas_]; cibles = [o.get_center() for o in objets]
        for o in objets: o.scale(0.5).move_to(main_de(ag, 1))
        ba26 = bras_tendu(ag, 1)
        self.at(W(26, 1, "organiser") - 0.4, Create(ba26), rt=0.2)
        self.play(LaggedStart(*[AnimationGroup(FadeIn(o, run_time=0.1), o.animate(path_arc=-0.5).scale(2).move_to(c)) for o, c in zip(objets, cibles)], lag_ratio=0.22), run_time=1.6); self.son("plop")
        self.play(FadeOut(ba26), run_time=0.2)
        self.jusqua(S(26, 2) - 0.2)
        jg = juge(1.45, "decide").move_to([5.9, -0.95, 0]); ljg = bandeau("Le juge", 18).next_to(jg, DOWN, buff=0.15)
        self.play(FadeIn(jg, shift=0.2 * LEFT), FadeIn(ljg), run_time=0.4)
        bud = page("Budget", ["d'assistance"], l=2.6, taille=18).scale(0.65).move_to([5.6, 2.3, 0]); xb = coche(False, 0.32).move_to(bud.get_corner(UR) + 0.05 * UR)
        self.at(W(26, 2, "budget") - 0.3, FadeIn(bud, scale=0.5), FadeIn(xb, scale=2), rt=0.4); self.son("thud", 0.5)
        sl = DashedLine([cadre.get_left()[0] - 0.3, planche.get_y(), 0], [4.5, planche.get_y(), 0], color=CREME, stroke_width=6, dash_length=0.18)
        lsl = bandeau("Le seuil indispensable", 20).next_to(cadre, DOWN, buff=0.2)
        self.at(W(26, 2, "seuil") - 0.4, Create(sl), FadeIn(lsl), rt=0.5); self.son("ding", 0.5)
        bq = baguette(jg, [4.5, planche.get_y(), 0])
        self.play(Create(bq), run_time=0.3)
        self.at(W(26, 2, "respecté") - 0.3, *[Indicate(o, color=AMBRE, scale_factor=1.12) for o in bas_], rt=0.6)
        # 27 — qui peut invoquer ce droit ? les Suisses seulement ? une personne étrangère sans droit de séjour ?
        self.vider(S(27, 1) - 0.4, rt=0.4)
        dc = puce("Une difficulté très concrète", 26).move_to([0, 2.6, 0])
        self.at(S(27, 1) - 0.05, FadeIn(dc, shift=0.15 * DOWN), rt=0.4)
        bc = parapluie(1.1, AMBRE, "?").move_to([0, 0.75, 0]); lq = T("Qui peut l'invoquer ?", 24).next_to(bc, DOWN, buff=0.25)
        self.at(S(27, 2) - 0.05, FadeIn(bc, scale=0.4), FadeIn(lq), rt=0.4); self.son("ding", 0.6)
        su = VGroup(*[candidat(1.25, k, "neutre") for k in (1, 3)]).arrange(RIGHT, buff=0.3).move_to([-4.3, -1.05, 0])
        for b in su: b.add(maillot_ch(b))
        lsu = bandeau("Citoyens suisses", 20).next_to(su, DOWN, buff=0.2)
        self.at(W(27, 3, "citoyens") - 0.3, FadeIn(su, shift=0.2 * RIGHT), FadeIn(lsu), rt=0.4)
        et = frere(1.3, 0, "perplexe").move_to([4.3, -1.05, 0]); let = bandeau("Une personne étrangère", 20).next_to(et, DOWN, buff=0.2)
        ss = etiquette("Sans droit de séjour", 20).next_to(et, UP, buff=0.25)
        self.at(W(27, 4, "étrangère") - 0.3, FadeIn(et, shift=0.2 * LEFT), FadeIn(let), rt=0.4)
        self.at(W(27, 4, "séjourner") - 0.3, FadeIn(ss, scale=0.5), rt=0.3); self.son("plop")
        # 28 — humanité ; aussi les étrangers, quel que soit leur statut ; pas de frontière de nationalité
        self.vider(S(28, 1) - 0.4, rt=0.4)
        jg = juge(1.45, "decide").move_to([-5.6, -0.9, 0]); ljg = bandeau("Tribunal fédéral", 18).next_to(jg, DOWN, buff=0.15)
        hu = VGroup(coeur(2.2), T("Humanité", 26)).arrange(RIGHT, buff=0.25).move_to([-1.6, 2.3, 0])
        self.at(S(28, 1), FadeIn(jg, shift=0.2 * RIGHT), FadeIn(ljg), rt=0.4)
        self.at(W(28, 1, "humanité") - 0.4, FadeIn(hu, scale=0.5), rt=0.4); self.son("ding", 0.6)
        su = VGroup(*[candidat(1.25, k, "content") for k in (1, 3)]).arrange(RIGHT, buff=0.3).move_to([-1.4, -1.05, 0])
        for b in su: b.add(maillot_ch(b))
        br = barriere(1.0).move_to([1.4, -0.95, 0]); et = frere(1.3, 0, "neutre").move_to([3.9, -1.05, 0]); ss = etiquette("Statut de séjour : peu importe", 18).next_to(et, DOWN, buff=0.25)
        self.at(W(28, 2, "appartient") - 0.3, FadeIn(su, shift=0.2 * UP), FadeIn(br), FadeIn(et, shift=0.2 * UP), rt=0.45)
        ok1 = VGroup(*[coche(True, 0.28).next_to(b, UP, buff=0.12) for b in su]); ok2 = coche(True, 0.28).next_to(et, UP, buff=0.12)
        self.at(W(28, 2, "étrangers") - 0.3, FadeIn(ok1, scale=2), FadeIn(ok2, scale=2), rt=0.35); self.son("joie", 0.5)
        visage(et, 1.3, "content")
        self.at(W(28, 2, "indépendamment") - 0.3, FadeOut(ok2), FadeIn(ss, scale=0.5), rt=0.35)
        bc = parapluie(0.9).move_to([-1.4, 1.05, 0]); lnat = bandeau("Frontière de la nationalité", 18).next_to(br, UP, buff=0.2)
        self.at(W(28, 3, "droit") - 0.3, FadeIn(bc, scale=0.5), FadeIn(lnat), rt=0.4)
        bc2 = bc.copy(); self.add(bc2)
        self.at(W(28, 3, "frontière") - 0.3, bc2.animate(path_arc=-0.6).move_to([3.9, 1.05, 0]), rt=1.0); self.son("souffle")
        visage(et, 1.3, "content"); self.play(Wiggle(bc2, scale_value=1.08), et.animate(rate_func=there_and_back).shift(0.15 * UP), run_time=0.45)
        # 29 — pas forcément les mêmes prestations ; selon les besoins, notamment un séjour provisoire
        self.vider(S(29, 1) - 0.4, rt=0.4)
        p1 = candidat(1.35, 1, "neutre").move_to([-3.6, -0.95, 0]); p1.add(maillot_ch(p1)); p2 = candidat(1.35, 2, "neutre").move_to([3.0, -0.95, 0])
        a1 = VGroup(colis(0.9), colis(0.8).shift(0.85 * RIGHT)).next_to(p1, RIGHT, buff=0.3).align_to(p1, DOWN); a2 = colis(0.75).next_to(p2, RIGHT, buff=0.3).align_to(p2, DOWN)
        ne = T("≠", 80).move_to([0.2, -0.4, 0])
        self.at(S(29, 1), FadeIn(p1, shift=0.2 * UP), FadeIn(p2, shift=0.2 * UP), rt=0.4)
        self.at(W(29, 1, "mêmes") - 0.4, FadeIn(a1, shift=0.2 * DOWN), FadeIn(a2, shift=0.2 * DOWN), FadeIn(ne, scale=0.5), rt=0.45); self.son("plop")
        lv = puce("Selon les besoins concrets", 24).move_to([0, 2.5, 0])
        self.at(W(29, 2, "besoins") - 0.4, FadeIn(lv, shift=0.15 * DOWN), rt=0.35)
        sb = sablier(0.6).next_to(p2, UP, buff=0.3); lsp = etiquette("Séjour provisoire", 20).next_to(sb, RIGHT, buff=0.2)
        self.at(W(29, 2, "provisoire") - 0.4, FadeIn(sb, scale=0.5), FadeIn(lsp, scale=0.5), rt=0.4); self.son("plop")
        self.play(Rotate(sb, PI), run_time=0.6)
        self.fin()
