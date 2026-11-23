"""Briques communes aux sections de l'arrêt 12 (nouveau style)."""
from suite import *


def page(titre, lignes, l=5.4, taille=26):
    corps = VGroup(*[T(x, taille, ENCRE, True) for x in lignes]).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
    h = corps.height + 1.25
    l = max(l, corps.width + 0.8)
    f = RoundedRectangle(corner_radius=0.14, width=l, height=h, fill_color=CREME, fill_opacity=1, stroke_width=0)
    ombre = f.copy().set_fill(ROUGE_4, 0.6).shift(0.1 * DOWN + 0.1 * RIGHT)
    tete = Rectangle(width=l, height=0.55, fill_color=ENCRE, fill_opacity=1, stroke_width=0).align_to(f, UP)
    tt = T(titre, 22).move_to(tete)
    corps.move_to(f.get_center() + 0.27 * DOWN).align_to(f, LEFT).shift(0.35 * RIGHT)
    g = VGroup(ombre, f, tete, tt, corps); g.corps = corps
    return g


def livre(l1, l2, gros=None):
    f = RoundedRectangle(corner_radius=0.12, width=2.5, height=3.2, fill_color=ENCRE, fill_opacity=1, stroke_width=0)
    ombre = f.copy().set_fill(ROUGE_4, 0.6).shift(0.1 * DOWN + 0.1 * RIGHT)
    dos = Rectangle(width=0.18, height=3.2, fill_color=ROUGE_4, fill_opacity=1, stroke_width=0).align_to(f, LEFT).shift(0.18 * RIGHT)
    cadre = RoundedRectangle(corner_radius=0.08, width=1.9, height=2.7, color=CREME, stroke_width=2, stroke_opacity=0.6).move_to(f.get_center() + 0.15 * RIGHT)
    t = VGroup(T(l1, 20), T(l2, 20)).arrange(DOWN, buff=0.1).move_to(cadre.get_center() + 0.75 * UP)
    g = VGroup(ombre, f, dos, cadre, t)
    if gros:
        g.add(T(gros, 44).move_to(cadre.get_center() + 0.5 * DOWN))
    return g


def balance(e=1.0):
    pied = VGroup(Rectangle(width=0.14 * e, height=1.9 * e, fill_color=CREME, fill_opacity=1, stroke_width=0),
                  Rectangle(width=1.1 * e, height=0.14 * e, fill_color=CREME, fill_opacity=1, stroke_width=0).shift(0.95 * e * DOWN))
    fleau = Rectangle(width=3.4 * e, height=0.12 * e, fill_color=CREME, fill_opacity=1, stroke_width=0).shift(0.9 * e * UP)
    plats = VGroup()
    for s in (-1, 1):
        x = s * 1.6 * e
        plats.add(VGroup(Line([x, 0.9 * e, 0], [x - 0.5 * e, 0.1 * e, 0], color=CREME, stroke_width=3 * e), Line([x, 0.9 * e, 0], [x + 0.5 * e, 0.1 * e, 0], color=CREME, stroke_width=3 * e),
                         Rectangle(width=1.2 * e, height=0.1 * e, fill_color=CREME, fill_opacity=1, stroke_width=0).move_to([x, 0.08 * e, 0])))
    g = VGroup(pied, fleau, plats); g.fleau, g.plats, g.e = fleau, plats, e
    return g


def urne(e=1.0):
    b = RoundedRectangle(corner_radius=0.08 * e, width=1.3 * e, height=1.0 * e, fill_color=CREME, fill_opacity=1, stroke_width=0)
    fente = Rectangle(width=0.7 * e, height=0.08 * e, fill_color=ENCRE, fill_opacity=1, stroke_width=0).move_to(b.get_top() + 0.12 * e * DOWN)
    bul = Rectangle(width=0.5 * e, height=0.5 * e, fill_color=CREME, fill_opacity=1, stroke_color=ENCRE, stroke_width=2).rotate(0.2).move_to(b.get_top() + 0.25 * e * UP)
    return VGroup(bul, b, fente)


