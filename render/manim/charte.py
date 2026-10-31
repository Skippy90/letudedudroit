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
FOND = "#0B0B0B"
TEXTE = "#F2EFE6"
ACCENT = "#E3A52F"
VERT = "#4CAF7D"
GRIS = "#6B7280"
ROUGE = "#D9534F"
SURFACE = "#1F1F22"  # fond des blocs, un cran plus clair que le fond

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
Y_TITRE, Y_SOUS_TITRE = 3.15, 2.3
Y_PERSONNAGE = 0.45
Y_FRISE = -1.3
# Bloc d'article au-dessus du bandeau des sous-titres (bas de l'image, environ 70 px sur 1080).
Y_ARTICLE = -2.85
# Centre de l'étage du bas du bâtiment : son pied reste au-dessus du bloc d'article.
Y_BATIMENT = -1.75


def texte(contenu, taille=T_CORPS, couleur=TEXTE, gras=False):
    return Text(contenu, font=POLICE, font_size=taille, color=couleur, weight="BOLD" if gras else "NORMAL")


def avec_fond(mob, buff=0.08):
    """Texte posé sur un fond noir légèrement transparent : les traits du décor ne le traversent pas."""
    fond = RoundedRectangle(corner_radius=0.06, width=mob.width + 2 * buff, height=mob.height + 2 * buff,
                            stroke_width=0, fill_color=FOND, fill_opacity=0.85).move_to(mob)
    return VGroup(fond, mob)


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
        etiquette = avec_fond(texte(nom, T_PETIT)).next_to(silhouette, DOWN, buff=0.12)
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


