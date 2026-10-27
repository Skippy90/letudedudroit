"""Éléments graphiques de la charte (docs/charte-visuelle.md), pour Manim.

Chaque classe dessine un élément du vocabulaire de la charte et expose des méthodes
qui renvoient des animations. Les positions sont fixes pour que deux éléments ne se
chevauchent pas : titres en haut, schéma au centre, bloc d'article centré en bas,
renvoi « vidéo N » en bas à droite.
"""

from manim import (
    DOWN, LEFT, RIGHT, UP, Arc, Circle, Create, Dot, Ellipse, FadeIn, FadeOut, GrowArrow,
    Line, Polygon, Rectangle, RoundedRectangle, Text, Transform, VGroup, Write, Arrow,
    CurvedArrow, there_and_back,
)

# Couleurs de la charte
FOND = "#0F1B2D"
TEXTE = "#F2EFE6"
ACCENT = "#E3A52F"
VERT = "#4CAF7D"
GRIS = "#6B7280"
ROUGE = "#D9534F"
SURFACE = "#1B2B44"  # fond des blocs, un cran plus clair que le fond

# Une couleur fixe par personnage, choisie dans visuals.md
COULEURS_PERSONNAGES = {
    "bleu_clair": "#7FB3E6",
    "ambre_pale": "#F0C987",
    "rose": "#E6A1C1",
    "violet": "#A78BFA",
    "turquoise": "#5EC8C0",
}
ETATS = {"vert": VERT, "gris": GRIS, "ambre": ACCENT, "neutre": SURFACE}

POLICE = "Inter"
# Tailles Manim ; 34 est le plus petit corps utilisé (au-dessus des 28 points de la charte
# sur une image 1920 × 1080).
T_TITRE, T_SOUS_TITRE, T_CORPS, T_PETIT = 58, 42, 40, 34

X_POSITIONS = {"gauche": -4.5, "centre-gauche": -2.2, "centre": 0.0, "centre-droite": 2.2, "droite": 4.5}
Y_TITRE, Y_SOUS_TITRE = 3.15, 2.35
Y_PERSONNAGE = 0.6
Y_FRISE = -1.9


def texte(contenu, taille=T_CORPS, couleur=TEXTE, gras=False):
    return Text(contenu, font=POLICE, font_size=taille, color=couleur, weight="BOLD" if gras else "NORMAL")


def mots(contenu: str) -> int:
    """Nombre de mots affichés (les numéros de liste et la ponctuation ne comptent pas)."""
    return sum(1 for m in contenu.replace("’", "'").split() if any(c.isalpha() for c in m))


class Personnage(VGroup):
    """Silhouette sans visage, couleur fixe, nom en dessous."""

    def __init__(self, nom, couleur, position):
        tete = Circle(radius=0.38, color=couleur, fill_color=couleur, fill_opacity=1, stroke_width=0)
        corps = RoundedRectangle(corner_radius=0.5, width=1.25, height=1.55, color=couleur,
                                 fill_color=couleur, fill_opacity=1, stroke_width=0)
        corps.next_to(tete, DOWN, buff=0.08)
        silhouette = VGroup(tete, corps)
        etiquette = texte(nom, T_PETIT).next_to(silhouette, DOWN, buff=0.2)
        super().__init__(silhouette, etiquette)
        self.silhouette, self.etiquette, self.nom = silhouette, etiquette, nom
        self.move_to([X_POSITIONS[position], Y_PERSONNAGE - 0.2, 0])
        self.position = position

    def vers_le_centre(self):
        return LEFT if X_POSITIONS[self.position] > 0 else RIGHT


class BlocArticle(VGroup):
    """La loi : bloc « Art. N CP », toujours centré en bas."""

    def __init__(self, libelle):
        etiquette = texte(libelle, T_CORPS, gras=True)
        cadre = RoundedRectangle(corner_radius=0.12, width=etiquette.width + 0.9, height=0.85,
                                 color=TEXTE, stroke_width=3, fill_color=SURFACE, fill_opacity=1)
        etiquette.move_to(cadre)
        super().__init__(cadre, etiquette)
        self.move_to([0, -3.35, 0])
        self.cadre, self.libelle = cadre, libelle


