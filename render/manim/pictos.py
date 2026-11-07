"""Pictogrammes supplémentaires, au trait (série Constitution, mais utilisables partout).

Chaque fonction renvoie la liste des formes d'un pictogramme centré à l'origine, d'environ 1,2 unité de côté.
Les formes « pleines » sont remplies de la couleur du fond : le décor ne se voit pas à travers.
Pas de croix (ni suisse ni Croix-Rouge : emblèmes protégés) ; pas de symbole religieux ni de drapeau.
"""

import numpy as np
from manim import (Arc, Circle, Dot, Ellipse, Line, Polygon, Rectangle, RoundedRectangle, VGroup, VMobject,
                   Annulus, Sector, PI, UP, DOWN, LEFT, RIGHT)

import charte as c

E = 4  # épaisseur du trait


def _p():
    return dict(fill_color=c.FOND, fill_opacity=1)


def L(a, b, w=E, col=None):
    return Line([a[0], a[1], 0], [b[0], b[1], 0], color=col or c.TEXTE, stroke_width=w)


def R(w, h, x=0, y=0, r=0.06, plein=True, col=None, sw=E):
    return RoundedRectangle(corner_radius=r, width=w, height=h, color=col or c.TEXTE, stroke_width=sw,
                            **(_p() if plein else {})).move_to([x, y, 0])


def C(r, x=0, y=0, plein=True, col=None, sw=E):
    return Circle(radius=r, color=col or c.TEXTE, stroke_width=sw, **(_p() if plein else {})).move_to([x, y, 0])


def P(*pts, plein=True, col=None, sw=E):
    return Polygon(*[[x, y, 0] for x, y in pts], color=col or c.TEXTE, stroke_width=sw, **(_p() if plein else {}))


def courbe(*pts, col=None, sw=E):
    v = VMobject(color=col or c.TEXTE, stroke_width=sw)
    v.set_points_smoothly([[x, y, 0] for x, y in pts])
    return v


def maison():
    return [P((-0.55, -0.5), (0.55, -0.5), (0.55, 0.15), (0, 0.6), (-0.55, 0.15)),
            R(0.26, 0.4, -0.12, -0.3, r=0.02), R(0.22, 0.2, 0.28, 0.0, r=0.02)]


def ecole():
    corps = R(1.3, 0.75, 0, -0.2, r=0.02)
    toit = P((-0.75, 0.17), (0.75, 0.17), (0, 0.55))
    cloche = VGroup(L((0, 0.55), (0, 0.72)), C(0.08, 0, 0.62, plein=False))
    porte = R(0.25, 0.4, 0, -0.38, r=0.02)
    fen = [R(0.22, 0.2, x, -0.05, r=0.02) for x in (-0.42, 0.42)]
    return [corps, toit, cloche, porte, *fen]


def usine():
    corps = P((-0.7, -0.5), (0.7, -0.5), (0.7, 0.05), (0.35, -0.15), (0.35, 0.05), (0.0, -0.15), (0.0, 0.05),
              (-0.35, -0.15), (-0.35, 0.05), (-0.7, 0.05))
    chem = R(0.18, 0.75, -0.55, 0.35, r=0.0)
    fumee = courbe((-0.55, 0.8), (-0.4, 0.92), (-0.5, 1.02), (-0.3, 1.1), sw=3)
    return [chem, corps, fumee]


def train():
    caisse = R(1.5, 0.7, 0, 0.0, r=0.14)
    vitres = [R(0.3, 0.24, x, 0.1, r=0.03, plein=False) for x in (-0.45, 0.0, 0.45)]
    roues = [C(0.12, x, -0.42) for x in (-0.45, 0.45)]
    rail = L((-0.85, -0.55), (0.85, -0.55))
    perche = VGroup(L((0, 0.35), (0.2, 0.6)), L((0.2, 0.6), (-0.1, 0.72)))
    return [perche, caisse, *vitres, rail, *roues]


def camion():
    benne = R(1.0, 0.7, -0.25, 0.05, r=0.03)
    cabine = P((0.3, -0.3), (0.75, -0.3), (0.75, 0.05), (0.6, 0.3), (0.3, 0.3))
    vitre = P((0.4, 0.05), (0.62, 0.05), (0.55, 0.22), (0.4, 0.22), plein=False, sw=3)
    roues = [C(0.15, x, -0.35) for x in (-0.5, 0.0, 0.55)]
    return [benne, cabine, vitre, *roues]


def avion():
    fuselage = Ellipse(width=1.6, height=0.28, color=c.TEXTE, stroke_width=E, **_p())
    aile = P((-0.15, 0.0), (0.25, 0.0), (-0.15, -0.55), (-0.35, -0.55))
    aile2 = P((-0.15, 0.0), (0.2, 0.0), (-0.1, 0.4), (-0.28, 0.4))
    derive = P((-0.62, 0.05), (-0.78, 0.4), (-0.66, 0.4), (-0.5, 0.08))
    return [aile2, derive, fuselage, aile]


