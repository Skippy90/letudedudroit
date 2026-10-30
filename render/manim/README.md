# Schémas Manim

`video.py` lit `scripts/<slug>/visuals.md`, cale chaque moment sur la narration (`voice/<slug>/timings.json`) et rend une vidéo muette 1920 × 1080 à 30 images par seconde. `charte.py` dessine les éléments de la charte (`docs/charte-visuelle.md`).

Rendu : `make visuals SLUG=...` (ou `make video` pour toute la chaîne). Aperçu rapide en 480p :

```
cd render/manim && SLUG=<slug> APERCU=1 ../../.venv/bin/python -m manim render video.py Schemas
```

## Format de visuals.md

Un tableau à deux colonnes : `Moment` et `Actions`.

- `Moment` : `ligne.phrase` du script (`12.3` = troisième phrase de la ligne 12), éventuellement suivi de `+secondes` (`19.2+1.5`) ou de `@mot` (`2.3@poignet` : au moment où ce mot est prononcé ; il faut une narration enregistrée, dont `timings.json` donne l'instant de chaque mot).
- `Actions` : une ou plusieurs actions séparées par `;`. Les textes vont entre guillemets droits.

## Actions

| Action | Effet |
| --- | --- |
| `scene-vide` | Efface tout sauf le bloc d'article ; se joue avant les autres actions du moment |
| `titre "…"` [`ambre`] [`mot-a-mot`] | Titre en haut ; `mot-a-mot` fait apparaître les mots un par un (phrases longues) |
| `sous-titre "…"` | Ligne sous le titre |
| `effacer-titres` | Retire titre et sous-titre |
| `barrer` | Barre le sous-titre, ou à défaut le titre |
| `renvoi "vidéo N"` | Renvoi en petit, en bas à droite |
| `mot-barre "…"` | Mot affiché à droite puis barré |
| `article "Art. N CP"` | Bloc d'article centré en bas (remplace le précédent) |
| `article-retirer` | Retire le bloc d'article |
| `article-etirer` / `article-reprendre` | Le bloc s'étire puis reprend sa taille (interprétation et ses limites) |
| `livre` [`"titre"`] / `livre-ouvrir` / `livre-retirer` | Un recueil fermé (« Code pénal » par défaut ; un titre long passe sur plusieurs lignes), ouvert, retiré |
| `livres "…" "…" "…"` | Plusieurs recueils côte à côte |
| `livres-surligner N` | Met en avant le recueil N |
| `personnage ID "Nom" COULEUR POSITION` | Silhouette ; couleurs : `bleu_clair`, `ambre_pale`, `rose`, `violet`, `turquoise` ; positions : `gauche`, `centre-gauche`, `centre`, `centre-droite`, `droite` |
| `retirer ID` | Retire un personnage, sa parole et sa bulle |
| `parole ID "…"` / `effacer-parole ID` | Ce que dit le personnage |
| `bulle ID "…"` / `effacer-bulle ID` | Bulle de pensée (état d'esprit) ; une nouvelle bulle remplace la précédente |
| `dommage ID` | Éclair rouge sur la silhouette (seul usage du rouge) |
| `deplacer ID POSITION` / `basculer ID` | Le personnage se déplace ; le personnage tombe |
| `accent CIBLE` | Met en avant : un personnage, `titre`, `livre`, `liste`, `cases`, `frise`, `livres`, `batiment` |
| `jetons ID1 ID2` | L'argent passe de ID1 à ID2 |
| `rembobiner` | Icône de rembobinage (variante du cas) |
| `batiment` | Bâtiment à trois étages, construit de bas en haut |
| `etage N vert\|gris\|ambre\|neutre` | Colore l'étage N |
| `batiment vide` + `etage-nom N` | Bâtiment sans noms, puis chaque nom écrit à son tour |
| `etage-question N` | Point d'interrogation à droite de l'étage N |
| `question-etage N "…"` | Question écrite à droite de l'étage N (une seule à la fois ; le bâtiment se décale à gauche) |
| `bouclier` / `bouclier-repousser` | Fait justificatif : bouclier à droite du bâtiment, qui repousse une flèche |
| `fleche N` | Flèche qui monte jusqu'à l'étage N |
| `liste "…" …` / `liste-ajouter "…"` / `liste-surligner N` | Liste à gauche |
| `cases "…" …` / `case "…"` | Cases à cocher (toutes d'un coup, ou une par une) |
| `cocher N vert\|gris\|question` | Condition remplie, manquante, ou en question |
| `colonnes "A" "B"` / `colonne-accent N` / `colonne-eteindre N` | Deux notions opposées |
| `pyramide` / `pyramide-niveau N COULEUR` / `retirer-pyramide` | Les autorités |
| `decor escalier` / `decor appartement` / `decor-retirer` | Décor au trait : cage d'escalier (sol, sept marches, rampe, porte, fenêtre) ; appartement en déménagement (porte, fenêtre, cartons ; `placer` de -3 à 2 le long du sol) ; `decor rue` : façades, boulangerie, réverbère (`placer` de -4 à 4) |
| `neige` | Flocons qui tombent derrière la fenêtre du décor |
| `placer ID N` | Pose un personnage sur la marche N du décor (0 : pied de l'escalier ; -1 à -3 : dans le hall, -3 devant la porte), sans animation ; à jouer avec son apparition |
| `marcher ID N` / `pousser ID CIBLE` / `chute ID N` | Le personnage va à la marche N ; pousse la cible ; tombe jusqu'à la marche N |
| `picto NOM X Y` / `picto-retirer NOM` | Pictogramme : `parking`, `tension`, `lune`, `telephone`, `tag` |
| `etiquette ID "…" X Y` / `etiquette-retirer ID` | Mot-clé en ambre à la position (X, Y) |
| `repere-batiment` / `repere-etage N COULEUR` | Petit bâtiment permanent en haut à droite (il survit aux `scene-vide`) et couleur de ses étages |
| `frise` | Frise du temps |
| `repere X "…"` | Repère (date d'entrée en vigueur…) à la fraction X de la frise (0 à 1) |
| `point X "…"` | Événement sur la frise |
| `zone A B vert\|gris` | Période colorée |
| `fleche-retour DE VERS casse\|vert` | Flèche qui remonte le temps : brisée (non-rétroactivité) ou verte (loi plus favorable) |
| `questions` | Point d'interrogation sur chaque événement de la frise |

## Essais

- `VISUELS=<fichier>` : rendre un autre `visuals.md` sur la même narration (prototype).
- `FIN=<secondes>` : ne rendre que le début.

## Contrôles automatiques

À la fin du rendu, le moteur écrit `out/<slug>--alertes-visuels.txt` :

- plus de douze mots affichés à la fois (hors bloc d'article) ;
- animation en retard de plus d'une demi-seconde sur la voix.

Il évite aussi les plans fixes de plus de quatre secondes : le dernier élément animé « respire » légèrement.