class Batiment(VGroup):
    """L'infraction : trois étages, Typicité en bas."""

    NOMS = ["Typicité", "Illicéité", "Culpabilité"]

    def __init__(self):
        self.etages = []
        groupe = []
        for i, nom in enumerate(self.NOMS):
            cadre = Rectangle(width=4.6, height=1.05, color=TEXTE, stroke_width=3,
                              fill_color=SURFACE, fill_opacity=1)
            cadre.move_to([0, -2.05 + i * 1.05, 0])
            etiquette = texte(nom, T_CORPS).move_to(cadre)
            etage = VGroup(cadre, etiquette)
            self.etages.append(etage)
            groupe.append(etage)
        sommet_etages = -2.05 + 2.5 * 1.05  # haut du troisième étage
        toit = Polygon([-2.6, sommet_etages, 0], [2.6, sommet_etages, 0], [0, sommet_etages + 0.8, 0],
                       color=TEXTE, stroke_width=3)
        super().__init__(*groupe, toit)

    def construire(self, vide=False):
        # Le schéma se construit devant le spectateur, de bas en haut ; « vide » laisse
        # les noms des étages à écrire un par un (etage-nom).
        if vide:
            for e in self.etages:
                e[1].set_opacity(0)
            return [Create(e[0]) for e in self.etages] + [Create(self[-1])]
        return [Create(e[0]) for e in self.etages] + [Write(e[1]) for e in self.etages] + [Create(self[-1])]

    def colorer(self, n, etat):
        cadre = self.etages[n - 1][0]
        return cadre.animate.set_fill(ETATS[etat], opacity=0.85 if etat != "neutre" else 1)


class Bouclier(VGroup):
    """Un fait justificatif : bouclier, à droite du bâtiment ou du personnage."""

    def __init__(self, centre):
        forme = Polygon([-0.7, 0.8, 0], [0.7, 0.8, 0], [0.7, 0.0, 0], [0, -0.9, 0], [-0.7, 0.0, 0],
                        color=TEXTE, stroke_width=5, fill_color=SURFACE, fill_opacity=1)
        bande = Line([0, 0.8, 0], [0, -0.9, 0], color=ACCENT, stroke_width=6)
        super().__init__(forme, bande)
        self.move_to(centre)


class Livre(VGroup):
    """Le Code pénal, fermé puis ouvert (élément du script de référence)."""

    def __init__(self, titre="Code pénal", x=0.0, largeur=3.3, hauteur=3.0, etiquette_dessous=False):
        couverture = RoundedRectangle(corner_radius=0.08, width=largeur, height=hauteur, color=TEXTE,
                                      stroke_width=3, fill_color=SURFACE, fill_opacity=1)
        dos = Line(couverture.get_corner(UP + LEFT) + RIGHT * 0.25, couverture.get_corner(DOWN + LEFT) + RIGHT * 0.25,
                   color=TEXTE, stroke_width=2)
        if etiquette_dessous:
            nom = texte(titre, T_PETIT).next_to(couverture, DOWN, buff=0.25)
        else:
            # Titre sur la couverture, décalé à droite du dos, sans jamais déborder.
            nom = texte(titre, T_PETIT).move_to(couverture).shift(RIGHT * 0.12)
            if nom.width > largeur - 0.6:
                raise ValueError(f"Titre trop long pour la couverture : {titre!r}")
        super().__init__(couverture, dos, nom)
        self.move_to([x, 0.4, 0])
        self.couverture = couverture

    def ouvert(self):
        gauche = Rectangle(width=2.4, height=2.6, color=TEXTE, stroke_width=3, fill_color=SURFACE, fill_opacity=1)
        droite = gauche.copy().next_to(gauche, RIGHT, buff=0)
        lignes = VGroup(*[Line([-1.0, 0.8 - 0.35 * k, 0], [0.9, 0.8 - 0.35 * k, 0], color=GRIS, stroke_width=2)
                          for k in range(6)])
        pages = VGroup(gauche, droite, lignes.copy().move_to(gauche), lignes.copy().move_to(droite))
        return pages.move_to(self.couverture.get_center())


