"""Briques de l'arrêt 25 (même style que l'arrêt 12)."""
import sys
sys.path.insert(0, "/home/claude/fr01"); sys.path.append("/home/claude/proto")
# ---- Série « Les grands arrêts français » : fond bleu du drapeau français (demande du 26 novembre 2026) ----
# Les teintes sombres du style rouge (panneaux, ombres, encre) deviennent bleues AVANT le chargement du kit, qui les recopie.
import proto as _proto
BLEU, BLEU_2, BLEU_3, BLEU_4, ENCRE_B = "#000091", "#00007A", "#2A2AA8", "#00005C", "#0A0A3F"
_proto.ROUGE_2, _proto.ROUGE_3, _proto.ROUGE_4, _proto.ENCRE = BLEU_2, BLEU_3, BLEU_4, ENCRE_B
_proto.config.background_color = BLEU
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

    def decor(self):
        """Fond bleu du drapeau français, en léger dégradé ; même fil conducteur que les autres séries."""
        self.fond = Rectangle(width=17, height=10, stroke_width=0).set_fill(color=[BLEU, BLEU_2], opacity=1).set_sheen_direction(DOWN)
        self.filc = fil(self.FIL); self.add(self.fond, self.filc)
        self.vie()

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
        open(f"/tmp/fr01v/sons-{type(self).__name__}.json", "w").write(_j.dumps({"t0": M(self.T0), "ev": self._sons}))


# ---------- Arrêt 25 : fil conducteur et accessoires ----------
import kit as _kit
NOMS_FIL = ["Les faits", "Le droit", "Le raisonnement", "La portée", "À retenir"]


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
    n = VGroup(*[T(x, 23) for x in nom]).arrange(DOWN, buff=0.07).move_to(f.get_top() + 2.3 * DOWN)
    g.add(n)
    if date: g.add(T(date, 17, CREME, False).move_to(f.get_bottom() + 0.24 * UP))
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
    for m in ms:
        m.h = h; c0 = m[0].get_center() - np.array([0, 0.33 * h, 0])
        m.add(Polygon(c0 + [-0.13 * h, 0.66 * h, 0], c0 + [-0.03 * h, 0.66 * h, 0], c0 + [0.13 * h, 0.1 * h, 0], c0 + [0.04 * h, 0.06 * h, 0], fill_color="#3FA35B", fill_opacity=1, stroke_width=0)); visage(m, h, "decide")
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


def maillot_ch(p):
    """La personne naturalisée : une croix suisse apparaît sur son maillot."""
    h = getattr(p, "h", 1.3)
    return croix_suisse(0.62 * h).move_to(p[0].get_center() + 0.02 * h * UP)


# =====================================================================================================================
# STANDARDS « GRANDS ARRÊTS » (docs/standards-grands-arrets.md) : couleur des icônes, identité des personnages, décisions
# =====================================================================================================================
BLEU_ZH = "#2B8FD9"; VERT_OK = "#2FB36B"; OR_S = "#F2C14E"; BOIS = "#B9773E"


def dossier(e=1.0):
    """Dossier : chemise ambre, feuille claire qui dépasse."""
    ch = RoundedRectangle(corner_radius=0.05 * e, width=0.66 * e, height=0.8 * e, fill_color=AMBRE, fill_opacity=1, stroke_width=0)
    onglet = RoundedRectangle(corner_radius=0.03 * e, width=0.3 * e, height=0.14 * e, fill_color=AMBRE, fill_opacity=1, stroke_width=0).move_to(ch.get_corner(UL) + np.array([0.17 * e, 0.04 * e, 0]))
    fe = Rectangle(width=0.5 * e, height=0.6 * e, fill_color=CREME, fill_opacity=1, stroke_width=0).move_to(ch.get_center() + 0.02 * e * UP)
    lg = VGroup(*[Line([-0.17 * e, y * e, 0], [0.17 * e, y * e, 0], color=ROUGE_3, stroke_width=3 * e) for y in (0.2, 0.06, -0.08)])
    return VGroup(VGroup(onglet, ch, fe), lg)


def urne(e=1.0):
    """Urne : caisse claire, bandeau menthe (neutre : ni bleu zurichois ni bleu lucernois), bulletin."""
    b = RoundedRectangle(corner_radius=0.08 * e, width=1.3 * e, height=1.0 * e, fill_color=CREME, fill_opacity=1, stroke_width=0)
    fente = Rectangle(width=0.7 * e, height=0.08 * e, fill_color=ENCRE, fill_opacity=1, stroke_width=0).move_to(b.get_top() + 0.12 * e * DOWN)
    bul = Rectangle(width=0.5 * e, height=0.5 * e, fill_color=BLANC, fill_opacity=1, stroke_color=ENCRE, stroke_width=2).rotate(0.2).move_to(b.get_top() + 0.25 * e * UP)
    bande = Rectangle(width=1.3 * e, height=0.2 * e, fill_color=MENTHE, fill_opacity=1, stroke_width=0)   # menthe : aucune couleur cantonale.move_to(b.get_center() + 0.2 * e * DOWN)
    g = VGroup(bul, b, fente, bande)
    _vivant(g[0], 0.05 * e, 1.9); return g


def loupe(e=1.0):
    g = VGroup(Line([0.3 * e, -0.3 * e, 0], [0.75 * e, -0.75 * e, 0], color=BOIS, stroke_width=12 * e), Circle(0.42 * e, color=ENCRE, stroke_width=9 * e, fill_color=CIEL, fill_opacity=0.55))
    return _vivant(g, 0.05 * e, 2.3)


def cadenas(e=1.0):
    anse = Arc(radius=0.2 * e, start_angle=0, angle=PI, color=ENCRE, stroke_width=8 * e).shift(0.2 * e * UP)
    corps = RoundedRectangle(corner_radius=0.06 * e, width=0.62 * e, height=0.46 * e, fill_color=OR_S, fill_opacity=1, stroke_color=ENCRE, stroke_width=2.5 * e)
    trou = VGroup(Circle(0.06 * e, fill_color=ENCRE, fill_opacity=1, stroke_width=0), Rectangle(width=0.05 * e, height=0.12 * e, fill_color=ENCRE, fill_opacity=1, stroke_width=0).shift(0.08 * e * DOWN))
    return VGroup(anse, corps, trou)


def passeport(e=1.0):
    """Passeport suisse : rouge, croix blanche."""
    f = RoundedRectangle(corner_radius=0.08 * e, width=1.0 * e, height=1.4 * e, fill_color="#C4161C", fill_opacity=1, stroke_color=CREME, stroke_width=3 * e)
    ombre = f.copy().set_fill(ROUGE_4, 0.6).set_stroke(width=0).shift(0.07 * e * (DOWN + RIGHT))
    c = VGroup(Rectangle(width=0.36 * e, height=0.11 * e), Rectangle(width=0.11 * e, height=0.36 * e)).set_fill(BLANC, 1).set_stroke(width=0).move_to(f.get_center() + 0.22 * e * UP)
    l = VGroup(*[Line([-0.26 * e, 0, 0], [0.26 * e, 0, 0], color=BLANC, stroke_width=3 * e, stroke_opacity=0.8) for _ in range(2)]).arrange(DOWN, buff=0.12 * e).move_to(f.get_center() + 0.35 * e * DOWN)
    return VGroup(ombre, f, c, l)


def coche(ok=True, r=0.42):
    """Oui : pastille verte. Non : pastille claire, croix rouge."""
    k = r / 0.42
    if ok:
        return VGroup(Circle(r, fill_color=VERT_OK, fill_opacity=1, stroke_color=BLANC, stroke_width=3 * k),
                      VMobject(color=BLANC, stroke_width=9 * k).set_points_as_corners([[-0.2 * k, 0, 0], [-0.05 * k, -0.16 * k, 0], [0.22 * k, 0.18 * k, 0]]))
    q = 0.17 * k
    return VGroup(Circle(r, fill_color=CREME, fill_opacity=1, stroke_width=0), VGroup(Line([-q, -q, 0], [q, q, 0], color=ROUGE, stroke_width=9 * k), Line([-q, q, 0], [q, -q, 0], color=ROUGE, stroke_width=9 * k)))


def maison(x, y, l=1.3, h=0.9, e=1.0):
    """Bâtiment : fenêtres éclairées (ambre), porte en bois."""
    mur = Rectangle(width=l, height=h, fill_color=CREME, fill_opacity=1, stroke_width=0).move_to([x, y + h / 2, 0])
    toit = Polygon([x - l / 2 - 0.12, y + h, 0], [x + l / 2 + 0.12, y + h, 0], [x, y + h + 0.55 * e, 0], fill_color=ENCRE, fill_opacity=1, stroke_width=0)
    fen = VGroup(*[Square(0.13, fill_color=AMBRE if (i + j) % 2 == 0 else ROUGE_3, fill_opacity=1, stroke_width=0).move_to([x - l / 2 + 0.22 + i * (l - 0.44) / 3, y + h * (0.3 + 0.38 * j), 0]) for i in range(4) for j in range(2)])
    return VGroup(mur, toit, fen)


