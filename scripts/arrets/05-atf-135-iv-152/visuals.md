# Visuels — Arrêts, vidéo 5 : Deux contre un : faut-il savoir qui a frappé ?

Ce fichier pilote les schémas Manim (`render/manim/video.py`). Vocabulaire des actions : `render/manim/README.md`.

Style « scène » : l'arrêt ne dit pas où l'agression a eu lieu ; les faits se jouent donc sans décor de lieu, avec trois silhouettes sans visage : X. (turquoise), le comparse (bleu clair), Y., la victime (ambre pâle). Le juge (violet) apparaît dans la salle d'audience (décor tribunal). Aucun coup n'est montré : la blessure est signalée par l'éclair du dommage, sans chute ni geste. Bloc de l'arrêt à côté de l'article.

| Moment | Actions |
| --- | --- |
| 1.1 | etiquette lieu "Fribourg, 2005" -3.6 1.7 |
| 1.1+2.5 | etiquette heure "6 h 40" 3.6 1.7 |
| 2.1 | etiquette-retirer lieu ; etiquette-retirer heure ; personnage x "X." turquoise centre-gauche ; personnage comparse "Le comparse" bleu_clair gauche |
| 2.2 | personnage y "Y." ambre_pale droite ; etiquette raison "Sans raison" 2.2 2.2 |
| 3.1 | etiquette-retirer raison ; accent x ; picto bouteille 0.4 0.3 |
| 4.1 | bulle x "J'étais seul" |
| 4.2 | etiquette temoins "Les témoins le contredisent" 3.0 2.6 ; accent comparse |
| 5.1 | effacer-bulle x ; etiquette-retirer temoins ; picto-retirer bouteille ; dommage y |
| 5.2 | etiquette hopital "Hospitalisé" 3.0 2.6 |
| 5.3 | etiquette hopital "Six à huit semaines" 3.0 2.6 |
| 6.1 | etiquette-retirer hopital ; titre "Qui a donné quel coup ?" ; etiquette doute "?" -3.35 0.4 |
| 7.1 | scene-vide ; decor tribunal ; personnage x "X." turquoise gauche ; placer x -1 ; personnage juge "Le juge" violet droite ; placer juge 3 ; arret "ATF 135 IV 152" |
| 7.2 | etiquette peine "22 mois, dont 6 à exécuter" 0.6 2.4 ; picto prison 0.6 1.1 |
| 8.1 | etiquette-retirer peine ; picto-retirer prison ; article "Art. 134 CP" ; titre "L'agression" |
| 8.2 | sous-titre "Quelqu'un est tué ou blessé" |
| 9.1 | effacer-titres ; titre "Cinq ans au plus" ; picto prison 0.6 1.1 |
| 9.2 | effacer-titres ; titre "Participer suffit" |
| 9.3 | sous-titre "Pas besoin de vouloir blesser" |
| 10.1 | effacer-titres ; article-retirer ; picto-retirer prison ; titre "Recours au Tribunal fédéral" ; accent x |
| 10.2 | parole x "Un seul blessé" |
| 10.3 | scene-vide ; colonnes "Agression" "Lésions simples" ; colonne-accent 2 ; picto prison -3.5 -1.2 |
| 11.1 | article "Art. 123 CP" ; picto prison:2 3.5 -1.2 |
| 12.1 | scene-vide ; article-retirer ; personnage x "X." turquoise centre-gauche ; personnage comparse "Le comparse" bleu_clair gauche ; titre "De quoi répond chacun ?" |
| 12.2 | sous-titre "Agression, lésions, ou les deux ?" ; accent x |
| 13.1 | scene-vide ; decor tribunal ; personnage juge "Le juge" violet droite ; placer juge 3 ; titre "Deux reproches" |
| 13.2 | sous-titre "La coactivité oubliée" ; accent juge |
| 14.1 | scene-vide ; renvoi "vidéo 10" ; personnage x "X." turquoise centre-droite ; personnage comparse "Le comparse" bleu_clair droite |
| 14.2 | titre "Coauteur" ; sous-titre "Intention, rôle déterminant" |
| 15.1 | effacer-titres ; liste "Décision" "Organisation" "Exécution" |
| 15.2 | titre "Contribution essentielle" ; accent x |
| 16.1 | scene-vide ; personnage x "X." turquoise gauche ; personnage comparse "Le comparse" bleu_clair droite ; bulle x "Ensemble" ; bulle comparse "Ensemble" |
| 16.2 | titre "Décision par les actes" |
| 17.1 | effacer-bulle x ; effacer-bulle comparse ; effacer-titres ; titre "Résultat : dol éventuel suffit" |
| 18.1 | scene-vide ; titre "Le cas" ; personnage x "X." turquoise centre-gauche ; personnage comparse "Le comparse" bleu_clair gauche ; personnage y "Y." ambre_pale droite |
| 18.2 | accent x ; accent comparse |
| 18.3 | etiquette sol "À terre" 4.5 2.2 |
| 18.4 | etiquette sol "Coups à la tête" 4.5 2.2 |
| 18.5 | dommage y ; etiquette sol "Perte de connaissance" 4.0 2.2 |
| 19.1 | etiquette-retirer sol ; effacer-titres ; titre "Contribution essentielle" |
| 19.2 | effacer-titres ; titre "Coauteurs" ambre |
| 20.1 | sous-titre "Qui a frappé ? Plus nécessaire" ; etiquette doute "?" -3.35 0.4 |
| 20.2 | etiquette-retirer doute ; effacer-titres ; titre "Une action commune" |
| 21.1 | scene-vide ; titre "Second reproche" ; personnage x "X." turquoise centre-gauche |
| 21.2 | bulle x "Aucun but" |
| 22.1 | effacer-titres ; titre "Le dol éventuel suffit" ; article "Art. 12 CP" ; renvoi "vidéo 4" |
| 22.2 | bulle x "Tant pis" ; sous-titre "Il s'en accommode" |
| 23.1 | scene-vide ; article-retirer ; titre "Des indices" ; personnage juge "Le juge" violet droite |
| 23.2 | liste "Risque connu" "Imprudence" "Mobiles" "Manière d'agir" |
| 24.1 | scene-vide ; titre "Ici" ; personnage x "X." turquoise centre-droite ; personnage comparse "Le comparse" bleu_clair droite ; liste "Ensemble" |
| 24.2 | liste-ajouter "Surtout la tête" |
| 24.3 | liste-ajouter "Victime à terre" |
| 25.1 | scene-vide ; personnage x "X." turquoise centre-gauche ; bulle x "Tant pis" ; titre "Il l'accepte" |
| 25.2 | effacer-bulle x ; article "Art. 123 CP" ; sous-titre "Au moins des lésions simples" |
| 26.1 | scene-vide ; article-retirer ; colonnes "Agression" "Lésions" ; picto prison -3.5 -1.2 ; picto prison:2 3.5 -1.2 |
| 26.2 | titre "Non : le second apport" ambre |
| 27.1 | effacer-titres ; colonne-accent 2 ; colonne-eteindre 1 ; picto-retirer prison |
| 27.2 | titre "Seules les lésions" |
| 28.1 | scene-vide ; titre "Sauf dans deux cas" ; picto danger 3.5 0.3 |
| 28.2 | liste "Un autre en danger" |
| 28.3 | liste-ajouter "Danger plus grave" ; liste-surligner 2 |
| 29.1 | scene-vide ; colonnes "Agression" "Lésions" ; colonne-accent 1 ; titre "Concours" ; picto prison -3.5 -1.2 |
| 29.2 | colonne-accent 2 ; picto prison:2 3.5 -1.2 |
| 30.1 | scene-vide ; personnage y "Y." ambre_pale droite ; picto danger 0 0.3 |
| 30.2 | titre "Lésions graves, voire la mort" |
| 31.1 | picto bouteille -2.6 0.3 |
| 31.2 | scene-vide ; titre "En théorie" ; personnage x "X." turquoise gauche ; cases "Agression" "Lésions corporelles" ; cocher 1 vert ; cocher 2 vert |
| 32.1 | cocher 2 gris ; effacer-titres ; titre "Pas de lésions en plus" |
| 32.2 | sous-titre "Reformatio in pejus" ; accent x |
| 33.1 | scene-vide ; article "Art. 134 CP" ; titre "Agression confirmée" ; personnage juge "Le juge" violet droite |
| 33.2 | effacer-titres ; titre "Recours partiellement admis" |
| 33.3 | sous-titre "Sursis pour toute la peine" ; accent juge |
| 33.4 | effacer-titres ; titre "Renvoi : délai d'épreuve" |
| 34.1 | scene-vide ; article-retirer ; titre "La course de voitures" ; picto voiture 0 0.3 ; renvoi "vidéo 1" |
| 35.1 | scene-vide ; titre "Des coups portés ensemble" ; personnage x "X." turquoise centre-gauche ; personnage comparse "Le comparse" bleu_clair gauche |
| 35.2 | etiquette demeler "Inutile de démêler" 2.6 0.4 |
| 36.1 | scene-vide ; colonnes "Agression" "Lésions" ; colonne-accent 2 ; picto prison:2 3.5 -1.2 |
| 36.2 | colonne-accent 1 ; picto prison -3.5 -1.2 ; titre "Autre personne, ou danger plus grave" |
| 37.1 | scene-vide ; arret-retirer ; titre "Le piège classique" ; personnage x "X." turquoise centre-gauche ; personnage comparse "Le comparse" bleu_clair gauche ; etiquette piege "Personne ne répond ?" 2.6 0.4 |
| 38.1 | etiquette-retirer piege ; mot-barre "Personne ne répond" |
| 38.2 | effacer-titres ; titre "Action commune" |
| 38.3 | accent x ; accent comparse |
| 39.1 | scene-vide ; titre "Retenons" ; personnage x "X." turquoise centre-droite ; personnage comparse "Le comparse" bleu_clair droite |
| 39.2 | liste "Rôle déterminant" |
| 39.3 | liste-ajouter "Décision par actes" |
| 40.1 | liste-ajouter "Indices" |
| 40.2 | liste-ajouter "Concours" |
| 41.1 | scene-vide ; titre "Une question pour finir" ; personnage juge "Le juge" violet gauche |
| 41.2 | effacer-titres ; titre "Pourquoi ignorer qui a frappé ?" ambre |
| 41.3 | accent juge |
| 42.1 | scene-vide ; livre "Code pénal" 0 -0.5 ; titre "L'étude du droit" ; sous-titre "Tout est dans la description" |
| 42.2 | accent titre |
