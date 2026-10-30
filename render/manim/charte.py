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
Y_FRISE = -1.5
# Bloc d'article au-dessus du bandeau des sous-titres (bas de l'image, environ 70 px sur 1080).
Y_ARTICLE = -2.85
# Centre de l'étage du bas du bâtiment : son pied reste au-dessus du bloc d'article.
Y_BATIMENT = -1.75


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
        self.move_to([0, Y_ARTICLE, 0])
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
            cadre.move_to([0, Y_BATIMENT + i * 1.05, 0])
            etiquette = texte(nom, T_CORPS).move_to(cadre)
            etage = VGroup(cadre, etiquette)
            self.etages.append(etage)
            groupe.append(etage)
        sommet_etages = Y_BATIMENT + 2.5 * 1.05  # haut du troisième étage
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
            nom = texte(titre, T_PETIT)
            if nom.width > largeur - 0.6:  # titre long : un mot par ligne (« Code de / procédure / pénale »)
                lignes, courante = [], ""
                for mot in titre.split():
                    essai = f"{courante} {mot}".strip()
                    if courante and texte(essai, T_PETIT).width > largeur - 0.6:
                        lignes.append(courante)
                        essai = mot
                    courante = essai
                nom = texte("\n".join(lignes + [courante]), T_PETIT)
            nom.move_to(couverture).shift(RIGHT * 0.12)
            if nom.width > largeur - 0.6 or nom.height > hauteur - 0.4:
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
        self.etiquettes = []
        super().__init__(self.ligne)

    def placer(self, etiquette, sens):
        """Décale une étiquette d'un rang (vers le haut ou le bas) tant qu'elle touche une voisine."""
        for _ in range(3):
            if not any(abs(etiquette.get_x() - e.get_x()) < (etiquette.width + e.width) / 2 + 0.15
                       and abs(etiquette.get_y() - e.get_y()) < (etiquette.height + e.height) / 2
                       for e in self.etiquettes):
                break
            etiquette.shift(sens * (etiquette.height + 0.12))
        self.etiquettes.append(etiquette)
        return etiquette

    @staticmethod
    def x(fraction):
        return -6.0 + 12.0 * float(fraction)

    def repere(self, fraction, libelle):
        x = self.x(fraction)
        trait = Line([x, Y_FRISE - 0.35, 0], [x, Y_FRISE + 0.35, 0], color=ACCENT, stroke_width=6)
        etiquette = self.placer(texte(libelle, T_PETIT, ACCENT).next_to(trait, DOWN, buff=0.15), DOWN)
        return VGroup(trait, etiquette)

    def point(self, fraction, libelle):
        x = self.x(fraction)
        point = Dot([x, Y_FRISE, 0], radius=0.13, color=TEXTE)
        etiquette = self.placer(texte(libelle, T_PETIT).next_to(point, UP, buff=0.25), UP)
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


# ----- Décors, pictogrammes et repère permanent -----
# Les décors sont dessinés au trait fin, en blanc cassé très atténué : ils situent la scène
# sans jamais concurrencer les silhouettes ni les schémas.
DECOR = dict(color=TEXTE, stroke_width=3, stroke_opacity=0.35)
Y_SOL = -2.3


class Escalier(VGroup):
    """Cage d'escalier : sol, marches qui montent vers la droite, rampe, porte, fenêtre de nuit."""

    MARCHE_L, MARCHE_H, N_MARCHES, X0 = 0.8, 0.42, 7, 0.6

    def __init__(self):
        sol = Line([-7.1, Y_SOL, 0], [self.X0, Y_SOL, 0], **DECOR)
        points, x, y = [[self.X0, Y_SOL, 0]], self.X0, Y_SOL
        for _ in range(self.N_MARCHES):
            y += self.MARCHE_H
            points.append([x, y, 0])
            x += self.MARCHE_L
            points.append([x, y, 0])
        marches = VGroup(*[Line(a, b, **DECOR) for a, b in zip(points, points[1:])])
        rampe = Line([self.X0 + 0.3, Y_SOL + 1.3, 0], [x - 0.2, y + 1.3, 0], **DECOR)
        montants = VGroup(*[Line([self.X0 + 0.3 + k * 1.5, Y_SOL + self.MARCHE_H * (1 + 2 * k) - 0.02, 0],
                                 [self.X0 + 0.3 + k * 1.5, Y_SOL + 1.3 + k * 1.5 * self.MARCHE_H / self.MARCHE_L, 0],
                                 **DECOR) for k in range(4)])
        porte = Rectangle(width=1.3, height=2.5, **DECOR).move_to([-5.8, Y_SOL + 1.25, 0])
        poignee = Dot([-5.35, Y_SOL + 1.2, 0], radius=0.05, color=TEXTE, fill_opacity=0.35)
        self.fenetre = Rectangle(width=1.8, height=1.4, **DECOR).move_to([-2.6, 1.3, 0])
        croisillon = VGroup(Line(self.fenetre.get_top(), self.fenetre.get_bottom(), **DECOR),
                            Line(self.fenetre.get_left(), self.fenetre.get_right(), **DECOR))
        super().__init__(sol, marches, rampe, montants, porte, poignee, self.fenetre, croisillon)

    def pied(self, n):
        """Point où se tient un personnage sur la marche n (0 = sol, au pied de l'escalier ;
        -1, -2, -3 : de plus en plus loin dans le hall, -3 étant devant la porte)."""
        if n <= 0:
            return [self.X0 - 0.6 + 1.6 * n, Y_SOL, 0]
        return [self.X0 + (n - 0.5) * self.MARCHE_L, Y_SOL + n * self.MARCHE_H, 0]