def drapeau_ch(e=1.0):
    """Drapeau suisse sur sa hampe."""
    mat = Line([0, 0, 0], [0, 1.5 * e, 0], color=BOIS, stroke_width=6 * e)
    d = Square(0.6 * e, fill_color="#D8232A", fill_opacity=1, stroke_color=BLANC, stroke_width=2 * e).move_to([0.34 * e, 1.18 * e, 0])
    c = VGroup(Rectangle(width=0.36 * e, height=0.12 * e), Rectangle(width=0.12 * e, height=0.36 * e)).set_fill(BLANC, 1).set_stroke(width=0).move_to(d)
    return VGroup(mat, d, c)


def drapeau_zh(e=1.0):
    """Drapeau zurichois : tranché, blanc en haut à droite, bleu en bas à gauche."""
    mat = Line([0, 0, 0], [0, 1.5 * e, 0], color=BOIS, stroke_width=6 * e)
    o = np.array([0.04 * e, 0.88 * e, 0]); a = 0.6 * e
    bl = Polygon(o + [0, a, 0], o + [a, a, 0], o + [a, 0, 0], fill_color=BLANC, fill_opacity=1, stroke_width=0)
    bu = Polygon(o + [0, a, 0], o + [0, 0, 0], o + [a, 0, 0], fill_color=BLEU_ZH, fill_opacity=1, stroke_width=0)
    cadre = Square(a, color=BLANC, stroke_width=2 * e).move_to(o + [a / 2, a / 2, 0])
    return VGroup(mat, bl, bu, cadre)


def ecusson_zh(e=1.0):
    a = 0.2 * e
    bl = Polygon([-a, a, 0], [a, a, 0], [a, -a, 0], fill_color=BLANC, fill_opacity=1, stroke_width=0)
    bu = Polygon([-a, a, 0], [-a, -a, 0], [a, -a, 0], fill_color=BLEU_ZH, fill_opacity=1, stroke_width=0)
    return VGroup(bl, bu, Square(2 * a, color=ENCRE, stroke_width=1.5 * e))


def electeur(h=1.1, femme=False, humeur="neutre"):
    """Un membre du corps électoral zurichois : maillot bleu et blanc, toujours un visage."""
    b = _bh(h, CREME, femme=femme); b.h = h
    b[0].set_fill(BLEU_ZH, 1)
    b.add(Polygon([-0.2 * h if not femme else -0.13 * h, 0.66 * h, 0], [0.2 * h if not femme else 0.13 * h, 0.66 * h, 0], [0.0, 0.3 * h, 0], fill_color=BLANC, fill_opacity=1, stroke_width=0))
    _vivant(b, 0.03 * h); visage(b, h, humeur)
    return b


def electeurs(n=6, h=1.1, humeur="neutre", drapeaux=False):
    g = VGroup(*[electeur(h, femme=(k % 2 == 1), humeur=humeur) for k in range(n)]).arrange(RIGHT, buff=0.16 * h)
    if drapeaux:
        fz = drapeau_zh(0.8 * h).next_to(g, LEFT, buff=0.12 * h).align_to(g, DOWN); fc = drapeau_ch(0.8 * h).next_to(g, RIGHT, buff=0.12 * h).align_to(g, DOWN)
        g.drapeaux = VGroup(fz, fc); g.add(fz, fc); g.n = n
    return g


def personnes(g):
    """Les seules silhouettes d'un groupe d'électeurs (sans les drapeaux)."""
    return [m for m in g if hasattr(m, "h")]


def humeur(g, k, h=None):
    """Change l'expression d'un personnage ou de tout un groupe."""
    for m in (personnes(g) if not hasattr(g, "h") else [g]): visage(m, h or m.h, k)


def colorer_foule(g):
    """Une foule de silhouettes devient le corps électoral zurichois : un maillot bleu sur deux."""
    for i, b in enumerate(g):
        if i % 2 == 0: b[0].set_fill(BLEU_ZH, 1)
    return g


def juge(h=1.0, humeur="neutre"):
    """Un juge : robe noire, rabat blanc, toque."""
    b = _bh(h, CREME); b[0].set_fill("#1B1B1F", 1); b.h = h
    rab = VGroup(*[Polygon([s * 0.01 * h, 0.66 * h, 0], [s * 0.085 * h, 0.66 * h, 0], [s * 0.07 * h, 0.42 * h, 0], [s * 0.01 * h, 0.42 * h, 0], fill_color=BLANC, fill_opacity=1, stroke_width=0) for s in (-1, 1)])
    toque = VGroup(RoundedRectangle(corner_radius=0.03 * h, width=0.3 * h, height=0.13 * h, fill_color="#1B1B1F", fill_opacity=1, stroke_width=0).move_to([0, 0.975 * h, 0]),
                   Rectangle(width=0.3 * h, height=0.03 * h, fill_color=OR_S, fill_opacity=1, stroke_width=0).move_to([0, 0.925 * h, 0]))
    b.add(rab, toque)
    _vivant(b, 0.02 * h); visage(b, h, humeur)
    return b


def decision(mot, ok, titre_="DÉCISION", e=1.0, sceau=True):
    """Le design des décisions : une feuille à en-tête, le dispositif en tampon, un sceau à ruban."""
    t = T(mot, 24, VERT_OK if ok else ROUGE)
    tt = T(titre_, 13); l = max(2.25, t.width + 0.75, tt.width + 0.9)
    f = RoundedRectangle(corner_radius=0.07, width=l, height=1.12, fill_color=CREME, fill_opacity=1, stroke_width=0)
    ombre = f.copy().set_fill(ROUGE_4, 0.6).shift(0.07 * DOWN + 0.07 * RIGHT)
    tete = Rectangle(width=l, height=0.3, fill_color=ENCRE, fill_opacity=1, stroke_width=0).align_to(f, UP)
    tt.move_to(tete)
    cadre = RoundedRectangle(corner_radius=0.06, width=t.width + 0.28, height=t.height + 0.24, color=VERT_OK if ok else ROUGE, stroke_width=4)
    VGroup(cadre, t).move_to(f.get_center() + 0.16 * DOWN + (0.16 * LEFT if sceau else 0)).rotate(-0.05)
    g = VGroup(ombre, f, tete, tt, cadre, t)
    if sceau:
        c = f.get_corner(DR) + np.array([-0.24, 0.2, 0])
        rub = VGroup(*[Polygon(c + [s * 0.02, 0, 0], c + [s * 0.17, -0.34, 0], c + [s * 0.05, -0.27, 0], c + [s * 0.0, -0.36, 0], fill_color="#C4161C", fill_opacity=1, stroke_width=0) for s in (-1, 1)])
        sc = VGroup(Circle(0.17, fill_color=OR_S, fill_opacity=1, stroke_color=ENCRE, stroke_width=2).move_to(c), Circle(0.09, color=ENCRE, stroke_width=1.5).move_to(c))
        g.add(rub, sc)
    g.scale(e); cadre.set_stroke(width=4 * e)
    return g


def verdict(s, ok):
    return decision(s, ok)


def arret_tf(mot, ok=False, e=1.0):
    """L'arrêt du Tribunal fédéral : même design, en-tête « ARRÊT », croix suisse."""
    g = decision(mot, ok, "ARRÊT DU TRIBUNAL FÉDÉRAL", 1.0)
    g.add(croix_suisse(0.5).move_to(g[2].get_left() + 0.22 * RIGHT)); g[3].shift(0.12 * RIGHT)
    return g.scale(e)


def militant(h=1.0, humeur="decide"):
    """Un militant du parti auteur de l'initiative (silhouette claire, écharpe verte)."""
    p = _bh(h, CREME); p.h = h
    p.add(Polygon([-0.2 * h, 0.66 * h, 0], [-0.08 * h, 0.66 * h, 0], [0.16 * h, 0.1 * h, 0], [0.06 * h, 0.06 * h, 0], fill_color="#3FA35B", fill_opacity=1, stroke_width=0))
    _vivant(p, 0.03 * h); visage(p, h, humeur)
    return p


def drapeau_lu(e=1.0):
    """Drapeau lucernois : coupé, blanc en haut, bleu en bas."""
    mat = Line([0, 0, 0], [0, 1.5 * e, 0], color=BOIS, stroke_width=6 * e)
    o = np.array([0.04 * e, 0.88 * e, 0]); a = 0.6 * e
    bl = Rectangle(width=a, height=a / 2, fill_color=BLANC, fill_opacity=1, stroke_width=0).move_to(o + [a / 2, 0.75 * a, 0])
    bu = Rectangle(width=a, height=a / 2, fill_color=BLEU_ZH, fill_opacity=1, stroke_width=0).move_to(o + [a / 2, 0.25 * a, 0])
    cadre = Square(a, color=BLANC, stroke_width=2 * e).move_to(o + [a / 2, a / 2, 0])
    return VGroup(mat, bl, bu, cadre)


def drapeau_nomme(d, nom, taille=16):
    """Un drapeau cantonal avec le nom du canton à côté (deux cantons ont parfois les mêmes couleurs)."""
    return VGroup(d, T(nom, taille).next_to(d, RIGHT, buff=0.08).align_to(d, DOWN))


# =====================================================================================================================
# ATF 121 I 367 (minimum vital) : les trois frères, leur mère, les besoins élémentaires, le noyau de l'article 12
# =====================================================================================================================
Sec367 = Sec25
FRERES = [MENTHE, AMBRE, CIEL]        # une couleur fixe par frère, gardée toute la vidéo
CS_BLEU, CS_ROUGE = "#11457E", "#D7141A"