def coche(ok=True, r=0.42):
    c = Circle(r, fill_color=CREME, fill_opacity=1, stroke_width=0)
    if ok:
        m = VMobject(color=ENCRE, stroke_width=9 * r / 0.42).set_points_as_corners([[-0.2 * r / 0.42, 0, 0], [-0.05 * r / 0.42, -0.16 * r / 0.42, 0], [0.22 * r / 0.42, 0.18 * r / 0.42, 0]])
    else:
        k = 0.17 * r / 0.42
        m = VGroup(Line([-k, -k, 0], [k, k, 0], color=ROUGE, stroke_width=9 * r / 0.42), Line([-k, k, 0], [k, -k, 0], color=ROUGE, stroke_width=9 * r / 0.42))
    return VGroup(c, m)


def loupe(e=1.0):
    return VGroup(Line([0.3 * e, -0.3 * e, 0], [0.75 * e, -0.75 * e, 0], color=ENCRE, stroke_width=12 * e), Circle(0.42 * e, color=ENCRE, stroke_width=9 * e, fill_color=CREME, fill_opacity=0.25))


def palais(l=2.6):
    base = Rectangle(width=l, height=0.9, fill_color=CREME, fill_opacity=1, stroke_width=0)
    cols = VGroup(*[Rectangle(width=0.1, height=0.6, fill_color=ROUGE_3, fill_opacity=1, stroke_width=0) for _ in range(7)]).arrange(RIGHT, buff=(l - 0.6 - 0.7) / 6).move_to(base)
    dome = AnnularSector(inner_radius=0, outer_radius=0.62, angle=PI, start_angle=0, fill_color=ENCRE, fill_opacity=1, stroke_width=0).next_to(base, UP, buff=0).shift(0.31 * DOWN)
    dome.move_to(base.get_top() + 0.31 * UP)
    fleche = Line(dome.get_top(), dome.get_top() + 0.35 * UP, color=ENCRE, stroke_width=5)
    return VGroup(base, cols, dome, fleche)


def bulle(lignes, taille=22):
    t = VGroup(*[T(x, taille, ENCRE) for x in lignes]).arrange(DOWN, buff=0.12)
    f = RoundedRectangle(corner_radius=0.2, width=t.width + 0.6, height=t.height + 0.5, fill_color=CREME, fill_opacity=1, stroke_width=0)
    q = Polygon(f.get_left() + [0.05, 0.18, 0], f.get_left() + [0.05, -0.18, 0], f.get_left() + [-0.4, -0.05, 0], fill_color=CREME, fill_opacity=1, stroke_width=0)
    return VGroup(q, f, t.move_to(f))


def sablier(e=1.0):
    return VGroup(Polygon([-0.3 * e, 0.45 * e, 0], [0.3 * e, 0.45 * e, 0], [0, 0, 0], fill_color=CREME, fill_opacity=1, stroke_width=0),
                  Polygon([-0.3 * e, -0.45 * e, 0], [0.3 * e, -0.45 * e, 0], [0, 0, 0], fill_color=CREME, fill_opacity=0.5, stroke_width=0),
                  Line([-0.36 * e, 0.47 * e, 0], [0.36 * e, 0.47 * e, 0], color=ENCRE, stroke_width=6 * e), Line([-0.36 * e, -0.47 * e, 0], [0.36 * e, -0.47 * e, 0], color=ENCRE, stroke_width=6 * e))


def cadre_autour(m, buff=0.12):
    return SurroundingRectangle(m, color=ROUGE, stroke_width=5, buff=buff, corner_radius=0.08)


def frise(a, b, x0=-3.0, x1=3.0, y=0.0, reperes=()):
    X = lambda v: x0 + (x1 - x0) * (v - a) / (b - a)
    g = VGroup(Arrow([x0, y, 0], [x1 + 0.5, y, 0], color=CREME, stroke_width=4, buff=0, max_tip_length_to_length_ratio=0.03))
    for v, nom in reperes:
        g.add(VGroup(Circle(0.11, fill_color=CREME, fill_opacity=1, stroke_width=0).move_to([X(v), y, 0]), T(nom, 20).next_to([X(v), y, 0], UP, buff=0.22)))
    g.X = X
    return g


