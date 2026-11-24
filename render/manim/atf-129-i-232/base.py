"""Briques de l'arrêt 25 (même style que l'arrêt 12)."""
import sys
sys.path.insert(0, "/home/claude/z232"); sys.path.append("/home/claude/proto")
from kit import *
from temps import S, E as F_, P, W, B, M, FIN, DERNIERE, NB

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
        fin_ = B(self.L1) if self.L1 <= DERNIERE else FIN
        ret = self.renderer.time - (M(fin_) - M(self.T0))
        if ret > 0.04: print("DEPASSEMENT", type(self).__name__, round(ret, 2))
        self.jusqua(fin_)
        import json as _j
        open(f"/tmp/z232v/sons-{type(self).__name__}.json", "w").write(_j.dumps({"t0": M(self.T0), "ev": self._sons}))


# ---------- Arrêt 25 : fil conducteur et accessoires ----------
import kit as _kit
NOMS_FIL = ["Les faits", "La question", "La motivation", "L'information", "À retenir"]


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


OCEAN = "#6EC1EE"; TERRE_V = "#7FD49A"; JOUE = "#F59AA5"


def _blob(pts, e, couleur):
    m = VMobject(fill_color=couleur, fill_opacity=1, stroke_width=0)
    m.set_points_smoothly([np.array([x * e, y * e, 0]) for x, y in pts] + [np.array([pts[0][0] * e, pts[0][1] * e, 0])])
    return m


def terre_visage(g, k="content"):
    """Pose (ou remplace) l'expression de la Terre : content, soulage, surpris, inquiet, malade (thermomètre, poche de glace), chaud (océan rougi, gouttes)."""
    e = g.e
    if getattr(g, "visage", None) is not None: g.remove(g.visage)
    c = g.mer.get_center(); ep = 5 * e
    f = VGroup(*[Dot(c + np.array([s * 0.26 * e, 0.08 * e, 0]), radius=0.065 * e, color=ENCRE) for s in (-1, 1)])
    f.add(*[Circle(0.1 * e, fill_color=JOUE, fill_opacity=0.75 if k == "chaud" else 0.5, stroke_width=0).move_to(c + np.array([s * 0.45 * e, -0.1 * e, 0])) for s in (-1, 1)])
    m = c + np.array([0, -0.2 * e, 0]); sourcil = lambda y0, y1: [Line(c + np.array([s * 0.38 * e, y0 * e, 0]), c + np.array([s * 0.16 * e, y1 * e, 0]), color=ENCRE, stroke_width=ep * 0.8) for s in (-1, 1)]
    if k == "content": f.add(Arc(radius=0.2 * e, start_angle=PI * 1.2, angle=PI * 0.6, color=ENCRE, stroke_width=ep).move_to(m))
    elif k == "soulage":
        f.remove(f[0], f[1])
        f.add(*[Arc(radius=0.09 * e, start_angle=PI * 0.1, angle=PI * 0.8, color=ENCRE, stroke_width=ep).move_to(c + np.array([s * 0.26 * e, 0.1 * e, 0])) for s in (-1, 1)])
        f.add(Arc(radius=0.24 * e, start_angle=PI * 1.15, angle=PI * 0.7, color=ENCRE, stroke_width=ep).move_to(m))
    elif k == "surpris":
        f.add(Ellipse(width=0.16 * e, height=0.22 * e, fill_color=ENCRE, fill_opacity=1, stroke_width=0).move_to(m + np.array([0, -0.03 * e, 0])))
        f.add(*[Arc(radius=0.12 * e, start_angle=PI * 0.2, angle=PI * 0.6, color=ENCRE, stroke_width=ep * 0.8).move_to(c + np.array([s * 0.26 * e, 0.3 * e, 0])) for s in (-1, 1)])
    elif k == "inquiet":
        f.add(Arc(radius=0.2 * e, start_angle=PI * 0.25, angle=PI * 0.5, color=ENCRE, stroke_width=ep).move_to(m + np.array([0, -0.04 * e, 0])))
        f.add(*sourcil(0.22, 0.32))
    elif k == "malade":
        f.add(Line(m + 0.16 * e * LEFT, m + 0.16 * e * RIGHT, color=ENCRE, stroke_width=ep), *sourcil(0.22, 0.32))
        poche = RoundedRectangle(corner_radius=0.1 * e, width=0.62 * e, height=0.3 * e, fill_color="#CFEBFA", fill_opacity=1, stroke_color=ENCRE, stroke_width=2 * e).rotate(0.2).move_to(c + np.array([-0.22 * e, 0.74 * e, 0]))
        th = VGroup(RoundedRectangle(corner_radius=0.07 * e, width=0.95 * e, height=0.14 * e, fill_color=BLANC, fill_opacity=1, stroke_color=ENCRE, stroke_width=2 * e),
                    Line(0.36 * e * LEFT, 0.12 * e * RIGHT, color=ROUGE, stroke_width=4 * e),
                    *[Line(ORIGIN, 0.05 * e * UP, color=ENCRE, stroke_width=1.5 * e).move_to([(-0.2 + 0.14 * i) * e, 0.035 * e, 0]) for i in range(5)],
                    Circle(0.1 * e, fill_color=ROUGE, fill_opacity=1, stroke_color=ENCRE, stroke_width=2 * e).move_to(0.5 * e * LEFT))
        th.rotate(-0.5).move_to(c + np.array([0.62 * e, 0.62 * e, 0]))
        f.add(th, poche)
    else:
        f.add(Ellipse(width=0.22 * e, height=0.16 * e, fill_color=ENCRE, fill_opacity=1, stroke_width=0).move_to(m + np.array([0, -0.02 * e, 0])))
        f.add(*sourcil(0.22, 0.32))
        for x, y in ((-1.02, 0.3), (1.04, 0.45), (0.98, 0.1)):
            f.add(VGroup(Circle(0.06 * e, fill_color="#CFEBFA", fill_opacity=1, stroke_width=0), Polygon([-0.05 * e, 0.03 * e, 0], [0.05 * e, 0.03 * e, 0], [0, 0.16 * e, 0], fill_color="#CFEBFA", fill_opacity=1, stroke_width=0)).move_to(c + np.array([x * e, y * e, 0])))
    g.mer.set_fill("#F2A47C" if k == "chaud" else ("#A9C9B8" if k == "malade" else OCEAN))
    g.add(f); g.visage = f
    return g