def frere(h=1.3, k=0, humeur="neutre"):
    """Un des trois frères V. : silhouette, maillot de sa couleur fixe, toujours un visage."""
    b = _bh(h, CREME); b[0].set_fill(FRERES[k % 3], 1); b.h = h
    _vivant(b, 0.03 * h); visage(b, h, humeur)
    return b


def freres(h=1.3, humeur="neutre", buff=0.32):
    g = VGroup(*[frere(h, k, humeur) for k in range(3)]).arrange(RIGHT, buff=buff * h, aligned_edge=DOWN); g.h = h
    return g


def mere(h=1.25, humeur="neutre"):
    """La mère des trois frères : robe lilas."""
    b = _bh(h, CREME, femme=True); b[0].set_fill(LILAS, 1); b.h = h
    _vivant(b, 0.03 * h); visage(b, h, humeur)
    return b


def drapeau_cs(e=1.0):
    """Drapeau tchécoslovaque (repris tel quel par la République tchèque) : blanc en haut, rouge en bas, triangle bleu côté hampe jusqu'au centre."""
    mat = Line([0, 0, 0], [0, 1.5 * e, 0], color=BOIS, stroke_width=6 * e)
    o = np.array([0.04 * e, 0.9 * e, 0]); L_, H_ = 0.9 * e, 0.6 * e
    bl = Rectangle(width=L_, height=H_ / 2, fill_color=BLANC, fill_opacity=1, stroke_width=0).move_to(o + [L_ / 2, 0.75 * H_, 0])
    ro = Rectangle(width=L_, height=H_ / 2, fill_color=CS_ROUGE, fill_opacity=1, stroke_width=0).move_to(o + [L_ / 2, 0.25 * H_, 0])
    tri = Polygon(o + [0, H_, 0], o + [0, 0, 0], o + [L_ / 2, H_ / 2, 0], fill_color=CS_BLEU, fill_opacity=1, stroke_width=0)
    cadre = Rectangle(width=L_, height=H_, color=BLANC, stroke_width=2 * e).move_to(o + [L_ / 2, H_ / 2, 0])
    return VGroup(mat, bl, ro, tri, cadre)


def suisse_be(l=5.0):
    """Carte de la Suisse, canton de Berne en clair."""
    c = carte(l)
    c.cantons["BE"].set_fill(CREME, 0.55)
    c.move_to(ORIGIN)
    return c


def guichet(h=1.35, texte="Commune", humeur="neutre"):
    """L'administration de la commune : un agent derrière un guichet, une enseigne."""
    a = agent(h, humeur)
    comptoir = RoundedRectangle(corner_radius=0.05, width=1.9 * h, height=0.3 * h, fill_color=BOIS, fill_opacity=1, stroke_color=ENCRE, stroke_width=2)
    comptoir.move_to(a.get_bottom() + 0.12 * h * UP)
    ens = puce(texte, int(19 * h)).next_to(a, UP, buff=0.15 * h)
    g = VGroup(a, comptoir, ens); g.agent = a; g.h = h
    return g


def barriere(e=1.0):
    """Une frontière : poteau et barrière rayée rouge et blanc."""
    pot = Rectangle(width=0.16 * e, height=1.1 * e, fill_color=BOIS, fill_opacity=1, stroke_color=ENCRE, stroke_width=2 * e).move_to([0, 0.55 * e, 0])
    barre_ = VGroup(*[Rectangle(width=0.3 * e, height=0.16 * e, fill_color=ENCRE if k % 2 == 0 else BLANC, fill_opacity=1, stroke_width=0).move_to([0.23 * e + 0.3 * e * k, 0.95 * e, 0]) for k in range(6)])
    cad = Rectangle(width=1.8 * e, height=0.16 * e, color=ENCRE, stroke_width=2 * e).move_to([0.98 * e, 0.95 * e, 0])
    pied = Rectangle(width=0.5 * e, height=0.1 * e, fill_color=ENCRE, fill_opacity=1, stroke_width=0).move_to([0, 0.05 * e, 0])
    return VGroup(pot, barre_, cad, pied)


def doc_voyage(e=1.0):
    """Document de voyage : livret ambre."""
    f = RoundedRectangle(corner_radius=0.07 * e, width=0.9 * e, height=1.2 * e, fill_color=AMBRE, fill_opacity=1, stroke_color=ENCRE, stroke_width=2.5 * e)
    l_ = VGroup(*[Line([-0.25 * e, 0, 0], [0.25 * e, 0, 0], color=ENCRE, stroke_width=3 * e) for _ in range(3)]).arrange(DOWN, buff=0.13 * e).move_to(f.get_center() + 0.2 * e * DOWN)
    c = Circle(0.16 * e, color=ENCRE, stroke_width=3 * e).move_to(f.get_center() + 0.3 * e * UP)
    return VGroup(f, c, l_)


def carte_nat(e=1.0):
    """Carte de nationalité tchécoslovaque : petit drapeau, portrait, lignes."""
    f = RoundedRectangle(corner_radius=0.08 * e, width=1.7 * e, height=1.1 * e, fill_color=CREME, fill_opacity=1, stroke_color=ENCRE, stroke_width=2.5 * e)
    d = drapeau_cs(0.55 * e)[1:]; d.move_to(f.get_corner(UL) + np.array([0.38 * e, -0.24 * e, 0]))
    t = Circle(0.13 * e, fill_color=ENCRE, fill_opacity=1, stroke_width=0).move_to(f.get_center() + np.array([0.42 * e, 0.12 * e, 0]))
    bu = AnnularSector(inner_radius=0, outer_radius=0.2 * e, angle=PI, start_angle=0, fill_color=ENCRE, fill_opacity=1, stroke_width=0).move_arc_center_to(f.get_center() + np.array([0.42 * e, -0.2 * e, 0]))
    lg = VGroup(*[Line([0, 0, 0], [0.62 * e, 0, 0], color=ROUGE_3, stroke_width=3 * e) for _ in range(3)]).arrange(DOWN, buff=0.12 * e).move_to(f.get_center() + np.array([-0.38 * e, -0.22 * e, 0]))
    return VGroup(f, d, t, bu, lg)


def mallette(e=1.0):
    """Le travail : une mallette."""
    poig = RoundedRectangle(corner_radius=0.06 * e, width=0.42 * e, height=0.24 * e, color=ENCRE, stroke_width=6 * e).move_to([0, 0.42 * e, 0])
    f = RoundedRectangle(corner_radius=0.08 * e, width=1.2 * e, height=0.8 * e, fill_color=BOIS, fill_opacity=1, stroke_color=ENCRE, stroke_width=2.5 * e)
    b = Rectangle(width=1.2 * e, height=0.06 * e, fill_color=ENCRE, fill_opacity=1, stroke_width=0).move_to([0, 0.08 * e, 0])
    fer = Rectangle(width=0.16 * e, height=0.12 * e, fill_color=OR_S, fill_opacity=1, stroke_width=0).move_to([0, 0.08 * e, 0])
    return VGroup(poig, f, b, fer)


def assiette(e=1.0):
    """Se nourrir : une assiette, du pain, une pomme."""
    a = Ellipse(width=1.3 * e, height=0.5 * e, fill_color=BLANC, fill_opacity=1, stroke_color=ENCRE, stroke_width=2.5 * e)
    i = Ellipse(width=0.9 * e, height=0.3 * e, color=GRIS, stroke_width=2 * e)
    pain = Ellipse(width=0.6 * e, height=0.3 * e, fill_color=BOIS, fill_opacity=1, stroke_width=0).move_to([-0.12 * e, 0.12 * e, 0])
    ent = VGroup(*[Line([x * e, 0.04 * e, 0], [(x + 0.06) * e, 0.2 * e, 0], color=OR_S, stroke_width=3 * e) for x in (-0.3, -0.16, -0.02)])
    pom = VGroup(Circle(0.17 * e, fill_color="#E2463F", fill_opacity=1, stroke_width=0).move_to([0.3 * e, 0.15 * e, 0]), Line([0.3 * e, 0.3 * e, 0], [0.33 * e, 0.4 * e, 0], color=BOIS, stroke_width=3 * e),
                 Ellipse(width=0.14 * e, height=0.07 * e, fill_color=TERRE_V, fill_opacity=1, stroke_width=0).move_to([0.4 * e, 0.38 * e, 0]))
    return VGroup(a, i, pain, ent, pom)


def habit(e=1.0, couleur=CIEL):
    """Se vêtir : un pull."""
    p = Polygon([-0.25, 0.5, 0], [-0.6, 0.3, 0], [-0.72, -0.1, 0], [-0.5, -0.18, 0], [-0.4, 0.05, 0], [-0.4, -0.55, 0], [0.4, -0.55, 0], [0.4, 0.05, 0], [0.5, -0.18, 0], [0.72, -0.1, 0], [0.6, 0.3, 0], [0.25, 0.5, 0], [0, 0.38, 0],
                fill_color=couleur, fill_opacity=1, stroke_color=ENCRE, stroke_width=2.5).scale(e)
    return p