def pont():
    tablier = L((-0.8, 0.0), (0.8, 0.0), w=5)
    arche = Arc(radius=0.55, start_angle=0, angle=PI, color=c.TEXTE, stroke_width=E).move_to([0, -0.3, 0])
    piles = [L((x, 0.0), (x, -0.55)) for x in (-0.8, 0.8)]
    eau = courbe((-0.9, -0.6), (-0.45, -0.52), (0, -0.6), (0.45, -0.52), (0.9, -0.6), sw=3)
    return [tablier, arche, *piles, eau]


def route():
    bords = [L((-0.25, 0.55), (-0.7, -0.55)), L((0.25, 0.55), (0.7, -0.55))]
    tirets = [L((0, 0.45 - 0.32 * k), (0, 0.3 - 0.32 * k), w=5) for k in range(4)]
    return [*bords, *tirets]


def panneau():
    # Panneau routier rond (vitesse limitée, sans chiffre) sur son mât.
    return [L((0, -0.6), (0, 0.05)), C(0.38, 0, 0.3, sw=6), C(0.22, 0, 0.3, plein=False, sw=2)]


def montagne():
    massif = P((-0.85, -0.5), (-0.25, 0.45), (0.05, 0.05), (0.3, 0.3), (0.85, -0.5))
    neige = courbe((-0.43, 0.17), (-0.32, 0.1), (-0.2, 0.2), (-0.1, 0.12), (-0.05, 0.16), sw=3)
    return [massif, neige]


def arbre():
    return [L((0, -0.55), (0, 0.0), w=5), C(0.42, 0, 0.25)]


def sapin():
    return [L((0, -0.6), (0, -0.35), w=5), P((-0.45, -0.35), (0.45, -0.35), (0, 0.15)),
            P((-0.35, 0.0), (0.35, 0.0), (0, 0.45)), P((-0.25, 0.3), (0.25, 0.3), (0, 0.65))]


def foret():
    return [m.shift(RIGHT * dx + DOWN * 0.05) for dx in (-0.55, 0.55) for m in sapin()] + \
           [m.scale(1.15).shift(UP * 0.1) for m in sapin()]


def fleur():
    tige = L((0, -0.6), (0, 0.05))
    feuille = Ellipse(width=0.3, height=0.14, color=c.TEXTE, stroke_width=3, **_p()).rotate(0.5).move_to([0.14, -0.3, 0])
    petales = [C(0.13, 0.17 * np.cos(a), 0.22 + 0.17 * np.sin(a)) for a in np.linspace(0, 2 * PI, 6)[:-1]]
    return [tige, feuille, *petales, C(0.09, 0, 0.22)]


def vache():
    corps = R(1.1, 0.5, 0, 0.05, r=0.2)
    tete = R(0.35, 0.32, 0.65, 0.2, r=0.1)
    cornes = [L((0.55, 0.36), (0.5, 0.48), w=3), L((0.75, 0.36), (0.8, 0.48), w=3)]
    pattes = [L((x, -0.2), (x, -0.5)) for x in (-0.38, -0.2, 0.2, 0.38)]
    tache = Ellipse(width=0.3, height=0.2, color=c.TEXTE, stroke_width=0, fill_color=c.TEXTE, fill_opacity=0.8).move_to([-0.15, 0.1, 0])
    queue = courbe((-0.55, 0.15), (-0.68, 0.0), (-0.65, -0.18), sw=3)
    return [*pattes, queue, corps, tache, tete, *cornes]


def poisson():
    corps = Ellipse(width=0.95, height=0.5, color=c.TEXTE, stroke_width=E, **_p())
    queue = P((-0.45, 0.0), (-0.8, 0.25), (-0.8, -0.25))
    oeil = Dot([0.25, 0.06, 0], radius=0.04, color=c.TEXTE)
    return [queue, corps, oeil]


def oiseau():
    return [courbe((-0.6, 0.1), (-0.3, 0.3), (0, 0.0), sw=5), courbe((0, 0.0), (0.3, 0.3), (0.6, 0.1), sw=5)]


def epi():
    tige = courbe((0, -0.6), (0.05, -0.1), (0, 0.5))
    grains = [Ellipse(width=0.16, height=0.28, color=c.TEXTE, stroke_width=3, **_p())
              .rotate(s * 0.6).move_to([s * 0.12, -0.05 + 0.18 * k, 0]) for k in range(4) for s in (-1, 1)]
    return [tige, *grains]


def coeur():
    return [courbe((0, -0.5), (-0.35, -0.15), (-0.5, 0.15), (-0.35, 0.38), (-0.12, 0.35), (0, 0.2), sw=5),
            courbe((0, -0.5), (0.35, -0.15), (0.5, 0.15), (0.35, 0.38), (0.12, 0.35), (0, 0.2), sw=5),
            courbe((-0.32, 0.0), (-0.12, 0.0), (-0.04, 0.15), (0.06, -0.15), (0.14, 0.0), (0.32, 0.0), sw=3)]


def adn():
    t = np.linspace(-0.6, 0.6, 40)
    b1 = courbe(*[(0.28 * np.sin(5 * y), y) for y in t], sw=4)
    b2 = courbe(*[(-0.28 * np.sin(5 * y), y) for y in t], sw=4)
    barreaux = [L((0.28 * np.sin(5 * y), y), (-0.28 * np.sin(5 * y), y), w=2) for y in np.linspace(-0.5, 0.5, 8)]
    return [*barreaux, b1, b2]