class BlocArret(VGroup):
    """La jurisprudence : bloc « ATF … » au cadre ambre, en bas, à côté du bloc d'article."""

    def __init__(self, libelle):
        etiquette = texte(libelle, T_PETIT, TEXTE, gras=True)
        cadre = RoundedRectangle(corner_radius=0.12, width=etiquette.width + 0.7, height=0.75,
                                 color=ACCENT, stroke_width=3, fill_color=SURFACE, fill_opacity=1)
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
        # Vers le centre, d'après la place réelle de la silhouette (elle a pu marcher depuis sa position de départ).
        cote = LEFT if personnage.silhouette.get_x() > 0 else RIGHT
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
        self.fenetre = Rectangle(width=1.8, height=1.4, **DECOR).move_to([-2.6, 1.05, 0])
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
        elif nom == "telephone":
            corps = RoundedRectangle(corner_radius=0.06, width=0.32, height=0.56, color=TEXTE, stroke_width=4)
            ecran = RoundedRectangle(corner_radius=0.03, width=0.22, height=0.38, color=ACCENT, stroke_width=0,
                                     fill_color=ACCENT, fill_opacity=0.5)
            elements = [corps, ecran]
        elif nom == "tag":
            # Gribouillis sur un mur : une courbe libre en ambre.
            from manim import VMobject
            trace = VMobject(color=ACCENT, stroke_width=7)
            trace.set_points_smoothly([[-0.9, -0.1, 0], [-0.5, 0.35, 0], [-0.2, -0.25, 0], [0.15, 0.3, 0],
                                       [0.45, -0.2, 0], [0.8, 0.25, 0], [1.0, 0.0, 0]])
            elements = [trace]
        elif nom == "lune":
            disque = Circle(radius=0.28, color=TEXTE, fill_color=TEXTE, fill_opacity=0.7, stroke_width=0)
            ombre = Circle(radius=0.26, color=FOND, fill_color=FOND, fill_opacity=1, stroke_width=0).shift(RIGHT * 0.14 + UP * 0.08)
            elements = [disque, ombre]
        elif nom == "vagues":
            elements = [Vagues()]
        elif nom == "coche":
            elements = [Coche()]
        elif nom == "feu":
            # Feu de camp : flamme ambre sur deux bûches (le rouge reste réservé au dommage).
            flamme = Polygon([0, 0.55, 0], [0.28, 0.05, 0], [0.12, -0.15, 0], [-0.12, -0.15, 0], [-0.28, 0.05, 0],
                             color=ACCENT, fill_color=ACCENT, fill_opacity=0.85, stroke_width=0)
            buches = VGroup(Line([-0.45, -0.3, 0], [0.45, -0.18, 0], color=TEXTE, stroke_width=6),
                            Line([-0.45, -0.18, 0], [0.45, -0.3, 0], color=TEXTE, stroke_width=6))
            elements = [flamme, buches]
        elif nom == "prison":
            # Peine privative de liberté : une fenêtre à barreaux.
            cadre = RoundedRectangle(corner_radius=0.08, width=1.1, height=1.1, color=TEXTE, stroke_width=4)
            barreaux = VGroup(*[Line([-0.33 + 0.22 * k, 0.55, 0], [-0.33 + 0.22 * k, -0.55, 0], color=TEXTE, stroke_width=4)
                                for k in range(4)])
            elements = [cadre, barreaux]
        elif nom == "pieces":
            # Argent (peine pécuniaire, amende, réparation) : trois pièces empilées.
            elements = [Ellipse(width=0.9, height=0.32, color=ACCENT, stroke_width=4, fill_color=SURFACE, fill_opacity=1)
                        .shift(UP * 0.16 * k) for k in range(3)]
        elif nom == "document":
            # Un écrit (contrat, plainte) : feuille à lignes et signature.
            feuille = Polygon([-0.4, 0.55, 0], [0.22, 0.55, 0], [0.4, 0.37, 0], [0.4, -0.55, 0], [-0.4, -0.55, 0],
                              color=TEXTE, stroke_width=4)
            lignes = VGroup(*[Line([-0.26, 0.3 - 0.18 * k, 0], [0.26, 0.3 - 0.18 * k, 0], color=GRIS, stroke_width=3)
                              for k in range(3)])
            from manim import VMobject
            signature = VMobject(color=ACCENT, stroke_width=4)
            signature.set_points_smoothly([[-0.25, -0.35, 0], [-0.1, -0.22, 0], [0.0, -0.38, 0], [0.12, -0.25, 0], [0.28, -0.33, 0]])
            elements = [feuille, lignes, signature]
        elif nom == "danger":
            triangle = Polygon([0, 0.55, 0], [0.6, -0.45, 0], [-0.6, -0.45, 0], color=ACCENT, stroke_width=5)
            point = VGroup(Line([0, 0.25, 0], [0, -0.12, 0], color=ACCENT, stroke_width=6),
                           Dot([0, -0.27, 0], radius=0.05, color=ACCENT))
            elements = [triangle, point]
        elif nom == "parlement":
            # La loi votée : un édifice à colonnes, générique.
            fronton = Polygon([-0.75, 0.3, 0], [0.75, 0.3, 0], [0, 0.65, 0], color=TEXTE, stroke_width=4)
            colonnes = VGroup(*[Line([-0.55 + 0.37 * k, 0.25, 0], [-0.55 + 0.37 * k, -0.4, 0], color=TEXTE, stroke_width=4)
                                for k in range(4)])
            socle = Line([-0.8, -0.48, 0], [0.8, -0.48, 0], color=TEXTE, stroke_width=5)
            elements = [fronton, colonnes, socle]
        elif nom == "corde":
            # La cordée : une corde qui relie deux points d'ancrage.
            from manim import VMobject
            corde = VMobject(color=ACCENT, stroke_width=5)
            corde.set_points_smoothly([[-0.8, 0.3, 0], [-0.4, -0.1, 0], [0, 0.2, 0], [0.4, -0.1, 0], [0.8, 0.3, 0]])
            elements = [corde, Dot([-0.8, 0.3, 0], radius=0.08, color=TEXTE), Dot([0.8, 0.3, 0], radius=0.08, color=TEXTE)]
        elif nom == "bouteille":
            corps = RoundedRectangle(corner_radius=0.08, width=0.3, height=0.55, color=ACCENT, stroke_width=4)
            col = Rectangle(width=0.12, height=0.25, color=ACCENT, stroke_width=4).next_to(corps, UP, buff=0)
            elements = [corps, col]
        elif nom == "voiture":
            caisse = RoundedRectangle(corner_radius=0.15, width=2.6, height=0.7, color=TEXTE, stroke_width=4)
            toit = Polygon([-0.8, 0.35, 0], [0.7, 0.35, 0], [0.4, 0.95, 0], [-0.5, 0.95, 0],
                           color=TEXTE, stroke_width=4)
            roues = VGroup(Circle(radius=0.25, color=TEXTE, stroke_width=4).move_to([-0.8, -0.38, 0]),
                           Circle(radius=0.25, color=TEXTE, stroke_width=4).move_to([0.8, -0.38, 0]))
            elements = [caisse, toit, roues]
        elif nom == "ballon":
            balle = Circle(radius=0.2, color=TEXTE, fill_color=TEXTE, fill_opacity=1, stroke_width=0)
            couture = Arc(radius=0.2, start_angle=-0.9, angle=1.8, color=FOND, stroke_width=3).shift(LEFT * 0.12)
            elements = [balle, couture]
        else:
            raise ValueError(f"picto inconnu « {nom} »")
        super().__init__(*elements)
        self.move_to(position)