def abri(e=1.0):
    """Un abri : petite maison éclairée."""
    mur = Rectangle(width=1.1 * e, height=0.7 * e, fill_color=CREME, fill_opacity=1, stroke_width=0).move_to([0, 0.35 * e, 0])
    toit = Polygon([-0.72 * e, 0.7 * e, 0], [0.72 * e, 0.7 * e, 0], [0, 1.22 * e, 0], fill_color=ENCRE, fill_opacity=1, stroke_width=0)
    fen = Square(0.26 * e, fill_color=AMBRE, fill_opacity=1, stroke_color=ENCRE, stroke_width=2 * e).move_to([0.26 * e, 0.42 * e, 0])
    porte = Rectangle(width=0.24 * e, height=0.42 * e, fill_color=BOIS, fill_opacity=1, stroke_width=0).move_to([-0.24 * e, 0.21 * e, 0])
    return VGroup(mur, toit, fen, porte)


def besoins(e=1.0):
    g = VGroup(assiette(e), habit(0.8 * e), abri(e)).arrange(RIGHT, buff=0.55 * e, aligned_edge=DOWN)
    return g


def piece(e=1.0):
    """L'aide en argent : une pièce dorée."""
    return VGroup(Circle(0.42 * e, fill_color=OR_S, fill_opacity=1, stroke_color=ENCRE, stroke_width=3 * e), Circle(0.31 * e, color=BOIS, stroke_width=2 * e), T("CHF", int(20 * e), ENCRE))


def colis(e=1.0):
    """L'aide en nature : un colis."""
    f = Rectangle(width=1.0 * e, height=0.75 * e, fill_color=BOIS, fill_opacity=1, stroke_color=ENCRE, stroke_width=2.5 * e)
    sc = Rectangle(width=0.18 * e, height=0.75 * e, fill_color=AMBRE, fill_opacity=1, stroke_width=0)
    rab = Polygon([-0.5 * e, 0.375 * e, 0], [0.5 * e, 0.375 * e, 0], [0.42 * e, 0.55 * e, 0], [-0.42 * e, 0.55 * e, 0], fill_color="#A2652F", fill_opacity=1, stroke_color=ENCRE, stroke_width=2.5 * e)
    return VGroup(rab, f, sc)


def texte_cantonal(l1, l2, gros=None, canton="Canton de Berne"):
    """Un texte cantonal (constitution, loi) : cahier clair, bandeau ambre au nom du canton, sans croix suisse."""
    f = RoundedRectangle(corner_radius=0.06, width=2.5, height=3.2, fill_color=CREME, fill_opacity=1, stroke_width=0)
    ombre = f.copy().set_fill(ROUGE_4, 0.6).shift(0.1 * DOWN + 0.1 * RIGHT)
    bande = Rectangle(width=2.5, height=0.62, fill_color=AMBRE, fill_opacity=1, stroke_width=0).align_to(f, UP)
    lf = T(canton, 18, ENCRE).move_to(bande)
    tt = _titres(l1, l2, ENCRE, 2.1).move_to(f.get_center() + 0.45 * UP)
    g = VGroup(ombre, f, bande, lf, tt)
    if gros: g.add(T(gros, 44, ROUGE).move_to(f.get_center() + 0.55 * DOWN))
    return g


def constit_1874(e=1.0):
    """La Constitution fédérale de 1874 : même cahier, papier jauni."""
    g = constit("1874")
    g[1].set_fill("#E9DDBF", 1); g.remove(g[-1])   # pas de numéro RS : c'est l'ancienne Constitution
    return g.scale(e)


def juges(n=3, h=1.25, humeur="neutre"):
    g = VGroup(*[juge(h, humeur) for _ in range(n)]).arrange(RIGHT, buff=0.22 * h, aligned_edge=DOWN); g.h = h
    return g


def seuil(l=6.0, texte="Minimum indispensable"):
    """Le seuil que le juge fait respecter : une ligne pointillée, nommée."""
    ln = DashedLine([-l / 2, 0, 0], [l / 2, 0, 0], color=CREME, stroke_width=6, dash_length=0.18)
    return VGroup(ln, bandeau(texte, 20).next_to(ln, UP, buff=0.15).align_to(ln, LEFT))


def noyau(e=1.0):
    """L'article 12 au cœur, l'aide sociale cantonale autour."""
    ext = Circle(2.0 * e, fill_color=ROUGE_3, fill_opacity=1, stroke_color=CREME, stroke_width=4 * e)
    inn = Circle(0.95 * e, fill_color=CREME, fill_opacity=1, stroke_width=0)
    a12 = VGroup(T("Art. 12", int(30 * e), ROUGE), T("Cst.", int(20 * e), ROUGE)).arrange(DOWN, buff=0.05).move_to(inn)
    return VGroup(ext, inn, a12)


def bouclier(e=1.0, texte=None, couleur=MENTHE):
    """Une garantie, une protection : un bouclier."""
    p = VMobject(fill_color=couleur, fill_opacity=1, stroke_color=ENCRE, stroke_width=4 * e)
    p.set_points_smoothly([[-0.7, 0.8, 0], [0, 0.95, 0], [0.7, 0.8, 0], [0.62, 0.0, 0], [0.3, -0.6, 0], [0, -0.9, 0], [-0.3, -0.6, 0], [-0.62, 0.0, 0], [-0.7, 0.8, 0]])
    p.scale(e)
    g = VGroup(p)
    if texte: g.add(T(texte, int(40 * e), ENCRE).move_to(p.get_center() + 0.05 * e * UP))
    return g


# ---------- Interactions entre personnages (standard : plus d'interactions illustratives, 25 novembre 2026) ----------
def main_de(p, cote=1):
    """Position de la main d'un personnage (côté droit par défaut, -1 pour la gauche)."""
    h = getattr(p, "h", 1.0); c = p[1].get_center()
    return c + np.array([cote * 0.27 * h, -0.36 * h, 0])


def bras_tendu(p, cote=1):
    """Un bras tendu (pour donner, montrer, frapper à une porte)."""
    h = getattr(p, "h", 1.0); c = p[1].get_center()
    a = c + np.array([cote * 0.13 * h, -0.24 * h, 0]); b = c + np.array([cote * 0.36 * h, -0.2 * h, 0])
    return Line(a, b, color=ENCRE, stroke_width=6 * h).set_cap_style(CapStyleType.ROUND)


def donner(obj, cible, arc=-0.6, rt=0.8):
    """Un objet passe d'une main à l'autre (ou va se poser sur une cible)."""
    c = cible if isinstance(cible, np.ndarray) or isinstance(cible, (list, tuple)) else cible.get_center()
    return obj.animate(path_arc=arc, run_time=rt).move_to(np.array(c, dtype=float))


def valise(e=1.0, couleur=CIEL):
    poig = RoundedRectangle(corner_radius=0.05 * e, width=0.3 * e, height=0.18 * e, color=ENCRE, stroke_width=5 * e).move_to([0, 0.36 * e, 0])
    f = RoundedRectangle(corner_radius=0.07 * e, width=0.75 * e, height=0.55 * e, fill_color=couleur, fill_opacity=1, stroke_color=ENCRE, stroke_width=2.5 * e)
    s = VGroup(*[Line([x * e, 0.27 * e, 0], [x * e, -0.27 * e, 0], color=ENCRE, stroke_width=2.5 * e) for x in (-0.2, 0.2)])
    return VGroup(poig, f, s)


def ouvrir_barriere(br, angle=1.35):
    """La barrière se lève (rotation de la lisse autour du poteau)."""
    return Rotate(VGroup(br[1], br[2]), angle=angle, about_point=np.array([br[0].get_x(), br[1].get_y(), 0]))


def porte(ab):
    """La porte de l'abri (dernier rectangle bois), pour l'ouvrir."""
    return ab[3]


def coeur_pop(pos, e=1.0):
    return coeur(e).move_to(pos)


def tamponner(scene, tampon_, cible_pos, juge_=None, son=True):
    """Le tampon descend sur la feuille (un juge ou un agent l'abat)."""
    tampon_.move_to(np.array(cible_pos) + 0.9 * UP).set_opacity(0)
    scene.add(tampon_)
    an = [tampon_.animate(rate_func=rate_functions.ease_in_quad).move_to(cible_pos).set_opacity(1)]
    if juge_ is not None: an.append(juge_.animate(rate_func=there_and_back).shift(0.1 * DOWN))
    return an


def parapluie(e=1.0, couleur=AMBRE, texte=None):
    """Le droit qui protège : un parapluie ouvert (plus lisible qu'un bouclier). Rend VGroup(toile, nervures, manche[, texte])."""
    R = 1.0 * e; n = 4
    haut = [[R * np.cos(a), R * 0.62 * np.sin(a), 0] for a in np.linspace(0, PI, 40)]
    bas = []
    for k in range(n):
        x0 = -R + 2 * R * k / n; x1 = -R + 2 * R * (k + 1) / n; c = (x0 + x1) / 2; r = (x1 - x0) / 2
        bas += [[c - r * np.cos(t), 0.12 * e * np.sin(t), 0] for t in np.linspace(0, PI, 12)]
    toile = VMobject(fill_color=couleur, fill_opacity=1, stroke_color=ENCRE, stroke_width=3.5 * e)
    toile.set_points_as_corners(haut[::-1][::-1] and [*haut[::-1], *bas[::1]][::1] + [haut[-1]])
    nerv = VGroup(*[Line([0, R * 0.62, 0], [x * e, 0.0, 0], color=ENCRE, stroke_width=2 * e, stroke_opacity=0.6) for x in (-0.5, 0, 0.5)])
    pointe = Line([0, R * 0.62, 0], [0, R * 0.62 + 0.14 * e, 0], color=ENCRE, stroke_width=4 * e)
    manche = VGroup(Line([0, 0, 0], [0, -0.95 * e, 0], color=ENCRE, stroke_width=5 * e),
                    Arc(radius=0.13 * e, start_angle=PI, angle=PI, color=ENCRE, stroke_width=5 * e).move_arc_center_to([0.13 * e, -0.95 * e, 0]))
    g = VGroup(toile, nerv, pointe, manche)
    if texte:
        g.add(VGroup(Circle(0.26 * e, fill_color=CREME, fill_opacity=1, stroke_color=ENCRE, stroke_width=2.5 * e), T(texte, int(30 * e), ENCRE)).move_to([0, R * 0.3, 0]))
    return g