def eprouvette():
    tube = VGroup(L((-0.15, 0.55), (-0.15, -0.35)), L((0.15, 0.55), (0.15, -0.35)),
                  Arc(radius=0.15, start_angle=PI, angle=PI, color=c.TEXTE, stroke_width=E).move_to([0, -0.42, 0]),
                  L((-0.22, 0.55), (0.22, 0.55)))
    liquide = L((-0.15, -0.1), (0.15, -0.1), w=3)
    bulles = [C(0.04, 0.03, 0.05, plein=False, sw=2), C(0.03, -0.05, 0.15, plein=False, sw=2)]
    return [tube, liquide, *bulles]


def seringue():
    corps = R(0.9, 0.24, 0, 0, r=0.03)
    graduations = [L((x, 0.12), (x, 0.0), w=2) for x in (-0.2, 0.0, 0.2)]
    piston = VGroup(L((-0.45, 0), (-0.7, 0)), L((-0.7, 0.15), (-0.7, -0.15)))
    aiguille = L((0.45, 0), (0.75, 0), w=2)
    return [VGroup(corps, *graduations, piston, aiguille).rotate(0.6)]


def pilule():
    a = RoundedRectangle(corner_radius=0.17, width=0.85, height=0.34, color=c.TEXTE, stroke_width=E, **_p())
    return [a.rotate(0.6), L((-0.1, 0.13), (0.1, -0.13)).rotate(0.0)]


def fauteuil():
    roue = C(0.35, 0.0, -0.2, plein=False)
    dossier = VGroup(L((-0.25, 0.55), (-0.25, 0.05)), L((-0.25, 0.05), (0.35, 0.05)), L((0.35, 0.05), (0.45, -0.35)))
    tete = C(0.1, -0.05, 0.62)
    return [roue, dossier, tete, C(0.07, 0.45, -0.48, plein=False, sw=3)]


def berceau():
    nacelle = Arc(radius=0.55, start_angle=PI, angle=PI, color=c.TEXTE, stroke_width=E).move_to([0, -0.05, 0])
    bord = L((-0.55, 0.0), (0.55, 0.0))
    tete = C(0.13, -0.25, 0.1)
    patins = courbe((-0.6, -0.55), (0, -0.62), (0.6, -0.55))
    return [nacelle, bord, patins, tete]


def canne():
    # L'âge : une canne et un dos courbé, en silhouette simple.
    tete = C(0.12, 0.05, 0.5)
    dos = courbe((0.0, 0.38), (-0.12, 0.15), (-0.08, -0.15))
    jambes = [L((-0.08, -0.15), (-0.2, -0.6)), L((-0.08, -0.15), (0.05, -0.6))]
    bras = L((-0.05, 0.2), (0.3, -0.05))
    canne_ = L((0.3, -0.05), (0.35, -0.6), w=3)
    return [tete, dos, *jambes, bras, canne_]


def enveloppe():
    corps = R(1.0, 0.65, 0, 0, r=0.03)
    rabat = VGroup(L((-0.5, 0.32), (0, -0.05)), L((0, -0.05), (0.5, 0.32)))
    return [corps, rabat]


def passeport():
    livret = R(0.7, 0.95, 0, 0, r=0.05)
    globe = VGroup(C(0.18, 0, 0.1, plein=False, sw=3), Ellipse(width=0.16, height=0.36, color=c.TEXTE, stroke_width=2).move_to([0, 0.1, 0]),
                   L((-0.18, 0.1), (0.18, 0.1), w=2))
    lignes = [L((-0.2, -0.22 - 0.1 * k), (0.2, -0.22 - 0.1 * k), w=2) for k in range(2)]
    return [livret, globe, *lignes]


def carte_identite():
    carte = R(1.0, 0.65, 0, 0, r=0.06)
    tete = VGroup(C(0.09, -0.27, 0.07, plein=False, sw=3), Arc(radius=0.15, start_angle=0, angle=PI, color=c.TEXTE, stroke_width=3).move_to([-0.27, -0.12, 0]))
    lignes = [L((0.0, 0.12 - 0.15 * k), (0.35, 0.12 - 0.15 * k), w=2) for k in range(3)]
    return [carte, tete, *lignes]


def camera():
    corps = R(0.75, 0.5, -0.1, 0, r=0.06)
    objectif = P((0.28, 0.12), (0.6, 0.25), (0.6, -0.25), (0.28, -0.12))
    bobines = [C(0.14, x, 0.42) for x in (-0.3, 0.05)]
    return [*bobines, corps, objectif]


def micro():
    tete = RoundedRectangle(corner_radius=0.17, width=0.34, height=0.55, color=c.TEXTE, stroke_width=E, **_p()).move_to([0, 0.25, 0])
    berceau_ = Arc(radius=0.27, start_angle=PI, angle=PI, color=c.TEXTE, stroke_width=E).move_to([0, 0.05, 0])
    pied = VGroup(L((0, -0.22), (0, -0.5)), L((-0.22, -0.5), (0.22, -0.5)))
    return [berceau_, tete, pied]