def terre(e=1.0, humeur="content"):
    """Une jolie Terre : halo, océan, continents, calotte, nuages, et un visage (humeur=None pour l'enlever)."""
    halo = VGroup(Circle(1.2 * e, fill_color=BLANC, fill_opacity=0.07, stroke_width=0), Circle(1.05 * e, fill_color=BLANC, fill_opacity=0.14, stroke_width=0))
    mer = Circle(0.9 * e, fill_color=OCEAN, fill_opacity=1, stroke_color=ENCRE, stroke_width=4 * e)
    ombre = AnnularSector(inner_radius=0.72 * e, outer_radius=0.88 * e, angle=PI * 0.7, start_angle=-PI * 0.75, fill_color="#3E93C9", fill_opacity=0.55, stroke_width=0)
    c1 = _blob([(-0.62, 0.22), (-0.42, 0.52), (-0.12, 0.6), (0.02, 0.4), (-0.18, 0.3), (-0.3, 0.05), (-0.5, -0.02)], e, TERRE_V)
    c2 = _blob([(0.22, 0.5), (0.5, 0.52), (0.68, 0.28), (0.52, 0.2), (0.36, 0.3)], e, TERRE_V)
    c3 = _blob([(0.12, -0.42), (0.4, -0.36), (0.56, -0.52), (0.38, -0.72), (0.14, -0.66)], e, TERRE_V)
    c4 = _blob([(-0.5, -0.4), (-0.3, -0.36), (-0.24, -0.58), (-0.42, -0.68)], e, TERRE_V)
    cal = Ellipse(width=0.5 * e, height=0.16 * e, fill_color=BLANC, fill_opacity=0.95, stroke_width=0).shift(0.78 * e * UP)
    def nu(x, y, k):
        return VGroup(*[Circle(r * e * k, fill_color=BLANC, fill_opacity=0.95, stroke_width=0).move_to([(x + dx * k) * e, (y + dy * k) * e, 0]) for dx, dy, r in ((-0.14, 0, 0.09), (0, 0.04, 0.12), (0.15, 0, 0.09))])
    n1, n2 = nu(-0.78, 0.6, 1.0), nu(0.8, -0.2, 0.9)
    for n_, v in ((n1, 0.05), (n2, -0.04)): _vivant(n_, 0.0, 3.0); n_.vx = v
    g = VGroup(halo, mer, ombre, c1, c2, c3, c4, cal, n1, n2); g.e, g.mer = e, mer
    _vivant(g, 0.04 * e, 3.4)
    if humeur: terre_visage(g, humeur)
    return g


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
    """La Cour de Strasbourg : silhouette à deux tours rondes (sans étoiles : on y lirait l'Union européenne).
    Rend VGroup(batiment, toit) ; batiment[2] est l'entrée, pour y poser une porte."""
    u = l / 3.0
    def tour(x, h, r):
        corps = Rectangle(width=2 * r * u, height=h * u, fill_color=CREME, fill_opacity=1, stroke_width=0).move_to([x * u, h * u / 2, 0])
        haut = Ellipse(width=2 * r * u, height=0.34 * u, fill_color=BLANC, fill_opacity=1, stroke_color=ENCRE, stroke_width=3 * u).move_to([x * u, h * u, 0])
        bandes = VGroup(*[Line([(x - r) * u, y * u, 0], [(x + r) * u, y * u, 0], color=ENCRE, stroke_width=2 * u).set_opacity(0.35) for y in np.arange(0.35, h - 0.1, 0.32)])
        return VGroup(corps, bandes, haut)
    socle = Rectangle(width=3.3 * u, height=0.16 * u, fill_color=ENCRE, fill_opacity=1, stroke_width=0).move_to([0, -0.08 * u, 0])
    ombre = Rectangle(width=3.3 * u, height=0.1 * u, fill_color=ROUGE_4, fill_opacity=0.6, stroke_width=0).move_to([0.06 * u, -0.2 * u, 0])
    entree = Rectangle(width=0.95 * u, height=1.15 * u, fill_color=ENCRE, fill_opacity=1, stroke_width=0).move_to([0, 0.575 * u, 0])
    vitr = VGroup(*[Line([x * u, 0.08 * u, 0], [x * u, 1.07 * u, 0], color=CREME, stroke_width=2 * u).set_opacity(0.5) for x in (-0.24, 0, 0.24)])
    bat = VGroup(ombre, socle, entree, tour(-1.0, 1.9, 0.58), tour(1.0, 1.55, 0.58), vitr)
    toit = Line([-0.6 * u, 1.2 * u, 0], [0.6 * u, 1.2 * u, 0], color=CREME, stroke_width=7 * u)
    return VGroup(bat, toit)