# ---------- Canton de Berne : drapeau, membre du gouvernement (standard « identité cantonale », comme Zurich) ----------
NOIR_BE = "#141414"; JAUNE_BE = "#F4C430"; ROUGE_BE = "#E2231A"


def ours(e=1.0, couleur=NOIR_BE):
    """L'ours bernois, simplifié : il marche vers la gauche ; langue et griffes rouges."""
    corps = Ellipse(width=1.0 * e, height=0.5 * e, fill_color=couleur, fill_opacity=1, stroke_width=0)
    tete = Circle(0.2 * e, fill_color=couleur, fill_opacity=1, stroke_width=0).move_to([-0.55 * e, 0.12 * e, 0])
    museau = Ellipse(width=0.22 * e, height=0.14 * e, fill_color=couleur, fill_opacity=1, stroke_width=0).move_to([-0.74 * e, 0.07 * e, 0])
    oreille = Circle(0.07 * e, fill_color=couleur, fill_opacity=1, stroke_width=0).move_to([-0.48 * e, 0.3 * e, 0])
    langue = Polygon([-0.83 * e, 0.03 * e, 0], [-0.93 * e, 0.0, 0], [-0.83 * e, -0.02 * e, 0], fill_color=ROUGE_BE, fill_opacity=1, stroke_width=0)
    pattes = VGroup(*[RoundedRectangle(corner_radius=0.04 * e, width=0.13 * e, height=0.32 * e, fill_color=couleur, fill_opacity=1, stroke_width=0).move_to([x * e, -0.27 * e, 0]) for x in (-0.33, -0.15, 0.17, 0.35)])
    griffes = VGroup(*[Line([x * e - 0.07 * e, -0.43 * e, 0], [x * e + 0.03 * e, -0.43 * e, 0], color=ROUGE_BE, stroke_width=2.5 * e) for x in (-0.33, -0.15, 0.17, 0.35)])
    queue = Circle(0.05 * e, fill_color=couleur, fill_opacity=1, stroke_width=0).move_to([0.52 * e, 0.08 * e, 0])
    return VGroup(pattes, corps, queue, tete, museau, oreille, langue, griffes)


def drapeau_be(e=1.0):
    """Drapeau bernois (vérifié : FOTW) : champ rouge, bande d'or de l'angle haut côté hampe vers l'angle bas,
    ours noir qui monte vers la hampe, langue et griffes rouges."""
    mat = Line([0, 0, 0], [0, 1.5 * e, 0], color=BOIS, stroke_width=6 * e)
    a = 0.62 * e; o = np.array([0.04 * e, 0.86 * e, 0])
    champ = Square(a, fill_color=ROUGE_BE, fill_opacity=1, stroke_width=0).move_to(o + [a / 2, a / 2, 0])
    l = 0.36 * a
    bande = Polygon(o + [0, a, 0], o + [l, a, 0], o + [a, l, 0], o + [a, 0, 0], o + [a - l, 0, 0], o + [0, a - l, 0], fill_color=JAUNE_BE, fill_opacity=1, stroke_width=0)
    o_ = ours(0.38 * e).rotate(-PI / 4).move_to(o + [a / 2, a / 2, 0])
    cadre = Square(a, color=BLANC, stroke_width=2 * e).move_to(champ)
    return VGroup(mat, champ, bande, o_, cadre)


def drapeaux_be_ch(e=1.0, buff=0.15):
    """L'identité bernoise : drapeau de Berne (nommé) et drapeau suisse, côte à côte."""
    return VGroup(drapeau_nomme(drapeau_be(e), "Berne", int(16 * e + 2)), drapeau_ch(e)).arrange(RIGHT, buff=buff * e + 0.25, aligned_edge=DOWN)


def membre_be(h=1.35, humeur="decide"):
    """Un membre du Conseil-exécutif bernois : silhouette claire, écharpe aux couleurs de Berne (noir et rouge)."""
    p = _bh(h, CREME); p.h = h
    ech = VGroup(Polygon([-0.2 * h, 0.66 * h, 0], [-0.06 * h, 0.66 * h, 0], [0.17 * h, 0.1 * h, 0], [0.04 * h, 0.05 * h, 0], fill_color=NOIR_BE, fill_opacity=1, stroke_width=0),
                 Polygon([-0.13 * h, 0.66 * h, 0], [-0.09 * h, 0.66 * h, 0], [0.13 * h, 0.09 * h, 0], [0.1 * h, 0.08 * h, 0], fill_color=ROUGE_BE, fill_opacity=1, stroke_width=0))
    p.add(ech); _vivant(p, 0.03 * h); visage(p, h, humeur)
    return p


# ---------- Montrer du doigt, sans « câble » : bras tendu et flèche courte près de la cible ----------
def baguette(p, cible, ep=5):
    h = getattr(p, "h", 1.0); c = p[1].get_center(); cible = np.array(cible, dtype=float)
    s = 1 if cible[0] > c[0] else -1
    bras_ = bras_tendu(p, s)
    d = cible - bras_.get_end(); n = np.linalg.norm(d); u = d / n if n > 1e-6 else RIGHT
    fl = Arrow(cible - 0.75 * u, cible - 0.08 * u, buff=0, color=AMBRE, stroke_width=8, max_tip_length_to_length_ratio=0.45, max_stroke_width_to_length_ratio=12)
    return VGroup(bras_, fl)


# ---------- Standards d'icônes : la demande, le réfugié ----------
def demande(e=1.0, titre="Demande", sous="de réintégration"):
    """Une demande : formulaire à en-tête ambre, case cochée, ligne de signature, stylo."""
    f = RoundedRectangle(corner_radius=0.08 * e, width=1.6 * e, height=2.0 * e, fill_color=CREME, fill_opacity=1, stroke_width=0)
    ombre = f.copy().set_fill(ROUGE_4, 0.6).shift(0.07 * e * (DOWN + RIGHT))
    tete = Rectangle(width=1.6 * e, height=0.42 * e, fill_color=AMBRE, fill_opacity=1, stroke_width=0).align_to(f, UP)
    tt = T(titre.upper(), int(15 * e), ENCRE).move_to(tete)
    st = T(sous, int(13 * e), ENCRE, False).move_to(f.get_top() + 0.62 * e * DOWN) if sous else VGroup()
    lg = VGroup(*[VGroup(Square(0.13 * e, color=ENCRE, stroke_width=2 * e), Line([0, 0, 0], [0.85 * e, 0, 0], color=ROUGE_3, stroke_width=3 * e)).arrange(RIGHT, buff=0.1 * e) for _ in range(3)]).arrange(DOWN, buff=0.16 * e, aligned_edge=LEFT).move_to(f.get_center() + 0.05 * e * DOWN)
    sig = VGroup(Line([0, 0, 0], [0.9 * e, 0, 0], color=ENCRE, stroke_width=2.5 * e), T("signature", int(10 * e), ENCRE, False)).arrange(DOWN, buff=0.04 * e).move_to(f.get_bottom() + 0.28 * e * UP)
    stylo = VGroup(RoundedRectangle(corner_radius=0.03 * e, width=0.12 * e, height=0.8 * e, fill_color=CIEL, fill_opacity=1, stroke_color=ENCRE, stroke_width=2 * e),
                   Polygon([-0.06 * e, -0.4 * e, 0], [0.06 * e, -0.4 * e, 0], [0, -0.55 * e, 0], fill_color=ENCRE, fill_opacity=1, stroke_width=0)).rotate(-0.6).move_to(f.get_corner(DR) + np.array([0.1 * e, 0.35 * e, 0]))
    return VGroup(ombre, f, tete, tt, st, lg, sig, stylo)


def toit(l=2.0, couleur=AMBRE, drapeau=None):
    """La protection d'un État : un toit ; drapeau facultatif posé au faîte (standard « toit protecteur »)."""
    e = l / 2.0
    t = VGroup(Polygon([-1.0 * e, 0, 0], [0, 0.7 * e, 0], [1.0 * e, 0, 0], [0.82 * e, 0, 0], [0, 0.5 * e, 0], [-0.82 * e, 0, 0], fill_color=couleur, fill_opacity=1, stroke_color=ENCRE, stroke_width=2.5))
    if drapeau is not None:
        d = drapeau.copy(); d.scale_to_fit_height(0.6 * e); d.shift([-d[0].get_x(), 0.62 * e - d.get_bottom()[1], 0])
        t.add(d)
    return t


