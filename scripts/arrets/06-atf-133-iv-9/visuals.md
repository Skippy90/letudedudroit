# Visuels — Arrêts, vidéo 6 : Il refuse de se laisser dépasser : meurtre ?

Ce fichier pilote les schémas Manim (`render/manim/video.py`). Vocabulaire des actions : `render/manim/README.md`.

Style « scène » : la vidéo commence dans la rue de la localité que X. traverse (décor rue), avec X. (silhouette turquoise) et F. (bleu clair). L'accident a lieu hors localité, sur une route droite, de nuit : le moteur n'a pas de décor « route de campagne » ; la route se joue donc sans décor, avec la lune et trois voitures au trait (X. sur la voie de droite, en bas ; F. sur la voie de gauche, au-dessus ; la voiture d'en face à droite). Le choc n'est pas montré : le pictogramme danger, puis l'écran se vide. Le juge (violet) apparaît dans la salle d'audience (décor tribunal). Une silhouette neutre (« L'auteur », rose) porte les bulles de la règle générale, pour ne pas prêter à X. un état d'esprit que l'arrêt ne retient pas. Bloc de l'arrêt à côté de l'article.

| Moment | Actions |
| --- | --- |
| 1.1 | picto lune 5.2 2.6 ; etiquette lieu "Argovie, 2003" -3.6 1.7 ; picto voiture -0.4 -1.7 |
| 1.1+2.5 | etiquette heure "19 h" 2.4 1.7 |
| 1.2 | picto-deplacer voiture 0.4 -1.7 |
| 2.1 | scene-vide ; decor rue ; picto voiture -2.0 -1.7 ; personnage x "X." turquoise centre-droite ; placer x 2 |
| 2.2 | picto voiture:2 -5.2 -1.7 ; personnage f "F." bleu_clair droite ; placer f 3 |
| 3.1 | accent f ; etiquette famille "Son épouse, quatre enfants" -3.6 1.7 |
| 4.1 | decor-retirer ; retirer x ; retirer f ; etiquette-retirer famille ; picto lune 5.2 2.6 ; etiquette limite "Limite : 80 km/h" -3.6 2.7 |
| 4.2 | etiquette route "Route droite" 2.0 2.7 ; picto-deplacer voiture -0.4 -0.9 ; picto-deplacer voiture:2 -3.6 -0.9 |
| 5.1 | etiquette-retirer route ; picto-deplacer voiture:2 -2.4 0.8 |
| 5.2 | picto voiture:3 5.6 0.8 ; etiquette limite "Des phares en face" -3.6 2.7 |
| 6.1 | picto-deplacer voiture 1.0 -0.9 |
| 6.2 | picto-deplacer voiture:2 1.0 0.8 |
| 6.3 | etiquette limite "Côte à côte" -3.6 2.7 |
| 7.1 | picto-deplacer voiture:3 4.6 0.8 ; etiquette limite "Se rabattre ?" -3.6 2.7 |
| 7.2 | etiquette limite "Plus de 100 km/h" -3.6 2.7 |
| 8.1 | picto danger 3.0 2.5 |
| 8.2 | scene-vide |
| 9.1 | etiquette morts "Deux morts" -2.6 0.6 ; picto lune 5.2 2.6 |
| 9.2 | etiquette blesses "Sept blessés" 2.4 0.6 |
| 9.3 | scene-vide ; personnage x "X." turquoise centre ; etiquette indemne "Indemne" 2.6 1.4 |
| 10.1 | scene-vide ; decor tribunal ; personnage x "X." turquoise gauche ; placer x -1 ; personnage juge "Le juge" violet droite ; placer juge 3 ; titre "Négligence" |
| 10.2 | effacer-titres ; titre "En appel : plus loin" |
| 11.1 | arret "ATF 133 IV 9" ; effacer-titres ; titre "Meurtre, par dol éventuel" |
| 11.2 | effacer-titres ; etiquette peine "Cinq ans et demi" 0.6 2.4 ; picto prison 0.6 1.1 |
| 12.1 | scene-vide ; colonnes "Meurtre" "Négligence" ; colonne-accent 1 ; article "Art. 111 CP" ; picto prison -3.5 -1.2 |
| 13.1 | colonne-accent 2 ; article "Art. 117 CP" ; picto pieces 3.5 -1.2 |
| 14.1 | scene-vide ; article-retirer ; personnage x "X." turquoise gauche ; bulle x "À tout prix" ; etiquette but "Empêcher le dépassement" 2.6 -0.4 |
| 14.2 | titre "Le but avant les conséquences" |
| 15.1 | scene-vide ; etiquette mai "Mai 2003" -3.6 1.7 ; picto voiture 0.4 -0.6 |
| 15.2 | picto voiture:2 4.4 -0.6 ; etiquette mai2 "Malgré une voiture en face" 2.4 1.7 |
| 16.1 | scene-vide ; personnage x "X." turquoise gauche ; titre "Recours au Tribunal fédéral" |
| 16.2 | scene-vide ; colonnes "Dol éventuel" "Négligence consciente" ; renvoi "vidéo 1" ; picto voiture -3.5 -1.2 ; picto voiture:2 3.5 -1.2 |
| 17.1 | scene-vide ; repere-liste "Négligence" "Dol éventuel" ; titre "Tribunal fédéral" ; personnage juge "Le juge" violet droite |
| 17.2 | sous-titre "Les deux connaissent le risque" |
| 17.3 | effacer-titres ; titre "La volonté" |
| 18.1 | repere-marquer 1 ambre ; personnage auteur "L'auteur" rose gauche ; bulle auteur "Rien n'arrivera" |
| 18.2 | repere-marquer 1 neutre ; repere-marquer 2 ambre ; bulle auteur "Tant pis" |
| 19.1 | effacer-bulle auteur ; article "Art. 12 CP" |
| 19.2 | effacer-titres ; titre "Déjà cité dans l'arrêt" |
| 20.1 | scene-vide ; repere-retirer ; article-retirer ; titre "Le juge déduit" ; personnage juge "Le juge" violet droite |
| 20.2 | liste "Risque connu" "Imprudence" "Mobiles" "Manière d'agir" |
| 21.1 | scene-vide ; picto voiture 0.6 -0.9 ; picto voiture:2 0.6 0.8 ; picto voiture:3 4.6 0.8 ; etiquette risque "Risque élevé" -3.6 2.7 |
| 21.2 | picto danger 2.8 2.5 |
| 22.1 | scene-vide ; personnage juge "Le juge" violet droite ; titre "Les indices cantonaux" |
| 22.2 | mot-barre "Mai 2003" -1.5 0.3 |
| 22.3 | sous-titre "X. n'est pas F." |
| 23.1 | scene-vide ; personnage f "F." bleu_clair centre-gauche ; etiquette famille "Sa famille à bord" 2.6 1.7 |
| 23.1+2.5 | etiquette renoncer "Il pouvait renoncer" 2.6 0.6 |
| 24.1 | scene-vide ; personnage x "X." turquoise gauche ; personnage f "F." bleu_clair droite ; titre "Qui cède le premier ?" ; etiquette bras "Bras de fer" 0 0.6 |
| 25.1 | effacer-titres ; etiquette-retirer bras ; titre "Plutôt l'inverse" ; bulle x "Il va freiner" |
| 25.2 | etiquette imprudence "Peut-être par imprudence" 0 -1.0 |
| 25.3 | accent x |
| 26.1 | effacer-titres ; effacer-bulle x ; etiquette-retirer imprudence ; etiquette danger "Lui aussi en danger" 0 -1.0 |
| 26.2 | titre "Pas à la légère" |
| 27.1 | scene-vide ; picto voiture 0.6 -0.9 ; picto voiture:2 0.6 0.8 ; picto voiture:3 5.0 0.8 ; etiquette voit "Il voit la voiture d'en face" -2.6 2.7 |
| 27.2 | etiquette voit "Personne derrière lui" -2.6 2.7 ; picto-deplacer voiture:2 -3.0 0.8 |
| 27.3 | etiquette voit "La maîtrise du dépassement" -2.6 2.7 |
| 28.1 | scene-vide ; titre "Renoncer : la réaction naturelle" ; picto voiture:2 -0.6 -0.6 |
| 28.2 | picto voiture:3 3.8 -0.6 ; picto danger 1.6 1.2 |
| 28.3 | sous-titre "Pas celle qu'il dépasse" |
| 29.1 | scene-vide ; colonnes "Vidéo 1" "Vidéo 6" ; colonne-accent 1 ; renvoi "vidéo 1" ; arret "ATF 130 IV 58" |
| 29.2 | picto voiture -3.5 -1.2 ; titre "Longue course, vitesse massive" |
| 30.1 | effacer-titres ; titre "Choix contre la vie" |
| 30.2 | sous-titre "D'où le dol" |
| 31.1 | colonne-accent 2 ; effacer-titres ; arret "ATF 133 IV 9" ; picto voiture:2 3.5 -1.2 ; titre "Ne pas se laisser dépasser" |
| 31.2 | sous-titre "F. voulait terminer" |
| 32.1 | effacer-titres ; titre "Choix contre la vie ?" ; barrer |
| 33.1 | scene-vide ; titre "Une règle pour la route" ; picto voiture 0 0.3 |
| 33.1+2.5 | sous-titre "Risque élevé : pas assez" |
| 34.1 | scene-vide ; personnage conducteur "Un conducteur" rose gauche ; bulle conducteur "Je maîtrise" ; picto voiture 3.4 -1.2 |
| 34.2 | titre "Risque mal mesuré" |
| 34.3 | effacer-titres ; titre "Pas de dol éventuel inconscient" |
| 35.1 | scene-vide ; titre "Avec retenue" ; personnage juge "Le juge" violet droite |
| 35.2 | sous-titre "Seulement les cas flagrants" |
| 36.1 | scene-vide ; case "Dol éventuel" ; titre "Pas le cas ici" ; picto voiture 4.4 -0.8 |
| 36.2 | cocher 1 gris ; sous-titre "Viole le droit fédéral" |
| 36.3 | effacer-titres ; titre "Recours admis" ; accent cases |
| 37.1 | scene-vide ; decor tribunal ; personnage x "X." turquoise gauche ; placer x -1 ; titre "Pas acquitté" |
| 37.2 | article "Art. 117 CP" ; personnage juge "Le juge" violet droite ; placer juge 3 ; sous-titre "Renvoi : négligence ?" |
| 38.1 | scene-vide ; article-retirer ; colonnes "Vidéo 1" "Vidéo 6" |
| 38.2 | titre "Seuls les faits changent" |
| 39.1 | effacer-titres ; colonne-accent 1 ; picto voiture -3.5 -1.2 |
| 39.2 | colonne-eteindre 2 ; picto voiture:2 3.5 -1.2 |
| 40.1 | scene-vide ; arret-retirer ; titre "Le piège classique" ; etiquette piege "Risque énorme, donc accepté ?" 0 0.6 ; picto danger 0 -1.2 |
| 41.1 | etiquette-retirer piege ; mot-barre "Risque énorme, donc accepté" 0 0.6 |
| 41.2 | effacer-titres ; titre "Tout le comportement" |
| 42.1 | scene-vide ; titre "Retenons" ; picto voiture 3.6 -0.8 |
| 42.2 | liste "Accepter le risque" |
| 42.3 | liste-ajouter "Au volant : cas flagrants" |
| 43.1 | scene-vide ; titre "Une question pour finir" ; personnage juge "Le juge" violet gauche |
| 43.2 | effacer-titres ; titre "Pourquoi pas ici ?" ambre ; picto voiture 3.0 -1.2 |
| 43.3 | accent juge |
| 44.1 | scene-vide ; livre "Code pénal" 0 -0.5 ; titre "L'étude du droit" ; sous-titre "Tout est dans la description" |
| 44.2 | accent titre |