def main_levee(b, h, cote=1):
    c = b[1].get_center()
    return Line(c + np.array([cote * 0.16 * h, -0.2 * h, 0]), c + np.array([cote * 0.27 * h, 0.27 * h, 0]), color=CREME, stroke_width=6 * h).set_cap_style(CapStyleType.ROUND)


def terre_pousse(g):
    """Une jeune pousse sur la Terre (l'espoir, le zéro net)."""
    e = g.e; c = g.mer.get_center(); h = c + np.array([0, 0.9 * e, 0])
    p = VGroup(Line(h, h + 0.42 * e * UP, color="#3E9E5F", stroke_width=6 * e),
               Ellipse(width=0.34 * e, height=0.16 * e, fill_color=TERRE_V, fill_opacity=1, stroke_color="#3E9E5F", stroke_width=2 * e).rotate(0.6).move_to(h + np.array([0.17 * e, 0.44 * e, 0])),
               Ellipse(width=0.34 * e, height=0.16 * e, fill_color=TERRE_V, fill_opacity=1, stroke_color="#3E9E5F", stroke_width=2 * e).rotate(-0.6).move_to(h + np.array([-0.17 * e, 0.4 * e, 0])))
    g.add(p); g.pousse = p
    return p


# ---------- Textes de loi : trois familles, trois couvertures ----------
JAUNE_CODE = "#F5C83B"; BLEU_TRAITE = "#1F3A6E"; OR = "#F3D27A"