class Etiquette(VGroup):
    """Mot-clé court, en ambre, posé près de ce dont il parle (« Lausanne », « Un soir d'hiver »)."""

    def __init__(self, contenu, position):
        mot = avec_fond(texte(contenu, T_PETIT, ACCENT))
        super().__init__(*mot)
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


class Appartement(VGroup):
    """Appartement en plein déménagement : sol, porte, fenêtre, piles de cartons."""

    def __init__(self):
        sol = Line([-7.1, Y_SOL, 0], [7.1, Y_SOL, 0], **DECOR)
        porte = Rectangle(width=1.3, height=2.5, **DECOR).move_to([-5.8, Y_SOL + 1.25, 0])
        poignee = Dot([-5.35, Y_SOL + 1.2, 0], radius=0.05, color=TEXTE, fill_opacity=0.35)
        self.fenetre = Rectangle(width=1.8, height=1.4, **DECOR).move_to([-2.6, 1.3, 0])
        croisillon = VGroup(Line(self.fenetre.get_top(), self.fenetre.get_bottom(), **DECOR),
                            Line(self.fenetre.get_left(), self.fenetre.get_right(), **DECOR))
        cartons = VGroup()
        for x, y, l, h in [(4.4, 0, 1.4, 0.9), (5.9, 0, 1.4, 0.9), (5.15, 0.9, 1.3, 0.85), (3.0, 0, 1.0, 0.7)]:
            boite = Rectangle(width=l, height=h, **DECOR).move_to([x, Y_SOL + y + h / 2, 0])
            scotch = Line(boite.get_top(), boite.get_top() + DOWN * 0.3, **DECOR)
            cartons.add(VGroup(boite, scotch))
        super().__init__(sol, porte, poignee, self.fenetre, croisillon, cartons)

    def pied(self, n):
        """Point au sol, de -3 (devant la porte) à 2 (devant les cartons), tous les 1,6."""
        return [1.6 * n, Y_SOL, 0]


class Rue(VGroup):
    """Une rue le soir : trottoir, façades, un commerce (boulangerie par défaut) et sa vitrine, un réverbère."""

    def __init__(self, enseigne="Boulangerie"):
        sol = Line([-7.1, Y_SOL, 0], [7.1, Y_SOL, 0], **DECOR)
        facades = VGroup(
            Rectangle(width=3.0, height=3.4, **DECOR).move_to([-5.4, Y_SOL + 1.7, 0]),
            Rectangle(width=3.6, height=3.0, **DECOR).move_to([4.6, Y_SOL + 1.5, 0]))
        self.mur = Rectangle(width=3.8, height=3.6, **DECOR).move_to([0.6, Y_SOL + 1.8, 0])
        vitrine = Rectangle(width=1.6, height=1.3, **DECOR).move_to([1.5, Y_SOL + 0.75, 0])
        store = Line([0.5, Y_SOL + 1.6, 0], [2.5, Y_SOL + 1.6, 0], **DECOR)
        enseigne = texte(enseigne, T_PETIT).set_opacity(0.4).move_to([0.6, Y_SOL + 3.05, 0])
        reverbere = VGroup(Line([6.6, Y_SOL, 0], [6.6, Y_SOL + 3.2, 0], **DECOR),
                           Line([6.6, Y_SOL + 3.2, 0], [6.2, Y_SOL + 3.2, 0], **DECOR),
                           Dot([6.2, Y_SOL + 3.05, 0], radius=0.09, color=ACCENT, fill_opacity=0.6))
        super().__init__(sol, facades, self.mur, vitrine, store, enseigne, reverbere)

    def pied(self, n):
        """Point au sol, tous les 1,6, de -4 (bord gauche) à 4 (bord droit)."""
        return [1.6 * n, Y_SOL, 0]