class Liste(VGroup):
    """Liste numérotée à gauche de l'écran."""

    def __init__(self):
        super().__init__()
        self.elements = []

    def nouvel_element(self, contenu):
        element = texte(contenu, 46)
        element.move_to([-6.2, 1.3 - 1.1 * len(self.elements), 0], aligned_edge=LEFT)
        self.elements.append(element)
        self.add(element)
        return element


class Cases(VGroup):
    """Cases à cocher, une par condition."""

    def __init__(self):
        super().__init__()
        self.lignes = []

    def nouvelle_case(self, contenu):
        boite = RoundedRectangle(corner_radius=0.08, width=0.6, height=0.6, color=TEXTE, stroke_width=3)
        etiquette = texte(contenu, T_CORPS)
        # À droite du centre : la moitié gauche reste libre pour une silhouette et sa bulle.
        # Un libellé trop long est réduit pour rester dans l'image.
        if etiquette.width > 5.4:
            etiquette.scale_to_fit_width(5.4)
        etiquette.next_to(boite, RIGHT, buff=0.35)
        ligne = VGroup(boite, etiquette)
        ligne.move_to([0.3, 1.1 - 0.95 * len(self.lignes), 0], aligned_edge=LEFT)
        self.lignes.append(ligne)
        self.add(ligne)
        return ligne

    def marque(self, n, etat):
        boite = self.lignes[n - 1][0]
        if etat == "vert":
            signe = VGroup(Line([-0.17, 0, 0], [-0.04, -0.15, 0], color=FOND, stroke_width=7),
                           Line([-0.04, -0.15, 0], [0.2, 0.17, 0], color=FOND, stroke_width=7)).move_to(boite)
            return boite.animate.set_fill(VERT, opacity=1), signe
        if etat == "gris":
            signe = Line([-0.15, 0, 0], [0.15, 0, 0], color=FOND, stroke_width=7).move_to(boite)
            return boite.animate.set_fill(GRIS, opacity=1), signe
        signe = texte("?", T_CORPS, ACCENT, gras=True).move_to(boite)  # « question »
        return boite.animate.set_stroke(ACCENT), signe


class Pyramide(VGroup):
    """Les autorités : trois niveaux, Tribunal fédéral au sommet."""

    NOMS = ["Première instance", "Recours cantonal", "Tribunal fédéral"]

    def __init__(self):
        niveaux = []
        for i, nom in enumerate(self.NOMS):
            bas, haut = 5.2 - 1.5 * i, 5.2 - 1.5 * (i + 1)
            y0, y1 = -1.6 + 1.1 * i, -1.6 + 1.1 * (i + 1)
            forme = Polygon([-bas / 2, y0, 0], [bas / 2, y0, 0], [haut / 2, y1, 0], [-haut / 2, y1, 0],
                            color=TEXTE, stroke_width=3, fill_color=SURFACE, fill_opacity=1)
            etiquette = texte(nom, 30 if i < 2 else 28).move_to(forme).shift(DOWN * 0.05)
            niveaux.append(VGroup(forme, etiquette))
        super().__init__(*niveaux)
        self.niveaux = niveaux
        self.shift(RIGHT * 2.6 + UP * 0.6)


class Frise(VGroup):
    """Le temps : frise horizontale, les repères se dessinent en direct."""

    def __init__(self):
        self.ligne = Arrow([-6.3, Y_FRISE, 0], [6.4, Y_FRISE, 0], color=TEXTE, stroke_width=4, buff=0,
                           max_tip_length_to_length_ratio=0.02)
        super().__init__(self.ligne)

    @staticmethod
    def x(fraction):
        return -6.0 + 12.0 * float(fraction)

    def repere(self, fraction, libelle):
        x = self.x(fraction)
        trait = Line([x, Y_FRISE - 0.35, 0], [x, Y_FRISE + 0.35, 0], color=ACCENT, stroke_width=6)
        etiquette = texte(libelle, T_PETIT, ACCENT).next_to(trait, DOWN, buff=0.15)
        return VGroup(trait, etiquette)

    def point(self, fraction, libelle):
        x = self.x(fraction)
        point = Dot([x, Y_FRISE, 0], radius=0.13, color=TEXTE)
        etiquette = texte(libelle, T_PETIT).next_to(point, UP, buff=0.25)
        return VGroup(point, etiquette)

    def zone(self, a, b, etat):
        xa, xb = self.x(a), self.x(b)
        return Rectangle(width=xb - xa, height=0.5, stroke_width=0, fill_color=ETATS[etat],
                         fill_opacity=0.35).move_to([(xa + xb) / 2, Y_FRISE, 0])

    def fleche_retour(self, de, vers, couleur):
        # Au-dessus des étiquettes des points, pour ne pas les masquer.
        return CurvedArrow([self.x(de), Y_FRISE + 1.0, 0], [self.x(vers), Y_FRISE + 1.0, 0],
                           angle=0.9, color=couleur, stroke_width=5)