def croix_suisse(e=1.0):
    return VGroup(RoundedRectangle(corner_radius=0.04 * e, width=0.42 * e, height=0.42 * e, fill_color=ROUGE, fill_opacity=1, stroke_width=0),
                  Rectangle(width=0.26 * e, height=0.08 * e, fill_color=BLANC, fill_opacity=1, stroke_width=0), Rectangle(width=0.08 * e, height=0.26 * e, fill_color=BLANC, fill_opacity=1, stroke_width=0))


def _titres(l1, l2, couleur, larg, taille=20):
    tt = VGroup(*[T(x, taille, couleur) for x in (l1, l2) if x]).arrange(DOWN, buff=0.1)
    if tt.width > larg: tt.scale_to_fit_width(larg)
    return tt


def code(l1, l2, gros=None):
    """Un code (Code civil, Code pénal, Code des obligations…) : couverture jaune, dos sombre, croix suisse."""
    f = RoundedRectangle(corner_radius=0.1, width=2.5, height=3.2, fill_color=JAUNE_CODE, fill_opacity=1, stroke_width=0)
    ombre = f.copy().set_fill(ROUGE_4, 0.6).shift(0.1 * DOWN + 0.1 * RIGHT)
    pages = Rectangle(width=2.36, height=0.12, fill_color=BLANC, fill_opacity=1, stroke_width=0).move_to(f.get_bottom() + 0.1 * UP)
    dos = Rectangle(width=0.3, height=3.2, fill_color=ENCRE, fill_opacity=1, stroke_width=0).align_to(f, LEFT)
    cx = croix_suisse(1.0).move_to(f.get_corner(UR) + 0.42 * LEFT + 0.42 * DOWN)
    tt = _titres(l1, l2, ENCRE, 1.9).move_to(f.get_center() + 0.15 * RIGHT + 0.55 * UP)
    g = VGroup(ombre, f, pages, dos, cx, tt)
    if gros: g.add(T(gros, 44, ENCRE).move_to(f.get_center() + 0.15 * RIGHT + 0.6 * DOWN))
    return g


def loi(l1, l2, gros=None, rs=None):
    """Une loi fédérale hors des codes (PA, LCl…) : cahier clair, bandeau rouge, croix suisse, numéro du recueil."""
    f = RoundedRectangle(corner_radius=0.06, width=2.5, height=3.2, fill_color=CREME, fill_opacity=1, stroke_width=0)
    ombre = f.copy().set_fill(ROUGE_4, 0.6).shift(0.1 * DOWN + 0.1 * RIGHT)
    bande = Rectangle(width=2.5, height=0.62, fill_color=ENCRE, fill_opacity=1, stroke_width=0).align_to(f, UP)
    cx = croix_suisse(0.9).move_to(bande.get_left() + 0.38 * RIGHT); lf = T("Loi fédérale", 18).move_to(bande.get_center() + 0.25 * RIGHT)
    agrafes = VGroup(*[Line(ORIGIN, 0.22 * UP, color=ENCRE, stroke_width=4).move_to(f.get_left() + 0.1 * RIGHT + y * UP) for y in (0.5, -0.9)])
    tt = _titres(l1, l2, ENCRE, 2.1).move_to(f.get_center() + 0.45 * UP)
    g = VGroup(ombre, f, bande, cx, lf, agrafes, tt)
    if gros: g.add(T(gros, 44, ROUGE).move_to(f.get_center() + 0.55 * DOWN))
    if rs: g.add(T(rs, 15, ENCRE, False).move_to(f.get_bottom() + 0.28 * UP))
    return g


