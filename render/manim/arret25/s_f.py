from base import *
from s_a import quatre
from s_b import asso
from s_c import bloc_art


class Ff(Sec25):
    L0, L1 = 44, 51

    def construct(self):
        self.debut(fil_avant=3); self.chapitre(4, "À retenir", 5)
        # 44 — le droit actuel : la loi sur le climat et l'innovation
        t = titre("Et le droit actuel ?"); q = quatre(1.0, "perplexe"); q.move_to([-4.6, -2.0, 0])
        self.at(S(44, 1) - 0.1, FadeIn(t, shift=0.2 * DOWN), FadeIn(q, shift=0.2 * UP), rt=0.4)
        cs = carte(3.4, (1.6, -1.6)); self.at(S(44, 2) - 0.05, FadeIn(cs), rt=0.4)
        lo = page("Loi fédérale", ["Loi sur le climat", "et l'innovation"], l=3.8, taille=20).move_to([-4.6, 0.6, 0])
        self.at(W(44, 2, "loi") - 0.4, FadeIn(lo, shift=0.3 * UP), rt=0.5); self.son("plop")
        def etape(an, quoi, x):
            return VGroup(puce(an, 26), T(quoi, 22)).arrange(DOWN, buff=0.18).move_to([x, 1.0, 0])
        es = [etape("2022", "adoptée", -1.4), etape("2023", "approuvée par le peuple", 1.5), etape("1er janvier 2025", "en vigueur", 4.9)]
        ur = urne(0.6).next_to(es[1], UP, buff=0.2)
        self.at(W(44, 2, "adoptée") - 0.3, FadeIn(es[0], shift=0.2 * UP), rt=0.35); self.son("plop", 0.7)
        self.at(W(44, 2, "approuvée") - 0.3, FadeIn(es[1], shift=0.2 * UP), FadeIn(ur, scale=0.6), rt=0.35); self.son("plop", 0.7)
        self.at(W(44, 2, "entrée") - 0.3, FadeIn(es[2], shift=0.2 * UP), rt=0.35); self.son("ding", 0.7)
        self.at(S(44, 3) - 0.45, *[FadeOut(x) for x in (*es, ur, cs, q)], lo.animate.move_to([-4.6, 0.2, 0]), rt=0.4)
        sol = Line([-1.2, -2.2, 0], [5.9, -2.2, 0], color=CREME, stroke_width=4)
        hs = [3.0, 2.3, 1.6, 0.9, 0.3]; bars = VGroup(*[Rectangle(width=0.8, height=h_, fill_color=GRIS, fill_opacity=1, stroke_width=0).move_to([-0.5 + 1.25 * k, -2.2 + h_ / 2, 0]) for k, h_ in enumerate(hs)])
        an = T("2050", 26).move_to([-0.5 + 1.25 * 5, -2.65, 0]); zn = puce("Zéro net", 34).move_to([-0.5 + 1.25 * 5 - 0.3, -0.6, 0])
        self.at(S(44, 3) - 0.05, Create(sol), LaggedStart(*[FadeIn(b, shift=0.2 * UP) for b in bars], lag_ratio=0.15), rt=1.0); self.son("zip")
        self.at(W(44, 3, "zéro") - 0.3, FadeIn(zn, scale=1.4), rt=0.4); self.son("ding", 0.8)
        ge = bandeau("Gaz à effet de serre", 20).move_to([1.2, 1.4, 0]); self.at(W(44, 3, "gaz") - 0.3, FadeIn(ge), rt=0.3)
        self.at(W(44, 3, "cinquante") - 0.6, FadeIn(an, scale=1.3), rt=0.3)
        # 45 — l'article 25a PA existe toujours
        self.vider(S(45, 1) - 0.5, rt=0.4)
        lv = livre("Procédure", "administrative", "25a").move_to([-4.6, 0.1, 0]); ba = bloc_art()
        self.at(S(45, 1) - 0.05, FadeIn(lv, shift=0.3 * UP), FadeIn(ba, scale=1.3), rt=0.5)
        tj = bandeau("Toujours en vigueur", 22).next_to(lv, DOWN, buff=0.2); self.at(W(45, 1, "existe") - 0.2, FadeIn(tj, shift=0.1 * UP), rt=0.3)
        un = ainee(1.6, MENTHE, "content"); un.move_to([-1.2, -1.0, 0])
        pt = VGroup(Rectangle(width=1.5, height=2.5, color=CREME, stroke_width=6), Rectangle(width=0.2, height=2.4, fill_color=ENCRE, fill_opacity=1, stroke_width=0).shift(0.62 * LEFT)).move_to([1.8, -0.6, 0])
        pp = bandeau("Les personnes touchées dans leurs droits", 22).move_to([0.6, 1.4, 0])
        self.at(S(45, 2) - 0.05, FadeIn(un, shift=0.2 * UP), FadeIn(pt), rt=0.4)
        self.at(W(45, 2, "personnes") - 0.3, FadeIn(pp, shift=0.1 * DOWN), rt=0.3); self.son("hop")
        self.play(*self.marche([un], [[1.8, -0.95, 0]], 3), run_time=1.0)
        st = cour(1.9).move_to([5.3, -0.7, 0]); gl = VGroup(puce("À lire avec la Convention", 22), T("telle qu'interprétée à Strasbourg", 20, CREME, False)).arrange(DOWN, buff=0.1).move_to([4.6, 1.5, 0])
        self.at(W(45, 3, "garanties") - 0.6, FadeOut(pp), FadeIn(gl[0], shift=0.15 * DOWN), FadeIn(st, shift=0.3 * UP), rt=0.5); self.son("ding", 0.7)
        self.at(W(45, 3, "telles") - 0.2, FadeIn(gl[1]), rt=0.3)
        # 46 — le principal piège
        self.vider(S(46, 1) - 0.5, rt=0.4)
        t = titre("Le principal piège", 36); self.at(S(46, 1) - 0.1, FadeIn(t, scale=1.3), rt=0.4); self.son("grelot", 0.6)
        p = acteur(2.3, None, False, "content"); p.move_to([-4.8, -1.2, 0])
        bu = bulle(["Recours rejeté en 2020,", "donc politique climatique validée"], 28); bu.next_to(p, RIGHT, buff=0.5).shift(0.8 * UP)
        self.at(S(46, 2) - 0.05, FadeIn(p, shift=0.2 * UP), rt=0.3)
        self.at(W(46, 2, "parce") - 0.2, FadeIn(bu[0]), FadeIn(bu[1]), FadeIn(bu[2][0], shift=0.2 * LEFT), rt=0.4)
        self.at(W(46, 2, "validé") - 0.5, FadeIn(bu[2][1], shift=0.2 * LEFT), rt=0.4)
        # 47 — non : une question d'accès au juge
        fx = tampon("NON", 54).move_to(bu.get_center() + 0.1 * UP)
        self.at(S(47, 1) - 0.1, FadeIn(fx, scale=2.4), bu.animate.set_opacity(0.45), rt=0.3); self.son("thud"); visage(p, 2.3, "surpris")
        self.vider(S(47, 2) - 0.4, garder=[t], rt=0.35)
        tf = tribunal(3.0).move_to([-3.8, -0.7, 0]); pt = Rectangle(width=0.95, height=1.2, fill_color=ENCRE, fill_opacity=1, stroke_color=CREME, stroke_width=3).move_to(tf[2].get_center())
        qe = puce("Les juges suisses", 28).next_to(tf, UP, buff=0.3)
        self.at(S(47, 2) - 0.05, FadeIn(tf, shift=0.3 * UP), FadeIn(pt), FadeIn(qe, scale=1.2), rt=0.5)
        e1 = VGroup(T("Peut-on obtenir une décision", 26), T("et un examen judiciaire ?", 26)).arrange(DOWN, buff=0.12).move_to([2.9, 0.8, 0]); self.at(W(47, 2, "possibilité") - 0.3, FadeIn(e1, shift=0.2 * LEFT), rt=0.4)
        e2 = bandeau("Ils se sont arrêtés là", 22).next_to(e1, DOWN, buff=0.25); self.at(W(47, 2, "examen") - 0.2, FadeIn(e2), rt=0.3)
        e3 = VGroup(coche(False, 0.3), T("Mesures suffisantes ? Pas tranché", 26)).arrange(RIGHT, buff=0.25).move_to([2.9, -1.6, 0]); self.at(W(47, 3, "mesures") - 0.4, FadeIn(e3, shift=0.15 * UP), rt=0.4); self.son("plop")
        # 48 — deux arrêts, deux questions
        self.vider(S(48, 1) - 0.5, rt=0.4)
        t = titre("Deux arrêts, deux questions", 34); self.at(S(48, 1) - 0.1, FadeIn(t, scale=1.3), rt=0.4)
        def pt_(n, a, b, y):
            c = VGroup(Circle(0.38, fill_color=CREME, fill_opacity=1, stroke_width=0), T(str(n), 30, ROUGE)).move_to([-5.6, y, 0])
            tx = VGroup(T(a, 26), T(b, 21, CREME, False)).arrange(DOWN, buff=0.1, aligned_edge=LEFT).next_to(c, RIGHT, buff=0.4)
            return VGroup(c, tx)
        e1 = pt_(1, "En Suisse : l'art. 25a PA ne permet pas cet examen", "une demande de portée générale", 1.7)
        e2 = pt_(2, "À Strasbourg : deux violations constatées", "à la demande de l'association · articles 8 et 6", 0.35)
        e3 = pt_(3, "Les quatre femmes : irrecevables", "à titre individuel", -1.0)
        i1 = tribunal(2.4).scale(0.45).move_to([5.4, 1.75, 0]); i3 = quatre(0.6, "triste"); i3.move_to([5.4, -1.0, 0])
        i2 = asso(8, 0.4); i2.remove(i2.ban); i2.move_to([5.4, 0.4, 0])
        self.at(S(48, 2) - 0.05, FadeIn(e1, shift=0.3 * LEFT), FadeIn(i1, shift=0.2 * UP), rt=0.5); self.son("plop")
        self.at(S(48, 3) - 0.05, FadeIn(e2, shift=0.3 * LEFT), FadeIn(i2, shift=0.2 * UP), rt=0.5); self.son("joie", 0.7)
        for x in i2.membres: visage(x, 0.4, "content")
        self.saut(*i2.membres, h=0.1, rt=0.35)
        self.at(W(48, 3, "tandis") - 0.2, FadeIn(e3, shift=0.3 * LEFT), FadeIn(i3, shift=0.2 * UP), rt=0.5); self.son("plop")
        # 49 — la question
        self.vider(S(49, 1) - 0.5, rt=0.4)
        t = titre("À vous", 34); self.at(S(49, 1) - 0.1, FadeIn(t, scale=1.3), rt=0.4)
        f = RoundedRectangle(corner_radius=0.3, width=11.6, height=2.9, fill_color=ROUGE_3, fill_opacity=1, stroke_width=0).move_to([0, 0.5, 0])
        l1 = T("Tribunal fédéral : une action populaire", 32)
        l2 = T("Strasbourg : l'association peut agir", 32)
        ls = VGroup(l1, l2).arrange(DOWN, buff=0.45).move_to(f)
        self.at(S(49, 2) - 0.1, FadeIn(f), FadeIn(l1, shift=0.15 * UP), rt=0.5)
        self.at(W(49, 2, "alors") - 0.2, FadeIn(l2, shift=0.15 * UP), rt=0.4)
        qt = VGroup(T("Qu'est-ce qui distingue", 38), T("ces deux solutions ?", 38)).arrange(DOWN, buff=0.25).move_to(f)
        q = quatre(0.9, "perplexe"); q.move_to([0, -2.0, 0])
        self.at(S(49, 3) - 0.2, FadeOut(ls, shift=0.3 * UP), FadeIn(qt, shift=0.3 * UP), FadeIn(q, shift=0.2 * UP), rt=0.5)
        sb = sablier(0.8).move_to([5.0, -1.9, 0]); self.at(F_(49, 3) + 0.3, FadeIn(sb, scale=0.5), rt=0.3); self.son("grelot", 0.6)
        self.play(Rotate(sb, PI), run_time=1.0)
        cm = bas("Votre réponse en commentaire", 28, -2.95)
        self.at(S(49, 4) - 0.1, FadeOut(sb), FadeOut(q), FadeIn(cm, shift=0.15 * UP), rt=0.4)
        # 50 — la suite dans la description
        self.vider(S(50, 1) - 0.5, rt=0.4)
        ds = VGroup(T("Les deux décisions et les textes applicables", 32), T("sont dans la description", 32)).arrange(DOWN, buff=0.2).move_to([0, 0.6, 0]); fb = T("▼", 44).move_to([0, -1.2, 0])
        self.at(S(50, 1), FadeIn(ds, shift=0.2 * UP), FadeIn(fb, shift=0.3 * DOWN), rt=0.5)
        logo = T("L'étude du droit", 72).move_to([0, -0.1, 0])
        self.at(S(50, 2) - 0.2, FadeOut(ds), FadeOut(fb), FadeOut(self.filc), FadeIn(logo, scale=1.1), rt=0.5)
        self.fin()


