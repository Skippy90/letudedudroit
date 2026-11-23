from base import *


class Ef(Sec15):
    L0, L1 = 37, 46

    def construct(self):
        self.debut(3); self.chapitre(4, "À retenir", 5)
        # 37 — l'arrêt voisin : Zurich
        cal = calendrier("9 JUIL.", "2003").scale(0.85).move_to([-5.9, 2.5, 0])
        a1 = VGroup(puce("ATF 129 I 217", 30), bandeau("Emmen", 24)).arrange(DOWN, buff=0.2).move_to([-2.9, 1.3, 0])
        a2 = VGroup(puce("ATF 129 I 232", 30), bandeau("Ville de Zurich", 24)).arrange(DOWN, buff=0.2).move_to([2.9, 1.3, 0])
        self.at(S(37, 1) - 0.3, FadeIn(cal, shift=0.3 * DOWN), FadeIn(a1, shift=0.2 * UP), rt=0.5)
        self.at(W(37, 1, "autre") - 0.2, FadeIn(a2, shift=0.3 * LEFT), rt=0.5)
        ini = VGroup(RoundedRectangle(corner_radius=0.15, width=6.0, height=1.3, fill_color=ROUGE_3, fill_opacity=1, stroke_width=0), VGroup(T("Initiative : soumettre", 22), T("les naturalisations au vote aux urnes", 22)).arrange(DOWN, buff=0.1)).move_to([2.9, -0.8, 0])
        self.at(W(37, 2, "initiative") - 0.4, a1.animate.set_opacity(0.45), FadeIn(ini, shift=0.2 * UP), rt=0.5)
        inv = tampon("INVALIDE", 26).move_to(ini.get_corner(UR) + 0.3 * LEFT)
        self.at(W(37, 2, "confirme") - 0.1, FadeIn(inv, scale=2.2), rt=0.3)
        mm = bas("Là encore : impossible de motiver un refus", 26, -2.85); self.at(S(37, 3), a1.animate.set_opacity(1), FadeIn(mm, shift=0.15 * UP), rt=0.5)
        # 38 — le principe
        self.vider(S(38, 1) - 0.5, rt=0.4)
        t = titre("Le principe"); self.at(S(38, 1), FadeIn(t, shift=0.2 * DOWN), rt=0.4)
        u = urne(1.3).move_to([-3.9, -1.1, 0]); vg = votants(3, 1.15).next_to(u, LEFT, buff=0.35).align_to(u, DOWN); vd = votants(3, 1.15).next_to(u, RIGHT, buff=0.35).align_to(u, DOWN)
        pe = visage(bonhomme(1.5), 1.5).move_to([-3.9, 1.3, 0]); fl = Arrow(u.get_top() + 0.15 * UP, pe.get_bottom() + 0.1 * DOWN, color=CREME, stroke_width=6, buff=0)
        self.at(S(38, 2), FadeIn(u), FadeIn(vg), FadeIn(vd), rt=0.5); self.at(W(38, 2, "situation") - 0.3, FadeIn(pe, shift=0.2 * DOWN), GrowArrow(fl), rt=0.5)
        eq = T("=", 70).move_to([0.1, -0.4, 0]); au = VGroup(maison(0, 0, 2.6, 1.4, 1.1), puce("Une autorité", 26)).arrange(DOWN, buff=0.25).move_to([3.6, -0.3, 0])
        self.at(W(38, 2, "exerce") - 0.3, FadeIn(eq, scale=1.5), FadeIn(au, shift=0.3 * LEFT), rt=0.5)
        ga = bas("Mêmes garanties fondamentales que les autres autorités", 26, -2.95); self.at(W(38, 3, "mêmes") - 0.3, FadeIn(ga, shift=0.15 * UP), rt=0.5)
        # 39 — et aujourd'hui ? art. 15 LN
        self.vider(S(39, 1) - 0.5, rt=0.4)
        t = titre("Et aujourd'hui ?", 34); self.at(S(39, 1) - 0.1, FadeIn(t, scale=1.3), rt=0.4)
        ln = livre("Loi sur la", "nationalité", "LN").move_to([-5.4, -0.4, 0]); self.at(S(39, 2), FadeIn(ln, shift=0.4 * RIGHT), rt=0.5)
        p15 = page("Art. 15 al. 2 LN", ["[Le droit cantonal] peut prévoir", "qu'une demande de naturalisation", "soit soumise au vote", "de l'assemblée communale."], taille=24).move_to([1.2, 0.3, 0])
        self.at(S(39, 3), FadeIn(p15, shift=0.4 * UP), rt=0.5)
        k = cadre_autour(VGroup(p15.corps[2], p15.corps[3]), 0.08); self.at(W(39, 3, "soumise") - 0.3, Create(k), rt=0.5)
        ok = VGroup(coche(True, 0.34), T("Le vote reste possible", 26)).arrange(RIGHT, buff=0.25).move_to([1.2, -2.3, 0]); self.play(FadeIn(ok, scale=1.2), run_time=0.4)
        # 40 — art. 16 LN
        self.jusqua(S(40, 1) - 0.5)
        self.play(FadeOut(t, shift=0.7 * LEFT), FadeOut(k), FadeOut(ok, shift=0.7 * LEFT), FadeOut(p15, shift=0.7 * LEFT), run_time=0.4)
        p16 = page("Art. 16 al. 1 LN", ["Tout rejet d'une demande", "de naturalisation", "doit être motivé."], taille=28).move_to([1.2, 0.9, 0])
        t = titre("Mais tout refus doit être motivé"); self.at(S(40, 1), FadeIn(t, shift=0.2 * DOWN), FadeIn(p16, shift=0.4 * UP), rt=0.5)
        al2 = VGroup(bandeau("Art. 16 al. 2 LN", 20), T("Rejet seulement sur proposition de rejet motivée", 24)).arrange(DOWN, buff=0.18).move_to([1.2, -1.7, 0])
        self.at(S(40, 2) + 0.3, FadeIn(al2, shift=0.2 * UP), rt=0.5)
        dv = bas("Participer : oui. Refuser sans justification : non.", 26, -2.95); self.at(S(40, 3) + 0.3, FadeIn(dv, shift=0.15 * UP), rt=0.5)
        # 41 — l'erreur à éviter
        self.vider(S(41, 1) - 0.5, rt=0.4)
        t = titre("L'erreur à éviter"); b = visage(bonhomme(2.4), 2.4, "content").move_to([-4.6, -1.1, 0])
        self.at(S(41, 1), FadeIn(t, shift=0.2 * DOWN), FadeIn(b, shift=0.3 * UP), rt=0.5)
        bu = bulle(["Le peuple est souverain :", "sa décision n'a jamais", "à être justifiée"], 28).next_to(b, RIGHT, buff=0.6).shift(0.9 * UP)
        self.at(S(41, 2), FadeIn(bu, shift=0.2 * LEFT), rt=0.5)
        # 42 — pourquoi c'est faux
        faux = tampon("FAUX", 50).move_to(bu.get_corner(UR) + 0.5 * UP + 0.4 * RIGHT)
        self.at(S(42, 1), FadeIn(faux, scale=2.4), rt=0.3); visage(b, 2.4, "surpris"); self.son("thud", 0.6)
        self.pop("Spoiler : non.", [0.6, -2.3, 0], 2.6)
        self.vider(S(42, 2) - 0.5, garder=[t], rt=0.4)
        d = VGroup(RoundedRectangle(corner_radius=0.15, width=4.4, height=1.6, fill_color=CREME, fill_opacity=1, stroke_width=0), VGroup(T("Décision sur les droits", 24, ENCRE), T("d'une personne", 24, ENCRE)).arrange(DOWN, buff=0.1)).move_to([-3.8, -0.3, 0])
        cad = RoundedRectangle(corner_radius=0.3, width=12.6, height=3.4, color=CREME, stroke_width=8).move_to([0, -0.3, 0]); og = puce("Constitution fédérale", 26).move_to(cad.get_top())
        self.at(S(42, 2), FadeIn(d, shift=0.2 * UP), rt=0.5); self.at(W(42, 2, "reste") - 0.3, Create(cad), FadeIn(og), rt=0.8)
        m1 = VGroup(coche(False, 0.3), T("Écarter les garanties fondamentales", 22)).arrange(RIGHT, buff=0.2); m2 = VGroup(coche(False, 0.3), T("Rendre licite une discrimination", 22)).arrange(RIGHT, buff=0.2)
        ms = VGroup(m1, m2).arrange(DOWN, buff=0.35, aligned_edge=LEFT).move_to([2.8, -0.75, 0]); mt = bandeau("La majorité ne peut pas :", 22).next_to(ms, UP, buff=0.3).align_to(ms, LEFT)
        self.at(S(42, 3), FadeIn(mt), rt=0.3); self.at(W(42, 3, "écarter") - 0.2, FadeIn(m1, shift=0.2 * LEFT), rt=0.4); self.at(W(42, 3, "transformer") - 0.2, FadeIn(m2, shift=0.2 * LEFT), rt=0.4)
        # 43 — l'essentiel
        self.vider(S(43, 1) - 0.5, rt=0.4)
        t = titre("L'essentiel", 36); self.at(S(43, 1) - 0.1, FadeIn(t, scale=1.3), rt=0.4)
        def pt(n, a, b, y):
            c = VGroup(Circle(0.38, fill_color=CREME, fill_opacity=1, stroke_width=0), T(str(n), 30, ROUGE)).move_to([-5.2, y, 0])
            tx = VGroup(T(a, 28), T(b, 21, CREME, False)).arrange(DOWN, buff=0.1, aligned_edge=LEFT).next_to(c, RIGHT, buff=0.4)
            return VGroup(c, tx)
        e1 = pt(1, "Voter sur une naturalisation : une tâche de l'État", "art. 35 al. 2 Cst.", 1.7)
        e2 = pt(2, "Pas de discrimination", "art. 8 al. 2 Cst.", 0.35); e3 = pt(3, "Pas de refus sans motifs", "art. 29 al. 2 Cst. · aujourd'hui art. 16 LN", -1.0)
        self.at(S(43, 2), FadeIn(e1, shift=0.3 * LEFT), rt=0.5); self.at(W(43, 3, "interdiction") - 0.3, FadeIn(e2, shift=0.3 * LEFT), rt=0.5); self.at(W(43, 3, "obligation") - 0.3, FadeIn(e3, shift=0.3 * LEFT), rt=0.5)
        ed = puce("La volonté populaire s'exerce dans l'État de droit", 26).move_to([0, -2.6, 0]); self.at(S(43, 4), FadeIn(ed, scale=1.15), rt=0.5)
        # 44 — la question
        self.vider(S(44, 1) - 0.5, rt=0.4)
        t = titre("À vous", 34); self.at(S(44, 1) - 0.1, FadeIn(t, scale=1.3), rt=0.4)
        f = RoundedRectangle(corner_radius=0.3, width=11.4, height=3.6, fill_color=ROUGE_3, fill_opacity=1, stroke_width=0).move_to([0, -0.1, 0])
        qt = VGroup(T("Pourquoi le Tribunal fédéral", 34), T("s'est-il appuyé sur des indices,", 34), T("plutôt que sur une preuve directe ?", 34)).arrange(DOWN, buff=0.22).move_to(f)
        lp = loupe(1.0).move_to(f.get_corner(UL) + 0.2 * RIGHT)
        self.at(S(44, 2) - 0.1, FadeIn(f), FadeIn(lp, scale=0.5), FadeIn(qt[0], shift=0.15 * UP), rt=0.5)
        self.at(W(44, 2, "appuyé") - 0.3, FadeIn(qt[1], shift=0.15 * UP), rt=0.4); self.at(W(44, 2, "plutôt") - 0.2, FadeIn(qt[2], shift=0.15 * UP), rt=0.4)
        cm = bas("Votre réponse en commentaire", 28, -2.7); self.at(S(44, 3) - 0.1, FadeIn(cm, shift=0.15 * UP), rt=0.4)
        # 45 — la suite dans la description
        self.vider(S(45, 1) - 0.5, rt=0.4)
        ds = VGroup(T("La solution et la référence de l'arrêt", 32), T("sont dans la description", 32)).arrange(DOWN, buff=0.2).move_to([0, 0.6, 0]); fb = T("▼", 44).move_to([0, -1.2, 0])
        self.at(S(45, 1), FadeIn(ds, shift=0.2 * UP), FadeIn(fb, shift=0.3 * DOWN), rt=0.5)
        logo = T("L'étude du droit", 72).move_to([0, -0.1, 0])
        self.at(S(45, 2) - 0.2, FadeOut(ds), FadeOut(fb), FadeOut(self.filc), FadeIn(logo, scale=1.1), rt=0.5)
        self.fin()


