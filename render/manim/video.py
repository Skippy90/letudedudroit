"""Rend les schémas d'une vidéo à partir de son visuals.md, calés sur la narration.

Usage (depuis la racine du dépôt) :
    SLUG=droit-penal-general/02-pas-de-peine-sans-loi manim render/manim/video.py Schemas

Entrées : scripts/<slug>/visuals.md et voice/<slug>/timings.json.
Sortie : vidéo muette 1920 × 1080, 30 images par seconde, de la durée exacte de la narration.

Le moteur vérifie deux règles de la charte et les signale en fin de rendu :
- jamais plus de douze mots affichés à la fois (hors bloc d'article) ;
- aucun plan fixe de plus de quatre secondes : quand deux moments sont trop éloignés,
  le dernier élément animé « respire » légèrement pour que l'image bouge.
"""

import json
import numpy as np
import os
import re
import shlex
from pathlib import Path

from manim import (
    DOWN, LEFT, RIGHT, UP, AnimationGroup, Create, FadeIn, FadeOut, GrowArrow, Indicate,
    Line, ReplacementTransform, Scene, Transform, VGroup, Write, config, there_and_back,
)

import charte as c

RACINE = Path(__file__).resolve().parents[2]
SLUG = os.environ.get("SLUG", "")
DUREE_ANIM = 0.7
PLAN_FIXE_MAX = 4.0
CREATIONS = {"cases", "liste", "colonnes", "livres", "frise", "repere-batiment", "repere-liste", "decor"}

config.background_color = c.FOND
if os.environ.get("APERCU"):
    config.pixel_width, config.pixel_height, config.frame_rate = 854, 480, 15
else:
    config.pixel_width, config.pixel_height, config.frame_rate = 1920, 1080, 30


def lire_moments(slug):
    """Renvoie [(instant en secondes, [actions])] trié, à partir de visuals.md et timings.json."""
    # TIMINGS permet un aperçu avant la narration, avec des timings estimés (tools/timings_estimes.py).
    fichier = Path(os.environ["TIMINGS"]) if os.environ.get("TIMINGS") else RACINE / "voice" / slug / "timings.json"
    timings = json.loads(fichier.read_text(encoding="utf-8"))
    lignes = {l["ligne"]: l for l in timings["lignes"]}
    moments = []
    # VISUELS=<fichier> : un autre visuals.md pour la même narration (prototype d'un nouveau style).
    visuels = Path(os.environ["VISUELS"]) if os.environ.get("VISUELS") else RACINE / "scripts" / slug / "visuals.md"
    for ligne in visuels.read_text(encoding="utf-8").splitlines():
        # « 2.3 », « 2.3+1.5 » (secondes après le début de la phrase) ou « 2.3@poignet »
        # (au moment où ce mot est prononcé ; il faut une narration avec l'instant de chaque mot).
        m = re.match(r"\|\s*(\d+)\.(\d+)(?:\+([\d.]+)|@([\w'-]+))?\s*\|(.*)\|\s*$", ligne)
        if not m:
            continue
        n, p, decalage, mot, actions = int(m[1]), int(m[2]), float(m[3] or 0), m[4], m[5]
        phrase = lignes[n]["phrases"][p - 1]
        instant = phrase["debut"] + decalage
        if mot:
            cible = mot.lower()
            trouves = [w for w in phrase.get("mots", []) if w["mot"] == cible]
            # Sans instant par mot (timings estimés, voix de synthèse), on prend le début de la phrase.
            instant = trouves[0]["debut"] if trouves else phrase["debut"]
        moments.append((instant, [shlex.split(a) for a in actions.split(";") if a.strip()],
                        f"{m[1]}.{m[2]}" + (f"@{mot}" if mot else "")))
    return sorted(moments, key=lambda x: x[0]), timings["duree"]