def icone_refugie(e=1.0, couleur=CIEL, drapeau=None):
    """Le statut de réfugié (standard) : une personne avec sa valise, à l'abri sous le toit protecteur de l'État d'accueil."""
    t_ = toit(2.0 * e, AMBRE, drapeau).shift(0.95 * e * UP - [0, 0, 0])
    pe = _bh(1.15 * e, CREME); pe[0].set_fill(couleur, 1); pe.h = 1.15 * e; visage(pe, 1.15 * e, "content")
    pe.move_to([-0.2 * e, 0.0, 0], aligned_edge=DOWN)
    va = valise(0.5 * e, AMBRE).next_to(pe, RIGHT, buff=0.02 * e).align_to(pe, DOWN)
    sol = Line([-0.9 * e, 0, 0], [0.9 * e, 0, 0], color=CREME, stroke_width=4 * e)
    return VGroup(sol, t_, pe, va)


# =====================================================================================================
# ---------- FRANCE (série « Les grands arrêts français ») ----------
# Drapeau : bleu, blanc, rouge en bandes verticales, bleu côté hampe (Constitution de 1958, art. 2) ; bleu foncé #000091.
# Écharpe du maire (CGCT, art. D. 2122-4) : de l'épaule droite au côté gauche, bleu près du col, glands à franges d'or.
BLEU_FR, ROUGE_FR, BLANC_FR = "#000091", "#E1000F", "#FFFFFF"
import json as _json
_GEO = _json.loads(open("/home/claude/geo/europe_ouest.json").read())


def drapeau_fr(e=1.0):
    mat = Line([0, 0, 0], [0, 1.5 * e, 0], color=BOIS, stroke_width=6 * e)
    w, h = 0.27 * e, 0.6 * e; o = np.array([0.04 * e, 0.86 * e, 0])
    bandes = VGroup(*[Rectangle(width=w, height=h, fill_color=c, fill_opacity=1, stroke_width=0).move_to(o + [w * (k + 0.5), h / 2, 0]) for k, c in enumerate((BLEU_FR, BLANC_FR, ROUGE_FR))])
    cadre = Rectangle(width=3 * w, height=h, color=CREME, stroke_width=2.5 * e).move_to(bandes)
    return VGroup(mat, bandes, cadre)


def echarpe_fr(p, h):
    """Écharpe tricolore portée de l'épaule droite (à gauche de l'image) au côté gauche ; bleu près du col."""
    a = np.array([-0.17 * h, 0.66 * h, 0]); b = np.array([0.16 * h, 0.12 * h, 0]); d = b - a; n = np.array([-d[1], d[0], 0]) / np.linalg.norm(d)
    l = 0.05 * h; bandes = VGroup()
    for k, c in enumerate((BLEU_FR, BLANC_FR, ROUGE_FR)):     # k = 0 : bande du côté du col (en haut à droite de la diagonale)
        o1 = (1.5 - k) * l; o2 = (0.5 - k) * l
        bandes.add(Polygon(a + o1 * n, b + o1 * n, b + o2 * n, a + o2 * n, fill_color=c, fill_opacity=1, stroke_color=ENCRE, stroke_width=0.8))
    glands = VGroup(*[Line(b + [x * h, -0.01 * h, 0], b + [x * h + 0.01 * h, -0.11 * h, 0], color="#E8B931", stroke_width=3.2) for x in (-0.03, 0.0, 0.03)])
    return VGroup(bandes, glands)


def maire(h=1.4, humeur="decide"):
    """Le maire : silhouette claire, écharpe tricolore."""
    p = _bh(h, CREME); p.h = h; p.add(echarpe_fr(p, h)); _vivant(p, 0.03 * h); visage(p, h, humeur)
    return p


def participant(h=1.05, humeur="neutre"):
    """Le participant : une couleur fixe (ambre), proportions ordinaires, sans caricature."""
    p = _bh(h, AMBRE); p.h = h; _vivant(p, 0.03 * h); visage(p, h, humeur)
    return p


def organisateur(h=1.35, humeur="content"):
    """La société organisatrice : personnage lilas, une mallette à la main."""
    p = _bh(h, LILAS); p.h = h; _vivant(p, 0.03 * h); visage(p, h, humeur)
    p.add(mallette(0.42).move_to(main_de(p, 1) + 0.18 * DOWN + 0.1 * RIGHT))
    return p


def spectateurs(n=4, h=1.05):
    cols = [MENTHE, CIEL, LILAS, CREME, MENTHE, CIEL]
    g = VGroup(*[_bh(h * (0.94 + 0.06 * (k % 2)), cols[k % len(cols)]) for k in range(n)]).arrange(RIGHT, buff=0.12, aligned_edge=DOWN)
    for b in g: b.h = h; _vivant(b, 0.03 * h); visage(b, h, "neutre")
    return g


def casque(e=1.0, couleur=CIEL):
    cal = Sector(radius=0.36 * e, angle=PI, start_angle=0, fill_color=couleur, fill_opacity=1, stroke_color=ENCRE, stroke_width=2 * e)
    vis = Rectangle(width=0.86 * e, height=0.09 * e, fill_color=ENCRE, fill_opacity=1, stroke_width=0).next_to(cal, DOWN, buff=0)
    bande = Line([-0.05 * e, 0.36 * e, 0], [-0.05 * e, 0.0, 0], color=CREME, stroke_width=4 * e)
    return VGroup(cal, bande, vis)


def tapis(l=2.2, couleur=CIEL):
    t = RoundedRectangle(corner_radius=0.08, width=l, height=0.32, fill_color=couleur, fill_opacity=1, stroke_color=ENCRE, stroke_width=2)
    plis = VGroup(*[Line([x, -0.12, 0], [x, 0.12, 0], color=ENCRE, stroke_width=1.5).set_opacity(0.5) for x in np.linspace(-l / 2 + 0.3, l / 2 - 0.3, 5)])
    return VGroup(t, plis.move_to(t))


def contrat(e=1.0, signe=True):
    f = RoundedRectangle(corner_radius=0.06 * e, width=1.1 * e, height=1.4 * e, fill_color=CREME, fill_opacity=1, stroke_width=0)
    tt = T("CONTRAT", int(13 * e), ENCRE).move_to(f.get_top() + 0.2 * e * DOWN)
    lg = VGroup(*[Line([-0.38 * e, 0, 0], [0.38 * e, 0, 0], color=BLEU_3, stroke_width=3 * e) for _ in range(3)]).arrange(DOWN, buff=0.14 * e).move_to(f.get_center() + 0.02 * e * DOWN)
    g = VGroup(f, tt, lg)
    if signe:
        g.add(VMobject(stroke_color=ENCRE, stroke_width=2.5 * e).set_points_smoothly([f.get_bottom() + np.array([x * e, 0.22 * e + 0.05 * e * np.sin(9 * x), 0]) for x in np.linspace(-0.35, 0.35, 9)]))
    return g


def billets(e=1.0, texte="10 000 francs"):
    bl = VGroup(*[RoundedRectangle(corner_radius=0.05 * e, width=1.2 * e, height=0.62 * e, fill_color="#B7DDB0", fill_opacity=1, stroke_color=ENCRE, stroke_width=2 * e).shift(k * 0.08 * e * (UP + RIGHT)) for k in range(3)])
    rond = Circle(0.16 * e, color=ENCRE, stroke_width=2 * e).move_to(bl[-1])
    t = T(texte, int(18 * e), CREME).next_to(bl, DOWN, buff=0.1 * e)
    return VGroup(bl, rond, t)


def mairie(e=1.0):
    corps = Rectangle(width=2.6 * e, height=1.3 * e, fill_color=CREME, fill_opacity=1, stroke_width=0)
    toit_ = Polygon([-1.45 * e, 0, 0], [1.45 * e, 0, 0], [0, 0.55 * e, 0], fill_color=ENCRE, fill_opacity=1, stroke_width=0).next_to(corps, UP, buff=0)
    horloge = VGroup(Circle(0.16 * e, fill_color=CREME, fill_opacity=1, stroke_color=ENCRE, stroke_width=2 * e), Line(ORIGIN, [0, 0.1 * e, 0], color=ENCRE, stroke_width=2 * e), Line(ORIGIN, [0.08 * e, 0, 0], color=ENCRE, stroke_width=2 * e)).move_to(toit_.get_center() + 0.05 * e * DOWN)
    fen = VGroup(*[RoundedRectangle(corner_radius=0.04 * e, width=0.32 * e, height=0.42 * e, fill_color=BLEU_3, fill_opacity=1, stroke_width=0) for _ in range(5)]).arrange(RIGHT, buff=0.16 * e).move_to(corps.get_center() + 0.25 * e * UP)
    porte_ = RoundedRectangle(corner_radius=0.12 * e, width=0.42 * e, height=0.55 * e, fill_color=ENCRE, fill_opacity=1, stroke_width=0).align_to(corps, DOWN)
    ens = VGroup(RoundedRectangle(corner_radius=0.05 * e, width=1.25 * e, height=0.26 * e, fill_color=ENCRE, fill_opacity=1, stroke_width=0), T("MAIRIE", int(14 * e), CREME)).move_to(corps.get_center() + 0.2 * e * DOWN + 0.68 * e * LEFT)
    dr = drapeau_fr(0.7 * e); dr.move_to(toit_.get_top() + [0.18 * e, 0.45 * e, 0])
    return VGroup(dr, corps, toit_, horloge, fen, porte_, ens)