def traite(l1, l2, gros=None, embleme="etoiles", rs=None):
    """Un traité international (Convention européenne, Accord de Paris…) : couverture bleu nuit, lettres dorées, sceau."""
    f = RoundedRectangle(corner_radius=0.1, width=2.5, height=3.2, fill_color=BLEU_TRAITE, fill_opacity=1, stroke_width=0)
    ombre = f.copy().set_fill(ROUGE_4, 0.6).shift(0.1 * DOWN + 0.1 * RIGHT)
    filet = RoundedRectangle(corner_radius=0.07, width=2.2, height=2.9, color=OR, stroke_width=2.5).move_to(f)
    if embleme == "balance": em = balance(0.4).set_color(OR)
    else:
        em = VGroup(Circle(0.36, color=OR, stroke_width=3), Ellipse(width=0.34, height=0.72, color=OR, stroke_width=2), Line(0.36 * LEFT, 0.36 * RIGHT, color=OR, stroke_width=2), Line(0.36 * UP, 0.36 * DOWN, color=OR, stroke_width=2))
    em.move_to(f.get_center() + 0.85 * UP)
    tt = _titres(l1, l2, OR, 2.0, 18).move_to(f.get_center() + 0.1 * UP)
    ruban = VGroup(Polygon([-0.12, 0, 0], [0.12, 0, 0], [0.16, -0.5, 0], [0, -0.38, 0], [-0.16, -0.5, 0], fill_color=ROUGE, fill_opacity=1, stroke_width=0), Circle(0.2, fill_color=OR, fill_opacity=1, stroke_width=0)).move_to(f.get_corner(DR) + 0.42 * LEFT + 0.5 * UP)
    g = VGroup(ombre, f, filet, em, tt, ruban)
    if gros: g.add(T(gros, 40, CREME).move_to(f.get_center() + 0.75 * DOWN + 0.2 * LEFT))
    if rs: g.add(T(rs, 14, OR, False).move_to(f.get_bottom() + 0.26 * UP + 0.3 * LEFT))
    return g


# ---------- Les droits, avec une image qui parle ----------
def coeur(e=1.0, couleur=JOUE):
    return VGroup(Circle(0.12 * e, fill_color=couleur, fill_opacity=1, stroke_width=0).shift(0.1 * e * LEFT), Circle(0.12 * e, fill_color=couleur, fill_opacity=1, stroke_width=0).shift(0.1 * e * RIGHT),
                  Polygon([-0.215 * e, -0.045 * e, 0], [0.215 * e, -0.045 * e, 0], [0, -0.3 * e, 0], fill_color=couleur, fill_opacity=1, stroke_width=0))


def icone_vie(e=1.0):
    """Le droit à la vie : un arbre en feuilles, une jeune pousse à son pied, un cœur."""
    sol = Line([-0.9 * e, 0, 0], [0.9 * e, 0, 0], color=CREME, stroke_width=4 * e)
    tronc = Polygon([-0.09 * e, 0, 0], [0.09 * e, 0, 0], [0.06 * e, 0.75 * e, 0], [-0.06 * e, 0.75 * e, 0], fill_color=ENCRE, fill_opacity=1, stroke_width=0)
    feuilles = VGroup(*[Circle(r * e, fill_color=c, fill_opacity=1, stroke_width=0).move_to([x * e, y * e, 0]) for x, y, r, c in ((-0.3, 0.95, 0.34, "#5FBF82"), (0.3, 0.98, 0.36, TERRE_V), (0, 1.3, 0.4, "#9BE0B0"), (0, 0.9, 0.3, TERRE_V))])
    pousse = VGroup(Line([0.6 * e, 0, 0], [0.6 * e, 0.28 * e, 0], color="#5FBF82", stroke_width=5 * e), Ellipse(width=0.22 * e, height=0.1 * e, fill_color=TERRE_V, fill_opacity=1, stroke_width=0).rotate(0.6).move_to([0.7 * e, 0.3 * e, 0]),
                    Ellipse(width=0.22 * e, height=0.1 * e, fill_color=TERRE_V, fill_opacity=1, stroke_width=0).rotate(-0.6).move_to([0.5 * e, 0.27 * e, 0]))
    c = coeur(0.9 * e).move_to([0, 1.12 * e, 0])
    _vivant(feuilles, 0.03 * e, 2.8); c.add_updater(lambda m: m.move_to(feuilles.get_center() + 0.02 * e * UP))
    return VGroup(sol, tronc, feuilles, pousse, c)


