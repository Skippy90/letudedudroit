"""Prototype « niveau supérieur » — arrêt 12, lignes 1 à 4. Hors moteur, pour comparaison."""
import json, random
from pathlib import Path
import numpy as np
from manim import *

ROUGE = "#DA291C"; ROUGE_2 = "#B81F15"; ROUGE_3 = "#96170F"; ROUGE_4 = "#74110B"
CREME = "#FBF3E4"; ENCRE = "#3B0906"
config.background_color = ROUGE
D = json.loads((Path(__file__).resolve().parents[1] / "donnees" / "suisse.json").read_text())
ANNEES = {"VD": 1959, "NE": 1959, "GE": 1960, "BS": 1966, "BL": 1968, "TI": 1969, "VS": 1970, "LU": 1970, "ZH": 1970,
          "AG": 1971, "FR": 1971, "SH": 1971, "ZG": 1971, "GL": 1971, "SO": 1971, "BE": 1971, "JU": 1971, "TG": 1971,
          "SG": 1972, "UR": 1972, "SZ": 1972, "GR": 1972, "NW": 1972, "OW": 1972, "AR": 1989}


def T(s, taille=30, couleur=CREME, gras=True):
    return Text(s, font="Inter", weight=BOLD if gras else MEDIUM, font_size=taille, color=couleur)


def puce(s, taille=26):
    t = T(s, taille, ROUGE)
    f = RoundedRectangle(corner_radius=0.12, width=t.width + 0.45, height=t.height + 0.3, fill_color=CREME, fill_opacity=1, stroke_width=0)
    return VGroup(f, t)


def bandeau(s, taille=26):
    t = T(s, taille, CREME, False)
    f = RoundedRectangle(corner_radius=0.12, width=t.width + 0.45, height=t.height + 0.28, fill_color=ENCRE, fill_opacity=0.82, stroke_width=0)
    return VGroup(f, t)


def carte(largeur=8.6, centre=(0, 0)):
    cx, cy = centre
    P = lambda p: [cx + p[0] * largeur, cy + p[1] * largeur, 0]
    cantons = {}
    for s, c in D["cantons"].items():
        cantons[s] = VGroup(*[Polygon(*[P(p) for p in a], color=CREME, stroke_width=1.4, stroke_opacity=0.75,
                                      fill_color=CREME, fill_opacity=0) for a in c["anneaux"]])
    pays = VGroup(*[Polygon(*[P(p) for p in a], color=CREME, stroke_width=4.5) for a in D["pays"]])
    ombre = pays.copy().set_stroke(width=0).set_fill(ROUGE_3, 0.55).shift(0.09 * DOWN + 0.07 * RIGHT)
    g = VGroup(ombre, *cantons.values(), pays)
    g.cantons, g.pt = cantons, lambda s: np.array(P(D["cantons"][s]["centre"]))
    return g


def bonhomme(h=1.0, couleur=CREME, femme=False, chapeau=False, sabre=False, opacite=1.0):
    tete = Circle(radius=0.13 * h, fill_color=couleur, fill_opacity=opacite, stroke_width=0).move_to([0, 0.83 * h, 0])
    if femme:
        corps = Polygon([-0.13*h, 0.66*h, 0], [0.13*h, 0.66*h, 0], [0.27*h, 0.02*h, 0], [-0.27*h, 0.02*h, 0])
    else:
        corps = Polygon([-0.2*h, 0.66*h, 0], [0.2*h, 0.66*h, 0], [0.15*h, 0, 0], [-0.15*h, 0, 0])
    corps.set_fill(couleur, opacite).set_stroke(width=0).round_corners(0.04 * h)
    g = VGroup(corps, tete)
    if chapeau:
        g.add(Rectangle(width=0.36*h, height=0.035*h, fill_color=ENCRE, fill_opacity=opacite, stroke_width=0).move_to([0, 0.94*h, 0]),
              RoundedRectangle(corner_radius=0.03*h, width=0.2*h, height=0.12*h, fill_color=ENCRE, fill_opacity=opacite, stroke_width=0).move_to([0, 1.0*h, 0]))
    if sabre:
        s = VGroup(Line([0.17*h, 0.42*h, 0], [0.36*h, 0.04*h, 0], color=ENCRE, stroke_width=7 * h),
                   Line([0.12*h, 0.40*h, 0], [0.22*h, 0.45*h, 0], color=ENCRE, stroke_width=5 * h))
        g.add(s); g.sabre = s
    return g