def discotheque(e=1.0, nom="Embassy Club"):
    corps = RoundedRectangle(corner_radius=0.1 * e, width=3.0 * e, height=1.6 * e, fill_color="#2B2450", fill_opacity=1, stroke_color=LILAS, stroke_width=3 * e)
    ens = VGroup(RoundedRectangle(corner_radius=0.1 * e, width=2.5 * e, height=0.45 * e, fill_color=ENCRE, fill_opacity=1, stroke_color=AMBRE, stroke_width=3 * e), T(nom, int(19 * e), AMBRE)).move_to(corps.get_top() + 0.05 * e * UP)
    porte_ = RoundedRectangle(corner_radius=0.1 * e, width=0.55 * e, height=0.8 * e, fill_color=ENCRE, fill_opacity=1, stroke_color=LILAS, stroke_width=2 * e).align_to(corps, DOWN)
    notes = VGroup(*[VGroup(Circle(0.07 * e, fill_color=c, fill_opacity=1, stroke_width=0), Line([0.07 * e, 0, 0], [0.07 * e, 0.28 * e, 0], color=c, stroke_width=3 * e)).move_to(corps.get_center() + [x * e, y * e, 0]) for x, y, c in ((-0.95, 0.1, MENTHE), (0.95, 0.05, CIEL), (-0.6, -0.4, LILAS), (0.62, -0.42, AMBRE))])
    boule = VGroup(Circle(0.2 * e, fill_color=GRIS, fill_opacity=1, stroke_color=CREME, stroke_width=2 * e), *[Line([-0.2 * e, y * e, 0], [0.2 * e, y * e, 0], color=CREME, stroke_width=1).set_opacity(0.6) for y in (-0.08, 0.0, 0.08)]).move_to(corps.get_center() + 0.25 * e * UP)
    return VGroup(corps, porte_, notes, boule, ens)


def affiche(e=1.0, l1="Ce soir", l2="Attraction"):
    f = RoundedRectangle(corner_radius=0.06 * e, width=1.5 * e, height=1.9 * e, fill_color=AMBRE, fill_opacity=1, stroke_color=ENCRE, stroke_width=2 * e)
    etoile = Star(5, outer_radius=0.3 * e, inner_radius=0.13 * e, fill_color=CREME, fill_opacity=1, stroke_width=0).move_to(f.get_center() + 0.35 * e * UP)
    t = VGroup(T(l1, int(15 * e), ENCRE, False), T(l2, int(17 * e), ENCRE)).arrange(DOWN, buff=0.06 * e).move_to(f.get_center() + 0.45 * e * DOWN)
    return VGroup(f, etoile, t)


def palais(e=1.0, nom=None):
    """Juridiction administrative française : façade à colonnes, drapeau tricolore."""
    t = tribunal(2.6 * e); dr = drapeau_fr(0.75 * e).next_to(t, UP, buff=-0.25 * e).shift(0.9 * e * RIGHT)
    g = VGroup(dr, t)
    if nom: g.add(puce(nom, int(20 * e + 2)).next_to(t, DOWN, buff=0.18))
    return g


def conseil_etat(e=1.0, nom=True):
    """Le Conseil d'État (Palais-Royal) : longue façade à arcades sur deux niveaux, drapeau tricolore."""
    corps = Rectangle(width=4.4 * e, height=1.5 * e, fill_color=CREME, fill_opacity=1, stroke_width=0)
    corniche = Rectangle(width=4.6 * e, height=0.16 * e, fill_color=ENCRE, fill_opacity=1, stroke_width=0).next_to(corps, UP, buff=0)
    arc = VGroup(*[VGroup(Rectangle(width=0.34 * e, height=0.42 * e, fill_color=BLEU_3, fill_opacity=1, stroke_width=0), Sector(radius=0.17 * e, angle=PI, start_angle=0, fill_color=BLEU_3, fill_opacity=1, stroke_width=0).shift(0.21 * e * UP)).arrange(UP, buff=0) for _ in range(9)]).arrange(RIGHT, buff=0.13 * e).move_to(corps.get_center() + 0.37 * e * DOWN)
    fen = VGroup(*[Rectangle(width=0.26 * e, height=0.36 * e, fill_color=BLEU_3, fill_opacity=1, stroke_width=0) for _ in range(9)]).arrange(RIGHT, buff=0.21 * e).move_to(corps.get_center() + 0.42 * e * UP)
    fronton = Polygon([-0.8 * e, 0, 0], [0.8 * e, 0, 0], [0, 0.38 * e, 0], fill_color=CREME, fill_opacity=1, stroke_color=ENCRE, stroke_width=2 * e).next_to(corniche, UP, buff=0)
    dr = drapeau_fr(0.75 * e).move_to(fronton.get_top() + [0.2 * e, 0.5 * e, 0])
    g = VGroup(dr, corps, corniche, fronton, arc, fen)
    if nom: g.add(puce("Conseil d'État", int(22 * e + 2)).next_to(corps, DOWN, buff=0.18))
    return g


def code_fr(l1="Code", l2="des communes", e=1.0):
    f = RoundedRectangle(corner_radius=0.06 * e, width=1.9 * e, height=2.5 * e, fill_color="#8FA8F0", fill_opacity=1, stroke_width=0)
    dos = Rectangle(width=0.2 * e, height=2.5 * e, fill_color=BLEU_4, fill_opacity=1, stroke_width=0).align_to(f, LEFT)
    tri = VGroup(*[Rectangle(width=0.16 * e, height=0.3 * e, fill_color=c, fill_opacity=1, stroke_width=0) for c in (BLEU_FR, BLANC_FR, ROUGE_FR)]).arrange(RIGHT, buff=0).move_to(f.get_bottom() + 0.4 * e * UP)
    t = VGroup(T(l1, int(22 * e), ENCRE), T(l2, int(17 * e), ENCRE, False)).arrange(DOWN, buff=0.08 * e).move_to(f.get_center() + 0.35 * e * UP)
    return VGroup(f, dos, tri, t)


def tuile(s, couleur=CREME, l=2.3, h=0.7, taille=21, texte_c=ENCRE):
    f = RoundedRectangle(corner_radius=0.12, width=l, height=h, fill_color=couleur, fill_opacity=1, stroke_width=0)
    t = VGroup(*[T(x, taille, texte_c) for x in s.split("\n")]).arrange(DOWN, buff=0.05).move_to(f)
    return VGroup(f, t)


def ordre_public(e=1.0, tuiles=("Bon ordre", "Sûreté", "Sécurité", "Salubrité")):
    """L'ordre public : un cadre titré, ses composantes en tuiles (standard de la série française)."""
    ts = VGroup(*[tuile(x) for x in tuiles]).arrange_in_grid(rows=2, buff=0.18)
    cadre = RoundedRectangle(corner_radius=0.22, width=ts.width + 0.6, height=ts.height + 1.15, fill_color=BLEU_3, fill_opacity=1, stroke_color=CREME, stroke_width=3)
    cadre.move_to(ts.get_center() + 0.25 * UP)
    titre_ = T("ORDRE PUBLIC", 24).move_to(cadre.get_top() + 0.33 * DOWN)
    g = VGroup(cadre, titre_, ts).scale(e); g.cadre, g.titre, g.tuiles = cadre, titre_, ts
    return g


def tuile_dignite(e=1.0):
    return tuile("Dignité de la\npersonne humaine", AMBRE, 3.0, 0.95, 21).scale(e)


def balance(e=1.0, g_=None, d_=None, angle=0.0):
    """Une balance : deux plateaux ; contenu facultatif posé sur chaque plateau."""
    pied = VGroup(Line([0, -1.1 * e, 0], [0, 0.9 * e, 0], color=CREME, stroke_width=7 * e), RoundedRectangle(corner_radius=0.06, width=1.2 * e, height=0.16 * e, fill_color=CREME, fill_opacity=1, stroke_width=0).move_to([0, -1.15 * e, 0]))
    fleau = Line([-1.8 * e, 0.9 * e, 0], [1.8 * e, 0.9 * e, 0], color=CREME, stroke_width=7 * e)
    def plateau(x):
        fils = VGroup(Line([x * e, 0.9 * e, 0], [x * e - 0.55 * e, 0.1 * e, 0], color=CREME, stroke_width=2.5 * e), Line([x * e, 0.9 * e, 0], [x * e + 0.55 * e, 0.1 * e, 0], color=CREME, stroke_width=2.5 * e))
        pl = ArcBetweenPoints([x * e - 0.65 * e, 0.1 * e, 0], [x * e + 0.65 * e, 0.1 * e, 0], angle=PI / 2, color=CREME, stroke_width=6 * e)
        return VGroup(fils, pl)
    pg, pd = plateau(-1.8), plateau(1.8)
    g = VGroup(pied, fleau, pg, pd); g.pg, g.pd, g.fleau = pg, pd, fleau
    if g_ is not None: g_.move_to(pg[1].get_center() + 0.35 * e * UP); pg.add(g_)
    if d_ is not None: d_.move_to(pd[1].get_center() + 0.35 * e * UP); pd.add(d_)
    return g