class Schemas(Scene):
    def setup(self):
        self.t = 0.0
        self.alertes = []
        self.personnages, self.paroles, self.bulles = {}, {}, {}
        self.titre = self.sous_titre = self.article = self.renvoi = None
        self.arret = None
        self.batiment = self.livre = self.liste = self.cases = self.pyramide = None
        self.frise = self.colonnes = self.livres = None
        self.frise_points, self.mots_barres, self.fleches_retour = [], [], []
        self.questions_etages, self.bouclier = {}, None
        self.decor = self.neige = None
        self.pictos, self.etiquettes = {}, {}
        self.focus = None

    # ----- temps -----
    # Manim arrondit le nombre d'images au-dessus pour une animation et au-dessous pour
    # une attente : sur des centaines d'actions, l'écart avec la voix dépassait une seconde.
    # L'horloge compte donc en images entières, et chaque durée est choisie pour que Manim
    # écrive exactement ce nombre d'images.
    def play(self, *animations, run_time=None, **kwargs):
        if getattr(self, "_attente_en_cours", False):
            # Appel interne de Scene.wait : la durée est déjà réglée par wait() ci-dessous.
            return super().play(*animations, **kwargs)
        images = max(1, round((1.0 if run_time is None else run_time) * config.frame_rate))
        super().play(*animations, run_time=(images - 0.5) / config.frame_rate, **kwargs)
        self.t += images / config.frame_rate

    def wait(self, duree=1.0, **kwargs):
        images = round(duree * config.frame_rate)
        if images > 0:
            self._attente_en_cours = True
            try:
                super().wait((images + 0.5) / config.frame_rate, **kwargs)
            finally:
                self._attente_en_cours = False
            self.t += images / config.frame_rate

    def jouer(self, *animations, duree=DUREE_ANIM):
        animations = [a for a in animations if a is not None]
        if animations:
            self.play(*animations, run_time=duree)

    def attendre_jusqua(self, instant):
        """Attend jusqu'à l'instant donné, en faisant respirer l'image si l'attente dépasse quatre secondes."""
        while instant - self.t > PLAN_FIXE_MAX and self.a_l_ecran(self.focus):
            self.wait(2.0)
            self.play(self.focus.animate(rate_func=there_and_back).scale(1.04), run_time=1.2)
        if instant > self.t:
            self.wait(instant - self.t)

    def a_l_ecran(self, m):
        """Vrai si l'objet, ou l'une de ses parties dessinées, est à l'écran (un groupe peut y être ajouté pièce par pièce)."""
        if m is None:
            return False
        famille = {id(x) for top in self.mobjects for x in top.get_family()}
        return id(m) in famille or any(id(x) in famille for x in m.family_members_with_points())

    # ----- règle des douze mots -----
    def mots_visibles(self):
        textes = []
        for m in [self.titre, self.sous_titre, self.renvoi]:
            if m is not None:
                textes.append(m.original_text)
        for p in self.personnages.values():
            textes.append(p.nom)
        textes += [e.contenu for e in self.etiquettes.values()]
        for g in list(self.paroles.values()) + list(self.bulles.values()):
            textes.append(g.contenu)
        for groupe in [self.liste and self.liste.elements, self.cases and [l[1] for l in self.cases.lignes],
                       self.mots_barres, self.colonnes and self.colonnes.mots]:
            for t in groupe or []:
                textes.append(t.original_text)
        if self.batiment:
            textes += c.Batiment.NOMS[:3 - sum(1 for e in self.batiment.etages if e[1].get_fill_opacity() == 0)]
            textes += [q.original_text for q in getattr(self, "questions_etages", {}).values()]
        if self.pyramide:
            textes += c.Pyramide.NOMS
        if self.livres:
            textes += [l[2].original_text for l in self.livres]
        elif self.livre and len(self.livre) == 3:
            textes.append(self.livre[2].original_text)
        textes += [g[1].original_text for g in self.frise_points]
        if isinstance(getattr(self, "repere", None), c.RepereListe):
            textes += self.repere.libelles
        return sum(c.mots(t) for t in textes)

    # ----- chevauchements -----
    def elements_visibles(self):
        """(nom, objet) de chaque élément affiché, hors décor (les décors sont en fond, au trait atténué)."""
        el = [("titre", self.titre), ("sous-titre", self.sous_titre), ("article", self.article), ("arrêt", self.arret),
              ("renvoi", self.renvoi), ("repère", getattr(self, "repere", None)),
              ("livre", self.livre), ("pyramide", self.pyramide)]
        if self.colonnes:
            el += [(f"colonne {i}", m) for i, m in enumerate(self.colonnes.mots, 1)] + [("trait des colonnes", self.colonnes[1])]
        for k, p in self.personnages.items():
            el += [(k, p.silhouette), (f"nom de {k}", p.etiquette)]
        el += [(f"parole de {k}", g) for k, g in self.paroles.items()]
        # La bulle elle-même (sans les petits ronds qui la relient à la tête) : elle ne doit pas couvrir sa silhouette.
        el += [(f"bulle de {k}", g[1]) for k, g in self.bulles.items()]
        el += [(f"étiquette {k}", e) for k, e in self.etiquettes.items()]
        el += [(f"picto {k}", e) for k, e in self.pictos.items()]
        el += [("bouclier", self.bouclier)] if self.bouclier is not None else []
        el += [(f"liste {i}", t) for i, t in enumerate(self.liste.elements, 1)] if self.liste else []
        el += [(f"case {i}", l) for i, l in enumerate(self.cases.lignes, 1)] if self.cases else []
        el += [(f"livre {i}", l) for i, l in enumerate(self.livres, 1)] if self.livres else []
        el += [(f"frise {g[1].original_text}", g[1]) for g in self.frise_points]
        el += [(f"repère de frise {g[1].original_text}", g[0]) for g in self.frise_points]
        if self.frise is not None:
            el.append(("ligne de frise", self.frise.ligne))
        el += [(f"mot barré {m.original_text}", m) for m in self.mots_barres]
        if self.batiment:
            el.append(("bâtiment", self.batiment))
        return [(n, m) for n, m in el if m is not None and self.a_l_ecran(m) and m.get_family()[0].has_points()
                or (m is not None and self.a_l_ecran(m) and len(m.get_family()) > 1)]

    def voulu(self, na, nb):
        """Contacts prévus par la charte : la bulle part de la tête, le nom s'inscrit sur le meuble."""
        # Un point et un repère posés au même endroit de la frise se croisent.
        if na.startswith("repère de frise ") and nb.startswith("repère de frise "):
            return True
        # La ligne de frise porte ses repères et ses points.
        if "ligne de frise" in (na, nb) and any(n.startswith("repère de frise ") for n in (na, nb)):
            return True
        # Le trait d'un repère de frise touche son propre libellé.
        if {na, nb} and any(n.startswith("repère de frise ") for n in (na, nb)):
            autre = nb if na.startswith("repère de frise ") else na
            if autre == "frise " + (na if na.startswith("repère de frise ") else nb)[len("repère de frise "):]:
                return True
        # Le ballon part du pied d'une silhouette, ou la touche.
        objet = next((n for n in ("picto ballon", "picto bouteille") if n in (na, nb)), None)
        if objet and ({na, nb} - {objet}) & set(self.personnages):
            return True
        for k, p in self.personnages.items():
            if {na, nb} == {k, f"nom de {k}"} and getattr(p, "derriere_meuble", False):
                return True
        return False

    TEXTES = ("titre", "sous-titre", "article", "arrêt", "renvoi", "nom de ", "parole de ", "bulle de ", "étiquette ",
              "liste ", "case ", "frise ", "mot barré ", "colonne ")

    def textes_sur_decor(self):
        """Un texte posé sur un trait du décor (façade, fenêtre, enseigne) : illisible, signalé."""
        if self.decor is None or not self.a_l_ecran(self.decor):
            return []
        meubles = getattr(self.decor, "meubles", [])
        points = []
        for m in self.decor.family_members_with_points():
            if any(m in mb.get_family() for mb in meubles):
                continue
            pts = m.get_anchors()
            for a, b in zip(pts[:-1], pts[1:]):
                for t in np.linspace(0, 1, 8):
                    points.append(a + (b - a) * t)
        if not points:
            return []
        pts = np.array(points)
        for mb in meubles:
            dedans = ((pts[:, 0] > mb.get_left()[0]) & (pts[:, 0] < mb.get_right()[0])
                      & (pts[:, 1] > mb.get_bottom()[1]) & (pts[:, 1] < mb.get_top()[1]))
            pts = pts[~dedans]
        alertes = []
        for nom, m in self.elements_visibles():
            # Noms, mots-clés, paroles et bulles ont un fond opaque : ils passent devant le décor sans s'y mêler.
            if not nom.startswith(self.TEXTES) or nom.startswith(("nom de ", "étiquette ", "parole de ", "bulle de ")):
                continue
            g, d, b, h = m.get_left()[0], m.get_right()[0], m.get_bottom()[1], m.get_top()[1]
            dedans = (pts[:, 0] > g - 0.05) & (pts[:, 0] < d + 0.05) & (pts[:, 1] > b - 0.05) & (pts[:, 1] < h + 0.05)
            if dedans.any():
                alertes.append(f"{nom} sur le décor")
        return alertes

    def que_du_texte(self):
        """Vrai si l'écran ne montre que du texte : ni personnage, ni décor, ni schéma, ni pictogramme."""
        graphiques = [self.decor, self.batiment, self.frise, self.livre, self.pyramide, self.bouclier,
                      self.livres and VGroup(*self.livres)]
        graphiques += list(self.personnages.values()) + list(self.pictos.values())
        return not any(m is not None and self.a_l_ecran(m) for m in graphiques)

    def chevauchements(self):
        """Deux éléments à moins de 0,1 l'un de l'autre, ou un élément dans la bande des sous-titres."""
        def boite(m):
            return m.get_left()[0], m.get_right()[0], m.get_bottom()[1], m.get_top()[1]
        el = self.elements_visibles()
        alertes = []
        for i, (na, a) in enumerate(el):
            g, d, b, h = boite(a)
            if b < -3.3:
                alertes.append(f"{na} dans la bande des sous-titres")
            for nb, bb in el[i + 1:]:
                if a in bb.get_family() or bb in a.get_family() or self.voulu(na, nb):
                    continue
                g2, d2, b2, h2 = boite(bb)
                if g < d2 + 0.1 and g2 < d + 0.1 and b < h2 + 0.1 and b2 < h + 0.1:
                    alertes.append(f"{na} touche {nb}")
        return alertes

    # ----- rendu -----
    def construct(self):
        moments, duree_totale = lire_moments(SLUG)
        # FIN=<secondes> : rendu limité au début de la vidéo (prototypes, essais).
        if os.environ.get("FIN"):
            duree_totale = float(os.environ["FIN"])
            moments = [m for m in moments if m[0] < duree_totale]
        for instant, actions, repere in moments:
            if self.t - instant > 0.5:
                self.alertes.append(f"{repere} : animation en retard de {self.t - instant:.1f} s sur la voix")
            self.attendre_jusqua(instant)
            # Une scène vide se joue d'abord, seule, pour libérer l'écran.
            if any(a[0] == "scene-vide" for a in actions):
                self.scene_vide()
                actions = [a for a in actions if a[0] != "scene-vide"]
            # Un groupe créé et modifié au même moment (des cases aussitôt cochées) apparaît
            # d'abord : sinon son animation d'apparition écrase les marques ajoutées.
            creations = [a for a in actions if a[0] in CREATIONS]
            if creations and len(creations) < len(actions):
                self.jouer(*[x for a in creations for x in self.executer(a, repere)], duree=0.5)
                actions = [a for a in actions if a[0] not in CREATIONS]
            self.jouer(*[x for a in actions for x in self.executer(a, repere)])
            total = self.mots_visibles()
            if total > 12:
                self.alertes.append(f"{repere} : {total} mots affichés (maximum 12)")
            self.alertes += [f"{repere} : {x}" for x in self.chevauchements() + self.textes_sur_decor()]
            self.pauvrete = getattr(self, "pauvrete", []) + [(instant, repere, self.que_du_texte())]
        self.attendre_jusqua(duree_totale)
        rapport = RACINE / "out" / (SLUG.replace("/", "--") + "--alertes-visuels.txt")
        rapport.parent.mkdir(exist_ok=True)
        # Passages où l'écran ne montre que du texte (la charte veut une image par idée) : signalés au-delà de 5 s.
        pauvrete = getattr(self, "pauvrete", [])
        bornes = [m[0] for m in pauvrete[1:]] + [duree_totale]
        total = 0.0
        for (debut, rep, texte_seul), fin in zip(pauvrete, bornes):
            if texte_seul:
                total += fin - debut
        segments, courant = [], None
        for (debut, rep, texte_seul), fin in zip(pauvrete, bornes):
            if texte_seul:
                courant = [courant[0], fin, courant[2]] if courant else [debut, fin, rep]
            elif courant:
                segments.append(courant); courant = None
        if courant:
            segments.append(courant)
        for debut, fin, rep in segments:
            if fin - debut > 5:
                self.alertes.append(f"{rep} : que du texte pendant {fin - debut:.0f} s")
        print(f"Texte seul : {total:.0f} s sur {duree_totale:.0f} s")
        rapport.write_text(("\n".join(self.alertes) + "\n" if self.alertes else "Aucune alerte.\n")
                           + f"Texte seul : {total:.0f} s sur {duree_totale:.0f} s\n", encoding="utf-8")
        print("\n".join(self.alertes) or "Aucune alerte de charte.")

    def executer(self, action, repere):
        methode = getattr(self, "a_" + action[0].replace("-", "_"), None)
        if methode is None:
            raise ValueError(f"{repere} : action inconnue « {action[0]} »")
        resultat = methode(*action[1:])
        return resultat if isinstance(resultat, list) else [resultat]

    def scene_vide(self):
        repere = getattr(self, "repere", None)
        garder = [m for m in (self.article, getattr(self, "arret", None), repere) if m is not None]
        # Une silhouette derrière un meuble part d'abord, tant que le meuble la masque encore.
        caches = [p.silhouette for p in self.personnages.values() if getattr(p, "derriere_meuble", False)]
        if caches:
            self.jouer(*[FadeOut(m) for m in caches], duree=0.2)
            for p in self.personnages.values():
                if getattr(p, "derriere_meuble", False):
                    p.remove(p.silhouette)
        a_retirer = [m for m in self.mobjects if m not in garder]
        if a_retirer:
            self.jouer(*[FadeOut(m) for m in a_retirer], duree=0.3)
        article, arret, t, alertes = self.article, getattr(self, "arret", None), self.t, self.alertes
        pauvrete = getattr(self, "pauvrete", [])
        self.setup()
        self.article, self.arret, self.t, self.alertes, self.repere = article, arret, t, alertes, repere
        self.pauvrete = pauvrete
        self.traits = []
        return []

    # ----- actions : texte -----
    def a_titre(self, contenu, *options):
        couleur = c.ACCENT if "ambre" in options else c.TEXTE
        anims = [FadeOut(self.titre)] if self.titre is not None else []
        anims += self.retirer_traits(self.titre)
        if "mot-a-mot" in options:
            # Les mots apparaissent un par un pendant la phrase (règle des quatre secondes).
            # Le texte est rendu d'un seul tenant (ligne de base commune), puis découpé en mots :
            # les sous-objets de Text sont les caractères, espaces exclus.
            nouveau = c.texte(contenu, c.T_TITRE, couleur, gras=True).move_to([0, c.Y_TITRE, 0])
            if nouveau.width > self.largeur_titres():
                nouveau.scale_to_fit_width(self.largeur_titres())
            nouveau.set_x(self.x_titres(nouveau.width))
            nouveau.original_text = contenu
            groupes, i = [], 0
            for mot in contenu.split():
                groupes.append(VGroup(*nouveau.submobjects[i:i + len(mot)]))
                i += len(mot)
            self.titre = self.focus = nouveau
            if anims:
                self.jouer(*anims, duree=0.3)
            self.play(AnimationGroup(*[FadeIn(g, shift=UP * 0.1) for g in groupes], lag_ratio=1.0), run_time=4.5)
            return []
        nouveau = c.texte(contenu, c.T_TITRE, couleur, gras=True).move_to([0, c.Y_TITRE, 0])
        # Thème « marque » : un titre mis en avant s'écrit en blanc sur une pastille rouge.
        if c.MARQUE and "ambre" in options:
            nouveau = c.pastille(c.texte(contenu, c.T_TITRE, "#FFFFFF", gras=True)).move_to([0, c.Y_TITRE, 0])
        if nouveau.width > self.largeur_titres():
            nouveau.scale_to_fit_width(self.largeur_titres())
        nouveau.set_x(self.x_titres(nouveau.width))
        nouveau.original_text = contenu
        # L'ancien titre part d'abord : jamais deux titres superposés pendant le fondu.
        if anims:
            self.jouer(*anims, duree=0.25)
        self.titre = nouveau
        self.focus = nouveau
        return [FadeIn(nouveau, shift=DOWN * 0.2)]

    def largeur_titres(self):
        """Largeur maximale d'un titre : dans le cadre, et à gauche du repère permanent s'il est là."""
        repere = getattr(self, "repere", None)
        if repere is None:
            return 13.0
        return min(13.0, repere.get_left()[0] - 0.3 + 6.9)

    def x_titres(self, largeur):
        """Abscisse du centre d'un titre : au milieu de l'écran, ou décalé à gauche juste assez pour laisser le repère libre."""
        repere = getattr(self, "repere", None)
        if repere is None:
            return 0.0
        return min(0.0, repere.get_left()[0] - 0.3 - largeur / 2)

    def a_sous_titre(self, contenu):
        nouveau = c.texte(contenu, c.T_SOUS_TITRE).move_to([0, c.Y_SOUS_TITRE, 0])
        if nouveau.width > self.largeur_titres():
            nouveau.scale_to_fit_width(self.largeur_titres())
        # Centré sous le titre s'il y en a un, sans jamais empiéter sur le repère.
        x = self.titre.get_x() if self.titre is not None else 0.0
        nouveau.set_x(min(x, self.x_titres(nouveau.width)) if getattr(self, "repere", None) is not None else x)
        nouveau.original_text = contenu
        anims = [FadeOut(self.sous_titre)] if self.sous_titre is not None else []
        anims += self.retirer_traits(self.sous_titre)
        if anims:
            self.jouer(*anims, duree=0.25)
        self.sous_titre = nouveau
        self.focus = nouveau
        return [FadeIn(nouveau, shift=DOWN * 0.15)]

    def a_effacer_titres(self):
        # Le trait d'un titre barré part avec le titre.
        anims = [FadeOut(m) for m in [self.titre, self.sous_titre] if m is not None]
        anims += self.retirer_traits(self.titre) + self.retirer_traits(self.sous_titre)
        self.titre = self.sous_titre = None
        # Joué tout de suite : un titre qui suit dans le même moment ne se superpose pas au fondu.
        if anims:
            self.jouer(*anims, duree=0.25)
        return []

    def retirer_traits(self, cible):
        """Le trait qui barre un titre part avec ce titre."""
        traits = getattr(self, "traits", [])
        partants = [t for c_, t in traits if c_ is cible and cible is not None]
        self.traits = [(c_, t) for c_, t in traits if not (c_ is cible and cible is not None)]
        return [FadeOut(t) for t in partants]

    def a_barrer(self):
        cible = self.sous_titre or self.titre
        trait = c.barre(cible)
        self.traits = getattr(self, "traits", []) + [(cible, trait)]
        self.focus = cible
        return [Create(trait), cible.animate.set_opacity(0.55)]

    def a_renvoi(self, contenu):
        # En bas à droite, à hauteur du bloc d'article : au-dessus de la bande des sous-titres.
        nouveau = c.texte(contenu, c.T_PETIT, c.GRIS).to_corner(DOWN + RIGHT, buff=0.4).set_y(c.Y_ARTICLE)
        nouveau.original_text = contenu
        anims = [FadeOut(self.renvoi)] if self.renvoi is not None else []
        self.renvoi = nouveau
        return anims + [FadeIn(nouveau)]

    def a_mot_barre(self, contenu, x=3.4, y=None):
        y = 1.0 - 1.2 * len(self.mots_barres) if y is None else float(y)
        mot = c.texte(contenu, 46).move_to([float(x), y, 0])
        mot.original_text = contenu
        self.mots_barres.append(mot)
        self.add(mot)
        self.focus = mot
        return [FadeIn(mot), Create(c.barre(mot))]

    # ----- actions : la loi -----
    def placer_bas(self):
        """Article et arrêt côte à côte, centrés en bas ; seul, chacun est centré. Renvoie les déplacements."""
        blocs = [m for m in (self.article, self.arret) if m is not None]
        largeur = sum(m.width for m in blocs) + 0.4 * (len(blocs) - 1)
        x, anims = -largeur / 2, []
        for m in blocs:
            cible = x + m.width / 2
            if self.a_l_ecran(m) and abs(m.get_x() - cible) > 0.01:
                anims.append(m.animate.set_x(cible))
            else:
                m.set_x(cible)
            x += m.width + 0.4
        return anims

    def a_article(self, libelle):
        nouveau = c.BlocArticle(libelle)
        anciens = [FadeOut(self.article)] if self.article is not None else []
        self.article = nouveau
        return anciens + self.placer_bas() + [FadeIn(nouveau, shift=UP * 0.2)]

    def a_arret(self, libelle):
        """Arrêt du Tribunal fédéral cité par la voix ou par l'audit : bloc ambre à côté de l'article."""
        nouveau = c.BlocArret(libelle)
        anciens = [FadeOut(self.arret)] if self.arret is not None else []
        self.arret = nouveau
        self.focus = nouveau
        return anciens + self.placer_bas() + [FadeIn(nouveau, shift=UP * 0.2)]

    def a_arret_retirer(self):
        if self.arret is None:
            return []
        ancien, self.arret = self.arret, None
        return [FadeOut(ancien)] + self.placer_bas()

    def a_article_retirer(self):
        if self.article is None:
            return []
        ancien, self.article = self.article, None
        return [FadeOut(ancien)] + self.placer_bas()

    def a_article_etirer(self):
        self.focus = self.article
        return [self.article.cadre.animate.stretch(1.6, 0).set_stroke(c.ACCENT)]

    def a_article_reprendre(self):
        cadre = c.BlocArticle(self.article.libelle).cadre
        return [Transform(self.article.cadre, cadre)]

    def a_livre(self, titre="Code pénal", x=None):
        """Un recueil fermé ; au centre, ou à l'abscisse x (à côté d'une liste)."""
        self.livre = c.Livre(titre, x=float(x) if x is not None else 0.0)
        self.focus = self.livre
        return [FadeIn(self.livre, shift=UP * 0.2)]

    def a_livre_ouvrir(self):
        pages = self.livre.ouvert()
        ancien = self.livre
        self.livre = pages
        self.focus = pages
        return [FadeOut(ancien), FadeIn(pages)]

    def a_livre_chercher(self):
        """On parcourt le livre ouvert : une bande ambre descend les lignes des deux pages, puis s'éteint."""
        pages = self.livre
        bande = c.Rectangle(width=2.1, height=0.3, stroke_width=0, fill_color=c.ACCENT, fill_opacity=0.35)
        bande.move_to(pages[2][0].get_center())
        self.play(FadeIn(bande), run_time=0.2)
        for lignes in (pages[2], pages[3]):
            for trait in lignes:
                self.play(bande.animate.move_to(trait.get_center()), run_time=0.15)
        self.focus = pages
        return [bande.animate.set_fill(c.GRIS, opacity=0)]

    def a_livre_retirer(self):
        ancien, self.livre = self.livre, None
        return [FadeOut(ancien)]

    def a_livres(self, *titres):
        self.livres = [c.Livre(t, x=-4.2 + 4.2 * i, largeur=1.8, hauteur=2.4, etiquette_dessous=True)
                       for i, t in enumerate(titres)]
        groupe = VGroup(*self.livres)
        repere = getattr(self, "repere", None)
        if repere is not None and groupe.get_right()[0] > repere.get_left()[0] - 0.2 and groupe.get_top()[1] > repere.get_bottom()[1] - 0.2:
            groupe.shift(LEFT * (groupe.get_right()[0] - repere.get_left()[0] + 0.3))
        self.focus = groupe
        return [FadeIn(l, shift=UP * 0.2) for l in self.livres]

    def a_livres_surligner(self, n):
        anims = []
        for i, livre in enumerate(self.livres, 1):
            if i == int(n):
                anims.append(livre.couverture.animate.set_stroke(c.ACCENT, width=6))
                self.focus = livre
            else:
                anims.append(livre.animate.set_opacity(0.35))
        return anims

    # ----- actions : personnes -----
    def a_personnage(self, ident, nom, couleur, position, *options):
        p = c.Personnage(nom, c.COULEURS_PERSONNAGES[couleur], position)
        # « haut » : un peu plus haut, pour laisser la place à une frise en dessous.
        if "haut" in options:
            p.shift(UP * 0.45)
        anims = [FadeOut(self.personnages[ident])] if ident in self.personnages else []
        self.personnages[ident] = p
        self.focus = p
        return anims + [FadeIn(p, shift=UP * 0.2)]

    # ----- actions : décors, mouvements, repère -----
    def a_decor(self, nom, *options):
        decors = {"escalier": c.Escalier, "appartement": c.Appartement, "rue": c.Rue, "tribunal": c.Tribunal, "parc": c.Parc, "piscine": c.Piscine}
        if nom not in decors:
            raise ValueError(f"décor inconnu « {nom} »")
        self.decor = decors[nom](*options)
        return [FadeIn(self.decor)]

    def a_decor_retirer(self):
        anims = [FadeOut(m) for m in (self.decor, self.neige) if m is not None]
        self.decor = self.neige = None
        return anims

    def a_neige(self):
        self.neige = c.Neige(self.decor.fenetre)
        return [FadeIn(self.neige)]

    def a_picto(self, nom, x, y):
        # « parlement:2 » : un deuxième pictogramme du même type, avec son propre nom.
        p = c.Picto(nom.split(":")[0], [float(x), float(y), 0])
        self.pictos[nom] = p
        self.focus = p
        return [FadeIn(p, scale=0.6)]

    def a_picto_deplacer(self, nom, x, y, arc="0"):
        """Déplace un pictogramme (le ballon qui part) ; arc > 0 : trajectoire en cloche."""
        p = self.pictos[nom]
        self.focus = p
        return [p.animate(path_arc=-float(arc)).move_to([float(x), float(y), 0])]

    def a_picto_retirer(self, nom):
        return [FadeOut(self.pictos.pop(nom))]

    def a_etiquette(self, ident, contenu, x, y):
        e = c.Etiquette(contenu, [float(x), float(y), 0])
        e.contenu = contenu
        # L'ancienne étiquette part d'abord : jamais deux textes superposés pendant le fondu.
        if ident in self.etiquettes:
            self.jouer(FadeOut(self.etiquettes[ident]), duree=0.25)
        self.etiquettes[ident] = e
        self.focus = e
        return [FadeIn(e, shift=UP * 0.15)]

    def a_etiquette_retirer(self, ident):
        return [FadeOut(self.etiquettes.pop(ident))]

    def pieds_sur(self, p, n):
        cible = np.array(self.decor.pied(int(n)))
        return cible - p.silhouette.get_bottom()

    def a_placer(self, ident, n):
        """Pose le personnage sur la marche n du décor, sans animation (à jouer avec son apparition)."""
        p = self.personnages[ident]
        # Dans un décor, la silhouette est un peu plus petite pour tenir sur les marches ;
        # le nom garde sa taille (lisibilité, 28 points au minimum).
        if not getattr(p, "dans_decor", False):
            p.silhouette.scale(0.8, about_edge=DOWN)
            p.etiquette.next_to(p.silhouette, DOWN, buff=0.2)
            p.dans_decor = True
        p.shift(self.pieds_sur(p, n))
        # Derrière un meuble (banc du juge, barre des témoins) : le nom s'inscrit sur le meuble, au premier plan.
        meuble = self.decor.meuble_devant(p.silhouette.get_x()) if hasattr(self.decor, "meuble_devant") else None
        if meuble is not None:
            p.etiquette.move_to(meuble).set_z_index(2)
            p.derriere_meuble = True
        return []

    def a_marcher(self, ident, n):
        p = self.personnages[ident]
        self.focus = p
        decalage = self.pieds_sur(p, n)
        meuble = (self.decor.meuble_devant(p.silhouette.get_x() + decalage[0])
                  if hasattr(self.decor, "meuble_devant") else None)
        if meuble is None:
            return [p.animate(run_time=1.2).shift(decalage)]
        # Jusque derrière un meuble : le nom vient s'inscrire dessus, au premier plan.
        p.etiquette.set_z_index(2)
        p.derriere_meuble = True
        return [p.silhouette.animate(run_time=1.2).shift(decalage), p.etiquette.animate(run_time=1.2).move_to(meuble)]

    def a_pousser(self, ident, cible):
        a, b = self.personnages[ident], self.personnages[cible]
        sens = 1 if b.get_center()[0] > a.get_center()[0] else -1
        self.focus = a
        return [a.silhouette.animate(rate_func=there_and_back).shift(RIGHT * 0.45 * sens).rotate(-0.15 * sens)]

    def a_chute(self, ident, n):
        p = self.personnages[ident]
        self.focus = p
        decalage = self.pieds_sur(p, n)
        return [p.silhouette.animate.shift(decalage).rotate(1.25), p.etiquette.animate.shift(decalage)]

    def a_repere_batiment(self):
        self.repere = c.MiniBatiment()
        return [FadeIn(self.repere)]

    def a_repere_liste(self, *libelles):
        """Pense-bête permanent en haut à droite. Si une liste est à l'écran, elle s'y range."""
        self.repere = c.RepereListe(*libelles)
        if self.liste is not None and self.a_l_ecran(self.liste):
            ancienne, self.liste = self.liste, None
            return [ReplacementTransform(ancienne, self.repere)]
        return [FadeIn(self.repere, shift=LEFT * 0.2)]

    def a_repere_marquer(self, n, etat):
        self.focus = self.repere.lignes[int(n) - 1]
        return self.repere.marquer(int(n), etat)

    def a_repere_retirer(self):
        ancien, self.repere = getattr(self, "repere", None), None
        return [FadeOut(ancien)] if ancien is not None else []

    def a_repere_etage(self, n, etat):
        return [self.repere.colorer(int(n), etat)]

    def a_retirer(self, ident):
        p = self.personnages.pop(ident)
        if self.focus is p:
            self.focus = None
        anims = [FadeOut(p)]
        for registre in (self.paroles, self.bulles):
            if ident in registre:
                anims.append(FadeOut(registre.pop(ident)))
        return anims

    def a_accent(self, cible):
        objets = {"titre": self.titre, "livre": self.livre, "liste": self.liste, "cases": self.cases,
                  "batiment": self.batiment,
                  "frise": self.frise, "livres": self.livres and VGroup(*self.livres)}
        m = self.personnages.get(cible) or objets.get(cible)
        if m is None:
            raise ValueError(f"accent : cible inconnue « {cible} »")
        self.focus = m
        return [Indicate(m, color=c.ACCENT, scale_factor=1.08)]

    def a_parole(self, ident, contenu):
        p = self.personnages[ident]
        g = c.avec_fond(c.texte(contenu, c.T_CORPS, gras=True)).next_to(p.silhouette, UP, buff=0.4)
        # Vers le centre de l'écran, d'après la place réelle du personnage (il a pu se déplacer),
        # puis ramenée dans le cadre.
        g.shift((LEFT if p.silhouette.get_center()[0] > 0 else RIGHT) * 1.2)
        if g.get_right()[0] > 6.9:
            g.shift(LEFT * (g.get_right()[0] - 6.9))
        if g.get_left()[0] < -6.9:
            g.shift(RIGHT * (-6.9 - g.get_left()[0]))
        g.contenu = contenu
        self.paroles[ident] = g
        self.focus = g
        return [FadeIn(g, shift=UP * 0.1)]

    def a_effacer_parole(self, ident):
        return [FadeOut(self.paroles.pop(ident))]

    def a_bulle(self, ident, contenu):
        b = c.Bulle(self.personnages[ident], contenu)
        b.contenu = contenu
        if ident in self.bulles:
            self.jouer(FadeOut(self.bulles[ident]), duree=0.25)
        self.bulles[ident] = b
        self.focus = b
        return [FadeIn(b, scale=0.8)]

    def a_jetons(self, de, vers):
        depart = self.personnages[de].silhouette.get_center()
        arrivee = self.personnages[vers].silhouette.get_center()
        jetons = c.Jetons(depart)
        self.add(jetons)
        self.play(FadeIn(jetons), run_time=0.3)
        self.focus = jetons
        return [jetons.animate.move_to(arrivee)]

    def a_rembobiner(self):
        icone = c.Rembobinage()
        self.play(FadeIn(icone, scale=0.7), run_time=0.2)
        self.play(icone.animate.rotate(-6.283), run_time=0.4)
        self.play(FadeOut(icone), run_time=0.15)
        return []

    # ----- actions : l'infraction -----
    def a_batiment(self, *options):
        self.batiment = c.Batiment()
        # « batiment 3.5 » : décalé sur le côté, à côté d'une liste.
        decalage = next((float(o) for o in options if o.replace(".", "", 1).lstrip("-").isdigit()), None)
        if decalage is not None:
            self.batiment.shift(RIGHT * decalage)
        # « petit » : réduit à 85 % (le corps des étages reste au-dessus du minimum de la charte), pied fixe.
        if "petit" in options:
            self.batiment.scale(0.85, about_point=[self.batiment.get_x(), c.Y_BATIMENT - 0.525, 0])
        self.batiment.vide = "vide" in options
        self.focus = self.batiment
        etapes = self.batiment.construire(vide=self.batiment.vide)
        self.play(AnimationGroup(*etapes, lag_ratio=0.25), run_time=1.6)
        return []

    def a_etage(self, n, etat):
        self.focus = self.batiment.etages[int(n) - 1]
        return [self.batiment.colorer(int(n), etat)]

    def a_etage_nom(self, n):
        etiquette = self.batiment.etages[int(n) - 1][1]
        self.focus = etiquette
        return [etiquette.animate.set_opacity(1)]

    def a_etage_question(self, n):
        cadre = self.batiment.etages[int(n) - 1][0]
        marque = c.texte("?", c.T_TITRE, c.ACCENT, gras=True).next_to(cadre, RIGHT, buff=0.3)
        self.focus = marque
        return [FadeIn(marque, scale=1.4)]

    def a_question_etage(self, n, contenu):
        """Écrit une question à droite d'un étage ; une seule à la fois (règle des douze mots)."""
        anims = []
        if not getattr(self, "questions_etages", None):
            self.questions_etages = {}
            # Le bâtiment se décale à gauche pour laisser la place au texte.
            self.play(self.batiment.animate.shift(LEFT * 3), run_time=0.5)
        for ancienne in self.questions_etages.values():
            anims.append(FadeOut(ancienne))
        self.questions_etages = {}
        cadre = self.batiment.etages[int(n) - 1][0]
        q = c.texte(contenu, c.T_CORPS, c.ACCENT).next_to(cadre, RIGHT, buff=0.4)
        q.original_text = contenu
        self.questions_etages[n] = q
        self.focus = q
        return anims + [FadeIn(q, shift=LEFT * 0.2)]

    def a_bouclier(self, x=None, y=None):
        # Au point donné ; sinon à droite du bâtiment, à hauteur de l'illicéité, ou au centre de l'écran.
        if x is not None:
            centre = [float(x), float(y), 0]
        else:
            centre = self.batiment.etages[1][0].get_right() + RIGHT * 1.4 if self.batiment else [0, 0.6, 0]
        ancien = [FadeOut(self.bouclier)] if self.bouclier is not None and self.a_l_ecran(self.bouclier) else []
        self.bouclier = c.Bouclier(centre)
        self.focus = self.bouclier
        return ancien + [FadeIn(self.bouclier, scale=0.6)]

    def a_bouclier_repousser(self):
        b = self.bouclier
        depart = b.get_right() + RIGHT * 2.2
        fleche = c.Arrow(depart, b.get_right() + RIGHT * 0.1, color=c.TEXTE, stroke_width=6, buff=0)
        self.play(GrowArrow(fleche), run_time=0.5)
        self.play(fleche.animate.shift(RIGHT * 1.5).set_opacity(0), b.animate(rate_func=there_and_back).scale(1.1),
                  run_time=0.6)
        self.remove(fleche)
        self.focus = b
        return []

    def a_dommage(self, ident):
        """Le dommage, seul usage du rouge : éclair sur la silhouette."""
        s = self.personnages[ident].silhouette
        eclair = c.Polygon([0.1, 0.35, 0], [-0.15, 0.0, 0], [0.05, 0.0, 0], [-0.1, -0.35, 0], [0.2, 0.05, 0],
                           [0.0, 0.05, 0], color=c.ROUGE, fill_color=c.ROUGE, fill_opacity=1, stroke_width=0)
        eclair.scale(1.6).next_to(s[1], RIGHT, buff=-0.15)
        self.focus = eclair
        return [FadeIn(eclair, scale=1.8)]

    def a_deplacer(self, ident, position):
        p = self.personnages[ident]
        p.position = position
        return [p.animate.move_to([c.X_POSITIONS[position], p.get_center()[1], 0])]

    def a_basculer(self, ident):
        p = self.personnages[ident]
        self.focus = p
        return [p.silhouette.animate.rotate(-1.2).shift(DOWN * 0.6 + RIGHT * 0.4)]

    def a_effacer_bulle(self, ident):
        return [FadeOut(self.bulles.pop(ident))]

    def a_fleche(self, n):
        bas = c.Y_BATIMENT - 0.55
        haut = bas + 1.05 * int(n) - 0.15
        x = self.batiment.get_left()[0] - 0.7 if self.batiment is not None else -3.0
        fleche = c.Arrow([x, bas, 0], [x, haut, 0], color=c.ACCENT, stroke_width=6, buff=0)
        return [GrowArrow(fleche)]

    # ----- actions : listes, cases, colonnes -----
    def a_liste(self, *elements):
        self.liste = c.Liste()
        for e in elements:
            t = self.liste.nouvel_element(e)
            t.original_text = e
        self.focus = self.liste
        return [FadeIn(self.liste, shift=RIGHT * 0.2)]

    def a_liste_ajouter(self, contenu):
        if self.liste is None:
            self.liste = c.Liste()
            self.add(self.liste)
        t = self.liste.nouvel_element(contenu)
        t.original_text = contenu
        self.focus = t
        return [FadeIn(t, shift=RIGHT * 0.3)]

    def a_liste_surligner(self, n):
        anims = []
        for i, t in enumerate(self.liste.elements, 1):
            anims.append(t.animate.set_color(c.ACCENT if i == int(n) else c.GRIS))
        self.focus = self.liste.elements[int(n) - 1]
        return anims

    def sous_le_repere(self, groupe):
        """Descend un groupe (des cases) qui toucherait le repère permanent."""
        repere = getattr(self, "repere", None)
        if repere is not None and groupe.get_right()[0] > repere.get_left()[0] - 0.15:
            ecart = groupe.get_top()[1] - (repere.get_bottom()[1] - 0.25)
            if ecart > 0:
                groupe.shift(DOWN * ecart)

    def a_cases(self, *libelles):
        self.cases = c.Cases()
        for l in libelles:
            ligne = self.cases.nouvelle_case(l)
            ligne[1].original_text = l
        self.sous_le_repere(self.cases)
        self.focus = self.cases
        return [FadeIn(self.cases, shift=UP * 0.2)]

    def a_case(self, libelle):
        if self.cases is None:
            self.cases = c.Cases()
            self.add(self.cases)
        ligne = self.cases.nouvelle_case(libelle)
        ligne[1].original_text = libelle
        # Alignée sous les cases déjà là (elles ont pu descendre sous le repère).
        if len(self.cases.lignes) > 1:
            ligne.set_y(self.cases.lignes[-2].get_y() - 0.95)
        else:
            self.sous_le_repere(ligne)
        self.focus = ligne
        return [FadeIn(ligne, shift=RIGHT * 0.2)]

    def a_cocher(self, n, etat):
        anim, signe = self.cases.marque(int(n), etat)
        self.cases.add(signe)
        self.focus = self.cases.lignes[int(n) - 1]
        return [anim, FadeIn(signe)]

    def a_retirer_pyramide(self):
        ancien, self.pyramide = self.pyramide, None
        return [FadeOut(ancien)]

    def a_colonnes(self, a, b):
        self.colonnes = c.Colonnes(a, b)
        for m, s in zip(self.colonnes.mots, (a, b)):
            m.original_text = s
        self.focus = self.colonnes
        return [FadeIn(self.colonnes)]

    def a_colonne_accent(self, n):
        m = self.colonnes.mots[int(n) - 1]
        self.focus = m
        return [m.animate.set_color(c.ACCENT)]

    def a_colonne_eteindre(self, n):
        return [self.colonnes.mots[int(n) - 1].animate.set_color(c.GRIS).set_opacity(0.5)]

    # ----- actions : autorités -----
    def a_pyramide(self):
        self.pyramide = c.Pyramide()
        self.focus = self.pyramide
        self.play(AnimationGroup(*[FadeIn(n, shift=UP * 0.15) for n in self.pyramide.niveaux], lag_ratio=0.3),
                  run_time=1.0)
        return []

    def a_pyramide_niveau(self, n, etat):
        forme = self.pyramide.niveaux[int(n) - 1][0]
        return [forme.animate.set_fill(c.ETATS[etat], opacity=0.85)]

    # ----- actions : le temps -----
    def a_frise(self, *options):
        # « bas » : plus bas, sous une liste.
        self.frise = c.Frise(c.Y_FRISE - 0.45 if "bas" in options else c.Y_FRISE)
        self.focus = self.frise
        return [GrowArrow(self.frise.ligne)]

    def a_repere(self, fraction, libelle):
        r = self.frise.repere(fraction, libelle)
        r[1].original_text = libelle
        self.frise_points.append(r)
        self.focus = r
        return [Create(r[0]), FadeIn(r[1])]

    def a_point(self, fraction, libelle):
        p = self.frise.point(fraction, libelle)
        p[1].original_text = libelle
        self.frise_points.append(p)
        self.focus = p
        return [FadeIn(p, scale=0.6)]

    def a_zone(self, a, b, etat):
        return [FadeIn(self.frise.zone(a, b, etat))]

    def a_fleche_retour(self, de, vers, issue):
        anciennes = getattr(self, "fleches_retour", [])
        if anciennes:
            self.jouer(*[FadeOut(m) for m in anciennes], duree=0.3)
        self.fleches_retour = []
        if issue == "vert":
            f = self.frise.fleche_retour(de, vers, c.VERT)
            self.focus = f
            self.fleches_retour = [f]
            return [Create(f)]
        # « casse » : la flèche part en arrière, puis se brise et devient grise.
        f = self.frise.fleche_retour(de, vers, c.TEXTE)
        self.play(Create(f), run_time=0.7)
        x = self.frise.x((float(de) + float(vers)) / 2)
        croix = VGroup(Line([x - 0.3, self.frise.y + 1.5, 0], [x + 0.3, self.frise.y + 2.1, 0], color=c.TEXTE, stroke_width=8),
                       Line([x - 0.3, self.frise.y + 2.1, 0], [x + 0.3, self.frise.y + 1.5, 0], color=c.TEXTE, stroke_width=8))
        self.focus = croix
        self.fleches_retour = [f, croix]
        return [f.animate.set_color(c.GRIS), Create(croix)]

    def a_questions(self):
        marques = [c.texte("?", c.T_TITRE, c.ACCENT, gras=True).next_to(p, UP, buff=0.1)
                   for p in self.frise_points if isinstance(p[0], c.Dot)]
        self.focus = VGroup(*marques)
        return [FadeIn(m, scale=1.4) for m in marques]
