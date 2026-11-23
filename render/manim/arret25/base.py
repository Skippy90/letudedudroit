"""Briques de l'arrêt 25 (même style que l'arrêt 12)."""
import sys
sys.path.insert(0, "/home/claude/a25"); sys.path.append("/home/claude/proto")
from kit import *
from temps import S, E as F_, P, W, B, M, FIN

VERT = "#BFE3C0"


import random as _r
_r.seed(15)


def _vivant(m, amp, per=None):
    """Petit mouvement de vie : va-et-vient vertical, par incréments (compatible avec les autres animations)."""
    ph = _r.random() * TAU; per = per or 2.6 + _r.random() * 1.4; st = {"t": 0.0}
    def u(mob, dt):
        a = st["t"]; st["t"] += dt
        mob.shift(amp * (np.sin(TAU * st["t"] / per + ph) - np.sin(TAU * a / per + ph)) * UP)
    m.add_updater(u); return m


_bh, _ur, _lp = bonhomme, urne, loupe
def bonhomme(h=1.0, *a, **k): return _vivant(_bh(h, *a, **k), 0.03 * h)
def urne(e=1.0):
    g = _ur(e); _vivant(g[0], 0.05 * e, 1.9); return g
def loupe(e=1.0): return _vivant(_lp(e), 0.05 * e, 2.3)


AMBRE = "#FFC94A"; MENTHE = "#A8E6CF"; LILAS = "#D9C2F0"
EQUIPE = {"it": MENTHE, "yu": AMBRE, "autre": LILAS, None: CREME}


BLANC, VERT_D, ROUGE_D, BLEU_D = "#F4F5F0", "#1E9E52", "#CE2B37", "#1F4E9E"
# Habits aux couleurs du drapeau : (sens des bandes, couleurs). « yu » : tricolore de l'ancienne Yougoslavie.
DRAPEAUX = {"it": ("v", [VERT_D, BLANC, ROUGE_D]), "yu": ("h", [BLEU_D, BLANC, ROUGE_D]), "tr": ("h", [ROUGE_D, BLANC, ROUGE_D]),
            "hu": ("h", [ROUGE_D, BLANC, VERT_D]), "pl": ("h", [BLANC, ROUGE_D]), "nl": ("h", [ROUGE_D, BLANC, BLEU_D])}


def _bandes(sens, cols, yt, yb, wt, wb):
    g = VGroup(); n = len(cols); hw = lambda y: wb + (wt - wb) * (y - yb) / (yt - yb)
    for i, c in enumerate(cols):
        if sens == "h":
            y1 = yt - (yt - yb) * i / n; y2 = yt - (yt - yb) * (i + 1) / n
            pts = [[-hw(y1), y1, 0], [hw(y1), y1, 0], [hw(y2), y2, 0], [-hw(y2), y2, 0]]
        else:
            f1 = -1 + 2 * i / n; f2 = -1 + 2 * (i + 1) / n
            pts = [[f1 * wt, yt, 0], [f2 * wt, yt, 0], [f2 * wb, yb, 0], [f1 * wb, yb, 0]]
        g.add(Polygon(*pts, fill_color=c, fill_opacity=1, stroke_width=0))
    coins = [[-wt, yt, 0], [wt, yt, 0], [wb, yb, 0], [-wb, yb, 0]]
    g.add(*[Line(coins[k], coins[(k + 1) % 4], color=ENCRE, stroke_width=1.2) for k in range(4)])
    return g


def acteur(h=1.0, eq=None, femme=False, humeur=None):
    """Petit personnage ; avec une équipe, son habit porte les couleurs du drapeau. La tête reste crème pour tous."""
    b = bonhomme(h, CREME, femme=femme); b.h = h
    if eq in DRAPEAUX:
        sens, cols = DRAPEAUX[eq]
        b.add(_bandes(sens, cols, 0.66 * h, 0.02 * h, 0.13 * h, 0.27 * h) if femme else _bandes(sens, cols, 0.66 * h, 0.0, 0.2 * h, 0.15 * h))
    if humeur: visage(b, h, humeur)
    return b