def bras(b, h):
    c = b[1].get_center()
    return Line(c + [0.16*h, -0.2*h, 0], c + [0.26*h, 0.26*h, 0], color=CREME, stroke_width=6 * h).set_cap_style(CapStyleType.ROUND)


def montagnes(y, couleur, pics, seed):
    random.seed(seed)
    pts = [[-8, y, 0]]
    for x, h in pics:
        pts += [[x - 1.4 - random.random(), y + h * 0.35, 0], [x - 0.35, y + h * 0.9, 0], [x, y + h, 0], [x + 0.5, y + h * 0.8, 0], [x + 1.5 + random.random(), y + h * 0.3, 0]]
    pts += [[8, y, 0], [8, -5, 0], [-8, -5, 0]]
    return Polygon(*pts, fill_color=couleur, fill_opacity=1, stroke_width=0)


def maison(x, y, l=1.3, h=0.9, e=1.0):
    mur = Rectangle(width=l, height=h, fill_color=CREME, fill_opacity=1, stroke_width=0).move_to([x, y + h / 2, 0])
    toit = Polygon([x - l/2 - 0.12, y + h, 0], [x + l/2 + 0.12, y + h, 0], [x, y + h + 0.55 * e, 0], fill_color=ENCRE, fill_opacity=1, stroke_width=0)
    fen = VGroup(*[Square(0.13, fill_color=ROUGE_3, fill_opacity=1, stroke_width=0).move_to([x - l/2 + 0.22 + i * (l - 0.44) / 3, y + h * (0.3 + 0.38 * j), 0]) for i in range(4) for j in range(2)])
    return VGroup(mur, toit, fen)