def antenne():
    mat = VGroup(L((0, 0.2), (-0.3, -0.6)), L((0, 0.2), (0.3, -0.6)), L((-0.15, -0.2), (0.15, -0.2), w=3))
    ondes = [Arc(radius=r, start_angle=-0.7, angle=1.4, color=c.TEXTE, stroke_width=3).move_arc_center_to([0, 0.25, 0]) for r in (0.2, 0.38)]
    ondes2 = [Arc(radius=r, start_angle=PI - 0.7, angle=1.4, color=c.TEXTE, stroke_width=3).move_arc_center_to([0, 0.25, 0]) for r in (0.2, 0.38)]
    return [mat, Dot([0, 0.25, 0], radius=0.06, color=c.TEXTE), *ondes, *ondes2]


def journal():
    page = R(1.0, 0.75, 0, 0, r=0.02)
    titre = L((-0.38, 0.22), (0.38, 0.22), w=7)
    photo = R(0.32, 0.28, -0.22, -0.1, r=0.0, plein=False, sw=3)
    lignes = [L((0.05, 0.03 - 0.1 * k), (0.38, 0.03 - 0.1 * k), w=2) for k in range(3)]
    return [page, titre, photo, *lignes]


def livre():
    gauche = P((0, -0.35), (-0.65, -0.25), (-0.65, 0.45), (0, 0.35))
    droite = P((0, -0.35), (0.65, -0.25), (0.65, 0.45), (0, 0.35))
    lignes = [L((s * 0.15, 0.2 - 0.12 * k), (s * 0.5, 0.25 - 0.12 * k), w=2) for s in (-1, 1) for k in range(4)]
    return [gauche, droite, *lignes]


def diplome():
    toque = P((-0.6, 0.25), (0, 0.5), (0.6, 0.25), (0, 0.0))
    calotte = P((-0.32, 0.12), (-0.32, -0.15), (0.32, -0.15), (0.32, 0.12))
    gland = VGroup(L((0.45, 0.2), (0.45, -0.15), w=3), Dot([0.45, -0.18, 0], radius=0.05, color=c.TEXTE))
    return [calotte, toque, gland]


def eclair():
    return [P((0.1, 0.6), (-0.3, -0.05), (0.0, -0.05), (-0.15, -0.6), (0.35, 0.1), (0.05, 0.1), (0.25, 0.6))]


def goutte():
    return [courbe((0, 0.6), (-0.2, 0.2), (-0.32, -0.15), (-0.2, -0.42), (0, -0.48), (0.2, -0.42), (0.32, -0.15), (0.2, 0.2), (0, 0.6), sw=5),
            Arc(radius=0.18, start_angle=PI, angle=0.9, color=c.TEXTE, stroke_width=3).move_arc_center_to([0, -0.18, 0])]


def barrage():
    mur = P((-0.25, 0.5), (0.05, 0.5), (0.25, -0.55), (-0.25, -0.55))
    lac = [courbe((-0.85, 0.35 - 0.18 * k), (-0.6, 0.4 - 0.18 * k), (-0.4, 0.35 - 0.18 * k), sw=3) for k in range(3)]
    sortie = [L((0.3, -0.3 - 0.1 * k), (0.7, -0.3 - 0.1 * k), w=2) for k in range(3)]
    return [*lac, mur, *sortie]


def eolienne():
    mat = P((-0.05, 0.25), (0.05, 0.25), (0.1, -0.6), (-0.1, -0.6))
    pales = [L((0, 0.3), (0.55 * np.cos(a), 0.3 + 0.55 * np.sin(a)), w=5) for a in (PI / 2, PI / 2 + 2 * PI / 3, PI / 2 + 4 * PI / 3)]
    return [mat, *pales, C(0.07, 0, 0.3)]


def solaire():
    panneau_ = P((-0.6, -0.1), (0.4, -0.1), (0.65, 0.35), (-0.35, 0.35))
    grille = [L((-0.6 + 0.333 * k, -0.1), (-0.35 + 0.333 * k, 0.35), w=2) for k in (1, 2)] + [L((-0.48, 0.12), (0.52, 0.12), w=2)]
    pied = L((0.0, -0.1), (0.0, -0.55))
    soleil = [C(0.13, 0.55, 0.62, plein=False, sw=3)]
    return [pied, panneau_, *grille, *soleil]


def casque():
    # Casque militaire de profil : calotte arrondie, bord évasé, jugulaire.
    calotte = courbe((-0.6, -0.1), (-0.5, 0.3), (-0.1, 0.52), (0.35, 0.42), (0.6, 0.05), (0.62, -0.1), sw=5)
    bord = courbe((-0.75, -0.18), (-0.6, -0.1), (0.62, -0.1), (0.78, -0.2), sw=5)
    bande = L((-0.52, 0.05), (0.56, 0.05), w=2)
    jugulaire = courbe((-0.35, -0.12), (-0.2, -0.42), (0.2, -0.42), (0.35, -0.12), sw=3)
    return [calotte, bord, bande, jugulaire]


def cadenas():
    anse = Arc(radius=0.25, start_angle=0, angle=PI, color=c.TEXTE, stroke_width=5).move_to([0, 0.32, 0])
    corps = R(0.75, 0.55, 0, -0.15, r=0.06)
    trou = VGroup(C(0.06, 0, -0.1, sw=3), L((0, -0.15), (0, -0.28), w=3))
    return [L((-0.25, 0.2), (-0.25, 0.12), w=5), L((0.25, 0.2), (0.25, 0.12), w=5), anse, corps, trou]


