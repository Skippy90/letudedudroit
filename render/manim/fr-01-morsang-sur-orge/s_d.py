from base import *
from base import _bh, _vivant


def badge_atteinte(e=1.0):
    return VGroup(RoundedRectangle(corner_radius=0.12, width=4.4 * e, height=0.8 * e, fill_color=AMBRE, fill_opacity=1, stroke_color=ENCRE, stroke_width=3 * e),
                  T("Atteinte à la dignité", int(26 * e), ENCRE))


class D1(Sec25):
    L0, L1 = 17, 23

    def construct(self):
        self.debut(2); self.chapitre(2, "Le raisonnement", 3)
        # 17.1 — la police municipale doit prévenir les atteintes à l'ordre public
        ce = conseil_etat(0.8).move_to([-4.6, 1.6, 0])
        jg = juge(1.7, "decide").move_to([-5.4, -1.0, 0])
        self.at(S(17, 1), FadeIn(ce, shift=0.2 * UP), FadeIn(jg, shift=0.2 * RIGHT), rt=0.45)
        op = ordre_public(1.05).move_to([2.0, -0.2, 0])
        self.at(W(17, 1, "fonction") - 0.3, FadeIn(op, shift=0.2 * UP), rt=0.45); self.son("plop")
        mr = maire(1.6, "decide").move_to([-1.9, -1.1, 0]); pr = bandeau("Prévenir les atteintes", 22).next_to(mr, DOWN, buff=0.15)
        self.at(W(17, 1, "prévenir") - 0.35, FadeIn(mr, shift=0.2 * UP), FadeIn(pr), rt=0.4)
        bt = bras_tendu(mr, 1); self.play(Create(bt), run_time=0.3)
        # 17.2 — puis il en précise le contenu
        lp_ = loupe(1.2).move_to(op.get_left() + 0.6 * LEFT + 0.3 * UP)
        self.at(S(17, 2) - 0.05, FadeIn(lp_, shift=0.3 * RIGHT), rt=0.35)
        self.play(lp_.animate.move_to(op.tuiles.get_center() + 0.2 * DOWN), run_time=0.8)
        # 18.1 — c'est ici que tout bascule
        self.jusqua(S(18, 1) - 0.2)
        self.play(FadeOut(lp_), FadeOut(bt), FadeOut(pr), FadeOut(mr), FadeOut(ce), jg.animate.move_to([-4.6, -0.95, 0]), op.animate.move_to([1.8, 0.45, 0]), run_time=0.45)
        self.play(Wiggle(op, scale_value=1.04, rotation_angle=0.03 * TAU), run_time=0.6); self.son("souffle", 0.6)
        # 18.2 — le respect de la dignité de la personne humaine fait partie de l'ordre public
        td = tuile_dignite(1.15).move_to(main_de(jg, 1) + 0.6 * UP)
        self.at(W(18, 2, "affirme") - 0.3, FadeIn(td, scale=0.4), rt=0.3)
        cible = op.cadre.get_bottom() + 0.75 * DOWN
        self.at(W(18, 2, "dignité") - 0.4, donner(td, cible, 0.5, 0.7), rt=0.7)
        grand = RoundedRectangle(corner_radius=0.22, width=op.cadre.width, height=op.cadre.height + 1.2, fill_color=BLEU_3, fill_opacity=1, stroke_color=CREME, stroke_width=3).align_to(op.cadre, UP)
        self.at(W(18, 2, "partie") - 0.4, Transform(op.cadre, grand), td.animate.move_to(grand.get_bottom() + 0.68 * UP), rt=0.5); self.son("ding", 0.8)
        self.play(Indicate(td, color=AMBRE, scale_factor=1.08), run_time=0.6)
        # 19.1 — une attraction qui porte atteinte à la dignité peut être interdite, même sans circonstances locales
        self.vider(S(19, 1) - 0.4, rt=0.35)
        af = affiche(1.15).move_to([-1.2, 0.9, 0]); td = tuile_dignite(0.9).move_to([-1.2, -1.0, 0])
        mr = maire(1.7, "decide").move_to([-4.6, -0.9, 0])
        self.at(S(19, 1), FadeIn(af, shift=0.2 * UP), FadeIn(td, shift=0.2 * UP), FadeIn(mr, shift=0.2 * RIGHT), rt=0.45)
        tq = tampon("INTERDIT", 30).rotate(-0.1)
        self.at(W(19, 1, "interdite") - 0.3, *tamponner(self, tq, af.get_center() + 0.1 * DOWN, mr), rt=0.35); self.son("thud", 0.8)
        qu = VGroup(quartier(1.15), loupe(0.85).shift(0.45 * RIGHT + 0.1 * UP)).move_to([4.2, 0.75, 0])
        self.at(W(19, 1, "circonstances") - 0.4, FadeIn(qu, shift=0.2 * LEFT), rt=0.35)
        # 19.2 — pas besoin de démontrer une situation propre à la commune
        nn = ligne_coche(True, "Pas nécessaire", None, 26).next_to(qu, DOWN, buff=0.3)
        self.at(S(19, 2) - 0.05, qu.animate.set_opacity(0.35), FadeIn(nn, shift=0.1 * UP), rt=0.4); self.son("plop")
        self.at(W(19, 2, "commune") - 0.3, mr.animate(rate_func=there_and_back).shift(0.2 * UP), rt=0.4)
        # 20.1 — encore faut-il appliquer ce principe au spectacle en cause
        self.vider(S(20, 1) - 0.4, rt=0.35)
        td = tuile_dignite(1.0).move_to([-4.4, 1.0, 0]); af = affiche(1.2).move_to([4.4, 0.9, 0])
        fl = Arrow(td.get_right(), af.get_left(), color=CREME, buff=0.3, stroke_width=7)
        lap = bandeau("Appliquer le principe", 22).next_to(fl, UP, buff=0.15)
        self.at(S(20, 1), FadeIn(td, shift=0.2 * RIGHT), FadeIn(af, shift=0.2 * LEFT), rt=0.4)
        self.at(W(20, 1, "appliquer") - 0.3, GrowArrow(fl), FadeIn(lap), rt=0.45); self.son("plop")
        # 20.2 — la formule de l'arrêt, citée (on ne montre pas l'attraction)
        cit = page("Conseil d'État, 27 octobre 1995", ["« …utiliser comme un projectile une personne", "affectée d'un handicap physique", "et présentée comme telle »"], l=7.4, taille=22).move_to([0, -1.25, 0])
        self.at(S(20, 2) - 0.05, FadeIn(cit, shift=0.2 * UP), rt=0.45); self.son("ding", 0.5)
        c1 = cadre_autour(cit.corps[0], 0.06)
        self.at(W(20, 2, "projectile") - 0.3, Create(c1), rt=0.4)
        c2 = cadre_autour(VGroup(cit.corps[1], cit.corps[2]), 0.06)
        self.at(W(20, 2, "présentée") - 0.4, Create(c2), rt=0.4)
        # 20.3 — par son objet même : atteinte à la dignité
        ba = badge_atteinte(0.8).move_to(af.get_center() + 0.2 * DOWN).rotate(-0.08)
        self.at(S(20, 3) - 0.05, FadeOut(fl), FadeOut(lap), rt=0.25)
        self.at(W(20, 3, "objet") - 0.3, *tamponner(self, ba, af.get_center() + 0.2 * DOWN), rt=0.35); self.son("thud", 0.8)
        self.play(Indicate(td, color=AMBRE, scale_factor=1.1), run_time=0.5)
        # 21.1 — c'est ici que le raisonnement devient particulièrement discuté
        self.vider(S(21, 1) - 0.4, rt=0.35)
        g = VGroup(*[_bh(1.35, c) for c in (MENTHE, CIEL)]).arrange(RIGHT, buff=4.4, aligned_edge=DOWN).move_to([0, -1.1, 0])
        for b in g: b.h = 1.35; _vivant(b, 0.04); visage(b, 1.35, "decide")
        b1 = bulle(["Il a le droit", "de choisir !"], 20).next_to(g[0], UP, buff=0.2).shift(0.7 * RIGHT)
        b2 = bulle(["Sa dignité", "est en jeu !"], 20).next_to(g[1], UP, buff=0.2).shift(0.7 * RIGHT)
        di = VGroup(Circle(0.5, fill_color=AMBRE, fill_opacity=1, stroke_width=0), T("?", 44, ENCRE)).move_to([0, 2.35, 0]); ld = bandeau("Une solution discutée", 22).next_to(di, DOWN, buff=0.2)
        self.at(S(21, 1), FadeIn(g, shift=0.2 * UP), rt=0.4)
        self.at(W(21, 1, "raisonnement") - 0.2, FadeIn(b1, scale=0.5), FadeIn(b2, scale=0.5), rt=0.4); self.son("plop")
        self.at(W(21, 1, "discuté") - 0.4, FadeIn(di, scale=0.5), FadeIn(ld), rt=0.4)
        # 21.2 — même librement et contre rémunération, l'appréciation est maintenue
        self.vider(S(21, 2) - 0.35, rt=0.35)
        pa = participant(1.55, "neutre").move_to([-2.6, -1.0, 0])
        af = affiche(1.0).move_to([3.2, 1.0, 0]); ba = badge_atteinte(0.7).rotate(-0.08).move_to(af.get_center() + 0.2 * DOWN)
        self.at(S(21, 2), FadeIn(pa, shift=0.2 * UP), FadeIn(af), FadeIn(ba), rt=0.4)
        ct = VGroup(contrat(0.85), T("Librement", 22)).arrange(DOWN, buff=0.15).move_to([-5.3, 0.6, 0])
        pc = VGroup(piece_fr(0.7), T("Rémunéré", 22)).arrange(DOWN, buff=0.15).move_to([-0.2, 0.6, 0])
        self.at(W(21, 2, "librement") - 0.35, FadeIn(ct, shift=0.2 * UP), rt=0.35); self.son("plop")
        self.at(W(21, 2, "rémunération") - 0.4, FadeIn(pc, shift=0.2 * UP), rt=0.35); self.son("plop")
        mt = bandeau("L'appréciation est maintenue", 22).next_to(af, DOWN, buff=0.35)
        self.play(FadeIn(mt, shift=0.1 * UP), Indicate(ba, color=AMBRE, scale_factor=1.08), run_time=0.5)
        # 22.1 — il ne dit pas que le participant était contraint
        self.vider(S(22, 1) - 0.4, garder=(pa,), rt=0.35)
        ch = chaine(1.4).move_to([1.4, 1.3, 0]); lc = T("Contraint ?", 26).next_to(ch, DOWN, buff=0.2)
        no = ligne_coche(False, "Il ne le dit pas", None, 24).next_to(lc, DOWN, buff=0.25)
        self.at(S(22, 1), FadeIn(ch, shift=0.2 * DOWN), FadeIn(lc), rt=0.4)
        self.at(W(22, 1, "contraint") - 0.3, FadeIn(no, shift=0.1 * UP), ch.animate.set_opacity(0.4), rt=0.35); self.son("thud", 0.5)
        # 22.2 — le consentement ne fait pas disparaître l'atteinte à la dignité
        self.jusqua(S(22, 2) - 0.3)
        self.play(*[FadeOut(x) for x in (ch, lc, no)], run_time=0.3)
        ba = badge_atteinte(0.9).move_to([2.6, 0.9, 0])
        ct = contrat(1.0).move_to(main_de(pa, 1) + [0.55, 0.45, 0])
        self.at(W(22, 2, "consentement") - 0.4, FadeIn(ba, scale=0.6), FadeIn(ct, scale=0.5), rt=0.4)
        self.play(ct.animate.move_to(ba.get_center()), run_time=0.5); self.son("thud", 0.5)
        self.play(ct.animate.move_to(ba.get_center() + 1.2 * DOWN + 1.6 * LEFT).rotate(0.4), Wiggle(ba, scale_value=1.06), run_time=0.5)
        np_ = bandeau("Le consentement ne l'efface pas", 22).next_to(ba, DOWN, buff=0.3)
        self.at(W(22, 2, "disparaître") - 0.4, FadeIn(np_, shift=0.1 * UP), rt=0.35)
        self.fin()