class Bulle(VGroup):
    """L'état d'esprit : bulle de pensée au-dessus de la silhouette."""

    def __init__(self, personnage, contenu):
        etiquette = texte(contenu, T_PETIT, FOND)
        ellipse = Ellipse(width=max(2.2, etiquette.width + 0.8), height=1.1, color=TEXTE,
                          fill_color=TEXTE, fill_opacity=1)
        etiquette.move_to(ellipse)
        cote = personnage.vers_le_centre()
        tete = personnage.silhouette[0]
        # À côté de la tête, légèrement au-dessus, pour ne pas monter dans la zone des titres.
        ellipse_groupe = VGroup(ellipse, etiquette).next_to(tete, cote, buff=0.75)
        petites = VGroup(
            Circle(radius=0.07, color=TEXTE, fill_opacity=1).move_to(tete.get_center() + cote * 0.5 + UP * 0.1),
            Circle(radius=0.11, color=TEXTE, fill_opacity=1).move_to(tete.get_center() + cote * 0.75 + UP * 0.28),
        )
        # Jamais hors du cadre (largeur visible : de -7,1 à 7,1).
        if ellipse_groupe.get_right()[0] > 6.9:
            ellipse_groupe.shift(LEFT * (ellipse_groupe.get_right()[0] - 6.9))
        if ellipse_groupe.get_left()[0] < -6.9:
            ellipse_groupe.shift(RIGHT * (-6.9 - ellipse_groupe.get_left()[0]))
        super().__init__(petites, ellipse_groupe)


class Rembobinage(VGroup):
    """Une variante du cas : icône de rembobinage."""

    def __init__(self):
        a = Polygon([0, 0.5, 0], [0, -0.5, 0], [-0.8, 0, 0], color=ACCENT, fill_color=ACCENT, fill_opacity=1)
        b = a.copy().shift(RIGHT * 0.8)
        cercle = Circle(radius=1.1, color=ACCENT, stroke_width=5)
        super().__init__(cercle, VGroup(a, b).move_to(cercle))
        self.move_to([0, 0.6, 0])


class Jetons(VGroup):
    """L'argent : jetons qui passent d'une silhouette à l'autre."""

    def __init__(self, depart):
        jetons = [Circle(radius=0.22, color=ACCENT, stroke_width=4, fill_color=SURFACE, fill_opacity=1)
                  .move_to(depart + RIGHT * 0.15 * k + UP * 0.1 * k) for k in range(3)]
        super().__init__(*jetons)


class Colonnes(VGroup):
    """Deux notions côte à côte, séparées par un trait."""

    def __init__(self, a, b):
        self.mots = [texte(a, 56, gras=True), texte(b, 56, gras=True)]
        for mot, x in zip(self.mots, (-3.5, 3.5)):
            # Un libellé long est réduit pour ne pas toucher le trait central.
            if mot.width > 6.0:
                mot.scale_to_fit_width(6.0)
            mot.move_to([x, 0.6, 0])
        separation = Line([0, 1.7, 0], [0, -0.5, 0], color=GRIS, stroke_width=3)
        super().__init__(self.mots[0], separation, self.mots[1])


def barre(mobject):
    return Line(mobject.get_left() + LEFT * 0.15, mobject.get_right() + RIGHT * 0.15, color=TEXTE, stroke_width=6)