def cle():
    anneau = C(0.2, -0.45, 0, plein=False, sw=5)
    tige = L((-0.25, 0), (0.6, 0), w=5)
    dents = [L((0.4, 0), (0.4, -0.18), w=5), L((0.55, 0), (0.55, -0.14), w=5)]
    return [anneau, tige, *dents]


def sablier():
    haut, bas = L((-0.35, 0.55), (0.35, 0.55), w=6), L((-0.35, -0.55), (0.35, -0.55), w=6)
    verre = P((-0.28, 0.55), (0.28, 0.55), (0.04, 0.0), (0.28, -0.55), (-0.28, -0.55), (-0.04, 0.0))
    sable = P((-0.18, -0.55), (0.18, -0.55), (0, -0.3), plein=False, sw=0)
    sable.set_fill(c.TEXTE, opacity=0.8)
    sable2 = P((-0.15, 0.4), (0.15, 0.4), (0, 0.1), plein=False, sw=0)
    sable2.set_fill(c.TEXTE, opacity=0.8)
    return [verre, sable, sable2, haut, bas]


def horloge():
    return [C(0.5), L((0, 0), (0, 0.32), w=5), L((0, 0), (0.22, -0.1), w=5), Dot([0, 0, 0], radius=0.05, color=c.TEXTE)]


def calendrier():
    feuille = R(0.95, 0.9, 0, -0.05, r=0.05)
    entete = L((-0.47, 0.22), (0.47, 0.22), w=4)
    anneaux = [L((x, 0.35), (x, 0.52), w=5) for x in (-0.25, 0.25)]
    cases = [R(0.13, 0.11, -0.3 + 0.2 * i, 0.05 - 0.17 * j, r=0.01, plein=False, sw=2) for i in range(4) for j in range(3)]
    return [feuille, entete, *anneaux, *cases]


def loupe():
    return [L((0.18, -0.18), (0.55, -0.55), w=8), C(0.32, -0.1, 0.1), Arc(radius=0.2, start_angle=1.8, angle=1.0, color=c.TEXTE, stroke_width=3).move_arc_center_to([-0.1, 0.1, 0])]


def marteau():
    # Marteau de juge (maillet) et son socle.
    tete = R(0.6, 0.26, -0.05, 0.25, r=0.05).rotate(0.6)
    manche = L((0.05, 0.2), (0.55, -0.3), w=6)
    socle = R(0.7, 0.14, -0.15, -0.45, r=0.03)
    return [socle, manche, tete]


def main_levee():
    paume = R(0.42, 0.45, 0, -0.1, r=0.12)
    doigts = [RoundedRectangle(corner_radius=0.05, width=0.1, height=h, color=c.TEXTE, stroke_width=3, **_p())
              .move_to([x, 0.12 + h / 2, 0]) for x, h in zip((-0.15, -0.05, 0.05, 0.15), (0.3, 0.38, 0.36, 0.28))]
    pouce = RoundedRectangle(corner_radius=0.05, width=0.1, height=0.28, color=c.TEXTE, stroke_width=3, **_p()).rotate(0.8).move_to([-0.3, -0.02, 0])
    poignet = R(0.3, 0.25, 0, -0.45, r=0.02)
    return [poignet, pouce, *doigts, paume]


def globe():
    return [C(0.55), Ellipse(width=0.5, height=1.1, color=c.TEXTE, stroke_width=3), L((-0.55, 0), (0.55, 0), w=3),
            courbe((-0.48, 0.27), (0, 0.32), (0.48, 0.27), sw=3), courbe((-0.48, -0.27), (0, -0.32), (0.48, -0.27), sw=3)]


def traite():
    # Un accord international : deux feuilles signées et un sceau à rubans.
    f1 = R(0.75, 0.95, -0.15, 0.08, r=0.02)
    f2 = R(0.75, 0.95, 0.1, -0.05, r=0.02)
    lignes = [L((-0.15, 0.25 - 0.14 * k), (0.35, 0.25 - 0.14 * k), w=2) for k in range(3)]
    sceau = VGroup(L((0.3, -0.4), (0.22, -0.68), w=4), L((0.3, -0.4), (0.4, -0.68), w=4), C(0.14, 0.3, -0.35))
    return [f1, f2, *lignes, sceau]


def megaphone():
    cone = P((-0.35, 0.12), (0.4, 0.45), (0.4, -0.45), (-0.35, -0.12))
    poignee = L((-0.15, -0.12), (-0.2, -0.45), w=5)
    arriere = R(0.18, 0.3, -0.45, 0, r=0.04)
    ondes = [Arc(radius=r, start_angle=-0.6, angle=1.2, color=c.TEXTE, stroke_width=3).move_arc_center_to([0.3, 0, 0]) for r in (0.35, 0.5)]
    return [poignee, arriere, cone, *ondes]


def graphique():
    axes = VGroup(L((-0.6, 0.55), (-0.6, -0.5)), L((-0.6, -0.5), (0.65, -0.5)))
    barres = [R(0.22, h, -0.35 + 0.32 * k, -0.5 + h / 2, r=0.0) for k, h in enumerate((0.35, 0.6, 0.85))]
    return [axes, *barres]