class D2(Sec25):
    L0, L1 = 23, 29

    def construct(self):
        self.debut(2)
        # 23.1 — une autre objection
        ob = puce("Une autre objection", 32).move_to([0, 2.4, 0])
        self.at(S(23, 1), FadeIn(ob, scale=1.2), rt=0.4); self.son("ding", 0.5)
        # 23.2 — interdire empêche une activité professionnelle et commerciale
        ml = VGroup(mallette(1.3), T("Activité professionnelle", 22)).arrange(DOWN, buff=0.2).move_to([-3.6, 0.3, 0])
        bo = VGroup(boutique(1.3), T("Activité commerciale", 22)).arrange(DOWN, buff=0.2).move_to([3.6, 0.3, 0])
        br = barriere(1.4).move_to([0, -0.2, 0])
        self.at(W(23, 2, "empêche") - 0.3, FadeIn(br, shift=0.2 * DOWN), rt=0.35); self.son("thud", 0.5)
        self.at(W(23, 2, "professionnelle") - 0.4, FadeIn(ml, shift=0.2 * UP), rt=0.35); self.son("plop")
        self.at(W(23, 2, "commerciale") - 0.3, FadeIn(bo, shift=0.2 * UP), rt=0.35); self.son("plop")
        # 23.3 — liberté du travail, liberté du commerce et de l'industrie : prévaloir ?
        self.vider(S(23, 3) - 0.35, rt=0.35)
        lt = tuile("Liberté\ndu travail", MENTHE, 2.0, 1.0, 19); lc = tuile("Liberté du commerce\net de l'industrie", MENTHE, 2.9, 1.0, 19)
        gauche = VGroup(lt, lc).arrange(DOWN, buff=0.12).scale(0.8)
        droite = ordre_public(0.42)
        bal = balance(1.25, gauche, droite).move_to([0, -0.35, 0])
        self.at(S(23, 3), FadeIn(bal, shift=0.2 * UP), rt=0.5); self.son("plop")
        q = bas("Ces libertés ne devraient-elles pas prévaloir ?", 28)
        self.at(W(23, 3, "prévaloir") - 0.5, FadeIn(q, shift=0.1 * UP), pencher(bal, 0.12), rt=0.6)
        # 24 — réponse : pas d'obstacle si c'est la seule mesure de nature à prévenir ou faire cesser le trouble
        ce = conseil_etat(0.7).move_to([-5.2, 2.3, 0])
        self.at(S(24, 1) - 0.05, FadeOut(q), FadeIn(ce, shift=0.2 * DOWN), rt=0.35)
        self.at(W(24, 1, "obstacle") - 0.3, pencher(bal, -0.26), rt=0.7); self.son("thud", 0.6)
        cs = puce("Si c'est la seule mesure de nature à prévenir le trouble", 24).move_to([0, -2.6, 0])
        self.at(W(24, 1, "seule") - 0.4, FadeIn(cs, shift=0.15 * UP), rt=0.4); self.son("ding", 0.5)
        self.at(W(24, 1, "cesser") - 0.3, Indicate(cs, color=CREME, scale_factor=1.05), rt=0.5)
        # 25.1 — la question n'est pas : rémunérée ? licite ?
        self.vider(S(25, 1) - 0.4, rt=0.35)
        vA = vignette(-3.4, False, "Est-elle rémunérée,", "est-elle licite ?")
        iA = VGroup(piece_fr(0.9), code_fr("La loi", "", 0.6)).arrange(RIGHT, buff=0.6).move_to(vA.f.get_center() + 0.35 * DOWN)
        self.at(S(25, 1), FadeIn(vA), rt=0.35)
        self.at(W(25, 1, "rémunérée") - 0.35, FadeIn(iA[0], scale=0.5), rt=0.3); self.son("plop", 0.5)
        self.at(W(25, 1, "licite") - 0.35, FadeIn(iA[1], scale=0.5), rt=0.3); self.son("plop", 0.5)
        # 25.2 — la question est : son exercice heurte-t-il une exigence d'ordre public ?
        vB = vignette(3.4, True, "Heurte-t-elle", "l'ordre public ?")
        opB = ordre_public(0.62).move_to(vB.f.get_center() + 0.45 * DOWN); ec = eclair(0.9).move_to(opB.get_corner(UL) + 0.15 * UL)
        self.at(S(25, 2) - 0.05, FadeIn(vB), FadeIn(opB, shift=0.2 * UP), rt=0.4)
        self.at(W(25, 2, "heurte") - 0.3, FadeIn(ec, shift=0.3 * DOWN), Wiggle(opB, scale_value=1.04), rt=0.5); self.son("thud", 0.6)
        # 26.1 — la nature de l'attraction justifie l'interdiction
        self.vider(S(26, 1) - 0.4, rt=0.35)
        js = juges(3, 1.45, "decide").move_to([-4.0, -1.05, 0])
        af = affiche(1.15).move_to([1.4, 1.0, 0]); lp_ = loupe(1.0).move_to(af.get_center() + 0.7 * RIGHT + 0.1 * UP)
        self.at(S(26, 1), FadeIn(js, shift=0.2 * UP), FadeIn(af, shift=0.2 * DOWN), rt=0.4)
        self.at(W(26, 1, "nature") - 0.35, FadeIn(lp_, shift=0.3 * LEFT), rt=0.35)
        tq = tampon("INTERDIT", 28).rotate(-0.1); ok = ligne_coche(True, "Justifié", None, 24).next_to(af, RIGHT, buff=0.9)
        self.at(W(26, 1, "justifie") - 0.35, *tamponner(self, tq, af.get_center() + 0.1 * DOWN, js[1]), rt=0.35); self.son("thud", 0.7)
        self.play(FadeIn(ok, shift=0.1 * LEFT), FadeOut(lp_), run_time=0.3)
        # 26.2 — la sécurité matérielle ne suffit pas à lever l'objection tirée de la dignité
        cq = VGroup(casque(1.2), tapis(1.8)).arrange(DOWN, buff=0.1).move_to([1.4, -1.6, 0])
        td = tuile_dignite(0.85).move_to([5.0, -1.6, 0])
        self.at(W(26, 2, "sécurité") - 0.35, FadeIn(cq, shift=0.2 * UP), rt=0.35)
        self.at(W(26, 2, "dignité") - 0.5, FadeIn(td, shift=0.2 * LEFT), rt=0.35)
        ns = coche(False, 0.42).move_to(cq.get_corner(UR) + 0.2 * UR); lns = bandeau("Ne suffit pas", 20).next_to(cq, LEFT, buff=0.25)
        self.play(FadeIn(ns, scale=2), FadeIn(lns), run_time=0.3); self.son("thud", 0.5)
        # 27 — le tribunal administratif avait commis une erreur de droit en exigeant des circonstances locales
        self.vider(S(27, 1) - 0.4, rt=0.35)
        jt = page("Jugement · Tribunal administratif", ["Pas d'interdiction sans", "circonstances locales", "particulières."], l=6.0, taille=22).move_to([1.6, 0.6, 0])
        jg = juge(1.75, "decide").move_to([-4.8, -0.85, 0]); lj = bandeau("Conseil d'État", 20).next_to(jg, DOWN, buff=0.15)
        self.at(S(27, 1), FadeIn(jt, shift=0.2 * UP), FadeIn(jg, shift=0.2 * RIGHT), FadeIn(lj), rt=0.45)
        ed = tampon("ERREUR DE DROIT", 30).rotate(-0.1)
        self.at(W(27, 1, "erreur") - 0.3, *tamponner(self, ed, jt.get_center() + 0.2 * DOWN, jg), rt=0.35); self.son("thud", 0.8)
        cl = cadre_autour(VGroup(jt.corps[0], jt.corps[1]), 0.06)
        self.at(W(27, 1, "circonstances") - 0.3, Create(cl), rt=0.4)
        # 28.1 — le Conseil d'État annule le jugement de Versailles
        self.vider(S(28, 1) - 0.4, rt=0.35)
        jt = page("Jugement · Tribunal administratif", ["Versailles, 25 février 1992"], l=5.4, taille=22).move_to([-3.2, 1.0, 0])
        jg = juge(1.75, "decide").move_to([0.6, -0.95, 0])
        self.at(S(28, 1), FadeIn(jt, shift=0.2 * UP), FadeIn(jg, shift=0.2 * UP), rt=0.4)
        an = tampon("ANNULÉ", 28).rotate(-0.1)
        self.at(W(28, 1, "annule") - 0.3, *tamponner(self, an, jt.get_corner(DR) + [-1.2, -0.35, 0], jg), rt=0.35); self.son("thud", 0.9)
        # 28.2 — il rejette les demandes de Fun Production et du participant
        rq = demande(0.75, "Recours", "contre l'arrêté").move_to([4.6, 1.1, 0])
        og = organisateur(1.6, "neutre").move_to([3.8, -1.25, 0]); pa = participant(1.2, "neutre").move_to([5.3, -1.4, 0])
        self.at(S(28, 2) - 0.05, FadeIn(rq, shift=0.2 * DOWN), FadeIn(og, shift=0.2 * LEFT), FadeIn(pa, shift=0.2 * LEFT), rt=0.4)
        rj = tampon("REJETÉ", 30).rotate(-0.1)
        self.at(W(28, 2, "rejette") - 0.3, *tamponner(self, rj, rq.get_center(), jg), rt=0.35); self.son("thud", 0.8)
        humeur(VGroup(og, pa), "triste")
        self.fin()
