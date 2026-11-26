from base import *


class Ff(Sec25):
    L0, L1 = 39, 46

    def construct(self):
        self.debut(4); self.chapitre(4, "À retenir", 5)
        # 39.1 — le piège : « interdit parce qu'il risquait de se blesser »
        pg = VGroup(RoundedRectangle(corner_radius=0.12, width=2.4, height=0.7, fill_color=ROUGE, fill_opacity=1, stroke_width=0), T("Le piège", 28)).move_to([-5.0, 2.45, 0])
        self.at(S(39, 1), FadeIn(pg, scale=1.3), rt=0.4); self.son("thud", 0.5)
        pa = participant(1.5, "neutre").move_to([-2.4, -1.0, 0]); cq = casque(1.0).move_to(pa[1].get_top() + 0.3 * UP)
        bu = bulle_pensee("Il risquait de se blesser", 22).move_to([2.2, 0.9, 0])
        self.at(W(39, 1, "maire") - 0.3, FadeIn(pa, shift=0.2 * UP), FadeIn(cq), rt=0.4)
        self.at(W(39, 1, "risquaient") - 0.4, FadeIn(bu, scale=0.5), rt=0.4); self.son("plop")
        # 39.2 — or le fondement décisif est différent
        x_ = coche(False, 0.55).move_to(bu.get_corner(UR) + 0.1 * UR)
        self.at(W(39, 2, "fondement") - 0.3, FadeIn(x_, scale=2), bu.animate.set_opacity(0.45), rt=0.35); self.son("thud", 0.6)
        df = bandeau("Le fondement décisif est différent", 24).move_to([2.2, -0.6, 0])
        self.at(W(39, 2, "différent") - 0.4, FadeIn(df, shift=0.1 * UP), rt=0.35)
        # 40 — la vraie raison : l'atteinte à la dignité, même avec protections et consentement
        self.vider(S(40, 1) - 0.4, rt=0.35)
        ba = VGroup(RoundedRectangle(corner_radius=0.14, width=6.4, height=1.0, fill_color=AMBRE, fill_opacity=1, stroke_width=0), T("L'atteinte à la dignité humaine", 30, ENCRE)).move_to([0, 1.9, 0])
        ok = coche(True, 0.45).next_to(ba, LEFT, buff=0.25)
        self.at(S(40, 1), FadeIn(ba, scale=1.2), rt=0.4)
        self.at(W(40, 1, "atteinte") - 0.3, FadeIn(ok, scale=2), Indicate(ba, color=AMBRE, scale_factor=1.05), rt=0.4); self.son("ding", 0.6)
        m1 = VGroup(VGroup(casque(1.1), tapis(1.6)).arrange(DOWN, buff=0.08), T("Même avec des mesures de sécurité", 22)).arrange(DOWN, buff=0.25).move_to([-3.4, -0.75, 0])
        m2 = VGroup(contrat(1.0), T("Même avec son consentement", 22)).arrange(DOWN, buff=0.25).move_to([3.4, -0.75, 0])
        self.at(W(40, 1, "mesures") - 0.4, FadeIn(m1, shift=0.2 * UP), rt=0.4); self.son("plop")
        self.at(W(40, 1, "consentant") - 0.4, FadeIn(m2, shift=0.2 * UP), rt=0.4); self.son("plop")
        # 41 — la règle : sécurité, tranquillité… et dignité
        self.vider(S(41, 1) - 0.4, rt=0.35)
        rg = puce("La règle", 34).move_to([0, 2.55, 0])
        self.at(S(41, 1), FadeIn(rg, scale=1.3), rt=0.4); self.son("ding", 0.5)
        op = ordre_public(1.05, ("Sécurité", "Tranquillité")).move_to([-2.6, 0.0, 0])
        self.at(W(41, 1, "ordre") - 0.3, FadeIn(op, shift=0.2 * UP), rt=0.45)
        nr = bandeau("Ne se réduit pas au matériel", 20).next_to(op, DOWN, buff=0.2)
        self.at(W(41, 1, "matérielles") - 0.4, FadeIn(nr, shift=0.1 * UP), rt=0.35)
        td = tuile_dignite(1.1).next_to(op, RIGHT, buff=0.9); plus = T("+", 60).move_to((op.get_right() + td.get_left()) / 2)
        self.at(W(41, 2, "comprend") - 0.3, FadeIn(plus), FadeIn(td, shift=0.3 * LEFT), rt=0.4); self.son("ding", 0.6)
        self.at(W(41, 2, "dignité") - 0.3, Indicate(td, color=AMBRE, scale_factor=1.1), rt=0.5)
        # 42.1 — le dilemme protection / autonomie dépasse Morsang-sur-Orge
        self.vider(S(42, 1) - 0.4, rt=0.35)
        bal = balance(1.25, VGroup(parapluie(0.6)), VGroup(participant(0.85, "decide"))).move_to([-2.6, -0.4, 0])
        lb = VGroup(T("Protection", 22).next_to(bal.pg, DOWN, buff=0.25), T("Autonomie", 22).next_to(bal.pd, DOWN, buff=0.25))
        self.at(W(42, 1, "protection") - 0.3, FadeIn(bal, shift=0.2 * UP), FadeIn(lb), rt=0.45); self.son("plop")
        self.at(W(42, 1, "autonomie") - 0.2, Wiggle(bal, scale_value=1.02, rotation_angle=0.02 * TAU), rt=0.6)
        # 42.2 — les grands arrêts révèlent les choix fondamentaux d'un ordre juridique
        lv = livres(1.5).move_to([3.8, 0.4, 0]); ch = bandeau("Les choix fondamentaux", 22).next_to(lv, DOWN, buff=0.25)
        self.at(W(42, 2, "grands") - 0.3, FadeIn(lv, shift=0.2 * UP), rt=0.4)
        lum = VGroup(*[Line(lv.get_top() + 0.1 * UP, lv.get_top() + 0.1 * UP + 0.7 * np.array([np.cos(a), np.sin(a), 0]), color=AMBRE, stroke_width=5) for a in np.linspace(0.4, PI - 0.4, 5)])
        self.at(W(42, 2, "révèlent") - 0.3, Create(lum), FadeIn(ch), rt=0.45); self.son("ding", 0.5)
        # 43 — la question finale
        self.vider(S(43, 1) - 0.4, rt=0.35)
        q1 = bandeau("Le consentement doit-il toujours empêcher l'État d'interdire ?", 24).move_to([0, 2.45, 0])
        pa = participant(1.5, "perplexe").move_to([-3.2, -0.9, 0]); ct = contrat(0.9).move_to(main_de(pa, 1) + [0.55, 0.3, 0])
        mr = maire(1.7, "perplexe").move_to([3.4, -0.85, 0]); pp = parapluie(0.95, AMBRE, "?").move_to([0.2, 0.6, 0])
        self.at(S(43, 1), FadeIn(q1, shift=0.1 * DOWN), FadeIn(pa, shift=0.2 * UP), FadeIn(ct), rt=0.45); self.son("ding", 0.5)
        self.at(W(43, 1, "interdire") - 0.3, FadeIn(mr, shift=0.2 * LEFT), FadeIn(pp, shift=0.2 * DOWN), rt=0.4)
        q2 = bandeau("Et quel est le motif précis retenu ?", 24).move_to([0, -2.6, 0])
        self.at(S(43, 2) - 0.05, FadeIn(q2, shift=0.1 * UP), rt=0.4); self.son("plop")
        self.at(W(43, 2, "motif") - 0.3, Indicate(q2, color=CREME, scale_factor=1.05), rt=0.5)
        # 44.1 — en commentaire : votre appréciation / la règle posée par le juge
        self.vider(S(44, 1) - 0.4, rt=0.35)
        vA = VGroup(bulle(["À mon avis…"], 24), T("Votre appréciation", 24)).arrange(DOWN, buff=0.3).move_to([-3.4, 0.4, 0])
        vB = VGroup(page("La règle du juge", ["La dignité fait partie", "de l'ordre public"], l=4.6, taille=20), T("La règle posée par le juge", 24)).arrange(DOWN, buff=0.3).move_to([3.4, 0.4, 0])
        cm = bandeau("Dans les commentaires", 22).move_to([0, 2.55, 0])
        self.at(W(44, 1, "commentaires") - 0.4, FadeIn(cm, shift=0.1 * DOWN), rt=0.35)
        self.at(W(44, 1, "appréciation") - 0.4, FadeIn(vA, shift=0.2 * UP), rt=0.4); self.son("plop")
        self.at(W(44, 1, "règle") - 0.4, FadeIn(vB, shift=0.2 * UP), rt=0.4); self.son("plop")
        # 44.2 — décision intégrale et références dans la description
        self.vider(S(44, 2) - 0.35, rt=0.35)
        ds = VGroup(dossier(1.4), T("La décision intégrale", 24), T("et les références : dans la description", 22, CREME, False)).arrange(DOWN, buff=0.22).move_to([0, 0.2, 0])
        self.at(S(44, 2), FadeIn(ds, shift=0.2 * UP), rt=0.45); self.son("plop")
        # 45 — c'était l'arrêt Commune de Morsang-sur-Orge ; à bientôt
        self.vider(S(45, 1) - 0.4, rt=0.35)
        ref = puce("Commune de Morsang-sur-Orge", 40).move_to([0, 1.4, 0]); dt = bandeau("Conseil d'État · 27 octobre 1995", 24).next_to(ref, DOWN, buff=0.25)
        self.at(S(45, 1), FadeIn(ref, scale=1.2), rt=0.45); self.son("ding", 0.5)
        cal = date_fr("27 octobre", "1995").scale(0.8).move_to([-5.7, -1.25, 0]); ce45 = conseil_etat(0.62, nom=False).move_to([5.5, -1.1, 0])
        self.at(W(45, 1, "Morsang") - 0.2, FadeIn(ce45, shift=0.2 * LEFT), rt=0.4)
        self.at(W(45, 1, "vingt") - 0.3, FadeIn(dt, shift=0.1 * UP), FadeIn(cal, shift=0.2 * DOWN), rt=0.4)
        logo = T("L'étude du droit", 64).move_to([0, -1.3, 0])
        self.at(S(45, 2) - 0.05, FadeIn(logo, scale=0.8), rt=0.45); self.son("joie")
        self.fin()