class Tribunal(VGroup):
    """Salle d'audience : sol, estrade et banc du juge à droite, barre des témoins à gauche du centre.

    Le banc et la barre sont au premier plan (z_index 1) : une silhouette placée derrière n'en dépasse
    que par le haut, et son nom s'inscrit sur le meuble (voir Schemas.a_placer)."""

    X_BANC, X_BARRE = 4.6, -1.6

    def __init__(self):
        sol = Line([-7.1, Y_SOL, 0], [7.1, Y_SOL, 0], **DECOR)
        mur = Rectangle(width=4.2, height=3.6, **DECOR).move_to([self.X_BANC, Y_SOL + 1.8, 0])
        estrade = Line([self.X_BANC - 2.1, Y_SOL + 0.6, 0], [self.X_BANC + 2.1, Y_SOL + 0.6, 0], **DECOR)
        porte = Rectangle(width=1.3, height=2.5, **DECOR).move_to([-5.8, Y_SOL + 1.25, 0])
        # Les meubles sont remplis du fond : ils masquent ce qui est derrière eux.
        meuble = dict(color=TEXTE, stroke_width=3, stroke_opacity=0.5, fill_color=FOND, fill_opacity=1)
        self.banc = Rectangle(width=3.2, height=1.45, **meuble).move_to([self.X_BANC, Y_SOL + 0.725, 0])
        self.barre = Rectangle(width=1.3, height=1.05, **meuble).move_to([self.X_BARRE, Y_SOL + 0.525, 0])
        self.meubles = [self.banc, self.barre]
        super().__init__(sol, mur, estrade, porte, self.banc, self.barre)
        for m in self.meubles:
            m.set_z_index(1)

    def pied(self, n):
        """Point au sol, tous les 1,6, de -4 à 4 ; 3 est derrière le banc du juge, sur l'estrade."""
        if n == 3:
            return [self.X_BANC, Y_SOL + 0.6, 0]
        return [1.6 * n, Y_SOL, 0]

    def meuble_devant(self, x):
        """Le meuble devant lequel se tient une silhouette d'abscisse x, s'il y en a un."""
        return next((m for m in self.meubles if abs(m.get_x() - x) < m.width / 2), None)


class Vagues(VGroup):
    """Le lac : trois lignes ondulées."""

    def __init__(self):
        from manim import VMobject
        lignes = []
        for k in range(3):
            v = VMobject(color=TEXTE if k else ACCENT, stroke_width=4)
            v.set_points_smoothly([[-0.8 + 0.2 * i, 0.1 * (-1) ** i - 0.25 * k, 0] for i in range(9)])
            lignes.append(v)
        super().__init__(*lignes)


class Coche(VGroup):
    """Condition remplie : coche verte dans un rond."""

    def __init__(self):
        rond = Circle(radius=0.36, color=VERT, fill_color=VERT, fill_opacity=1, stroke_width=0)
        signe = VGroup(Line([-0.17, 0, 0], [-0.04, -0.15, 0], color=FOND, stroke_width=7),
                       Line([-0.04, -0.15, 0], [0.2, 0.17, 0], color=FOND, stroke_width=7)).move_to(rond)
        super().__init__(rond, signe)


class RepereListe(VGroup):
    """Pense-bête permanent en haut à droite : une case et un mot par exigence ; il survit aux scene-vide."""

    def __init__(self, *libelles):
        self.lignes = []
        for i, libelle in enumerate(libelles):
            boite = RoundedRectangle(corner_radius=0.05, width=0.34, height=0.34, color=TEXTE, stroke_width=2.5)
            mot = texte(libelle, T_PETIT).next_to(boite, RIGHT, buff=0.18)
            ligne = VGroup(boite, mot)
            ligne.move_to([0, -0.58 * i, 0], aligned_edge=LEFT)
            self.lignes.append(ligne)
        cadre_contenu = VGroup(*self.lignes)
        fond = RoundedRectangle(corner_radius=0.12, width=cadre_contenu.width + 0.45,
                                height=cadre_contenu.height + 0.4, stroke_width=0,
                                fill_color=SURFACE, fill_opacity=0.9).move_to(cadre_contenu)
        super().__init__(fond, *self.lignes)
        self.libelles = list(libelles)
        self.to_corner(UP + RIGHT, buff=0.3)

    def marquer(self, n, etat):
        boite, mot = self.lignes[n - 1]
        if etat == "neutre":
            return [boite.animate.set_fill(SURFACE, opacity=0).set_stroke(TEXTE), mot.animate.set_color(TEXTE)]
        couleur = ETATS[etat]
        return [boite.animate.set_fill(couleur, opacity=1).set_stroke(couleur),
                mot.animate.set_color(ACCENT if etat == "ambre" else GRIS if etat == "gris" else TEXTE)]


