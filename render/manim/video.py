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
import os
import re
import shlex
from pathlib import Path

from manim import (
    DOWN, LEFT, RIGHT, UP, AnimationGroup, Create, FadeIn, FadeOut, GrowArrow, Indicate,
    Line, Scene, Transform, VGroup, Write, config, there_and_back,
)

import charte as c

RACINE = Path(__file__).resolve().parents[2]
SLUG = os.environ.get("SLUG", "")
DUREE_ANIM = 0.7
PLAN_FIXE_MAX = 4.0

config.background_color = c.FOND
if os.environ.get("APERCU"):
    config.pixel_width, config.pixel_height, config.frame_rate = 854, 480, 15
else:
    config.pixel_width, config.pixel_height, config.frame_rate = 1920, 1080, 30


def lire_moments(slug):
    """Renvoie [(instant en secondes, [actions])] trié, à partir de visuals.md et timings.json."""
    timings = json.loads((RACINE / "voice" / slug / "timings.json").read_text(encoding="utf-8"))
    lignes = {l["ligne"]: l for l in timings["lignes"]}
    moments = []
    for ligne in (RACINE / "scripts" / slug / "visuals.md").read_text(encoding="utf-8").splitlines():
        m = re.match(r"\|\s*(\d+)\.(\d+)(?:\+([\d.]+))?\s*\|(.*)\|\s*$", ligne)
        if not m:
            continue
        n, p, decalage, actions = int(m[1]), int(m[2]), float(m[3] or 0), m[4]
        phrase = lignes[n]["phrases"][p - 1]
        moments.append((phrase["debut"] + decalage, [shlex.split(a) for a in actions.split(";") if a.strip()],
                        f"{m[1]}.{m[2]}"))
    return sorted(moments, key=lambda x: x[0]), timings["duree"]