class Neige(VGroup):
    """Flocons qui tombent derrière la fenêtre (soir d'hiver)."""

    def __init__(self, fenetre, n=14):
        import random
        alea = random.Random(7)
        self.zone = fenetre
        flocons = [Dot([alea.uniform(fenetre.get_left()[0] + 0.1, fenetre.get_right()[0] - 0.1),
                        alea.uniform(fenetre.get_bottom()[1] + 0.1, fenetre.get_top()[1] - 0.1), 0],
                       radius=0.035, color=TEXTE, fill_opacity=0.8) for _ in range(n)]
        super().__init__(*flocons)

        def tomber(groupe, dt):
            bas, haut = self.zone.get_bottom()[1] + 0.06, self.zone.get_top()[1] - 0.06
            for f in groupe:
                f.shift(DOWN * 0.25 * dt)
                if f.get_center()[1] < bas:
                    f.shift(UP * (haut - bas))
        self.add_updater(tomber)


class Picto(VGroup):
    """Pictogrammes au trait, dans les couleurs de la charte."""

    def __init__(self, nom, position):
        if nom == "parking":
            cadre = RoundedRectangle(corner_radius=0.12, width=0.9, height=0.9, color=TEXTE, stroke_width=4)
            lettre = texte("P", T_SOUS_TITRE, TEXTE, gras=True).move_to(cadre)
            elements = [cadre, lettre]
        elif nom == "tension":
            # Ligne brisée entre deux personnes : l'hostilité.
            pts = [[-1.2 + 0.3 * k, 0.18 * (-1) ** k, 0] for k in range(9)]
            elements = [VGroup(*[Line(a, b, color=ACCENT, stroke_width=5) for a, b in zip(pts, pts[1:])])]
        elif nom == "lune":
            disque = Circle(radius=0.28, color=TEXTE, fill_color=TEXTE, fill_opacity=0.7, stroke_width=0)
            ombre = Circle(radius=0.26, color=FOND, fill_color=FOND, fill_opacity=1, stroke_width=0).shift(RIGHT * 0.14 + UP * 0.08)
            elements = [disque, ombre]
        else:
            raise ValueError(f"picto inconnu « {nom} »")
        super().__init__(*elements)
        self.move_to(position)


class Etiquette(VGroup):
    """Mot-clé court, en ambre, posé près de ce dont il parle (« Lausanne », « Un soir d'hiver »)."""

    def __init__(self, contenu, position):
        mot = texte(contenu, T_PETIT, ACCENT)
        super().__init__(mot)
        self.move_to(position)


class MiniBatiment(VGroup):
    """Le bâtiment à trois étages en petit, en haut à droite : où en est le raisonnement."""

    def __init__(self):
        etages = []
        for i in range(3):
            cadre = Rectangle(width=1.0, height=0.3, color=TEXTE, stroke_width=2, fill_color=SURFACE, fill_opacity=1)
            cadre.move_to([0, i * 0.3, 0])
            etages.append(cadre)
        toit = Polygon([-0.6, 0.75, 0], [0.6, 0.75, 0], [0, 1.0, 0], color=TEXTE, stroke_width=2)
        super().__init__(*etages, toit)
        self.etages = etages
        self.move_to([6.35, 2.7, 0])

    def colorer(self, n, etat):
        return self.etages[n - 1].animate.set_fill(ETATS[etat], opacity=0.9)