def pourcent():
    return [C(0.15, -0.3, 0.3, plein=False, sw=5), C(0.15, 0.3, -0.3, plein=False, sw=5), L((0.4, 0.5), (-0.4, -0.5), w=5)]


def drapeau_blanc():  # pour les armistices / la paix : un drapeau uni, sans emblème
    return [L((-0.4, -0.6), (-0.4, 0.6), w=5), P((-0.4, 0.55), (0.5, 0.45), (0.45, 0.05), (-0.4, 0.1))]


def colombe():
    corps = courbe((-0.55, 0.0), (-0.2, 0.15), (0.2, 0.1), (0.45, 0.25), sw=5)
    aile = courbe((-0.15, 0.12), (0.0, 0.5), (0.25, 0.55), (0.15, 0.15), sw=4)
    queue = courbe((-0.55, 0.0), (-0.3, -0.15), (0.1, -0.1), (0.2, 0.1), sw=4)
    rameau = VGroup(L((0.45, 0.25), (0.65, 0.05), w=3), Ellipse(width=0.14, height=0.07, color=c.TEXTE, stroke_width=2).move_to([0.58, 0.18, 0]))
    return [corps, aile, queue, rameau]


def poignee_main():
    # Deux mains qui se serrent (accord, collaboration) : deux poignets qui se rejoignent.
    g = VGroup(R(0.45, 0.3, -0.55, 0, r=0.04), P((-0.33, 0.15), (0.05, 0.2), (0.15, 0.0), (-0.33, -0.15)))
    d = VGroup(R(0.45, 0.3, 0.55, 0, r=0.04), P((0.33, 0.15), (-0.05, 0.05), (-0.1, -0.2), (0.33, -0.15)))
    return [g, d]


def chantier():  # construction : grue simple
    mat = VGroup(L((-0.3, -0.6), (-0.3, 0.55)), L((-0.15, -0.6), (-0.15, 0.55)))
    fleche_ = L((-0.5, 0.55), (0.65, 0.55))
    cable = L((0.45, 0.55), (0.45, 0.0), w=2)
    charge = R(0.24, 0.18, 0.45, -0.08, r=0.02)
    return [mat, fleche_, cable, charge]


def tente():  # asile, hébergement
    return [P((-0.65, -0.5), (0.65, -0.5), (0, 0.5)), P((-0.15, -0.5), (0.15, -0.5), (0, -0.05), plein=False, sw=3)]


def cible():
    return [C(0.55), C(0.35), C(0.15), Dot([0, 0, 0], radius=0.05, color=c.TEXTE)]


def pompe():  # carburant, huiles minérales
    corps = R(0.55, 0.95, -0.1, -0.05, r=0.05)
    ecran = R(0.32, 0.22, -0.1, 0.2, r=0.02, plein=False, sw=3)
    tuyau = courbe((0.18, 0.2), (0.38, 0.15), (0.4, -0.2), (0.32, -0.3), sw=3)
    return [corps, ecran, tuyau]


def tabac():
    cig = R(0.95, 0.14, 0, 0, r=0.02)
    filtre = L((0.28, 0.07), (0.28, -0.07), w=3)
    fumee = courbe((-0.48, 0.1), (-0.4, 0.3), (-0.52, 0.45), (-0.42, 0.6), sw=3)
    return [cig, filtre, fumee]


def billet():
    b = R(1.0, 0.55, 0, 0, r=0.03)
    rond = C(0.15, 0, 0, plein=False, sw=3)
    return [b, rond, C(0.04, -0.35, 0.15, plein=False, sw=2), C(0.04, 0.35, -0.15, plein=False, sw=2)]


def banque():
    fronton = P((-0.7, 0.25), (0.7, 0.25), (0, 0.6))
    colonnes = [R(0.1, 0.55, -0.48 + 0.32 * k, -0.08, r=0.0) for k in range(4)]
    socle = R(1.4, 0.12, 0, -0.42, r=0.0)
    return [fronton, *colonnes, socle]


def tirelire():
    corps = Ellipse(width=1.0, height=0.7, color=c.TEXTE, stroke_width=E, **_p())
    fente = L((-0.12, 0.35), (0.12, 0.35), w=5)
    pattes = [L((x, -0.28), (x, -0.5), w=5) for x in (-0.25, 0.25)]
    groin = R(0.12, 0.2, 0.52, 0.0, r=0.04)
    return [*pattes, corps, groin, fente, Dot([0.3, 0.12, 0], radius=0.035, color=c.TEXTE)]


def bulletin():  # bulletin de vote avec une coche
    feuille = R(0.7, 0.9, 0, 0, r=0.02)
    cases = [R(0.15, 0.15, -0.15, 0.2 - 0.3 * k, r=0.01, plein=False, sw=3) for k in range(2)]
    coche = VGroup(L((-0.2, 0.2), (-0.15, 0.13), w=4), L((-0.15, 0.13), (-0.05, 0.3), w=4))
    lignes = [L((0.0, 0.2 - 0.3 * k), (0.25, 0.2 - 0.3 * k), w=2) for k in range(2)]
    return [feuille, *cases, coche, *lignes]