def icone_foyer(e=1.0):
    """La vie privée et familiale : une maison éclairée, une famille devant, un cœur."""
    mur = Rectangle(width=1.3 * e, height=0.85 * e, fill_color=CREME, fill_opacity=1, stroke_width=0).move_to([0, 0.425 * e, 0])
    toit = Polygon([-0.82 * e, 0.85 * e, 0], [0.82 * e, 0.85 * e, 0], [0, 1.45 * e, 0], fill_color=ENCRE, fill_opacity=1, stroke_width=0)
    fen = Square(0.3 * e, fill_color=AMBRE, fill_opacity=1, stroke_color=ENCRE, stroke_width=2 * e).move_to([0.32 * e, 0.5 * e, 0])
    porte = Rectangle(width=0.28 * e, height=0.5 * e, fill_color=ENCRE, fill_opacity=1, stroke_width=0).move_to([-0.3 * e, 0.25 * e, 0])
    sol = Line([-1.0 * e, 0, 0], [1.9 * e, 0, 0], color=CREME, stroke_width=4 * e)
    fam = VGroup(_bh(0.72 * e, MENTHE, femme=True), _bh(0.46 * e, AMBRE), _bh(0.76 * e, LILAS)).arrange(RIGHT, buff=0.05 * e, aligned_edge=DOWN).move_to([1.25 * e, 0, 0], aligned_edge=DOWN)
    c = coeur(0.8 * e).move_to([0, 1.72 * e, 0]); _vivant(c, 0.04 * e, 2.2)
    return VGroup(sol, mur, toit, fen, porte, fam, c)


def carte_droit(icone, titre_, sous, l=6.5, h=2.5):
    """Un droit fondamental : son image à gauche, son nom et ses articles à droite."""
    f = RoundedRectangle(corner_radius=0.22, width=l, height=h, fill_color=ROUGE_3, fill_opacity=1, stroke_width=0)
    icone.move_to(f.get_left() + 1.35 * RIGHT)
    tx = VGroup(T(titre_, 26), T(sous, 19, CREME, False)).arrange(DOWN, buff=0.14, aligned_edge=LEFT)
    if tx.width > l - 2.9: tx.scale_to_fit_width(l - 2.9)
    tx.move_to(f.get_left() + 2.65 * RIGHT, aligned_edge=LEFT)
    g = VGroup(f, icone, tx); g.icone = icone
    return g


# ---------- ATF 129 I 232 (Zurich) ----------
Sec232 = Sec25


def constit(gros=None, e=1.0):
    """La Constitution fédérale : cahier clair, bandeau sombre, croix suisse."""
    f = RoundedRectangle(corner_radius=0.06, width=2.5, height=3.2, fill_color=CREME, fill_opacity=1, stroke_width=0)
    ombre = f.copy().set_fill(ROUGE_4, 0.6).shift(0.1 * DOWN + 0.1 * RIGHT)
    bande = Rectangle(width=2.5, height=0.62, fill_color=ENCRE, fill_opacity=1, stroke_width=0).align_to(f, UP)
    cx = croix_suisse(0.9).move_to(bande.get_left() + 0.38 * RIGHT); lf = T("Confédération", 17).move_to(bande.get_center() + 0.28 * RIGHT)
    tt = _titres("Constitution", "fédérale", ENCRE, 2.1).move_to(f.get_center() + 0.45 * UP)
    g = VGroup(ombre, f, bande, cx, lf, tt)
    if gros: g.add(T(gros, 40, ROUGE).move_to(f.get_center() + 0.55 * DOWN))
    g.add(T("RS 101", 15, ENCRE, False).move_to(f.get_bottom() + 0.28 * UP))
    return g.scale(e)


def candidat(h=1.3, k=0, humeur="neutre", femme=None):
    """Une personne qui demande la naturalisation : une couleur fixe par personnage."""
    b = _bh(h, CREME, femme=(k % 2 == 1) if femme is None else femme); b[0].set_fill(ROBES[k % 4], 1); b.h = h
    _vivant(b, 0.03 * h); visage(b, h, humeur)
    return b


def electeurs(n=6, h=1.1, humeur=None):
    g = VGroup(*[bonhomme(h, CREME, femme=(k % 2 == 1)) for k in range(n)]).arrange(RIGHT, buff=0.16 * h)
    for b in g:
        b.h = h
        if humeur: visage(b, h, humeur)
    return g


def initiative(e=1.0, court=False):
    g = page("Initiative populaire", ["Les naturalisations", "devant le peuple"] if not court else ["Naturalisations", "devant le peuple"], taille=22)
    return g.scale(e)