def au_sol(b, x, y):
    return b.shift([x - b.get_center()[0], y - b.get_bottom()[1], 0])


def legende(eq, nom, taille=20):
    sens, cols = DRAPEAUX[eq]
    return VGroup(_bandes(sens, cols, 0.14, -0.14, 0.21, 0.21), T(nom, taille, CREME, False)).arrange(RIGHT, buff=0.15)


def visage(b, h, k="neutre"):
    """Pose (ou remplace) une expression sur la tête d'une silhouette : neutre, content, triste, perplexe, surpris, muet, decide."""
    if getattr(b, "visage", None) is not None: b.remove(b.visage)
    c = b[1].get_center(); r = 0.13 * h; ep = 3.2 * h; op = b[1].get_fill_opacity()
    g = VGroup(*[Dot(c + np.array([s * 0.42 * r, 0.16 * r, 0]), radius=0.12 * r, color=ENCRE) for s in (-1, 1)])
    m = c + np.array([0, -0.42 * r, 0])
    if k == "content": g.add(Arc(radius=0.42 * r, start_angle=PI * 1.2, angle=PI * 0.6, color=ENCRE, stroke_width=ep).move_to(m))
    elif k == "triste": g.add(Arc(radius=0.42 * r, start_angle=PI * 0.2, angle=PI * 0.6, color=ENCRE, stroke_width=ep).move_to(m + np.array([0, -0.05 * r, 0])))
    elif k == "surpris": g.add(Circle(0.17 * r, color=ENCRE, stroke_width=ep).move_to(m))
    elif k == "muet":
        g.add(Line(m + 0.38 * r * LEFT, m + 0.38 * r * RIGHT, color=ENCRE, stroke_width=ep), *[Line(m + np.array([x * r, 0.12 * r, 0]), m + np.array([x * r, -0.12 * r, 0]), color=ENCRE, stroke_width=ep * 0.7) for x in (-0.2, 0, 0.2)])
    elif k == "perplexe":
        g.add(Line(m + 0.3 * r * LEFT + 0.06 * r * DOWN, m + 0.3 * r * RIGHT + 0.08 * r * UP, color=ENCRE, stroke_width=ep),
              Line(c + np.array([0.2 * r, 0.5 * r, 0]), c + np.array([0.66 * r, 0.62 * r, 0]), color=ENCRE, stroke_width=ep))
    elif k == "decide":
        g.add(Line(m + 0.3 * r * LEFT, m + 0.3 * r * RIGHT, color=ENCRE, stroke_width=ep),
              Line(c + np.array([-0.68 * r, 0.56 * r, 0]), c + np.array([-0.2 * r, 0.42 * r, 0]), color=ENCRE, stroke_width=ep), Line(c + np.array([0.68 * r, 0.56 * r, 0]), c + np.array([0.2 * r, 0.42 * r, 0]), color=ENCRE, stroke_width=ep))
    else: g.add(Line(m + 0.25 * r * LEFT, m + 0.25 * r * RIGHT, color=ENCRE, stroke_width=ep))
    g.set_opacity(op); b.add(g); b.visage = g
    return b


def etiquette(s, taille=26, angle=-0.07):
    """Étiquette malicieuse, couleur ambre, légèrement penchée."""
    t = T(s, taille, ENCRE)
    f = RoundedRectangle(corner_radius=0.16, width=t.width + 0.5, height=t.height + 0.36, fill_color=AMBRE, fill_opacity=1, stroke_color=ENCRE, stroke_width=3)
    return VGroup(f, t).rotate(angle)


def titre(s, taille=30, y=3.2): return puce(s, taille).move_to([0, y, 0])
def bas(s, taille=24, y=-2.75): return bandeau(s, taille).move_to([0, y, 0])


