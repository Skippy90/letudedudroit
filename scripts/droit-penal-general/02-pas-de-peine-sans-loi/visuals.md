# Visuels — Vidéo 2 : Pas de peine sans loi

Ce fichier pilote les schémas Manim (`render/manim/video.py`). Le vocabulaire des actions est décrit dans `render/manim/README.md` ; il ne contient que des éléments de la charte (`docs/charte-visuelle.md`), plus du texte, des listes et des cases à cocher, déjà utilisés par le script de référence.

Colonne « Moment » : `ligne.phrase` du script, éventuellement `+secondes` après le début de la phrase. Le moteur cale chaque moment sur la narration (`voice/.../timings.json`). Plusieurs actions d'un même moment sont séparées par `;`.

Personnages : Sami bleu clair, Tom ambre pâle, la sœur de Sami rose, Nora violet.

Écarts assumés avec la colonne « À l'écran » du script, pour rester dans la charte : pas de cartons ni de ligne d'eau (ligne 1 à 3), pas de loupe (ligne 13), les cantons sont des cases et non des silhouettes (lignes 35 et 36).

| Moment | Actions |
| --- | --- |
| 1.1 | decor appartement ; etiquette lieu "Fribourg, samedi matin" -2.6 2.45 |
| 1.2 | personnage sami "Sami" bleu_clair gauche ; placer sami -3 |
| 1.2@déménage | marcher sami 1 |
| 1.3@tom | etiquette-retirer lieu ; etiquette promesse "Tom a promis de venir" 0.2 1.4 |
| 1.3@cartons | accent sami |
| 2.1 | etiquette-retirer promesse ; personnage tom "Tom" ambre_pale droite ; placer tom -1 |
| 2.1@message | parole tom "Désolé, je suis malade." |
| 2.2@lac | effacer-parole tom ; bulle tom "Une journée au lac" |
| 3.1 | retirer tom ; personnage soeur "Sa sœur" rose centre ; placer soeur -1 |
| 3.2@vérité | etiquette verite "Tom était au lac" -0.8 1.4 |
| 3.3@furieux | etiquette-retirer verite ; picto tension 0.8 1.6 |
| 4.1 | picto-retirer tension ; retirer soeur ; parole sami "Tu m'as menti. Je porte plainte !" |
| 5.1 | scene-vide ; titre "Infraction ?" ambre |
| 5.2 | sous-titre "Mentir à un ami, est-ce puni ?" |
| 5.3 | accent titre |
| 6.1 | scene-vide ; batiment ; renvoi "vidéo 1" |
| 6.2 | etage 1 ambre ; titre "La loi décrit-elle l'acte ?" ; repere-batiment ; repere-etage 1 ambre |
| 7.1 | scene-vide ; titre "La règle du premier étage" |
| 7.2 | livre ; article "Art. 1 CP" |
| 7.3 | accent livre |
| 8.1 | livre-ouvrir |
| 8.2 | titre "expressément réprimé par la loi" mot-a-mot |
| 9.1 | livre-retirer ; titre "Pas de loi, pas de peine" |
| 9.2 | sous-titre "Le principe de la légalité" |
| 10.1 | effacer-titres ; colonnes "Peine" "Mesure" |
| 10.2 | colonne-accent 2 ; renvoi "vidéo 12" |
| 11.1 | scene-vide ; titre "Trois exigences" |
| 11.2 | liste-ajouter "1. Un texte" |
| 11.3 | liste-ajouter "2. Qui décrit l'acte" |
| 11.4 | liste-ajouter "3. Qui existait déjà" |
| 12.1 | effacer-titres ; liste-surligner 1 |
| 12.2 | mot-barre "Avis du juge" |
| 12.3 | mot-barre "Morale" |
| 12.4 | accent liste |
| 13.1 | scene-vide ; livre ; titre "Un article contre le mensonge ?" |
| 13.2 | livre-ouvrir ; sous-titre "Aucune infraction « mentir »" |
| 14.1 | scene-vide ; personnage tom "Tom" ambre_pale centre |
| 14.2 | colonnes "Morale" "Loi pénale" |
| 14.3 | colonne-accent 1 ; colonne-eteindre 2 |
| 15.1 | scene-vide ; batiment |
| 15.2 | fleche 1 ; etage 1 gris ; repere-etage 1 gris |
| 15.3 | titre "Pas d'infraction" |
| 16.1 | scene-vide ; liste "1. Un texte" "2. Qui décrit l'acte" "3. Qui existait déjà" ; liste-surligner 2 |
| 16.2 | titre "« expressément »" ambre |
| 17.1 | scene-vide ; titre "Le mensonge en général ?" |
| 17.2 | cases "Devant un tribunal" "Pour obtenir de l'argent" |
| 17.3 | accent cases |
| 18.1 | scene-vide ; rembobiner |
| 18.2 | personnage tom "Tom" ambre_pale gauche ; pyramide ; pyramide-niveau 1 ambre |
| 19.1 | article "Art. 307 CP" |
| 19.2 | retirer-pyramide ; cases "Témoin" "Déposition fausse" |
| 19.2+1.5 | cocher 1 vert |
| 19.2+3 | cocher 2 vert |
| 20.1 | scene-vide ; rembobiner |
| 20.2 | personnage sami "Sami" bleu_clair gauche ; personnage tom "Tom" ambre_pale droite ; jetons sami tom |
| 21.1 | article "Art. 146 CP" ; titre "Escroquerie" |
| 21.2 | sous-titre "Mentir ne suffit pas" |
| 22.1 | scene-vide ; case "Tromperie astucieuse" |
| 22.2 | case "Préjudice financier" |
| 22.3 | case "Volonté de s'enrichir" |
| 23.1 | cocher 1 gris |
| 23.2 | cocher 2 gris ; cocher 3 gris |
| 23.3 | titre "Aucune description ne correspond" |
| 24.1 | scene-vide ; personnage tom "Tom" ambre_pale droite ; article-etirer |
| 24.2 | article-reprendre |
| 24.3 | titre "Ressembler ne suffit pas" |
| 25.1 | scene-vide ; cases "Élément 1" "Élément 2" "Élément 3" ; cocher 1 vert ; cocher 2 vert ; cocher 3 gris |
| 25.2 | titre "Proche ?" |
| 25.3 | sous-titre "Choquant ? Pas suffisant" |
| 26.1 | scene-vide ; article-retirer ; liste "1. Un texte" "2. Qui décrit l'acte" "3. Qui existait déjà" ; liste-surligner 3 |
| 27.1 | scene-vide ; frise ; titre "Fiction" |
| 27.2 | repere 0.65 "Nouvelle loi" |
| 28.1 | point 0.25 "Mensonge de Tom" |
| 28.2 | fleche-retour 0.65 0.25 casse |
| 28.3 | titre "Non" |
| 29.1 | article "Art. 2 CP" |
| 29.2 | zone 0.65 1 vert |
| 30.1 | zone 0 0.65 gris |
| 30.2 | titre "Savoir à l'avance" |
| 31.1 | titre "Une exception" |
| 31.2 | sous-titre "Une loi plus douce" |
| 31.3 | fleche-retour 0.65 0.25 vert |
| 32.1 | scene-vide ; article-retirer ; titre "Le piège classique" |
| 32.2 | sous-titre "« Pas dans le Code pénal, donc permis »" |
| 32.3 | barrer |
| 33.1 | scene-vide ; livres "Code pénal" "Circulation routière" "Autres lois" |
| 33.2 | article "Art. 333 CP" |
| 33.2+3.5 | accent livres |
| 34.1 | livres-surligner 2 |
| 34.2 | article "Art. 90 LCR" |
| 35.1 | scene-vide ; cases "Genève" "Vaud" |
| 35.2 | article "Art. 335 CP" |
| 36.1 | titre "Règles cantonales" |
| 36.2 | cocher 1 vert ; cocher 2 question |
| 37.1 | scene-vide ; article-retirer ; titre "Il faut un texte" |
| 37.2 | livres "Code pénal" "Circulation routière" "Autres lois" |
| 38.1 | scene-vide ; personnage sami "Sami" bleu_clair gauche |
| 38.2 | personnage tom "Tom" ambre_pale droite |
| 38.3 | titre "Porter plainte ?" |
| 38.4 | barrer |
| 39.1 | scene-vide ; colonnes "Morale" "Loi pénale" |
| 39.2 | colonne-accent 1 ; colonne-eteindre 2 |
| 40.1 | scene-vide ; article "Art. 1 CP" ; titre "Trois exigences" |
| 40.2 | liste-ajouter "1. Un texte" |
| 40.3 | liste-ajouter "2. Qui décrit l'acte" |
| 40.4 | liste-ajouter "3. Qui existait déjà" |
| 41.1 | scene-vide ; article-retirer ; titre "Une question pour finir" |
| 41.2 | effacer-titres ; personnage nora "Nora" violet centre ; frise ; point 0.15 "1er mars" |
| 42.1 | repere 0.5 "1er juin : nouvelle loi" |
| 42.2 | point 0.8 "1er juillet" |
| 43.1 | questions |
| 43.2 | accent frise |
| 43.3 | titre "Réponse en commentaire" |
| 44.1 | scene-vide ; titre "L'étude du droit" ; sous-titre "Script et articles sur GitHub" |
| 44.2 | accent titre |