class Fin(Sec25):
    """Écran de fin, muet, 15 s : ce qui est offert (script, fiche, licence), puis la place des éléments YouTube."""
    def construct(self):
        self.fond = Rectangle(width=17, height=10, stroke_width=0).set_fill(color=[BLEU, BLEU_2], opacity=1).set_sheen_direction(DOWN).move_to([0, -0.45, 0])
        self.add(self.fond); self.camera.frame.scale(1.1125).move_to([0, -0.45, 0])
        logo = T("L'étude du droit", 72).move_to([0, -0.1, 0]); self.add(logo)
        self.play(logo.animate.scale(0.5).move_to([0, 3.25, 0]), run_time=0.7)
        t = puce("Gratuit, pour aller plus loin", 30).move_to([0, 2.25, 0])

        def carte_(icone, a, b, c, x):
            f = RoundedRectangle(corner_radius=0.25, width=4.6, height=3.5, fill_color=BLEU_3, fill_opacity=1, stroke_width=0).move_to([x, -0.35, 0])
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
        ligne = T("Script · Fiche · Licence CC BY-SA 4.0 : liens dans la description", 22, CREME, False).move_to([0, -3.2, 0])
        cad = RoundedRectangle(corner_radius=0.25, width=6.4, height=3.6, color=CREME, stroke_width=5).move_to([-3.3, -0.2, 0]); suiv = puce("Vidéo suivante", 26).move_to(cad.get_top())
        rond = Circle(1.25, color=CREME, stroke_width=5).move_to([3.6, 0.2, 0]); ab = bandeau("S'abonner", 24).next_to(rond, DOWN, buff=0.3)
        self.play(*[FadeOut(x, shift=0.3 * DOWN) for x in (c1, c2, c3, liens, t)], run_time=0.4)
        self.play(Create(cad), FadeIn(suiv), Create(rond), FadeIn(ab), FadeIn(ligne), run_time=0.9)
        self.wait(15.0 - self.renderer.time)