class Sec(MovingCameraScene):
    T0, FIL = 0.0, 0

    def jusqua(self, t):
        from temps import M
        d = (M(t) - M(self.T0)) + getattr(self, 'decal', 0.0) - self.renderer.time
        if d > 1 / 30: self.wait(d)

    def at(self, t, *anims, rt=0.6):
        self.jusqua(t); self.play(*anims, run_time=rt)

    def decor(self):
        self.fond = Rectangle(width=17, height=10, stroke_width=0).set_fill(color=[ROUGE, ROUGE_2], opacity=1).set_sheen_direction(DOWN)
        self.filc = fil(self.FIL); self.add(self.fond, self.filc)
        self.vie()

    def vie(self):
        """L'image respire : très lent va-et-vient de la caméra ; le fond et le fil conducteur restent fixes à l'écran."""
        cam = self.camera.frame; t = ValueTracker(0)
        t.add_updater(lambda m, dt: m.increment_value(dt)); self.add(t)
        def respire(f):
            x = t.get_value()
            f.set(width=1.1125 * config.frame_width * (1 - 0.035 * (1 - np.cos(TAU * x / 15)) / 2))
            f.move_to([0.10 * np.sin(TAU * x / 23), -0.45 + 0.05 * np.sin(TAU * x / 17), 0])
        cam.add_updater(respire); self.add(cam); respire(cam)
        def colle(m):
            k = cam.width / (1.1125 * config.frame_width)
            m.set(width=m.w0 * k); m.move_to(cam.get_center() + np.array([0, (m.y0 + 0.45) * k, 0]))
        self.filc.w0, self.filc.y0 = self.filc.width, self.filc.get_y(); self.filc.add_updater(colle)
        self.fond.add_updater(lambda m: m.move_to(cam.get_center()))

    def etape(self, k, rt=0.5):
        n = fil(k); self.filc.clear_updaters(); self.play(Transform(self.filc, n), run_time=rt)
        cam = self.camera.frame; self.filc.w0, self.filc.y0 = n.width, n.get_y()
        self.filc.add_updater(lambda m: (m.set(width=m.w0 * cam.width / (1.1125 * config.frame_width)), m.move_to(cam.get_center() + np.array([0, (m.y0 + 0.45) * cam.width / (1.1125 * config.frame_width), 0]))))

    def vider(self, t=None, garder=(), rt=0.5):
        if t is not None: self.jusqua(t)
        g = set()
        for m in (self.fond, self.filc, *garder): g.update(m.get_family())
        sortants = [m for m in self.mobjects if m not in g and m is not self.camera.frame]
        if sortants: self.play(*[FadeOut(m, shift=0.7 * LEFT) for m in sortants], run_time=rt, rate_func=rate_functions.ease_in_sine)

    def chapitre(self, k, titre, num):
        """Carton de partie : un panneau traverse l'écran, le fil conducteur avance dessous."""
        c = self.camera.frame.get_center()
        pan = Rectangle(width=20, height=11.5, fill_color=ROUGE_4, fill_opacity=1, stroke_width=0)
        t = VGroup(T(f"{num} / 5", 30, CREME, False).set_opacity(0.7), T(titre, 86)).arrange(DOWN, buff=0.3)
        trait = Line(LEFT * 1.6, RIGHT * 1.6, color=CREME, stroke_width=6).next_to(t, DOWN, buff=0.4)
        g = VGroup(pan, t, trait).move_to(c)
        self.play(FadeIn(pan), FadeIn(t, shift=0.15 * UP), Create(trait), run_time=0.45)
        self.etape(k, rt=0.25); self.wait(0.45)
        self.play(FadeOut(g), run_time=0.45)
        self.remove(g)