def passeport(e=1.0):
    f = RoundedRectangle(corner_radius=0.08 * e, width=1.0 * e, height=1.4 * e, fill_color=ENCRE, fill_opacity=1, stroke_width=0)
    ombre = f.copy().set_fill(ROUGE_4, 0.6).shift(0.07 * e * (DOWN + RIGHT))
    c = VGroup(Rectangle(width=0.36 * e, height=0.11 * e), Rectangle(width=0.11 * e, height=0.36 * e)).set_fill(CREME, 1).set_stroke(width=0).move_to(f.get_center() + 0.22 * e * UP)
    l = VGroup(*[Line([-0.26 * e, 0, 0], [0.26 * e, 0, 0], color=CREME, stroke_width=3 * e, stroke_opacity=0.7) for _ in range(2)]).arrange(DOWN, buff=0.12 * e).move_to(f.get_center() + 0.35 * e * DOWN)
    return VGroup(ombre, f, c, l)


def cadenas(e=1.0):
    anse = Arc(radius=0.2 * e, start_angle=0, angle=PI, color=ENCRE, stroke_width=8 * e).shift(0.2 * e * UP)
    corps = RoundedRectangle(corner_radius=0.06 * e, width=0.62 * e, height=0.46 * e, fill_color=ENCRE, fill_opacity=1, stroke_width=0)
    trou = Circle(0.06 * e, fill_color=CREME, fill_opacity=1, stroke_width=0)
    return VGroup(anse, corps, trou)


def tampon(s, taille=34, angle=-0.12):
    t = T(s, taille, ROUGE)
    f = RoundedRectangle(corner_radius=0.08, width=t.width + 0.5, height=t.height + 0.4, color=ROUGE, stroke_width=6, fill_color=CREME, fill_opacity=1)
    return VGroup(f, t).rotate(angle)


def tas(n, cols, e=0.8, dx=0.62, dy=0.78):
    g = VGroup()
    for i in range(n):
        r, c = divmod(i, cols)
        g.add(dossier(e).move_to([c * dx * e / 0.8, -r * dy * e / 0.8, 0]))
    return g.move_to(ORIGIN)


def carton(lignes, l=5.6, h=2.2, taille=26, fond=ROUGE_3):
    f = RoundedRectangle(corner_radius=0.2, width=l, height=h, fill_color=fond, fill_opacity=1, stroke_width=0)
    g = VGroup(f, VGroup(*[T(x, taille) for x in lignes]).arrange(DOWN, buff=0.15).move_to(f)); g.fond = f
    return g


def perso(h, nom=None, femme=False, taille=20, **k):
    b = bonhomme(h, CREME, femme=femme, **k)
    g = VGroup(b); g.b = b
    if nom:
        g.add(puce(nom, taille).next_to(b, UP, buff=0.12))
    return g


def barre(m, couleur=ENCRE, ep=6):
    return Line(m.get_left() + 0.08 * LEFT, m.get_right() + 0.08 * RIGHT, color=couleur, stroke_width=ep)


def votants(n=7, h=1.0):
    return VGroup(*[bonhomme(h, CREME, femme=(k % 2 == 1)) for k in range(n)]).arrange(RIGHT, buff=0.2 * h)


