# Visuels — Arrêts, vidéo 1 : Une course de voitures, deux morts : meurtre ?

Ce fichier pilote les schémas Manim (`render/manim/video.py`). Vocabulaire des actions : `render/manim/README.md`.

Style « scène » : la course se joue dans une rue de village (décor rue, enseigne « Poste »), deux voitures au trait ; les deux conducteurs sont des silhouettes sans visage (turquoise pour le premier, bleu clair pour le second). Pense-bête en haut à droite : « Négligence » / « Dol éventuel ». L'accident n'est pas montré : un éclair ambre, puis l'écran se vide. Bloc de l'arrêt à côté de l'article.

| Moment | Actions |
| --- | --- |
| 1.1 | decor rue Poste ; etiquette lieu "Lucerne, 1999" -3.6 1.7 |
| 1.2 | etiquette lieu "Vendredi, 22 h 30" -3.6 1.7 |
| 2.1 | etiquette-retirer lieu ; picto voiture -5.2 -1.7 ; picto voiture:2 -2.0 -1.7 |
| 2.2 | personnage premier "Le 1er" turquoise centre-droite ; placer premier 2 ; personnage second "Le 2e" bleu_clair droite ; placer second 3 |
| 2.3 | etiquette passagers "Des passagers" 3.2 1.7 |
| 3.1 | etiquette-retirer passagers ; etiquette provoc "Provocation" -2.0 1.7 |
| 3.2 | picto-deplacer voiture:2 -1.0 -1.7 |
| 3.3 | picto-deplacer voiture -4.0 -1.7 |
| 4.1 | etiquette provoc "Une course improvisée" -2.0 1.7 |
| 4.2 | picto-deplacer voiture -1.0 -1.7 0.3 ; picto-deplacer voiture:2 -4.0 -1.7 |
| 5.1 | etiquette provoc "Dépassement" -2.0 1.7 |
| 5.2 | etiquette vitesse "120–140 km/h" 4.2 1.7 |
| 6.1 | etiquette limite "Limite : 50 km/h" 4.2 1.0 |
| 7.1 | scene-vide ; picto voiture 0 0.3 |
| 7.2 | picto-deplacer voiture 0.6 0.3 |
| 7.3 | picto danger 2.8 0.3 |
| 7.4 | scene-vide |
| 8.1 | titre "Meurtre ?" ; arret "ATF 130 IV 58" |
| 8.2 | personnage premier "Le 1er" turquoise gauche ; personnage second "Le 2e" bleu_clair droite |
| 9.1 | effacer-titres ; titre "Un accident ?" |
| 9.2 | sous-titre "Au plus : négligence" |
| 10.1 | scene-vide ; colonnes "Meurtre" "Négligence" |
| 10.2 | colonne-accent 1 ; article "Art. 111 CP" ; picto prison -3.5 -1.2 |
| 11.1 | colonne-accent 2 ; article "Art. 117 CP" ; picto pieces 3.5 -1.2 |
| 12.1 | scene-vide ; article-retirer ; personnage premier "Le 1er" turquoise gauche |
| 12.2 | bulle premier "Accepter le risque ?" |
| 12.3 | personnage second "Le 2e" bleu_clair droite ; accent second |
| 13.1 | scene-vide ; repere-liste "Négligence" "Dol éventuel" ; titre "Tribunal fédéral" ; arret "ATF 130 IV 58" ; personnage juge "Le juge" violet droite |
| 13.2 | sous-titre "Les deux connaissent le risque" |
| 14.1 | scene-vide ; titre "La volonté" |
| 14.2 | repere-marquer 1 ambre ; personnage premier "Le 1er" turquoise gauche ; bulle premier "Rien n'arrivera" |
| 15.1 | repere-marquer 1 neutre ; repere-marquer 2 ambre ; bulle premier "Tant pis" |
| 15.2 | effacer-titres ; titre "Pas besoin de souhaiter" |
| 16.1 | effacer-titres ; effacer-bulle premier ; article "Art. 12 CP" |
| 17.1 | scene-vide ; repere-retirer ; article-retirer ; titre "Lire dans une tête ?" ; personnage juge "Le juge" violet droite |
| 17.2 | effacer-titres ; titre "Le juge déduit" |
| 18.1 | liste-ajouter "Risque connu" ; liste-ajouter "Imprudence grave" |
| 19.1 | effacer-titres ; titre "Savoir ne suffit pas" |
| 19.2 | accent juge |
| 20.1 | scene-vide ; arret-retirer ; decor rue Poste ; picto voiture -0.4 -1.7 ; picto voiture:2 -3.4 -1.7 ; titre "Ce cas précis" |
| 20.2 | etiquette vitesse "120–140 km/h" 4.2 1.7 |
| 21.1 | etiquette limite "+ 90 km/h" 4.2 1.0 |
| 21.2 | effacer-titres ; titre "Plus de confiance possible" |
| 22.1 | scene-vide ; personnage premier "Le 1er" turquoise gauche ; bulle premier "Pourvu que ça passe" |
| 22.2 | titre "Laissé au hasard" |
| 23.1 | scene-vide ; titre "La phrase clé" ambre ; arret "ATF 130 IV 58" ; picto voiture 4.6 -1.3 |
| 23.2 | mot-barre "Un simple espoir" |
| 23.3 | sous-titre "Seule la confiance exclut le dol" |
| 24.1 | scene-vide ; arret-retirer ; personnage premier "Le 1er" turquoise gauche ; etiquette but "Ne pas perdre la face" 0.6 1.7 |
| 24.2 | accent premier |
| 25.1 | etiquette-retirer but ; titre "Dol éventuel confirmé" |
| 26.1 | personnage second "Le 2e" bleu_clair droite ; accent second |
| 26.2 | sous-titre "Pas heurté les victimes" |
| 26.3 | effacer-titres ; titre "Vitesse maintenue" |
| 26.4 | effacer-titres ; titre "Dépassement empêché" |
| 27.1 | effacer-titres ; titre "Levé le pied : trop tard" |
| 27.2 | effacer-titres ; titre "Participation déterminante" ; sous-titre "Un duel sur la route" |
| 27.3 | effacer-titres ; titre "Coauteur" ; renvoi "vidéo 10" |
| 28.1 | scene-vide ; titre "Pas tout excès de vitesse" ; picto voiture 0 0.3 |
| 29.1 | effacer-titres ; titre "Le Tribunal fédéral le dit" |
| 29.2 | sous-titre "Le conducteur risque sa vie" |
| 29.3 | sous-titre "En principe : négligence" |
| 30.1 | effacer-titres ; titre "Pas à la légère" ; arret "ATF 130 IV 58" |
| 31.1 | scene-vide ; arret-retirer ; liste-ajouter "La course" ; liste-ajouter "Le dépassement" ; liste-ajouter "La vitesse au village" ; picto voiture 4.0 0.3 |
| 32.1 | scene-vide ; titre "Le piège classique" ; personnage premier "Le 1er" turquoise gauche ; bulle premier "Pas voulu tuer" |
| 33.1 | effacer-titres ; effacer-bulle premier ; mot-barre "Pas voulu, donc pas meurtre" |
| 33.2 | sous-titre "Accepter, c'est déjà l'intention" |
| 34.1 | scene-vide ; colonnes "Négligence" "Dol éventuel" ; picto voiture 0 -1.6 |
| 34.2 | colonne-accent 1 ; titre "Compte que rien n'arrive" |
| 35.1 | colonne-accent 2 ; effacer-titres ; titre "S'en accommode" |
| 35.2 | sous-titre "Espérer ne suffit pas" |
| 36.1 | scene-vide ; titre "Une question pour finir" ; personnage juge "Le juge" violet gauche |
| 36.2 | effacer-titres ; titre "Savoir le danger suffit-il ?" ambre |
| 36.3 | accent juge |
| 37.1 | scene-vide ; livre "Code pénal" 0 -0.5 ; titre "L'étude du droit" ; sous-titre "Tout est dans la description" |
| 37.2 | accent titre |