def signature():  # liste de signatures (initiative, référendum)
    feuille = R(0.75, 0.95, 0, 0, r=0.02)
    traits = [courbe((-0.25, 0.3 - 0.18 * k), (-0.1, 0.38 - 0.18 * k), (0.0, 0.26 - 0.18 * k), (0.12, 0.35 - 0.18 * k), (0.25, 0.3 - 0.18 * k), sw=3)
              for k in range(4)]
    return [feuille, *traits]


def stylo():
    return [VGroup(R(0.9, 0.14, 0, 0, r=0.05), P((0.45, 0.07), (0.62, 0.0), (0.45, -0.07))).rotate(0.6)]


def ampoule():  # recherche, innovation
    verre = courbe((-0.12, -0.25), (-0.3, 0.05), (-0.25, 0.35), (0, 0.5), (0.25, 0.35), (0.3, 0.05), (0.12, -0.25), sw=5)
    culot = [L((-0.13, -0.32 - 0.09 * k), (0.13, -0.32 - 0.09 * k), w=4) for k in range(3)]
    return [verre, *culot]


def velo_simple():
    return []


def roue_dentee():  # économie, industrie
    dents = [R(0.16, 0.2, 0.48 * np.cos(a), 0.48 * np.sin(a), r=0.02).rotate(a) for a in np.linspace(0, 2 * PI, 9)[:-1]]
    return [*dents, C(0.42), C(0.14, plein=False)]


def sac_courses():  # consommation
    sac = P((-0.4, 0.2), (0.4, 0.2), (0.32, -0.55), (-0.32, -0.55))
    anses = [Arc(radius=0.12, start_angle=0, angle=PI, color=c.TEXTE, stroke_width=4).move_to([x, 0.28, 0]) for x in (-0.18, 0.18)]
    return [*anses, sac]


def chien():
    corps = R(0.8, 0.32, 0, 0, r=0.14)
    tete = C(0.17, 0.48, 0.22)
    oreille = P((0.42, 0.35), (0.35, 0.15), (0.45, 0.2))
    pattes = [L((x, -0.15), (x, -0.45)) for x in (-0.28, 0.25)]
    queue = L((-0.4, 0.05), (-0.58, 0.28))
    return [*pattes, queue, corps, tete, oreille]


def chasse():  # chasse et pêche : canne à pêche
    canne_ = L((-0.6, -0.55), (0.45, 0.55), w=4)
    fil = courbe((0.45, 0.55), (0.55, 0.2), (0.5, -0.2), sw=2)
    hamecon = Arc(radius=0.07, start_angle=PI, angle=PI, color=c.TEXTE, stroke_width=3).move_to([0.5, -0.25, 0])
    return [canne_, fil, hamecon]


def casino():  # jeux d'argent : un dé
    de = R(0.75, 0.75, 0, 0, r=0.12)
    points = [Dot([x, y, 0], radius=0.06, color=c.TEXTE) for x, y in ((-0.2, 0.2), (0, 0), (0.2, -0.2), (0.2, 0.2), (-0.2, -0.2))]
    return [de, *points]


def fusil_croise():  # armes (art. 107) : silhouette de pistolet, sobre
    corps = P((-0.55, 0.2), (0.55, 0.2), (0.55, 0.0), (-0.1, 0.0), (-0.2, -0.45), (-0.45, -0.45), (-0.35, 0.0), (-0.55, 0.0))
    return [corps]


def silhouette_foule():
    return []


def poste():  # poste et télécommunications : cor postal générique (cor de chasse)
    cor = VGroup(Arc(radius=0.35, start_angle=0.3, angle=2 * PI - 0.6, color=c.TEXTE, stroke_width=5),
                 P((0.32, 0.12), (0.62, 0.32), (0.62, -0.32), (0.32, -0.12)))
    return [cor]


def bateau():
    coque = P((-0.65, -0.1), (0.65, -0.1), (0.45, -0.4), (-0.45, -0.4))
    mat = L((0, -0.1), (0, 0.6))
    voile = P((0.05, 0.55), (0.45, -0.02), (0.05, -0.02))
    return [mat, voile, coque]


def velo_():
    return []


def poignee():
    # Deux mains qui se serrent, vues de côté : deux manches et des doigts entrelacés.
    manche_g = R(0.42, 0.34, -0.62, -0.05, r=0.04)
    manche_d = R(0.42, 0.34, 0.62, -0.05, r=0.04)
    main_g = P((-0.41, 0.12), (0.05, 0.22), (0.25, 0.08), (0.05, -0.05), (-0.41, -0.2))
    main_d = P((0.41, 0.12), (0.12, 0.12), (-0.18, -0.05), (-0.1, -0.22), (0.41, -0.2))
    doigts = [L((-0.05 + 0.1 * k, -0.06), (0.02 + 0.1 * k, -0.2), w=3) for k in range(3)]
    return [manche_g, manche_d, main_g, main_d, *doigts]


def atome():
    orbites = [Ellipse(width=1.2, height=0.42, color=c.TEXTE, stroke_width=3).rotate(a) for a in (0, PI / 3, 2 * PI / 3)]
    return [*orbites, C(0.1, plein=False, sw=0).set_fill(c.TEXTE, 1)]