class Sec25(Sec):
    L0, L1 = 1, 4   # la section couvre les lignes L0 à L1 - 1

    def debut(self, fil_avant=None):
        self.T0 = B(self.L0); self._sons = []
        if fil_avant is not None: self.FIL = fil_avant
        self.decor()
        self.deco = VGroup()
        for k in range(6):
            c = Circle(1.6 + 0.5 * k, fill_color=CREME if k % 2 else ROUGE_4, fill_opacity=0.03 if k % 2 else 0.075, stroke_width=0).move_to([-8 + 3.3 * k, (-1) ** k * 1.8 - 0.4, 0])
            c.vx = (0.16 + 0.05 * k) * (1 if k % 2 else -1)
            def glisse(m, dt):
                m.shift(m.vx * dt * RIGHT)
                if m.get_x() > 11: m.set_x(-11)
                if m.get_x() < -11: m.set_x(11)
            c.add_updater(glisse); self.deco.add(c)
        self.add(self.deco); self.bring_to_back(self.deco); self.bring_to_back(self.fond)

    def vie(self):
        """Caméra : lente avancée sur chaque plan (jusqu'à 5 %), retour en douceur à chaque changement de plan, léger balancement."""
        cam = self.camera.frame; self._t = 0.0; self._t0 = 0.0; self._cur = 1.0
        def respire(f, dt):
            self._t += dt; x = self._t
            u = min(1.0, max(0.0, (x - self._t0 - 0.3) / 10.0)); cible = 1 - 0.03 * u * u * (3 - 2 * u)
            self._cur += (cible - self._cur) * min(1.0, dt * 5)
            f.set(width=1.1125 * config.frame_width * self._cur)
            f.move_to([0.05 * np.sin(TAU * x / 19), -0.45 + 0.05 * np.sin(TAU * x / 13), 0])
        cam.set(width=1.1125 * config.frame_width); cam.move_to([0, -0.45, 0]); cam.add_updater(respire); self.add(cam)
        def colle(m):
            k = cam.width / (1.1125 * config.frame_width)
            m.set(width=m.w0 * k); m.move_to(cam.get_center() + np.array([0, (m.y0 + 0.45) * k, 0]))
        self.filc.w0, self.filc.y0 = self.filc.width, self.filc.get_y(); self.filc.add_updater(colle)
        self.fond.add_updater(lambda m: m.move_to(cam.get_center()))

    def vider(self, t=None, garder=(), rt=0.5):
        super().vider(t, garder=(*garder, self.deco), rt=rt); self._t0 = self._t

    def chapitre(self, k, titre, num):
        super().chapitre(k, titre, num); self._t0 = self._t

    def son(self, nom, g=1.0, dt=0.0):
        """Note un bruitage à l'instant courant de la section (lu ensuite par le mixage)."""
        self._sons.append((round(self.renderer.time + dt, 3), nom, g))

    def marche(self, bs, cibles, bonds=3):
        """Animations : chaque personnage rejoint sa cible en sautillant."""
        an = []
        for b, c in zip(bs, cibles):
            a = b.get_center().copy(); c = np.array(c, dtype=float); hh = getattr(b, "h", 1.0)
            an.append(UpdateFromAlphaFunc(b, lambda m, al, a=a, c=c, hh=hh: m.move_to(a + (c - a) * al + abs(np.sin(al * PI * bonds)) * 0.13 * hh * UP)))
        return an

    def pop(self, s, pos, dur=2.6, taille=26, angle=-0.07):
        return None

    def pop_ancien(self, s, pos, dur=2.6, taille=26, angle=-0.07):
        m = etiquette(s, taille, angle).move_to(pos); st = {"t": 0.0, "s": 0.2}; m.scale(0.2)
        def u(mob, dt):
            st["t"] += dt; x = st["t"]
            if x < 0.2: k = 0.2 + 0.94 * x / 0.2
            elif x < 0.32: k = 1.14 - 0.14 * (x - 0.2) / 0.12
            elif x < dur: k = 1 + 0.02 * np.sin(TAU * (x - 0.32) / 1.0)
            elif x < dur + 0.22: k = max(0.05, 1 - (x - dur) / 0.22)
            else:
                mob.set_opacity(0); mob.clear_updaters(); return
            mob.scale(k / st["s"]); st["s"] = k
        m.add_updater(u); self.add(m); return m

    def saut(self, *bs, h=0.18, rt=0.35):
        self.play(*[b.animate(rate_func=there_and_back).shift(h * UP) for b in bs], run_time=rt)

    def fin(self):
        self.jusqua(B(self.L1) if self.L1 <= 50 else FIN)
        import json as _j
        open(f"/tmp/a25/sons-{type(self).__name__}.json", "w").write(_j.dumps({"t0": M(self.T0), "ev": self._sons}))


# ---------- Arrêt 25 : fil conducteur et accessoires ----------
import kit as _kit
NOMS_FIL = ["Les faits", "Le texte", "Le Tribunal fédéral", "Strasbourg", "À retenir"]