class Schemas(Scene):
    def setup(self):
        self.t = 0.0
        self.alertes = []
        self.personnages, self.paroles, self.bulles = {}, {}, {}
        self.titre = self.sous_titre = self.article = self.renvoi = None
        self.batiment = self.livre = self.liste = self.cases = self.pyramide = None
        self.frise = self.colonnes = self.livres = None
        self.frise_points, self.mots_barres, self.fleches_retour = [], [], []
        self.questions_etages, self.bouclier = {}, None
        self.focus = None

    # ----- temps -----
    def jouer(self, *animations, duree=DUREE_ANIM):
        animations = [a for a in animations if a is not None]
        if animations:
            self.play(*animations, run_time=duree)
            self.t += duree

    def attendre_jusqua(self, instant):
        """Attend jusqu'à l'instant donné, en faisant respirer l'image si l'attente dépasse quatre secondes."""
        while instant - self.t > PLAN_FIXE_MAX and self.a_l_ecran(self.focus):
            self.wait(2.0)
            self.t += 2.0
            self.play(self.focus.animate(rate_func=there_and_back).scale(1.04), run_time=1.2)
            self.t += 1.2
        if instant > self.t:
            self.wait(instant - self.t)
            self.t = instant

    def a_l_ecran(self, m):
        return m is not None and any(m is x or m in x.get_family() for x in self.mobjects)

    # ----- règle des douze mots -----
    def mots_visibles(self):
        textes = []
        for m in [self.titre, self.sous_titre, self.renvoi]:
            if m is not None:
                textes.append(m.original_text)
        for p in self.personnages.values():
            textes.append(p.nom)
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
        return sum(c.mots(t) for t in textes)

    # ----- rendu -----
    def construct(self):
        moments, duree_totale = lire_moments(SLUG)
        for instant, actions, repere in moments:
            if self.t - instant > 0.5:
                self.alertes.append(f"{repere} : animation en retard de {self.t - instant:.1f} s sur la voix")
            self.attendre_jusqua(instant)
            # Une scène vide se joue d'abord, seule, pour libérer l'écran.
            if any(a[0] == "scene-vide" for a in actions):
                self.scene_vide()
                actions = [a for a in actions if a[0] != "scene-vide"]
            animations = []
            for action in actions:
                methode = getattr(self, "a_" + action[0].replace("-", "_"), None)
                if methode is None:
                    raise ValueError(f"{repere} : action inconnue « {action[0]} »")
                resultat = methode(*action[1:])
                animations += resultat if isinstance(resultat, list) else [resultat]
            self.jouer(*animations)
            total = self.mots_visibles()
            if total > 12:
                self.alertes.append(f"{repere} : {total} mots affichés (maximum 12)")
        self.attendre_jusqua(duree_totale)
        rapport = RACINE / "out" / (SLUG.replace("/", "--") + "--alertes-visuels.txt")
        rapport.parent.mkdir(exist_ok=True)
        rapport.write_text("\n".join(self.alertes) + "\n" if self.alertes else "Aucune alerte.\n", encoding="utf-8")
        print("\n".join(self.alertes) or "Aucune alerte de charte.")

    def scene_vide(self):
        garder = [self.article] if self.article is not None else []
        a_retirer = [m for m in self.mobjects if m not in garder]
        if a_retirer:
            self.jouer(*[FadeOut(m) for m in a_retirer], duree=0.4)
        article, t, alertes = self.article, self.t, self.alertes
        self.setup()
        self.article, self.t, self.alertes = article, t, alertes
        return []

    # ----- actions : texte -----
    def a_titre(self, contenu, *options):
        couleur = c.ACCENT if "ambre" in options else c.TEXTE
        anims = [FadeOut(self.titre)] if self.titre is not None else []
        if "mot-a-mot" in options:
            # Les mots apparaissent un par un pendant la phrase (règle des quatre secondes).
            # Le texte est rendu d'un seul tenant (ligne de base commune), puis découpé en mots :
            # les sous-objets de Text sont les caractères, espaces exclus.
            nouveau = c.texte(contenu, c.T_TITRE, couleur, gras=True).move_to([0, c.Y_TITRE, 0])
            nouveau.original_text = contenu
            groupes, i = [], 0
            for mot in contenu.split():
                groupes.append(VGroup(*nouveau.submobjects[i:i + len(mot)]))
                i += len(mot)
            self.titre = self.focus = nouveau
            if anims:
                self.jouer(*anims, duree=0.3)
            self.play(AnimationGroup(*[FadeIn(g, shift=UP * 0.1) for g in groupes], lag_ratio=1.0), run_time=4.5)
            self.t += 4.5
            return []
        nouveau = c.texte(contenu, c.T_TITRE, couleur, gras=True).move_to([0, c.Y_TITRE, 0])
        nouveau.original_text = contenu
        self.titre = nouveau
        self.focus = nouveau
        anims.append(FadeIn(nouveau, shift=DOWN * 0.2))
        return anims

    def a_sous_titre(self, contenu):
        nouveau = c.texte(contenu, c.T_SOUS_TITRE).move_to([0, c.Y_SOUS_TITRE, 0])
        nouveau.original_text = contenu
        anims = [FadeOut(self.sous_titre)] if self.sous_titre is not None else []
        self.sous_titre = nouveau
        self.focus = nouveau
        return anims + [FadeIn(nouveau, shift=DOWN * 0.15)]

    def a_effacer_titres(self):
        anims = [FadeOut(m) for m in [self.titre, self.sous_titre] if m is not None]
        self.titre = self.sous_titre = None
        return anims

    def a_barrer(self):
        cible = self.sous_titre or self.titre
        trait = c.barre(cible)
        self.focus = cible
        return [Create(trait), cible.animate.set_opacity(0.55)]

    def a_renvoi(self, contenu):
        nouveau = c.texte(contenu, c.T_PETIT, c.GRIS).to_corner(DOWN + RIGHT, buff=0.4)
        nouveau.original_text = contenu
        anims = [FadeOut(self.renvoi)] if self.renvoi is not None else []
        self.renvoi = nouveau
        return anims + [FadeIn(nouveau)]

    def a_mot_barre(self, contenu):
        mot = c.texte(contenu, 46).move_to([3.4, 1.0 - 1.2 * len(self.mots_barres), 0])
        mot.original_text = contenu
        self.mots_barres.append(mot)
        self.add(mot)
        self.focus = mot
        return [FadeIn(mot), Create(c.barre(mot))]

    # ----- actions : la loi -----
    def a_article(self, libelle):
        nouveau = c.BlocArticle(libelle)
        if self.article is None:
            self.article = nouveau
            return [FadeIn(nouveau, shift=UP * 0.2)]
        ancien = self.article
        self.article = nouveau
        return [FadeOut(ancien), FadeIn(nouveau, shift=UP * 0.2)]

    def a_article_retirer(self):
        if self.article is None:
            return []
        ancien, self.article = self.article, None
        return [FadeOut(ancien)]

    def a_article_etirer(self):
        self.focus = self.article
        return [self.article.cadre.animate.stretch(1.6, 0).set_stroke(c.ACCENT)]

    def a_article_reprendre(self):
        cadre = c.BlocArticle(self.article.libelle).cadre
        return [Transform(self.article.cadre, cadre)]

    def a_livre(self):
        self.livre = c.Livre()
        self.focus = self.livre
        return [FadeIn(self.livre, shift=UP * 0.2)]

    def a_livre_ouvrir(self):
        pages = self.livre.ouvert()
        ancien = self.livre
        self.livre = pages
        self.focus = pages
        return [FadeOut(ancien), FadeIn(pages)]

    def a_livre_retirer(self):
        ancien, self.livre = self.livre, None
        return [FadeOut(ancien)]

    def a_livres(self, *titres):
        self.livres = [c.Livre(t, x=-4.2 + 4.2 * i, largeur=1.8, hauteur=2.4, etiquette_dessous=True)
                       for i, t in enumerate(titres)]
        self.focus = VGroup(*self.livres)
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
    def a_personnage(self, ident, nom, couleur, position):
        p = c.Personnage(nom, c.COULEURS_PERSONNAGES[couleur], position)
        anims = [FadeOut(self.personnages[ident])] if ident in self.personnages else []
        self.personnages[ident] = p
        self.focus = p
        return anims + [FadeIn(p, shift=UP * 0.2)]

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
        g = c.texte(contenu, c.T_CORPS, gras=True).next_to(p.silhouette, UP, buff=0.4)
        g.shift(p.vers_le_centre() * 1.2)
        g.contenu = contenu
        self.paroles[ident] = g
        self.focus = g
        return [FadeIn(g, shift=UP * 0.1)]

    def a_effacer_parole(self, ident):
        return [FadeOut(self.paroles.pop(ident))]

    def a_bulle(self, ident, contenu):
        b = c.Bulle(self.personnages[ident], contenu)
        b.contenu = contenu
        anims = [FadeOut(self.bulles[ident])] if ident in self.bulles else []
        self.bulles[ident] = b
        self.focus = b
        return anims + [FadeIn(b, scale=0.8)]

    def a_jetons(self, de, vers):
        depart = self.personnages[de].silhouette.get_center()
        arrivee = self.personnages[vers].silhouette.get_center()
        jetons = c.Jetons(depart)
        self.add(jetons)
        self.play(FadeIn(jetons), run_time=0.3)
        self.t += 0.3
        self.focus = jetons
        return [jetons.animate.move_to(arrivee)]

    def a_rembobiner(self):
        icone = c.Rembobinage()
        self.play(FadeIn(icone, scale=0.7), run_time=0.35)
        self.play(icone.animate.rotate(-6.283), run_time=0.6)
        self.play(FadeOut(icone), run_time=0.25)
        self.t += 1.2
        return []

    # ----- actions : l'infraction -----
    def a_batiment(self, *options):
        self.batiment = c.Batiment()
        self.batiment.vide = "vide" in options
        self.focus = self.batiment
        etapes = self.batiment.construire(vide=self.batiment.vide)
        self.play(AnimationGroup(*etapes, lag_ratio=0.25), run_time=1.6)
        self.t += 1.6
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
            self.t += 0.5
        for ancienne in self.questions_etages.values():
            anims.append(FadeOut(ancienne))
        self.questions_etages = {}
        cadre = self.batiment.etages[int(n) - 1][0]
        q = c.texte(contenu, c.T_CORPS, c.ACCENT).next_to(cadre, RIGHT, buff=0.4)
        q.original_text = contenu
        self.questions_etages[n] = q
        self.focus = q
        return anims + [FadeIn(q, shift=LEFT * 0.2)]

    def a_bouclier(self):
        # À droite du bâtiment, à hauteur de l'illicéité ; sinon au centre de l'écran.
        centre = self.batiment.etages[1][0].get_right() + RIGHT * 1.4 if self.batiment else [0, 0.6, 0]
        self.bouclier = c.Bouclier(centre)
        self.focus = self.bouclier
        return [FadeIn(self.bouclier, scale=0.6)]

    def a_bouclier_repousser(self):
        b = self.bouclier
        depart = b.get_right() + RIGHT * 2.2
        fleche = c.Arrow(depart, b.get_right() + RIGHT * 0.1, color=c.TEXTE, stroke_width=6, buff=0)
        self.play(GrowArrow(fleche), run_time=0.5)
        self.play(fleche.animate.shift(RIGHT * 1.5).set_opacity(0), b.animate(rate_func=there_and_back).scale(1.1),
                  run_time=0.6)
        self.remove(fleche)
        self.t += 1.1
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
        haut = -2.6 + 1.05 * int(n) - 0.15
        fleche = c.Arrow([-3.0, -2.6, 0], [-3.0, haut, 0], color=c.ACCENT, stroke_width=6, buff=0)
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

    def a_cases(self, *libelles):
        self.cases = c.Cases()
        for l in libelles:
            ligne = self.cases.nouvelle_case(l)
            ligne[1].original_text = l
        self.focus = self.cases
        return [FadeIn(self.cases, shift=UP * 0.2)]

    def a_case(self, libelle):
        if self.cases is None:
            self.cases = c.Cases()
            self.add(self.cases)
        ligne = self.cases.nouvelle_case(libelle)
        ligne[1].original_text = libelle
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
        self.t += 1.0
        return []

    def a_pyramide_niveau(self, n, etat):
        forme = self.pyramide.niveaux[int(n) - 1][0]
        return [forme.animate.set_fill(c.ETATS[etat], opacity=0.85)]

    # ----- actions : le temps -----
    def a_frise(self):
        self.frise = c.Frise()
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
        self.t += 0.7
        x = self.frise.x((float(de) + float(vers)) / 2)
        croix = VGroup(Line([x - 0.3, c.Y_FRISE + 1.5, 0], [x + 0.3, c.Y_FRISE + 2.1, 0], color=c.TEXTE, stroke_width=8),
                       Line([x - 0.3, c.Y_FRISE + 2.1, 0], [x + 0.3, c.Y_FRISE + 1.5, 0], color=c.TEXTE, stroke_width=8))
        self.focus = croix
        self.fleches_retour = [f, croix]
        return [f.animate.set_color(c.GRIS), Create(croix)]

    def a_questions(self):
        marques = [c.texte("?", c.T_TITRE, c.ACCENT, gras=True).next_to(p, UP, buff=0.1)
                   for p in self.frise_points if isinstance(p[0], c.Dot)]
        self.focus = VGroup(*marques)
        return [FadeIn(m, scale=1.4) for m in marques]
