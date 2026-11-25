# Visuels — Arrêts, vidéo 8 : Un test, un mensonge : dol éventuel ou négligence ?

Ce fichier pilote les schémas Manim (`render/manim/video.py`). Vocabulaire des actions : `render/manim/README.md`.

Style « scène », abstrait et pudique : aucun décor de lieu pour les faits (l'arrêt ne situe pas la vie du couple), seulement des silhouettes sans visage : l'homme (turquoise), sa compagne (ambre pâle), une autre femme (rose). Le juge (violet) apparaît dans la salle d'audience (décor tribunal). Aucune image intime, aucun geste : la relation se dit par des étiquettes de dates, l'état d'esprit par des bulles de pensée, l'infection par l'éclair du dommage. Aucun mot ne réduit une personne à son état de santé. Bloc de l'arrêt à côté de l'article ; chaque article apparaît au moment où il est dit.

| Moment | Actions |
| --- | --- |
| 1.1 | personnage homme "L'homme" turquoise gauche ; personnage compagne "Sa compagne" ambre_pale droite |
| 1.2 | etiquette date "Fin 1991" 0 2.4 |
| 2.1 | etiquette-retirer date ; bulle compagne "Un test d'abord" |
| 2.2 | picto document -2.0 0.3 ; etiquette test "Test du VIH" 0 2.4 |
| 3.1 | effacer-bulle compagne ; etiquette test "Janvier 1992" 0 2.4 |
| 3.2 | picto coche 3.0 0.3 |
| 4.1 | etiquette-retirer test ; parole compagne "Et ton résultat ?" |
| 4.2 | effacer-parole compagne ; parole homme "Négatif aussi" |
| 4.3 | effacer-parole homme ; mot-barre "Négatif aussi" -3.0 2.4 |
| 5.1 | scene-vide ; personnage homme "L'homme" turquoise gauche ; personnage compagne "Sa compagne" ambre_pale droite ; etiquette faux "Aucun test en janvier" 3.0 2.4 |
| 5.2 | etiquette-retirer faux ; bulle homme "Je sais depuis 1990" |
| 6.1 | effacer-bulle homme ; bulle compagne "Je le crois" |
| 6.2 | effacer-bulle compagne ; etiquette periode "1992–1993" 0 2.4 |
| 7.1 | etiquette-retirer periode ; dommage compagne |
| 8.1 | scene-vide ; personnage homme "L'homme" turquoise centre-gauche ; personnage autre "Une autre femme" rose droite ; etiquette annee "1991" 0 2.4 |
| 8.2 | bulle homme "Ne rien dire" |
| 8.3 | effacer-bulle homme ; etiquette annee "Non infectée" 0 2.4 |
| 9.1 | scene-vide ; decor tribunal ; personnage homme "L'homme" turquoise gauche ; placer homme -1 ; personnage juge "Le juge" violet droite ; placer juge 3 ; arret "ATF 125 IV 242" ; etiquette peine "Trois ans" 0.6 2.4 ; picto prison 0.6 1.1 |
| 9.2 | etiquette peine "Lésions graves, maladie propagée" 0.6 2.4 |
| 10.1 | etiquette peine "Autre femme : tentative" 0.6 2.4 |
| 11.1 | etiquette-retirer peine ; picto-retirer prison ; titre "Recours" ; accent homme |
| 11.2 | parole homme "Transmis, oui" |
| 11.3 | effacer-parole homme ; parole homme "Pas d'intention" |
| 12.1 | scene-vide ; colonnes "Dol éventuel" "Négligence consciente" ; colonne-accent 2 |
| 12.2 | picto prison -3.5 -1.2 ; picto pieces 3.5 -1.2 |
| 13.1 | renvoi "vidéo 4" ; colonne-accent 1 |
| 13.2 | titre "Les deux connaissent le risque" |
| 13.3 | effacer-titres ; titre "Ce qui change : la volonté" ambre |
| 14.1 | scene-vide ; personnage juge "Le juge" violet droite ; titre "D'abord, le résultat" |
| 14.2 | effacer-titres ; titre "Une lésion grave" ; accent juge |
| 15.1 | etiquette epoque "Selon l'arrêt, en 1999" -2.6 0.4 |
| 15.2 | picto danger -2.6 -1.0 |
| 16.1 | effacer-titres ; titre "Vie mise en danger" |
| 16.2 | article "Art. 122 CP" ; sous-titre "Aujourd'hui : lettre a" |
| 17.1 | etiquette-retirer epoque ; picto-retirer danger ; effacer-titres ; article "Art. 231 CP" ; titre "Maladie dangereuse, transmissible" |
| 17.2 | effacer-titres ; titre "Les deux ensemble" ; accent juge |
| 18.1 | scene-vide ; article-retirer ; titre "L'intention" ; personnage homme "L'homme" turquoise gauche |
| 18.2 | effacer-titres ; titre "Savoir ne suffit pas" |
| 19.1 | effacer-titres ; titre "Accepter le résultat" ; accent homme |
| 19.2 | personnage juge "Le juge" violet droite ; sous-titre "Savoir et circonstances" |
| 20.1 | scene-vide ; titre "Trois circonstances" ; personnage juge "Le juge" violet droite |
| 20.2 | liste "Chaque fois un risque" |
| 21.1 | liste-ajouter "Risque incalculable" |
| 21.2 | liste-ajouter "Aucune défense" ; liste-surligner 3 |
| 22.1 | scene-vide ; personnage homme "L'homme" turquoise centre-gauche ; bulle homme "Rien n'arrivera" ; titre "Il ne peut pas y compter" |
| 22.2 | effacer-titres ; titre "Il accepte l'infection" ambre |
| 23.1 | effacer-titres ; bulle homme "Pourvu que rien n'arrive" |
| 23.2 | titre "Espoir : pas souhaité" |
| 23.3 | effacer-titres ; titre "Le dol éventuel demeure" ; accent homme |
| 24.1 | scene-vide ; personnage homme "L'homme" turquoise gauche ; etiquette risque "Risque faible" 2.4 0.4 ; picto danger 2.4 -1.0 |
| 24.2 | titre "L'arrêt le dit" |
| 24.3 | effacer-titres ; etiquette risque "Chaque fois possible" 2.4 0.4 ; titre "Pas décisif" |
| 25.1 | scene-vide ; personnage homme "L'homme" turquoise centre-gauche ; bulle homme "Je sais" ; titre "Pas à chaque fois ?" |
| 25.2 | effacer-titres ; titre "Savoir en arrière-plan" |
| 26.1 | effacer-titres ; effacer-bulle homme ; etiquette devoir "Devoir d'informer" 2.8 0.4 ; picto document 2.8 -1.0 ; accent homme |
| 27.1 | scene-vide ; arret "ATF 125 IV 242" ; personnage juge "Le juge" violet gauche ; cases "Art. 122 CP" "Art. 231 CP" ; cocher 1 vert ; cocher 2 vert |
| 27.2 | titre "Recours rejeté" ; accent juge |
| 28.1 | scene-vide ; frise ; point 0.15 "1999" ; titre "Le droit de 1999" ambre |
| 28.2 | article "Art. 231 CP" ; effacer-titres ; titre "Intention ou négligence" |
| 29.1 | effacer-titres ; point 0.9 "Aujourd'hui" ; titre "Texte actuel différent" |
| 29.2 | effacer-titres ; titre "Par bassesse de caractère" ; zone 0.6 1 gris |
| 30.1 | repere 0.6 "2016" ; sous-titre "Loi sur les épidémies" |
| 31.1 | scene-vide ; article-retirer ; titre "La médecine a progressé" ; picto document 0 0.3 |
| 31.2 | effacer-titres ; titre "Le droit de l'époque" |
| 32.1 | scene-vide ; personnage homme "L'homme" turquoise gauche ; titre "Ce qui reste" |
| 32.2 | article "Art. 12 CP" ; sous-titre "Dol éventuel ou négligence consciente" |
| 33.1 | scene-vide ; article-retirer ; titre "Pas besoin de nombreux actes" ; personnage homme "L'homme" turquoise gauche |
| 33.2 | etiquette premier "Le premier suffit" 2.4 0.4 ; picto danger 2.4 -1.0 |
| 34.1 | scene-vide ; titre "La course de voitures" ; picto voiture 0 0.3 ; renvoi "vidéo 1" |
| 34.2 | effacer-titres ; titre "Espérer n'écarte pas le dol" ambre |
| 35.1 | scene-vide ; arret-retirer ; titre "Le piège classique" ; personnage homme "L'homme" turquoise gauche ; bulle homme "Pas voulu" |
| 36.1 | effacer-bulle homme ; mot-barre "Pas voulu, pas d'intention" 1.8 0.3 |
| 36.2 | effacer-titres ; titre "Ne pas souhaiter ne suffit pas" |
| 36.3 | effacer-titres ; titre "Espoir n'est pas confiance" ambre ; accent homme |
| 37.1 | scene-vide ; titre "Retenons" ; personnage juge "Le juge" violet droite |
| 37.2 | liste "Lésion grave (1999)" |
| 38.1 | liste-ajouter "Savoir et circonstances" |
| 38.2 | liste-ajouter "Espoir n'est pas confiance" ; liste-surligner 3 |
| 39.1 | scene-vide ; titre "Une question pour finir" ; personnage juge "Le juge" violet gauche |
| 39.2 | effacer-titres ; titre "Un risque faible suffit-il ?" ambre |
| 39.3 | accent juge |
| 40.1 | scene-vide ; livre "Code pénal" 0 -0.5 ; titre "L'étude du droit" ; sous-titre "Tout est dans la description" |
| 40.2 | accent titre |
