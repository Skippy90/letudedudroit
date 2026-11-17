# Visuels — Arrêts, vidéo 12 : En 1990, des Suissesses ne pouvaient toujours pas voter dans leur canton

Ce fichier pilote les schémas Manim (`render/manim/video.py`). Vocabulaire des actions : `render/manim/README.md`.

Style « scène ». Le décor « place de vote » (Landsgemeinde) prévu par le plan n'existe pas encore dans le moteur : la Landsgemeinde est rendue par la carte de la Suisse (canton AI mis en avant), une foule de citoyens et le pictogramme `main_levee`. Aucune arme n'est dessinée (ligne 2 : le mot-clé suffit). Silhouettes : Theresa Rohner (turquoise), Ursula Baumann (ambre pâle, pour les cinquante-trois recourantes), Mario Sonderegger (bleu clair, pour les quarante-neuf recourants), le juge (violet, décor tribunal). Droit ancien et droit cantonal sont dits par des mots-clés à l'écran. Bloc de l'arrêt à côté de l'article.

| Moment | Actions |
| --- | --- |
| 1.1 | carte cantons ; carte-canton AI ; etiquette date "29 avril 1990" -4.2 2.8 |
| 1.2 | etiquette lg "Landsgemeinde" 3.6 2.8 ; picto main_levee 4.6 1.2 |
| 1.3 | etiquette lg "Elle fait la loi" 3.6 2.8 |
| 2.1 | scene-vide ; foule hommes -1.5 -0.6 18 9 ; titre "Les hommes seulement" |
| 2.2 | sous-titre "Une arme blanche pour preuve" |
| 3.1 | scene-vide ; picto bulletin 0 0.2 1.4 ; titre "Ouvrir le vote aux femmes ?" |
| 3.2 | effacer-titres ; titre "Refusé" ambre ; sous-titre "Environ 6 contre 4" |
| 4.1 | scene-vide ; frise ; point 0.3 "1971 : vote fédéral" ; picto urne 3.6 1.4 |
| 4.2 | scene-vide ; carte cantons ; carte-cantons-tous ; etiquette seul "Tous les cantons, sauf un" 0 2.8 |
| 5.1 | scene-vide ; personnage rohner "Theresa Rohner" turquoise centre-gauche ; etiquette an "Avril 1989" -3.6 2.6 |
| 5.2 | etiquette refus "Demande refusée" 2.8 2.6 ; pose rohner debout triste |
| 6.1 | etiquette-retirer an ; etiquette-retirer refus ; picto document 2.6 0.2 1.2 ; titre "Recours au Tribunal fédéral" |
| 6.2 | sous-titre "Dossier suspendu" |
| 7.1 | scene-vide ; foule femmes -2.6 -0.4 12 6 ; etiquette nb "53 femmes" 3 2.4 |
| 7.2 | personnage baumann "Ursula Baumann" ambre_pale droite |
| 8.1 | scene-vide ; foule hommes -2.6 -0.4 12 6 ; etiquette nb "49 hommes" 3 2.4 ; personnage sonderegger "Mario Sonderegger" bleu_clair droite |
| 8.2 | picto urne -4.6 2.2 ; etiquette nb "Ils votent déjà" 3 2.4 |
| 8.3 | accent sonderegger |
| 9.1 | scene-vide ; article "Art. 16 Cst. AI" ; livre "Constitution cantonale" 0 -0.3 |
| 9.2 | titre "Droit cantonal" ambre ; sous-titre "Appenzell Rhodes-Intérieures" |
| 10.1 | scene-vide ; colonnes "Landleute" "Suisses" ; titre "Qui vote ?" ; picto main_levee 3.5 -1.2 |
| 10.2 | sous-titre "Lecture du canton : les hommes" |
| 11.1 | scene-vide ; article-retirer ; livre "Constitution fédérale" 0 -0.3 |
| 11.2 | titre "Celle de 1874" ambre |
| 11.3 | sous-titre "Droit ancien : remplacée depuis" |
| 12.1 | scene-vide ; article "Art. 4 al. 2 Cst. 1874" ; picto balance 0 0.2 1.5 ; titre "Égaux en droits" ; sous-titre "Depuis 1981" |
| 13.1 | scene-vide ; article "Art. 74 al. 4 Cst. 1874" ; frise ; point 0.3 "1971" |
| 13.2 | picto urne 3.6 1.6 ; titre "Vote fédéral des femmes" |
| 13.3 | effacer-titres ; titre "Le droit cantonal reste réservé" ambre |
| 14.1 | scene-vide ; colonnes "Art. 4 : égalité" "Art. 74 : réserve" ; colonne-accent 2 ; picto balance -3.5 -1.2 |
| 14.2 | titre "Conseil fédéral, 1980 : même lecture" |
| 15.1 | scene-vide ; article-retirer ; titre "La question" ; picto balance -2.6 0 1.3 ; picto urne 2.6 0 1.3 |
| 15.2 | effacer-titres ; titre "Une réserve contre l'égalité ?" ambre |
| 16.1 | scene-vide ; decor tribunal ; personnage juge "Le juge" violet droite ; placer juge 3 ; arret "ATF 116 Ia 359" ; etiquette date "27 novembre 1990" -3.4 2.6 |
| 17.1 | scene-vide ; personnage rohner "Theresa Rohner" turquoise centre-gauche ; titre "D'abord, une surprise" |
| 17.2 | effacer-titres ; titre "Irrecevable" ; pose rohner debout surpris |
| 17.3 | sous-titre "La Landsgemeinde de 1989 a eu lieu" |
| 17.4 | accent rohner |
| 18.1 | scene-vide ; personnage baumann "Ursula Baumann" ambre_pale centre-gauche ; etiquette nb "53 femmes" 3.4 1.5 |
| 18.2 | titre "Droits politiques refusés à tort ?" |
| 18.3 | picto coche 3.4 -0.3 1.3 ; effacer-titres ; titre "Recevable" |
| 19.1 | scene-vide ; personnage sonderegger "Mario Sonderegger" bleu_clair centre-gauche ; etiquette nb "49 hommes" 3.4 1.5 |
| 19.2 | picto coche 3.4 -0.3 1.3 ; titre "Recevable aussi" |
| 19.3 | effacer-titres ; titre "Un corps électoral bien composé" ambre |
| 19.4 | accent sonderegger |
| 20.1 | scene-vide ; article "Art. 16 Cst. AI" ; picto parlement 0 0.3 1.4 ; titre "Autre obstacle" |
| 20.2 | effacer-titres ; titre "Approuvé en 1979" |
| 20.3 | sous-titre "On dit : « garanti »" |
| 21.1 | scene-vide ; frise ; point 0.3 "1979 : garantie" ; point 0.7 "1981 : égalité" |
| 21.2 | titre "Le contrôle reste possible" ambre |
| 22.1 | scene-vide ; article "Art. 74 Cst. 1874" ; titre "Le fond" |
| 22.2 | picto urne 0 0.2 1.4 ; effacer-titres ; titre "Vote fédéral des femmes" |
| 22.3 | effacer-titres ; titre "Un simple rappel de compétence" ambre |
| 23.1 | mot-barre "Exception" 3.4 0.2 |
| 23.2 | effacer-titres ; titre "Il aurait fallu l'écrire" |
| 24.1 | scene-vide ; article-retirer ; picto balance 0 0.1 1.6 ; titre "Une part essentielle de l'égalité" ambre |
| 25.1 | scene-vide ; titre "L'avis du Conseil fédéral ?" ; picto urne 0 0.2 1.4 |
| 25.2 | sous-titre "Il ne lie pas peuple et cantons" |
| 25.3 | effacer-titres ; titre "Tous les domaines du droit" ambre ; sous-titre "Votation du 14 juin 1981" |
| 26.1 | scene-vide ; titre "Les cantons décident" ; carte cantons petite |
| 26.2 | cases "Âge du vote" |
| 26.3 | case "Vote des étrangers" ; cocher 1 vert ; cocher 2 vert |
| 26.4 | case "Exclure les femmes" ; cocher 3 gris |
| 27.1 | scene-vide ; titre "Un délai pour s'adapter ?" ; frise ; point 0.2 "1981" ; point 0.8 "1990" |
| 27.2 | sous-titre "Question laissée ouverte" |
| 27.3 | zone 0.2 0.8 gris |
| 27.4 | effacer-titres ; titre "Près de neuf ans : assez" ambre |
| 28.1 | scene-vide ; titre "Quel remède ?" ; personnage juge "Le juge" violet droite |
| 28.2 | mot-barre "Annuler le vote" -2.6 0.8 |
| 28.3 | mot-barre "Réécrire l'article" -2.6 -0.6 |
| 29.1 | scene-vide ; article "Art. 16 Cst. AI" ; livre "Constitution cantonale" 0 -0.3 ; livre-ouvrir ; titre "Il relit le texte" |
| 29.2 | scene-vide ; colonnes "Landleute" "Suisses" ; colonne-accent 2 ; titre "Les Suissesses aussi" ; picto main_levee 3.5 -1.2 |
| 29.3 | colonne-accent 1 ; effacer-titres ; titre "Femmes et hommes" ambre |
| 30.1 | sous-titre "Le texte reste le même" |
| 30.2 | sous-titre "Son sens change" |
| 30.3 | scene-vide ; titre "Interprétation conforme" ambre ; sous-titre "… à la Constitution" ; livre "Constitution fédérale" 0 -0.6 |
| 31.1 | scene-vide ; article-retirer ; titre "Les femmes ont les droits politiques" ; personnage baumann "Ursula Baumann" ambre_pale droite |
| 31.2 | liste "Landsgemeinde" "Districts" "Communes" |
| 32.1 | scene-vide ; titre "Dès quand ?" ; frise ; point 0.4 "27 novembre 1990" |
| 32.2 | zone 0.4 1 vert ; sous-titre "Pour l'avenir seulement" |
| 32.3 | zone 0 0.4 gris ; sous-titre "Le passé reste valable" |
| 33.1 | scene-vide ; arret-retirer ; foule citoyens -1.5 -1.8 18 9 ; livre "Constitution fédérale" 0 0.5 |
| 33.2 | etiquette viol "Même le peuple doit la respecter" 0 2.9 |
| 34.1 | scene-vide ; titre "Un même texte" ; livre "Constitution cantonale" 0 -0.3 |
| 34.2 | sous-titre "Un sens qui évolue" ; accent livre |
| 35.1 | scene-vide ; titre "Et aujourd'hui ?" ambre |
| 35.2 | livre "Constitution fédérale" 0 -0.3 ; sous-titre "Constitution de 1999" |
| 35.3 | article "Art. 8 al. 3 Cst." ; picto balance 3.6 0 1.2 |
| 36.1 | scene-vide ; carte cantons petite ; titre "Aujourd'hui" |
| 36.2 | article "Art. 39 Cst." ; sous-titre "Les cantons règlent leurs votes" |
| 36.3 | sous-titre "Mais dans le respect du droit fédéral" |
| 36.4 | article "Art. 51 Cst." |
| 37.1 | scene-vide ; article-retirer ; titre "Le piège classique" ; personnage sonderegger "Mario Sonderegger" bleu_clair gauche ; bulle sonderegger "Vote annulé ?" |
| 37.2 | bulle sonderegger "Texte réécrit ?" |
| 38.1 | effacer-bulle sonderegger ; effacer-titres ; titre "Faux" |
| 38.2 | mot-barre "Annulé" 2.4 0.8 ; mot-barre "Réécrit" 2.4 -0.6 |
| 38.3 | effacer-titres ; titre "Le même texte, bien lu" ambre |
| 39.1 | scene-vide ; titre "Retenons" ; arret "ATF 116 Ia 359" ; personnage juge "Le juge" violet droite |
| 39.2 | liste "La réserve ne suffit plus" |
| 39.3 | liste-ajouter "Égalité : aussi pour voter" ; liste-surligner 2 |
| 40.1 | scene-vide ; arret-retirer ; titre "Une question pour finir" ; personnage sonderegger "Mario Sonderegger" bleu_clair gauche |
| 40.2 | effacer-titres ; titre "Pourquoi les hommes ont-ils pu recourir ?" ambre |
| 40.3 | accent sonderegger |
| 41.1 | scene-vide ; livre "Constitution fédérale" 0 -0.5 ; titre "L'étude du droit" ; sous-titre "Tout est dans la description" |
| 41.2 | accent titre |