def fil(actif=0):
    g = VGroup(*[T(n, 20, CREME, k == actif).set_opacity(1 if k == actif else 0.45) for k, n in enumerate(NOMS_FIL)]).arrange(RIGHT, buff=0.9).move_to([0, -3.72, 0])
    g.set_x(0)
    b = Line(g[actif].get_corner(DL) + 0.1 * DOWN, g[actif].get_corner(DR) + 0.1 * DOWN, color=CREME, stroke_width=4)
    return VGroup(g, b).set_x(0)
_kit.fil = fil

GRIS = "#CFC9C0"; CIEL = "#9FD3F2"
ROBES = [MENTHE, AMBRE, LILAS, CIEL]


def ainee(h=1.0, robe=CREME, humeur="neutre", canne=True):
    """Une aînée : silhouette en robe, cheveux gris en chignon, canne. Une couleur de robe fixe par personnage."""
    b = _bh(h, CREME, femme=True); b[0].set_fill(robe, 1); b.h = h
    c = b[1].get_center()
    chev = AnnularSector(inner_radius=0.088 * h, outer_radius=0.15 * h, angle=PI * 0.9, start_angle=PI * 0.05, fill_color=GRIS, fill_opacity=1, stroke_width=0).move_arc_center_to(c)
    chig = Circle(0.068 * h, fill_color=GRIS, fill_opacity=1, stroke_width=0).move_to(c + np.array([0, 0.185 * h, 0]))
    b.add(chig, chev)
    if canne:
        b.add(VGroup(Line([0.33 * h, 0.4 * h, 0], [0.36 * h, 0.0, 0], color=ENCRE, stroke_width=5 * h),
                     Arc(radius=0.05 * h, start_angle=0, angle=PI, color=ENCRE, stroke_width=5 * h).move_to([0.28 * h, 0.42 * h, 0])))
    _vivant(b, 0.03 * h); visage(b, h, humeur)
    return b


def juge(h=1.0, humeur="neutre"):
    """Un juge : robe sombre, rabat clair."""
    b = _bh(h, CREME); b[0].set_fill(ENCRE, 1); b.h = h
    b.add(Polygon([-0.05 * h, 0.66 * h, 0], [0.05 * h, 0.66 * h, 0], [0, 0.48 * h, 0], fill_color=CREME, fill_opacity=1, stroke_width=0))
    _vivant(b, 0.02 * h); visage(b, h, humeur)
    return b


def soleil(e=1.0):
    d = Circle(0.5 * e, fill_color=AMBRE, fill_opacity=1, stroke_width=0)
    r = VGroup(*[Line(0.66 * e * RIGHT, 0.92 * e * RIGHT, color=AMBRE, stroke_width=7 * e).rotate(k * TAU / 10, about_point=ORIGIN) for k in range(10)])
    g = VGroup(r, d); r.add_updater(lambda m, dt: m.rotate(0.25 * dt, about_point=d.get_center())); return g


def thermometre(e=1.0, niveau=0.4):
    """Thermomètre ; g.niv (ValueTracker, 0 à 1) règle la hauteur de la colonne."""
    tube = RoundedRectangle(corner_radius=0.16 * e, width=0.32 * e, height=2.2 * e, fill_color=CREME, fill_opacity=1, stroke_color=ENCRE, stroke_width=4 * e).shift(0.5 * e * UP)
    boule = Circle(0.32 * e, fill_color=AMBRE, fill_opacity=1, stroke_color=ENCRE, stroke_width=4 * e).shift(0.75 * e * DOWN)
    v = ValueTracker(niveau)
    col = always_redraw(lambda: Rectangle(width=0.14 * e, height=0.25 * e + 1.75 * e * v.get_value(), fill_color=AMBRE, fill_opacity=1, stroke_width=0).move_to(boule.get_center() + (0.25 * e + (0.25 * e + 1.75 * e * v.get_value()) / 2) * UP))
    gr = VGroup(*[Line(ORIGIN, 0.12 * e * RIGHT, color=ENCRE, stroke_width=2.5 * e).move_to(tube.get_right() + 0.14 * e * RIGHT + (k - 2) * 0.38 * e * UP) for k in range(5)])
    g = VGroup(tube, col, boule, gr); g.niv = v; g.boule = boule
    return g