class Fin(Sec25):
    """Écran de fin, muet, 15 s : ce qui est offert (script, fiche, licence), puis la place des éléments YouTube."""
    def construct(self):
        self.fond = Rectangle(width=17, height=10, stroke_width=0).set_fill(color=[ROUGE, ROUGE_2], opacity=1).set_sheen_direction(DOWN).move_to([0, -0.45, 0])
        self.add(self.fond); self.camera.frame.scale(1.1125).move_to([0, -0.45, 0])
        logo = T("L'étude du droit", 72).move_to([0, -0.1, 0]); self.add(logo)
        self.play(logo.animate.scale(0.5).move_to([0, 3.25, 0]), run_time=0.7)
        t = puce("Gratuit, pour aller plus loin", 30).move_to([0, 2.25, 0])

        def carte_(icone, a, b, c, x):
            f = RoundedRectangle(corner_radius=0.25, width=4.6, height=3.5, fill_color=ROUGE_3, fill_opacity=1, stroke_width=0).move_to([x, -0.35, 0])
            icone.move_to(f.get_center() + 0.85 * UP)
            tx = VGroup(T(a, 28), T(b, 20, CREME, False), T(c, 20, CREME, False)).arrange(DOWN, buff=0.14).move_to(f.get_center() + 0.8 * DOWN)
            return VGroup(f, icone, tx)
        cc = VGroup(RoundedRectangle(corner_radius=0.12, width=2.5, height=0.8, fill_color=CREME, fill_opacity=1, stroke_width=0), T("CC BY-SA 4.0", 26, ROUGE))
        c1 = carte_(dossier(1.5), "Le script complet", "et l'audit des sources,", "sur GitHub", -4.9)
        c2 = carte_(page("Fiche", ["Faits", "Réponse", "À retenir"], l=1.9, taille=13).scale(0.68), "La fiche du cours", "en PDF,", "sur letudedudroit.ch", 0)
        c3 = carte_(cc, "Un contenu libre", "à réutiliser en citant", "L'étude du droit", 4.9)
        liens = bandeau("Tous les liens sont dans la description", 24).move_to([0, -2.75, 0])
        self.play(FadeIn(t, shift=0.2 * DOWN), run_time=0.4)
        for c in (c1, c2, c3): self.play(FadeIn(c, shift=0.3 * UP), run_time=0.45); self.wait(0.75)
        self.play(FadeIn(liens, shift=0.15 * UP), run_time=0.4); self.wait(2.3)
        # place aux éléments de fin de YouTube (vidéo suivante, abonnement)
        ligne = T("Script · Fiche · Licence CC BY-SA 4.0 : liens dans la description", 22, CREME, False).move_to([0, -3.2, 0])
        cad = RoundedRectangle(corner_radius=0.25, width=6.4, height=3.6, color=CREME, stroke_width=5).move_to([-3.3, -0.2, 0]); suiv = puce("Vidéo suivante", 26).move_to(cad.get_top())
        rond = Circle(1.25, color=CREME, stroke_width=5).move_to([3.6, 0.2, 0]); ab = bandeau("S'abonner", 24).next_to(rond, DOWN, buff=0.3)
        self.play(*[FadeOut(x, shift=0.3 * DOWN) for x in (c1, c2, c3, liens, t)], run_time=0.4)
        self.play(Create(cad), FadeIn(suiv), Create(rond), FadeIn(ab), FadeIn(ligne), run_time=0.9)
        self.wait(15.0 - self.renderer.time)