def pencher(bal, angle):
    """Animation : le fléau pivote, les plateaux descendent ou montent avec lui."""
    c = bal.fleau.get_center(); dy = 1.8 * np.sin(angle) * bal.fleau.width / 3.6
    return AnimationGroup(Rotate(bal.fleau, angle, about_point=c), bal.pg.animate.shift(dy * UP), bal.pd.animate.shift(dy * DOWN))


def projette(lon, lat, k=0.62, lon0=2.5, lat0=46.6):
    return np.array([(lon - lon0) * np.cos(np.radians(lat0)) * k, (lat - lat0) * k, 0])


def carte_france(k=0.62, suisse=True):
    """France métropolitaine (Natural Earth, world-atlas 10m) ; la Suisse en repère, plus claire."""
    def poly(pts, pas, **st):
        return Polygon(*[projette(x, y, k) for x, y in pts[::pas]], **st)
    fr = VGroup(*[poly(p, 6 if len(p) > 1000 else 2, fill_color=CREME, fill_opacity=1, stroke_color=ENCRE, stroke_width=2) for p in _GEO["France"] if len(p) > 30])
    g = VGroup(fr); g.fr = fr
    if suisse:
        ch = poly(_GEO["Switzerland"][0], 3, fill_color=CREME, fill_opacity=0.35, stroke_color=CREME, stroke_width=1.5)
        g.add(ch); g.ch = ch
    g.k = k
    return g


PARIS = (2.3522, 48.8566); MORSANG = (2.3461, 48.6618)   # coordonnées vérifiées (Morsang-sur-Orge : 48°39′42″ N, 2°20′46″ E)


def reperes(carte):
    """Repère invisible de Paris, ajouté à la carte (il suit ses déplacements) : carte.paris.get_center()."""
    d = Dot(projette(*PARIS, carte.k), radius=0.01).set_opacity(0); carte.add(d); carte.paris = d
    return carte


# ---------- Petites icônes de la série française ----------
def chaine(e=1.0, couleur=GRIS):
    m = VGroup(*[Ellipse(width=0.62 * e, height=0.34 * e, color=couleur, stroke_width=9 * e).rotate(0.0 if k % 2 == 0 else 0.0).move_to([k * 0.45 * e, 0, 0]) for k in range(4)])
    for k in range(1, 4, 2): m[k].stretch(0.55, 1)
    return m.move_to(ORIGIN)


def eclair(e=1.0, couleur=AMBRE):
    return Polygon([0.1 * e, 0.5 * e, 0], [-0.25 * e, -0.02 * e, 0], [0.0, -0.02 * e, 0], [-0.12 * e, -0.5 * e, 0], [0.28 * e, 0.08 * e, 0], [0.03 * e, 0.08 * e, 0], fill_color=couleur, fill_opacity=1, stroke_color=ENCRE, stroke_width=2 * e)


def panneau_danger(e=1.0):
    tri = Triangle(fill_color=CREME, fill_opacity=1, stroke_color=ROUGE, stroke_width=8 * e).scale(0.55 * e)
    return VGroup(tri, T("!", int(40 * e), ENCRE).move_to(tri.get_center() + 0.06 * e * DOWN))


def desordre(e=1.0):
    return VGroup(*[RoundedRectangle(corner_radius=0.04 * e, width=0.45 * e, height=0.4 * e, fill_color=c, fill_opacity=1, stroke_color=ENCRE, stroke_width=2 * e).rotate(a).move_to([x * e, y * e, 0])
                    for x, y, a, c in ((-0.35, -0.2, 0.3, AMBRE), (0.15, -0.22, -0.2, MENTHE), (-0.08, 0.2, 0.7, CIEL), (0.45, 0.12, 1.1, LILAS))])


def bagarre(e=1.0):
    a = _bh(0.9 * e, MENTHE); b = _bh(0.9 * e, CIEL); visage(a, 0.9 * e, "decide"); visage(b, 0.9 * e, "decide")
    g = VGroup(a, b).arrange(RIGHT, buff=0.55 * e, aligned_edge=DOWN); ec = eclair(0.75 * e).move_to(g.get_center() + 0.15 * e * UP)
    return VGroup(g, ec)


def quartier(e=1.0):
    """La commune vue de près : quelques maisons."""
    return VGroup(*[maison(x * e, y * e, 0.8 * e, 0.55 * e, e) for x, y in ((-0.9, 0.0), (0.0, 0.25), (0.9, -0.05))])


def boutique(e=1.0):
    corps = Rectangle(width=1.4 * e, height=0.9 * e, fill_color=CREME, fill_opacity=1, stroke_width=0)
    store = VGroup(*[Polygon([x * e, 0, 0], [(x + 0.28) * e, 0, 0], [(x + 0.28) * e, -0.3 * e, 0], [x * e, -0.3 * e, 0], fill_color=c, fill_opacity=1, stroke_width=0) for x, c in zip(np.arange(-0.7, 0.7, 0.28), [ROUGE, CREME, ROUGE, CREME, ROUGE])]).next_to(corps, UP, buff=-0.05)
    vit = Rectangle(width=0.8 * e, height=0.45 * e, fill_color=CIEL, fill_opacity=1, stroke_width=0).move_to(corps.get_center() + 0.12 * e * DOWN + 0.2 * e * LEFT)
    return VGroup(corps, store, vit)


def bobine(e=1.0):
    c = Circle(0.5 * e, fill_color=GRIS, fill_opacity=1, stroke_color=ENCRE, stroke_width=3 * e)
    trous = VGroup(*[Circle(0.12 * e, fill_color=ENCRE, fill_opacity=1, stroke_width=0).move_to(0.27 * e * np.array([np.cos(a), np.sin(a), 0])) for a in np.linspace(0, TAU, 6)[:-1]])
    pel = Rectangle(width=0.9 * e, height=0.28 * e, fill_color=ENCRE, fill_opacity=1, stroke_width=0).next_to(c, RIGHT, buff=-0.1 * e).shift(0.32 * e * DOWN)
    return VGroup(pel, c, trous)


def livres(e=1.0, texte="Grands arrêts"):
    cols = (CIEL, AMBRE, MENTHE)
    g = VGroup(*[RoundedRectangle(corner_radius=0.04 * e, width=2.0 * e, height=0.32 * e, fill_color=c, fill_opacity=1, stroke_color=ENCRE, stroke_width=2 * e).shift(k * 0.33 * e * UP + (0.06 * (k % 2) - 0.03) * e * RIGHT) for k, c in enumerate(cols)])
    t = T(texte, int(15 * e), ENCRE).move_to(g[-1])
    return VGroup(g, t)


def ecran(e=1.0):
    f = RoundedRectangle(corner_radius=0.1 * e, width=1.8 * e, height=1.15 * e, fill_color=ENCRE, fill_opacity=1, stroke_color=CREME, stroke_width=3 * e)
    jeu = Triangle(fill_color=CREME, fill_opacity=1, stroke_width=0).rotate(-PI / 2).scale(0.22 * e).move_to(f)
    pied = Rectangle(width=0.5 * e, height=0.12 * e, fill_color=CREME, fill_opacity=1, stroke_width=0).next_to(f, DOWN, buff=0.06 * e)
    return VGroup(f, jeu, pied)


def insigne_police(e=1.0):
    et = Star(6, outer_radius=0.32 * e, inner_radius=0.2 * e, fill_color=OR_S, fill_opacity=1, stroke_color=ENCRE, stroke_width=2 * e)
    t = T("Police municipale", int(18 * e), CREME)
    return VGroup(et, t).arrange(RIGHT, buff=0.15 * e)


def vignette(x, ok, a, b=None, l=6.0, h=4.0, y=-0.65, taille=24):
    """Cadre d'une vignette (standard « distinction juridique ») : titre coché ou barré, ou neutre (ok=None, pastille ambre)."""
    f = RoundedRectangle(corner_radius=0.2, width=l, height=h, fill_color=BLEU_3, fill_opacity=0.55, stroke_width=0).move_to([x, y, 0])
    if ok is None:
        t = VGroup(VGroup(Circle(0.26, fill_color=AMBRE, fill_opacity=1, stroke_width=0), T("?", 22, ENCRE)), VGroup(*[T(z, taille) for z in (a, b) if z]).arrange(DOWN, buff=0.05)).arrange(RIGHT, buff=0.2)
    else:
        t = ligne_coche(ok, a, b, taille)
    t.move_to(f.get_top() + (0.55 if b else 0.4) * DOWN)
    g = VGroup(f, t); g.f, g.t = f, t
    return g


def date_fr(jour_mois, annee):
    return calendrier(jour_mois.upper(), annee)


def piece_fr(e=1.0):
    """Une pièce en francs français (1991-1995 : avant l'euro)."""
    return VGroup(Circle(0.42 * e, fill_color=OR_S, fill_opacity=1, stroke_color=ENCRE, stroke_width=3 * e), Circle(0.31 * e, color=BOIS, stroke_width=2 * e), T("F", int(30 * e), ENCRE))


def pencher(bal, angle):
    """Le fléau pivote ; le plateau du côté qui descend suit son extrémité (angle > 0 : la gauche descend)."""
    c = bal.fleau.get_center(); dy = 1.8 * np.sin(angle) * bal.fleau.width / 3.6
    return AnimationGroup(Rotate(bal.fleau, angle, about_point=c), bal.pg.animate.shift(dy * DOWN), bal.pd.animate.shift(dy * UP))