class Fin(Sec15):
    """Écran de fin : 10,9 s après la narration."""
    def construct(self):
        self.fond = Rectangle(width=17, height=10, stroke_width=0).set_fill(color=[ROUGE, ROUGE_2], opacity=1).set_sheen_direction(DOWN).move_to([0, -0.45, 0])
        self.add(self.fond); self.camera.frame.scale(1.1125).move_to([0, -0.45, 0])
        logo = T("L'étude du droit", 72).move_to([0, -0.1, 0]); self.add(logo)
        self.play(logo.animate.scale(0.55).move_to([0, 3.1, 0]), run_time=0.8)
        cad = RoundedRectangle(corner_radius=0.25, width=6.4, height=3.6, color=CREME, stroke_width=5).move_to([-3.3, -0.2, 0])
        suiv = puce("Vidéo suivante", 26).move_to(cad.get_top())
        rond = Circle(1.25, color=CREME, stroke_width=5).move_to([3.6, 0.2, 0]); ab = bandeau("S'abonner", 24).next_to(rond, DOWN, buff=0.3)
        src = T("Script, sources et arrêt : dans la description", 22, CREME, False).move_to([0, -3.2, 0])
        self.play(Create(cad), FadeIn(suiv), Create(rond), FadeIn(ab), FadeIn(src), run_time=1.0)
        self.wait(10.9 - 0.8 - 1.0)
