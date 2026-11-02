# Visuels — Vidéo 12 : Quand la justice ne poursuit plus

Ce fichier pilote les schémas Manim (`render/manim/video.py`). Vocabulaire des actions : `render/manim/README.md`.

Colonne « Moment » : `ligne.phrase` du script, éventuellement `+secondes`. Plusieurs actions d'un même moment sont séparées par `;`.

Personnages : Théo turquoise (vidéo 8), l'agent de sécurité bleu clair (vidéo 8), Noah turquoise (vidéo 3) — Théo et Noah ne sont jamais à l'écran ensemble —, l'auteur (exemple des mesures) ambre pâle, l'expert bleu clair, Lina violet.

Style « scène » (repris le 1er novembre 2026) : Théo revient devant l'entrée du festival (décor rue, enseigne « Festival »), Noah devant la boulangerie et son tag (décor rue) ; un pense-bête « Mesure / Prescription » en haut à droite s'allume sur l'outil dont on parle ; les délais se dessinent sur la frise.

Écarts assumés avec la colonne « À l'écran » du script, pour rester dans la charte : pas de barrière dessinée devant le bâtiment (ligne 31) ; le bâtiment reste, sans étage coloré (la prescription ne dit rien des trois étages), et l'étiquette « Plus de poursuite » s'affiche. L'établissement, l'expertise et le délai n'ont pas de pictogramme : ils sont nommés par une étiquette (l'expertise par le pictogramme `document`).

| Moment | Actions |
| --- | --- |
| 1.1 | titre "Deux histoires pour finir" ; livre "Code pénal" 0 -0.5 |
| 1.2 | scene-vide ; decor rue Festival ; etiquette lieu "Près de Nyon" -3.6 1.7 |
| 1.3 | personnage theo "Théo" turquoise gauche ; placer theo -2 ; personnage agent "L'agent" bleu_clair droite ; placer agent 1 ; renvoi "vidéo 8" |
| 1.3+2.5 | pousser theo agent |
| 1.3+4 | chute agent 2 ; dommage agent |
| 2.1 | etiquette-retirer lieu ; bulle theo "Un démon" |
| 2.1+1.5 | etiquette irr "Pas punissable" 3.6 1.7 |
| 2.2 | effacer-bulle theo ; titre "Le laisser repartir ?" ; marcher theo -4 |
| 3.1 | scene-vide ; decor rue ; personnage noah "Noah" turquoise gauche ; placer noah -2 ; renvoi "vidéo 3" |
| 3.2 | picto tag -0.3 -0.1 ; etiquette grand "Un grand tag" 0.6 1.7 |
| 3.3 | marcher noah -4 ; etiquette-retirer grand ; etiquette onze "Onze ans plus tard" 3.6 1.7 |
| 4.1 | titre "Encore poursuivable ?" ; accent noah |
| 4.2 | scene-vide ; repere-liste "Mesure" "Prescription" ; colonnes "La mesure" "La prescription" |
| 4.2+1.8 | colonne-accent 1 ; repere-marquer 1 ambre ; picto danger -3.5 -1.3 |
| 4.2+3.4 | colonne-accent 2 ; repere-marquer 2 ambre ; picto tag 3.5 -1.3 |
| 5.1 | scene-vide ; repere-marquer 2 neutre ; renvoi "vidéo 8" ; personnage theo "Théo" turquoise gauche |
| 5.2 | picto prison -1.0 0.2 ; etiquette peine "Peine : faute" -1.0 1.5 |
| 5.3 | picto danger 3.4 0.2 ; etiquette mesure "Mesure : danger" 3.4 1.5 |
| 5.3+2.4 | etiquette mesure "Danger ou soins" 3.4 1.5 |
| 6.1 | scene-vide ; article "Art. 56 CP" ; titre "Trois conditions" ; personnage theo "Théo" turquoise gauche |
| 6.2 | effacer-titres ; case "Peine seule insuffisante" |
| 7.1 | case "Traitement ou sécurité" |
| 7.2 | case "Mesure précise remplie" |
| 8.1 | scene-vide ; titre "Proportionnée" ; personnage theo "Théo" turquoise gauche |
| 8.2 | picto prison -0.6 0.2 ; etiquette atteinte "L'atteinte" -0.6 1.5 |
| 8.3 | picto danger 3.4 0.2 ; etiquette risque "Le risque" 3.4 1.5 |
| 8.3+2.5 | etiquette egal "Même poids" 1.4 -1.1 |
| 9.1 | scene-vide ; titre "Une expertise" ; personnage theo "Théo" turquoise gauche ; personnage expert "L'expert" bleu_clair droite ; picto document 0 0.2 |
| 9.2 | effacer-titres ; picto-retirer document ; retirer expert ; etiquette levee "Conditions tombées : levée" -0.6 1.5 ; deplacer theo droite |
| 10.1 | scene-vide ; article-retirer ; repere-marquer 1 ambre ; titre "Plusieurs mesures" ; livre "Code pénal" 0 -0.5 |
| 10.2 | livre-ouvrir ; sous-titre "Les trois principales" |
| 11.1 | scene-vide ; article "Art. 59 CP" ; liste-ajouter "1. Traitement institutionnel" ; personnage auteur "L'auteur" ambre_pale droite |
| 11.2 | etiquette trouble "Grave trouble mental" 4.2 -1.9 |
| 12.1 | scene-vide ; personnage auteur "L'auteur" ambre_pale gauche ; case "Lien avec le trouble" |
| 12.1+3 | case "Effet attendu" |
| 12.2 | etiquette lieu "Établissement adapté" 3.0 -1.0 |
| 13.1 | scene-vide ; frise ; point 0.05 "Début" ; repere 0.45 "5 ans" |
| 13.2 | repere 0.85 "+ 5 ans" |
| 13.2+2.5 | etiquette risque "Si le risque demeure" 1.4 1.5 |
| 14.1 | scene-vide ; article "Art. 63 CP" ; liste "1. Traitement institutionnel" "2. Traitement ambulatoire" ; liste-surligner 2 ; personnage auteur "L'auteur" ambre_pale droite |
| 14.2 | etiquette trouble "Trouble, addiction" 4.2 -1.9 |
| 14.3 | etiquette-retirer trouble ; mot-barre "Enfermé" 4.2 -1.9 |
| 15.1 | scene-vide ; article "Art. 64 CP" ; liste "1. Traitement institutionnel" "2. Traitement ambulatoire" "3. Internement" ; liste-surligner 3 ; picto prison 3.8 0.2 |
| 15.2 | etiquette lourde "La plus lourde" 3.8 1.5 |
| 15.3 | etiquette lourde "Meurtre, viol, brigandage" 3.9 -1.2 |
| 16.1 | scene-vide ; personnage auteur "L'auteur" ambre_pale gauche haut ; picto danger 3.4 0.6 ; etiquette serieux "Risque sérieux" 1.0 1.7 |
| 16.2 | article "Art. 64 CP" ; etiquette serieux "Des conditions précises" 1.0 1.7 |
| 16.3 | retirer auteur ; frise ; point 0.25 "Peine" ; zone 0 0.5 gris |
| 16.4 | point 0.75 "Internement" ; zone 0.5 1 ambre |
| 17.1 | scene-vide ; article-retirer ; personnage theo "Théo" turquoise gauche ; personnage expert "L'expert" bleu_clair droite ; titre "Traitement institutionnel ?" |
| 17.2 | sous-titre "Une crise ne suffit pas" |
| 17.3 | picto document 0 0.2 |
| 17.3+2 | effacer-titres ; picto-retirer document ; retirer expert ; case "Grave trouble lié à l'acte" |
| 17.3+3.5 | case "Risque de récidive" |
| 17.3+5 | case "Soins utiles" |
| 18.1 | scene-vide ; repere-marquer 1 neutre ; repere-marquer 2 ambre ; decor rue ; personnage noah "Noah" turquoise gauche ; placer noah -2 ; picto tag -0.3 -0.1 |
| 18.2 | etiquette presc "La prescription" -3.2 1.7 |
| 18.2+2.5 | etiquette delai "Un délai écoulé" 3.6 1.7 |
| 19.1 | scene-vide ; titre "Pourquoi ?" ; personnage noah "Noah" turquoise gauche |
| 19.2 | effacer-titres ; etiquette preuves "Preuves perdues" 1.4 1.6 |
| 19.2+1.8 | etiquette souvenirs "Souvenirs effacés" 1.4 0.3 |
| 19.2+3.6 | etiquette punir "Moins besoin de punir" 1.4 -1.0 |
| 20.1 | scene-vide ; article "Art. 97 CP" ; frise |
| 20.1+2.5 | titre "Selon la peine maximale" |
| 20.2 | repere 0.95 "30 ans" ; picto prison 4.9 0.5 |
| 21.1 | picto-retirer prison ; repere 0.5 "15 ans" |
| 21.2 | repere 0.33 "10" |
| 21.3 | repere 0.23 "7" |
| 22.1 | repere 0.1 "3 ans" ; renvoi "vidéo 3" |
| 23.1 | effacer-titres ; titre "Dès l'acte" ; point 0.02 "Le tag" |
| 23.2 | article "Art. 98 CP" |
| 24.1 | scene-vide ; decor rue ; personnage noah "Noah" turquoise gauche ; placer noah -2 ; picto tag -0.3 -0.1 ; etiquette max "Environ 2000 francs" 3.6 1.7 |
| 24.2 | etiquette max "Pas de moindre importance" 3.6 1.7 |
| 24.3 | article "Art. 144 CP" ; etiquette max "Trois ans au plus" 3.6 1.7 |
| 24.4 | etiquette max "Délai : dix ans" 3.6 1.7 |
| 24.5 | scene-vide ; frise ; point 0.05 "Le tag" ; repere 0.6 "10 ans" ; zone 0.6 1 gris ; point 0.7 "Découverte" |
| 24.5+1.5 | titre "Prescrit" ambre |
| 24.6 | sous-titre "Plus de poursuite" ; accent frise |
| 25.1 | scene-vide ; article "Art. 97 CP" ; decor tribunal ; personnage juge "Le juge" bleu_clair droite ; placer juge 3 ; etiquette regle "Règle importante" -3.6 1.7 |
| 25.2 | etiquette regle "Jugement de première instance" -2.4 1.7 |
| 25.2+2.5 | etiquette stop "Le délai s'arrête" 3.6 1.7 |
| 25.3 | etiquette-retirer regle ; etiquette appel "Appel : rien ne change" -2.4 1.7 |
| 25.4 | scene-vide ; article-retirer ; personnage victime "La victime" rose gauche ; titre "Autre délai : la plainte" ; picto document 0 0.2 |
| 25.5 | retirer victime ; frise ; point 0.1 "Connaît l'auteur" ; repere 0.4 "3 mois" |
| 25.6 | article "Art. 31 CP" |
| 26.1 | scene-vide ; personnage noah "Noah" turquoise gauche ; titre "Jamais prescrits" ambre |
| 26.2 | retirer noah ; article "Art. 101 CP" ; livre "Code pénal" 0 -0.3 |
| 27.1 | effacer-titres ; livre-retirer ; picto danger 3.6 0.2 ; liste-ajouter "Génocide" ; liste-ajouter "Crimes contre l'humanité" ; liste-ajouter "Crimes de guerre" |
| 27.2 | liste-ajouter "Crimes sexuels : enfants" |
| 28.1 | scene-vide ; frise ; point 0.05 "L'acte" ; zone 0.05 1 vert ; titre "Jamais effacé" ambre |
| 29.1 | scene-vide ; article "Art. 99 CP" ; titre "Prescription de la peine" ; picto prison 0 0.2 |
| 29.2 | effacer-titres ; picto-retirer prison ; frise ; point 0.05 "Jugement" ; titre "Exécuter dans un délai" |
| 29.3 | repere 0.45 "5 ans" ; picto pieces 0 0.4 |
| 30.1 | scene-vide ; article-retirer ; repere-marquer 2 neutre ; titre "Le piège classique" ; personnage noah "Noah" turquoise gauche |
| 30.2 | sous-titre "« Prescrit, donc innocent »" |
| 30.3 | barrer |
| 31.1 | scene-vide ; repere-marquer 2 ambre ; batiment |
| 31.2 | titre "Pas rendu licite" |
| 31.3 | effacer-titres ; titre "Plus de poursuite" ambre |
| 32.1 | scene-vide ; repere-marquer 2 neutre ; repere-marquer 1 ambre ; personnage theo "Théo" turquoise gauche ; mot-barre "Peine déguisée" |
| 32.2 | etiquette levee "Conditions tombées : levée" 3.4 -0.9 |
| 32.2+2.5 | deplacer theo centre |
| 33.1 | scene-vide ; titre "Retenons" ; personnage theo "Théo" turquoise gauche |
| 33.2 | article "Art. 56 CP" ; picto danger 3.4 0.2 ; etiquette soins "Danger ou soins" 3.4 1.5 |
| 33.3 | effacer-titres ; picto-retirer danger ; etiquette soins "Proportionnée, puis levée" 2.0 1.5 |
| 34.1 | scene-vide ; repere-marquer 1 neutre ; repere-marquer 2 ambre ; article "Art. 97 CP" ; frise ; repere 0.1 "3 ans" ; repere 0.23 "7" ; repere 0.33 "10" ; repere 0.5 "15" ; repere 0.95 "30 ans" |
| 34.2 | titre "Plus grave, plus long" ; picto prison 4.9 0.5 |
| 34.3 | effacer-titres ; titre "Certains crimes : jamais" ; zone 0.95 1 vert |
| 35.1 | scene-vide ; repere-marquer 2 neutre ; article-retirer ; titre "Une question pour finir" |
| 35.2 | effacer-titres ; decor rue ; personnage lina "Lina" violet gauche ; placer lina -2 ; picto velo 1.0 -1.85 ; etiquette valeur "Vélo à 1000 francs" 3.6 1.7 |
| 35.2+1 | marcher lina -4 ; picto-deplacer velo -4.6 -1.85 |
| 35.3 | etiquette valeur "Découvert douze ans après" 2.4 1.7 |
| 35.4 | repere-marquer 2 ambre ; titre "Encore poursuivable ?" ambre |
| 35.5 | accent lina |
| 36.1 | scene-vide ; repere-marquer 2 neutre ; batiment ; etage 1 vert |
| 36.1+1.6 | etage 2 vert |
| 36.1+2.9 | etage 3 vert |
| 36.2 | titre "Du premier étage à la peine" ; picto prison 4.6 0.2 |
| 36.3 | effacer-titres ; titre "Merci" ambre ; accent batiment |
| 37.1 | scene-vide ; repere-retirer ; livre "Code pénal" 0 -0.5 ; titre "L'étude du droit" ; sous-titre "Tout est dans la description" |
| 37.2 | accent titre |