def ic_parlement(e=1.0):
    """Parlement communal : un hémicycle, ses rangées de sièges, la tribune."""
    g = VGroup()
    for r, n in ((0.55, 5), (0.85, 8), (1.15, 11)):
        for k in range(n):
            an = PI * (0.08 + 0.84 * k / (n - 1))
            g.add(Circle(0.085 * e, fill_color=CREME, fill_opacity=1, stroke_width=0).move_to([r * e * np.cos(an), r * e * np.sin(an), 0]))
    trib = VGroup(Rectangle(width=0.5 * e, height=0.22 * e, fill_color=ENCRE, fill_opacity=1, stroke_width=0).move_to([0, 0.06 * e, 0]), Circle(0.1 * e, fill_color=CREME, fill_opacity=1, stroke_width=0).move_to([0, 0.3 * e, 0]))
    sol = Line([-1.3 * e, -0.08 * e, 0], [1.3 * e, -0.08 * e, 0], color=CREME, stroke_width=4 * e)
    return VGroup(g, trib, sol)


def ic_district(e=1.0):
    """Conseil de district : une petite autorité de surveillance, quelques membres autour d'une table."""
    table = RoundedRectangle(corner_radius=0.06 * e, width=1.9 * e, height=0.32 * e, fill_color=ENCRE, fill_opacity=1, stroke_width=0).move_to([0, 0.16 * e, 0])
    mb = VGroup(*[_bh(0.95 * e, CREME, femme=(k == 1)) for k in range(3)]).arrange(RIGHT, buff=0.22 * e).move_to([0, 0.75 * e, 0])
    pieds = VGroup(*[Rectangle(width=0.08 * e, height=0.25 * e, fill_color=ENCRE, fill_opacity=1, stroke_width=0).move_to([x * e, -0.1 * e, 0]) for x in (-0.75, 0.75)])
    doc = Rectangle(width=0.3 * e, height=0.2 * e, fill_color=CREME, fill_opacity=1, stroke_width=0).move_to([0, 0.2 * e, 0])
    return VGroup(mb, table, pieds, doc)


def ic_gouvernement(e=1.0):
    """Gouvernement cantonal : un hôtel du gouvernement, avec son drapeau."""
    p = palais(2.3).scale(e * 0.74)
    mat = Line(p.get_top(), p.get_top() + 0.4 * e * UP, color=ENCRE, stroke_width=4 * e)
    drap = Polygon(mat.get_end(), mat.get_end() + 0.42 * e * RIGHT + 0.1 * e * DOWN, mat.get_end() + 0.2 * e * DOWN, fill_color=CREME, fill_opacity=1, stroke_color=ENCRE, stroke_width=2)
    return VGroup(p, mat, drap)


def ic_tf(e=1.0):
    return tribunal(2.2).scale(e * 0.62)


def station(nom, date=None, l=3.15, icone=None):
    f = RoundedRectangle(corner_radius=0.2, width=l, height=4.2, fill_color=ROUGE_3, fill_opacity=1, stroke_width=0)
    g = VGroup(f); g.f = f
    if icone is not None:
        icone.move_to(f.get_top() + 1.0 * DOWN); g.add(icone)
    n = VGroup(*[T(x, 23) for x in nom]).arrange(DOWN, buff=0.07).move_to(f.get_top() + 2.4 * DOWN)
    g.add(n)
    if date: g.add(T(date, 18, CREME, False).move_to(f.get_bottom() + 0.3 * UP))
    g.zone_verdict = f.get_bottom() + 0.95 * UP
    return g


def verdict(s, ok):
    t = T(s, 27, ENCRE if ok else ROUGE)
    return VGroup(RoundedRectangle(corner_radius=0.08, width=t.width + 0.4, height=t.height + 0.32, fill_color=VERT if ok else CREME, fill_opacity=1, stroke_color=ENCRE if ok else ROUGE, stroke_width=4), t).rotate(-0.06)


def ligne_coche(ok, a, b=None, taille=26):
    c = coche(ok, 0.36) if ok is not None else VGroup(Circle(0.36, fill_color=AMBRE, fill_opacity=1, stroke_width=0), T("?", 30, ENCRE))
    tx = VGroup(T(a, taille), *([T(b, taille - 5, CREME, False)] if b else [])).arrange(DOWN, buff=0.1, aligned_edge=LEFT)
    return VGroup(c, tx).arrange(RIGHT, buff=0.35)