def terre(e=1.0):
    m = Circle(0.9 * e, fill_color=CIEL, fill_opacity=1, stroke_color=ENCRE, stroke_width=4 * e)
    c1 = Ellipse(width=0.75 * e, height=0.5 * e, fill_color=MENTHE, fill_opacity=1, stroke_width=0).shift(0.3 * e * LEFT + 0.3 * e * UP).rotate(0.4)
    c2 = Ellipse(width=0.55 * e, height=0.7 * e, fill_color=MENTHE, fill_opacity=1, stroke_width=0).shift(0.35 * e * RIGHT + 0.25 * e * DOWN).rotate(-0.3)
    c3 = Ellipse(width=0.3 * e, height=0.2 * e, fill_color=MENTHE, fill_opacity=1, stroke_width=0).shift(0.45 * e * LEFT + 0.45 * e * DOWN)
    return VGroup(m, c1, c2, c3)


def enveloppe(e=1.0):
    f = RoundedRectangle(corner_radius=0.05 * e, width=1.1 * e, height=0.75 * e, fill_color=CREME, fill_opacity=1, stroke_color=ENCRE, stroke_width=3 * e)
    v = VMobject(color=ENCRE, stroke_width=3 * e).set_points_as_corners([f.get_corner(UL), f.get_center() + 0.05 * e * DOWN, f.get_corner(UR)])
    return VGroup(f, v)


def nuage(e=1.0, texte="CO₂"):
    g = VGroup(*[Circle(r * e, fill_color=GRIS, fill_opacity=1, stroke_width=0).move_to([x * e, y * e, 0]) for x, y, r in ((-0.45, 0, 0.32), (0, 0.16, 0.42), (0.45, 0, 0.32), (0, -0.1, 0.36))])
    if texte: g.add(T(texte, int(24 * e), ENCRE).move_to(g))
    return g


def usine(e=1.0):
    b = Rectangle(width=1.5 * e, height=0.8 * e, fill_color=ENCRE, fill_opacity=1, stroke_width=0)
    ch = Rectangle(width=0.26 * e, height=1.1 * e, fill_color=ENCRE, fill_opacity=1, stroke_width=0).move_to(b.get_corner(UR) + 0.3 * e * LEFT + 0.35 * e * UP)
    fen = VGroup(*[Square(0.2 * e, fill_color=AMBRE, fill_opacity=1, stroke_width=0) for _ in range(3)]).arrange(RIGHT, buff=0.18 * e).move_to(b.get_center() + 0.2 * e * LEFT)
    g = VGroup(ch, b, fen); g.cheminee = ch
    return g


def etoiles(r=0.7, n=12, t=0.1):
    return VGroup(*[Star(5, outer_radius=t, fill_color=AMBRE, fill_opacity=1, stroke_width=0).move_to([r * np.sin(k * TAU / n), r * np.cos(k * TAU / n), 0]) for k in range(n)])


def cour(l=3.0):
    """La Cour de Strasbourg : un tribunal surmonté d'un cercle d'étoiles."""
    t = tribunal(l); et = etoiles(0.42, 12, 0.07).move_to(t.get_top() + 0.62 * UP)
    return VGroup(t, et)


def livre(l1, l2, gros=None):
    """Livre du kit, titre ajusté à la largeur du cadre."""
    g = _kit.livre(l1, l2, gros)
    if g[4].width > 1.85: g[4].scale_to_fit_width(1.85)
    return g


def main_levee(b, h, cote=1):
    c = b[1].get_center()
    return Line(c + np.array([cote * 0.16 * h, -0.2 * h, 0]), c + np.array([cote * 0.27 * h, 0.27 * h, 0]), color=CREME, stroke_width=6 * h).set_cap_style(CapStyleType.ROUND)