def cerf():
    corps = R(0.8, 0.34, 0, 0, r=0.15)
    cou = L((0.32, 0.1), (0.45, 0.42), w=5)
    tete = Ellipse(width=0.3, height=0.16, color=c.TEXTE, stroke_width=E, **_p()).rotate(-0.4).move_to([0.55, 0.45, 0])
    bois = [L((0.45, 0.52), (0.35, 0.85), w=3), L((0.39, 0.68), (0.25, 0.75), w=3),
            L((0.55, 0.52), (0.7, 0.85), w=3), L((0.63, 0.68), (0.78, 0.72), w=3)]
    pattes = [L((x, -0.15), (x, -0.55)) for x in (-0.3, -0.15, 0.18, 0.32)]
    return [*pattes, cou, corps, tete, *bois]


def telepherique():
    cable = L((-0.85, 0.55), (0.85, 0.25), w=3)
    suspente = L((0, 0.4), (0, 0.15), w=3)
    cabine = R(0.6, 0.5, 0, -0.1, r=0.06)
    vitre = R(0.42, 0.18, 0, -0.02, r=0.02, plein=False, sw=3)
    return [cable, suspente, cabine, vitre]


def satellite():
    corps = R(0.32, 0.32, 0, 0, r=0.03).rotate(PI / 4)
    panneaux = [R(0.45, 0.22, s * 0.45, s * 0.45, r=0.0).rotate(PI / 4) for s in (-1, 1)]
    antenne_ = Arc(radius=0.15, start_angle=PI / 4 + PI / 2, angle=PI, color=c.TEXTE, stroke_width=3).move_to([0.22, -0.22, 0])
    return [*panneaux, corps, antenne_]


def poubelle():
    bac = P((-0.35, 0.3), (0.35, 0.3), (0.28, -0.55), (-0.28, -0.55))
    couvercle = L((-0.45, 0.38), (0.45, 0.38), w=5)
    poignee_ = R(0.24, 0.1, 0, 0.47, r=0.03, plein=False, sw=3)
    stries = [L((x, 0.15), (x * 0.85, -0.42), w=2) for x in (-0.15, 0, 0.15)]
    return [bac, couvercle, poignee_, *stries]


def anneaux():
    return [C(0.3, -0.18, -0.05, plein=False, sw=5), C(0.3, 0.18, -0.05, plein=False, sw=5),
            P((0.12, 0.3), (0.24, 0.3), (0.3, 0.4), (0.18, 0.48), (0.06, 0.4), sw=3)]


def palette():
    corps = courbe((0.1, -0.5), (-0.4, -0.38), (-0.6, 0.0), (-0.35, 0.42), (0.15, 0.48), (0.55, 0.22), (0.5, -0.05),
                   (0.25, -0.08), (0.2, -0.3), (0.1, -0.5), sw=4)
    trou = C(0.08, 0.22, 0.12, plein=False, sw=3)
    taches = [C(0.07, x, y, plein=False, sw=0).set_fill(c.TEXTE, 0.9) for x, y in ((-0.3, 0.15), (-0.1, 0.32), (-0.3, -0.15), (0.0, -0.25))]
    pinceau = L((0.35, -0.55), (0.75, 0.0), w=4)
    return [corps, trou, *taches, pinceau]


def bus():
    caisse = R(1.5, 0.75, 0, 0.05, r=0.1)
    vitres = [R(0.26, 0.24, -0.5 + 0.33 * k, 0.17, r=0.03, plein=False, sw=3) for k in range(4)]
    porte = R(0.2, 0.42, 0.58, -0.04, r=0.02, plein=False, sw=3)
    roues = [C(0.14, x, -0.38) for x in (-0.45, 0.4)]
    return [caisse, *vitres, porte, *roues]


def flocon():
    branches = []
    for k in range(6):
        a = k * PI / 3
        d = np.array([np.cos(a), np.sin(a)])
        branches.append(L((0, 0), tuple(0.55 * d), w=4))
        for t in (0.3, 0.42):
            base = t * d
            for s in (-1, 1):
                b = np.array([np.cos(a + s * 0.7), np.sin(a + s * 0.7)])
                branches.append(L(tuple(base), tuple(base + 0.14 * b), w=3))
    return branches


def thermometre():
    tube = RoundedRectangle(corner_radius=0.1, width=0.2, height=0.95, color=c.TEXTE, stroke_width=E, **_p()).move_to([0, 0.12, 0])
    boule = C(0.18, 0, -0.42)
    mercure = VGroup(L((0, -0.3), (0, 0.25), w=6), C(0.1, 0, -0.42, plein=False, sw=0).set_fill(c.TEXTE, 1))
    graduations = [L((0.14, 0.4 - 0.15 * k), (0.25, 0.4 - 0.15 * k), w=2) for k in range(4)]
    return [tube, boule, mercure, *graduations]


FONCTIONS = {n: f for n, f in globals().items() if callable(f) and f.__module__ == __name__
             and n not in ("L", "R", "C", "P", "courbe", "_p") and not n.startswith("_")}
FONCTIONS.pop("silhouette_foule", None)
FONCTIONS.pop("velo_simple", None)
FONCTIONS.pop("velo_", None)
for _n in ("colombe", "poignee_main", "poste"):
    FONCTIONS.pop(_n, None)
FONCTIONS["fusil"] = FONCTIONS.pop("fusil_croise")


def dessiner(nom):
    if nom not in FONCTIONS:
        return None
    return FONCTIONS[nom]()