def bulle_pensee(s, taille=20, couleur=CREME):
    t = T(s, taille, ENCRE)
    f = RoundedRectangle(corner_radius=0.2, width=max(0.9, t.width + 0.4), height=t.height + 0.36, fill_color=couleur, fill_opacity=1, stroke_width=0)
    pts = VGroup(Circle(0.07, fill_color=couleur, fill_opacity=1, stroke_width=0).move_to(f.get_bottom() + 0.16 * DOWN), Circle(0.045, fill_color=couleur, fill_opacity=1, stroke_width=0).move_to(f.get_bottom() + 0.3 * DOWN))
    return VGroup(f, t, pts)


def parti(h=1.3, texte="UDC · ville de Zurich"):
    """Un parti politique, sans son logo : trois militants derrière une banderole à son nom."""
    ms = VGroup(*[_bh(h, CREME, femme=(k == 1)) for k in range(3)]).arrange(RIGHT, buff=0.3 * h)
    for m in ms: m.h = h; visage(m, h, "decide")
    t = T(texte, max(16, int(17 * h)), ENCRE)
    ban = RoundedRectangle(corner_radius=0.05, width=max(ms.width + 0.5 * h, t.width + 0.4), height=0.42 * h, fill_color=CREME, fill_opacity=1, stroke_color=ENCRE, stroke_width=3)
    ban.move_to(ms.get_top() + 0.42 * h * UP); t.move_to(ban)
    pots = VGroup(*[Line(ban.get_bottom() + s * (ban.width / 2 - 0.12) * RIGHT, [ban.get_center()[0] + s * (ban.width / 2 - 0.12), ms.get_center()[1] - 0.05 * h, 0], color=ENCRE, stroke_width=5) for s in (-1, 1)])
    g = VGroup(pots, ms, ban, t); _vivant(g, 0.03 * h); g.h = h
    return g


def baguette(p, cible, ep=5):
    """Le personnage montre quelque chose : un trait part de sa main vers la cible."""
    h = getattr(p, "h", 1.0); c = p[1].get_center(); cible = np.array(cible, dtype=float); s = 1 if cible[0] > c[0] else -1
    a = c + np.array([s * 0.2 * h, -0.28 * h, 0])
    return VGroup(Line(a, cible, color=ENCRE, stroke_width=ep).set_cap_style(CapStyleType.ROUND), Circle(0.07, fill_color=CREME, fill_opacity=1, stroke_color=ENCRE, stroke_width=2).move_to(cible))


def agent(h=1.4, humeur="neutre"):
    """Une personne de l'administration : silhouette claire, col sombre."""
    p = _bh(h, CREME); p.h = h
    p.add(Rectangle(width=0.2 * h, height=0.07 * h, fill_color=ENCRE, fill_opacity=1, stroke_width=0).move_to([0, 0.63 * h, 0]))
    _vivant(p, 0.03 * h); visage(p, h, humeur)
    return p


def donnees(e=1.0):
    """Les données personnelles : une fiche avec un portrait, gardée par un cadenas."""
    f = RoundedRectangle(corner_radius=0.07 * e, width=1.25 * e, height=1.5 * e, fill_color=CREME, fill_opacity=1, stroke_width=0)
    tete = Circle(0.17 * e, fill_color=ENCRE, fill_opacity=1, stroke_width=0).move_to(f.get_center() + np.array([-0.3 * e, 0.42 * e, 0]))
    buste = AnnularSector(inner_radius=0, outer_radius=0.24 * e, angle=PI, start_angle=0, fill_color=ENCRE, fill_opacity=1, stroke_width=0).move_arc_center_to(f.get_center() + np.array([-0.3 * e, 0.08 * e, 0]))
    lg = VGroup(*[Line([0, 0, 0], [l_ * e, 0, 0], color=ROUGE_3, stroke_width=4 * e) for l_ in (0.42, 0.3, 0.9, 0.9, 0.6)])
    for k, l_ in enumerate(lg): l_.move_to(f.get_center() + np.array([(0.28 if k < 2 else 0) * e, (0.45 - 0.16 * k if k < 2 else -0.05 - 0.2 * (k - 1)) * e, 0]))
    c = cadenas(0.75 * e).move_to(f.get_corner(DR) + np.array([-0.12 * e, 0.18 * e, 0]))
    return VGroup(f, tete, buste, lg, c)