class Proto(MovingCameraScene):
    def jusqua(self, t):
        from temps import M
        d = M(t) - self.renderer.time
        if d > 1 / 30: self.wait(d)

    def construct(self):
        fond = Rectangle(width=17, height=10, stroke_width=0).set_fill(color=[ROUGE, ROUGE_2], opacity=1).set_sheen_direction(DOWN).move_to([0, -0.45, 0])
        self.add(fond)
        self.camera.frame.scale(1.1125).move_to([0, -0.45, 0])
        # ——— Ligne 1.1 : la carte, puis le canton ———
        c = carte()
        date = puce("29 avril 1990").to_corner(UL, buff=0.6)
        self.play(LaggedStart(*[Create(k) for k in c.cantons.values()], lag_ratio=0.03), FadeIn(c[0]), Create(c[-1]), run_time=1.6)
        self.play(FadeIn(date, shift=0.3 * RIGHT), run_time=0.5)
        ai = c.cantons["AI"]
        nom = bandeau("Appenzell Rhodes-Intérieures", 26).move_to([3.9, 3.2, 0])
        trait = Line(nom.get_bottom() + 0.3 * LEFT, c.pt("AI"), color=CREME, stroke_width=2.5)
        self.jusqua(2.3)
        self.play(ai.animate.set_fill(CREME, 1), FadeIn(nom, shift=0.2 * UP), Create(trait), run_time=0.7)
        self.play(Indicate(ai, scale_factor=1.8, color=CREME), run_time=0.9)
        self.jusqua(4.6)
        self.play(self.camera.frame.animate.scale(0.16).move_to(c.pt("AI")), FadeOut(nom), FadeOut(trait), FadeOut(date), run_time=1.1, rate_func=rate_functions.ease_in_cubic)
        # ——— Ligne 1.2 : la place ———
        self.remove(c, *c, *c.cantons.values()); self.camera.frame.scale(1 / 0.16).move_to([0, -0.45, 0])
        m3 = montagnes(-0.2, ROUGE_4, [(-4.6, 2.6), (-1.2, 3.5), (2.4, 2.9), (5.6, 2.2)], 1)
        m2 = montagnes(-0.6, ROUGE_3, [(-5.8, 1.6), (-2.6, 2.0), (0.8, 1.7), (4.2, 2.1), (6.8, 1.4)], 2)
        neige = VGroup(*[Polygon([x - 0.3, 3.5 * 0.9 - 0.2 + dy, 0], [x, 3.5 - 0.2 + dy, 0], [x + 0.42, 3.5 * 0.8 - 0.2 + dy, 0], [x + 0.1, 2.95 + dy - 0.3, 0], fill_color=CREME, fill_opacity=0.9, stroke_width=0)
                         for x, dy in [(-1.2, 0)]])
        sol = Rectangle(width=16, height=4.2, fill_color=ROUGE_2, fill_opacity=1, stroke_width=0).move_to([0, -2.5, 0])
        maisons = VGroup(*[maison(x, -0.42, l, h, e) for x, l, h, e in [(-6.2, 1.5, 1.0, 1.0), (-4.5, 1.2, 0.8, 1.1), (-3.0, 1.4, 1.05, 0.9), (3.1, 1.3, 0.9, 1.0), (4.7, 1.5, 1.1, 1.0), (6.3, 1.2, 0.85, 1.1)]])
        eglise = VGroup(Rectangle(width=0.6, height=1.7, fill_color=CREME, fill_opacity=1, stroke_width=0).move_to([0.0, 0.43, 0]),
                        Polygon([-0.36, 1.28, 0], [0.36, 1.28, 0], [0, 2.2, 0], fill_color=ENCRE, fill_opacity=1, stroke_width=0),
                        Circle(0.12, fill_color=ROUGE_3, fill_opacity=1, stroke_width=0).move_to([0, 0.9, 0]))
        anneau = Ellipse(width=13.2, height=3.6, color=CREME, stroke_width=3, stroke_opacity=0.5).move_to([0, -2.2, 0])
        estrade = VGroup(Rectangle(width=2.6, height=0.32, fill_color=ENCRE, fill_opacity=1, stroke_width=0).move_to([0, -0.95, 0]),
                         *[bonhomme(0.62, CREME, chapeau=True).move_to([x, -0.45, 0]) for x in (-0.8, 0, 0.8)])
        random.seed(7)
        foule = VGroup(); rangs = [(-1.75, 0.74, 11), (-2.45, 0.92, 10), (-3.3, 1.12, 9)]
        for y, h, n in rangs:
            for i in range(n):
                x = (i - (n - 1) / 2) * (11.6 / n) + random.uniform(-0.12, 0.12)
                foule.add(bonhomme(h * random.uniform(0.93, 1.06), CREME, chapeau=random.random() < 0.35, sabre=False).move_to([x, y + random.uniform(-0.05, 0.05), 0]))
        decor = VGroup(m3, neige, m2, sol, maisons, eglise, anneau, estrade)
        self.play(FadeIn(m3, shift=0.6 * UP), FadeIn(neige, shift=0.6 * UP), FadeIn(m2, shift=0.35 * UP), FadeIn(sol), run_time=0.5)
        self.play(LaggedStart(*[GrowFromEdge(m, DOWN) for m in [*maisons, eglise]], lag_ratio=0.08), run_time=0.7)
        titre = puce("Landsgemeinde", 34).to_edge(UP, buff=0.45)
        self.play(FadeIn(anneau), FadeIn(estrade, shift=0.2 * UP), LaggedStart(*[FadeIn(b, shift=0.25 * UP) for b in foule], lag_ratio=0.02), FadeIn(titre, shift=0.2 * DOWN), run_time=1.5)
        sous = bandeau("L'assemblée des citoyens, sur la place").next_to(titre, DOWN, buff=0.15)
        self.jusqua(7.4); self.play(FadeIn(sous), run_time=0.5)
        # ——— Ligne 1.3 : les mains se lèvent ———
        self.jusqua(10.5)
        mains = VGroup(*[bras(b, b.height / 1.0) for b in foule])
        ordre = sorted(range(len(foule)), key=lambda i: foule[i].get_x() + random.uniform(-1.5, 1.5))
        sous2 = bandeau("On y décide à main levée").move_to(sous)
        self.play(LaggedStart(*[GrowFromPoint(mains[i], mains[i].get_start()) for i in ordre], lag_ratio=0.03), ReplacementTransform(sous, sous2), run_time=2.2)
        self.play(*[m.animate(rate_func=there_and_back).shift(0.06 * UP) for m in mains], run_time=0.8)
        self.jusqua(14.5)
        # ——— Ligne 2.1 : gros plan, le sabre ———
        self.play(FadeOut(mains), FadeOut(sous2), FadeOut(titre), FadeOut(foule), FadeOut(estrade), FadeOut(anneau),
                  m2.animate.shift(0.5 * DOWN), maisons.animate.set_opacity(0.35), eglise.animate.set_opacity(0.35), run_time=0.7)
        trio = VGroup(*[bonhomme(3.0, CREME, chapeau=True, sabre=True).move_to([x, -2.2, 0], aligned_edge=DOWN) for x in (-4.6, -2.5, -0.4)])
        for b in trio: b.shift(-b.get_bottom()[1] * UP + 3.4 * DOWN)
        self.play(LaggedStart(*[FadeIn(b, shift=0.5 * UP) for b in trio], lag_ratio=0.15), run_time=0.9)
        self.jusqua(17.6)
        halos = VGroup(*[Circle(0.62, color=CREME, stroke_width=5).move_to(b.sabre) for b in trio])
        etiq = puce("L'arme au côté", 30).move_to([3.6, 1.2, 0])
        etiq2 = bandeau("Elle atteste du droit de vote").next_to(etiq, DOWN, buff=0.2)
        fl = Arrow(etiq.get_left(), halos[2].get_right(), color=CREME, stroke_width=5, buff=0.15)
        self.play(LaggedStart(*[Create(h) for h in halos], lag_ratio=0.2), FadeIn(etiq, shift=0.2 * LEFT), GrowArrow(fl), run_time=1.0)
        self.play(FadeIn(etiq2), *[Wiggle(b.sabre, scale_value=1.15, rotation_angle=0.04 * TAU) for b in trio], run_time=1.0)
        # ——— Ligne 2.2 : les femmes derrière la corde ———
        self.jusqua(21.6)
        self.play(FadeOut(etiq), FadeOut(etiq2), FadeOut(fl), FadeOut(halos), run_time=0.4)
        femmes = VGroup(*[bonhomme(2.6, CREME, femme=True, opacite=0.38) for _ in range(3)])
        for b, x in zip(femmes, (2.6, 4.3, 6.0)): b.shift((x - b.get_x()) * RIGHT + (-3.4 - b.get_bottom()[1]) * UP)
        poteaux = VGroup(*[Rectangle(width=0.1, height=1.5, fill_color=ENCRE, fill_opacity=1, stroke_width=0).move_to([x, -2.75, 0]) for x in (1.5, 7.2)])
        corde = ArcBetweenPoints([1.5, -2.05, 0], [7.2, -2.05, 0], angle=0.5, color=ENCRE, stroke_width=7)
        e3 = puce("Seuls les hommes décident", 30).move_to([2.2, 2.3, 0])
        self.play(FadeIn(femmes, shift=0.3 * LEFT), FadeIn(poteaux), Create(corde), run_time=0.8)
        self.play(FadeIn(e3, shift=0.2 * DOWN), run_time=0.5)
        self.jusqua(24.5)
        # ——— Ligne 3 : la proposition, puis le vote ———
        self.play(*[FadeOut(m) for m in [trio, femmes, poteaux, corde, e3, maisons, eglise, m2, m3, neige, sol]], run_time=0.6)
        from suite import fil
        filc = fil(0); self.play(FadeIn(filc), run_time=0.3)
        feuille = RoundedRectangle(corner_radius=0.15, width=5.6, height=2.5, fill_color=CREME, fill_opacity=1, stroke_width=0).move_to([0, 1.6, 0])
        ombre = feuille.copy().set_fill(ROUGE_4, 0.6).shift(0.1 * DOWN + 0.1 * RIGHT)
        ft = VGroup(T("Proposition du gouvernement", 20, ROUGE_3, False), T("et du parlement", 20, ROUGE_3, False), T("Le droit de vote", 34, ENCRE), T("pour les femmes ?", 34, ENCRE)).arrange(DOWN, buff=0.14).move_to(feuille)
        self.play(FadeIn(ombre), FadeIn(feuille, shift=0.4 * DOWN), run_time=0.5); self.play(Write(ft), run_time=1.3)
        self.jusqua(29.6)
        pts = VGroup(*[Circle(0.13, fill_color=CREME, fill_opacity=0.35, stroke_width=0) for _ in range(100)]).arrange_in_grid(5, 20, buff=0.14).move_to([0, -1.5, 0])
        self.play(LaggedStart(*[FadeIn(p, scale=0.3) for p in pts], lag_ratio=0.006), run_time=0.8)
        non = [p for k, p in enumerate(pts) if k % 20 < 12]; oui = [p for k, p in enumerate(pts) if k % 20 >= 12]
        ln = T("Non", 34).next_to(VGroup(*non), DOWN, buff=0.3); lo = T("Oui", 34).next_to(VGroup(*oui), DOWN, buff=0.3)
        self.play(LaggedStart(*[p.animate.set_fill(ENCRE, 1) for p in non], lag_ratio=0.01), LaggedStart(*[p.animate.set_fill(CREME, 1) for p in oui], lag_ratio=0.01), FadeIn(ln), FadeIn(lo), run_time=1.2)
        rap = T("environ 6 contre 4", 26).next_to(pts, UP, buff=0.25)
        self.play(FadeIn(rap), run_time=0.4)
        tampon = VGroup(RoundedRectangle(corner_radius=0.1, width=3.9, height=1.2, color=ROUGE, stroke_width=9, fill_color=CREME, fill_opacity=0.9), T("REFUSÉ", 60, ROUGE)).rotate(-0.16).move_to(feuille.get_center() + 0.9 * RIGHT + 0.45 * DOWN)
        self.jusqua(32.3)
        self.play(FadeIn(tampon, scale=2.4), ft.animate.set_opacity(0.45), run_time=0.25, rate_func=rate_functions.ease_in_quad)
        self.play(feuille.animate(rate_func=there_and_back).shift(0.07 * DOWN), ft.animate(rate_func=there_and_back).shift(0.07 * DOWN), run_time=0.2)
        self.jusqua(34.7)
        # ——— Ligne 4 : la carte se remplit, année après année ———
        self.play(*[FadeOut(m) for m in [feuille, ombre, ft, tampon, pts, ln, lo, rap]], run_time=0.5)
        c = carte(7.2, (-1.9, 0.75))
        self.play(FadeIn(c), run_time=0.5)
        axe = Line([-6, -2.6, 0], [6, -2.6, 0], color=CREME, stroke_width=4)
        X = lambda a: -6 + 12 * (a - 1957) / (1991 - 1957)
        reperes = VGroup(*[VGroup(Line([X(a), -2.5, 0], [X(a), -2.7, 0], color=CREME, stroke_width=3), T(str(a), 18, CREME, False).move_to([X(a), -3.0, 0])) for a in (1959, 1971, 1981, 1990)])
        an = ValueTracker(1957)
        curseur = always_redraw(lambda: Triangle(fill_color=CREME, fill_opacity=1, stroke_width=0).scale(0.14).rotate(PI).move_to([X(an.get_value()), -2.35, 0]))
        annee = always_redraw(lambda: T(str(int(an.get_value())), 64).move_to([4.6, 1.9, 0]))
        nb = always_redraw(lambda: T(f"{sum(1 for s, v in ANNEES.items() if v <= an.get_value() and s != 'JU') + (1 if an.get_value() >= 1979 else 0)} cantons", 26, CREME, False).move_to([4.6, 1.05, 0]))
        self.play(Create(axe), FadeIn(reperes), run_time=0.5); self.add(curseur)
        fed = VGroup(puce("1971", 30), T("Les Suissesses votent\nau niveau fédéral", 26)).arrange(DOWN, buff=0.2).move_to([4.6, 1.5, 0])
        self.play(an.animate.set_value(1971), FadeIn(fed), run_time=1.0)
        self.play(Indicate(fed[0], color=CREME, scale_factor=1.15), run_time=0.8)
        self.jusqua(40.2)
        self.play(FadeOut(fed), an.animate.set_value(1958.5), run_time=0.4); self.add(annee, nb)
        rempli = set()

        def maj(m):
            for s, a in ANNEES.items():
                if a <= an.get_value() and s not in rempli:
                    rempli.add(s); c.cantons[s].set_fill(CREME, 0.95)
        c.add_updater(maj)
        self.play(an.animate.set_value(1989.4), run_time=3.6, rate_func=rate_functions.ease_in_out_sine)
        c.remove_updater(maj)
        # ——— Ligne 4.3 : le dernier ———
        self.jusqua(44.6)
        ai = c.cantons["AI"]; self.remove(annee, nb)
        a2 = T("1990", 64).move_to([4.6, 1.9, 0]); n2 = T("25 cantons sur 26", 26, CREME, False).move_to([4.6, 1.05, 0]); self.add(a2, n2)
        cible = c.pt("AI") + 1.5 * RIGHT + 0.2 * UP
        self.add(ai)
        self.play(an.animate.set_value(1990), ai.animate.set_fill(ENCRE, 1).set_stroke(ENCRE, 3, 1), run_time=0.5)
        cam = self.camera.frame
        bande = Rectangle(width=1, height=1, fill_color=ROUGE_2, fill_opacity=1, stroke_width=0)
        bande.add_updater(lambda m: m.stretch_to_fit_width(cam.width).stretch_to_fit_height(cam.height * 0.105).move_to(cam.get_bottom() + UP * cam.height * 0.0525))
        self.add(bande)
        self.play(self.camera.frame.animate.scale(0.5).move_to(cible), a2.animate.scale(0.5).move_to(cible + [2.2, 1.2, 0]), n2.animate.scale(0.5).move_to(cible + [2.2, 0.75, 0]), FadeOut(axe), FadeOut(reperes), FadeOut(curseur), FadeOut(filc), run_time=1.2)
        der = puce("Le dernier", 15).next_to(c.pt("AI"), RIGHT, buff=0.75)
        tr = Line(der.get_left(), c.pt("AI") + 0.12 * RIGHT, color=ENCRE, stroke_width=2.5)
        self.play(FadeIn(der, shift=0.1 * LEFT), Create(tr), run_time=0.5)
        self.play(Indicate(ai, color=ENCRE, scale_factor=1.6), run_time=0.9)
        self.jusqua(49.4)