class Parc(VGroup):
    """Un parc : pelouse, un arbre, un poteau, une haie à droite.

    La haie est au premier plan (z_index 1, comme les meubles du tribunal) : une silhouette placée
    derrière (placer … 3) n'en dépasse que par le haut et son nom s'inscrit sur la haie."""

    X_HAIE = 5.4

    def __init__(self):
        sol = Line([-7.1, Y_SOL, 0], [7.1, Y_SOL, 0], **DECOR)
        tronc = Line([-1.8, Y_SOL, 0], [-1.8, Y_SOL + 1.6, 0], **DECOR)
        feuillage = Circle(radius=1.0, **DECOR).move_to([-1.8, Y_SOL + 2.4, 0])
        self.poteau = Line([0.6, Y_SOL, 0], [0.6, Y_SOL + 2.3, 0], color=TEXTE, stroke_width=4, stroke_opacity=0.5)
        bosses = VGroup(*[Arc(radius=0.3, start_angle=0, angle=3.1416, **DECOR).move_to(
            [self.X_HAIE - 1.2 + 0.6 * k + 0.3, Y_SOL + 1.05, 0]) for k in range(4)])
        corps = Rectangle(width=2.4, height=0.95, color=TEXTE, stroke_width=3, stroke_opacity=0.35,
                          fill_color=FOND, fill_opacity=1).move_to([self.X_HAIE, Y_SOL + 0.475, 0])
        self.haie = VGroup(corps, bosses)
        self.meubles = [self.haie]
        super().__init__(sol, tronc, feuillage, self.poteau, self.haie)
        self.haie.set_z_index(1)

    def pied(self, n):
        """Point au sol, tous les 1,6, de -4 à 4 ; 3 est derrière la haie."""
        if n == 3:
            return [self.X_HAIE, Y_SOL, 0]
        return [1.6 * n, Y_SOL, 0]

    def meuble_devant(self, x):
        return self.haie if abs(self.haie.get_x() - x) < self.haie.width / 2 else None


class Piscine(VGroup):
    """Une piscine : la chaise haute de la surveillante à gauche, le bassin à droite.

    Le bord du bassin est au premier plan (z_index 1) : une silhouette placée dans l'eau (placer … 2 à 4)
    n'en dépasse que par la tête, et son nom s'inscrit sur le bord."""

    X_BASSIN, L_BASSIN = 4.0, 5.6

    def __init__(self):
        sol = Line([-7.1, Y_SOL, 0], [7.1, Y_SOL, 0], **DECOR)
        pieds = VGroup(Line([-5.4, Y_SOL, 0], [-5.0, Y_SOL + 2.0, 0], **DECOR),
                       Line([-4.2, Y_SOL, 0], [-4.6, Y_SOL + 2.0, 0], **DECOR))
        siege = Line([-5.2, Y_SOL + 2.0, 0], [-4.4, Y_SOL + 2.0, 0], color=TEXTE, stroke_width=4, stroke_opacity=0.5)
        dossier = Line([-5.2, Y_SOL + 2.0, 0], [-5.2, Y_SOL + 2.7, 0], **DECOR)
        bord = Rectangle(width=self.L_BASSIN, height=1.0, color=TEXTE, stroke_width=3, stroke_opacity=0.45,
                         fill_color=FOND, fill_opacity=1).move_to([self.X_BASSIN, Y_SOL + 0.5, 0])
        from manim import VMobject
        eau = VMobject(color=TEXTE, stroke_width=3, stroke_opacity=0.35)
        x0 = self.X_BASSIN - self.L_BASSIN / 2
        eau.set_points_smoothly([[x0 + 0.35 * i, Y_SOL + 1.0 + 0.06 * (-1) ** i, 0]
                                 for i in range(int(self.L_BASSIN / 0.35) + 1)])
        self.bassin = VGroup(bord, eau)
        self.meubles = [self.bassin]
        super().__init__(sol, pieds, siege, dossier, self.bassin)
        self.bassin.set_z_index(1)

    def pied(self, n):
        """Point au sol, tous les 1,6, de -4 à 4 ; de 2 à 4, dans l'eau."""
        return [1.6 * n, Y_SOL, 0]

    def meuble_devant(self, x):
        return self.bassin if abs(self.bassin.get_x() - x) < self.bassin.width / 2 else None
