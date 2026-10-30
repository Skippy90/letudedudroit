# Visuels — Vidéo 1 : Qu'est-ce qu'une infraction ? Les trois étages

Ce fichier pilote les schémas Manim (`render/manim/video.py`). Le vocabulaire des actions est décrit dans `render/manim/README.md` ; il ne contient que des éléments de la charte (`docs/charte-visuelle.md`), plus du texte et des cases à cocher, déjà utilisés par le script de référence.

Colonne « Moment » : `ligne.phrase` du script, éventuellement `+secondes` après le début de la phrase. Plusieurs actions d'un même moment sont séparées par `;`.

Personnages : Marc turquoise, Julien rose.

Écarts assumés avec la colonne « À l'écran » du script, pour rester dans la charte :

- lignes 21 et 22 : la balance « dans la tête de Marc » n'est pas un élément de la charte ; l'état d'esprit passe par la bulle de pensée, qui en est un ;
- ligne 26 : les trois questions s'affichent une à une à côté de leur étage, et non toutes ensemble, pour ne jamais dépasser douze mots à l'écran.

| Moment | Actions |
| --- | --- |
| 1.1 | titre "Un soir d'hiver, à Lausanne" |
| 1.2 | personnage marc "Marc" turquoise gauche ; personnage julien "Julien" rose droite |
| 1.3 | bulle marc "La place de parc" |
| 2.1 | effacer-titres ; effacer-bulle marc ; accent julien |
| 2.2 | deplacer marc centre-gauche |
| 2.3 | basculer julien ; dommage julien |
| 2.4 | sous-titre "Fracture simple" |
| 3.1 | titre "Infraction ?" |
| 3.2 | sous-titre "Votre réponse instinctive ?" |
| 3.3 | accent titre |
| 4.1 | scene-vide ; titre "Une infraction" |
| 4.2 | batiment vide |
| 5.1 | etage-nom 1 |
| 5.2 | etage-nom 2 |
| 5.3 | etage-nom 3 |
| 5.4 | accent batiment |
| 6.1 | effacer-titres ; fleche 1 |
| 6.2 | etage 1 vert |
| 6.3 | etage 2 gris ; titre "Pas d'infraction, pas de peine" |
| 7.1 | scene-vide ; titre "Premier étage : la typicité" |
| 7.2 | sous-titre "La loi décrit-elle l'acte ?" |
| 8.1 | effacer-titres ; livre |
| 8.2 | article "Art. 1 CP" |
| 9.1 | livre-ouvrir |
| 9.2 | article "Art. 123 CP" |
| 9.2+3 | titre "Lésions corporelles simples" |
| 10.1 | scene-vide ; personnage julien "Julien" rose droite ; dommage julien |
| 10.2 | cases "Atteinte au corps" ; cocher 1 vert |
| 10.3 | titre "Les éléments objectifs" |
| 11.1 | scene-vide ; personnage marc "Marc" turquoise gauche ; titre "Le côté intérieur" |
| 11.2 | article "Art. 12 CP" ; bulle marc "Intention ?" |
| 12.1 | accent marc |
| 12.2 | bulle marc "Une poussée" |
| 12.3 | bulle marc "Une chute" |
| 12.4 | titre "Dol éventuel" ambre |
| 12.5 | renvoi "vidéo 4" |
| 13.1 | scene-vide ; article-retirer ; batiment ; fleche 1 ; etage 1 vert |
| 14.1 | scene-vide ; titre "Deuxième étage : l'illicéité" |
| 14.2 | sous-titre "Était-ce malgré tout permis ?" |
| 15.1 | effacer-titres ; batiment ; etage 1 vert |
| 15.2 | bouclier |
| 15.3 | titre "Les faits justificatifs" |
| 16.1 | article "Art. 15 CP" ; sous-titre "La légitime défense" |
| 16.2 | bouclier-repousser |
| 17.1 | scene-vide ; rembobiner |
| 17.2 | personnage marc "Marc" turquoise gauche ; personnage julien "Julien" rose droite ; deplacer julien centre-droite ; accent julien |
| 18.1 | dommage julien |
| 18.2 | scene-vide ; batiment ; etage 1 vert |
| 18.3 | bouclier |
| 18.4 | etage 2 gris |
| 18.5 | titre "Infraction" ; barrer |
| 19.1 | scene-vide ; article-retirer ; rembobiner ; personnage julien "Julien" rose droite |
| 19.2 | titre "Une remarque, pas une attaque" |
| 19.3 | sous-titre "Pas de légitime défense" |
| 19.4 | scene-vide ; batiment ; etage 1 vert ; fleche 2 ; etage 2 vert |
| 20.1 | scene-vide ; titre "Troisième étage : la culpabilité" |
| 20.2 | personnage marc "Marc" turquoise gauche |
| 20.3 | sous-titre "Peut-on le lui reprocher ?" |
| 21.1 | effacer-titres ; article "Art. 19 CP" ; bulle marc "Comprendre ? Se maîtriser ?" |
| 21.1+4 | accent marc |
| 22.1 | rembobiner ; bulle marc "Plus aucune prise" |
| 22.2 | scene-vide ; batiment ; etage 1 vert ; etage 2 vert |
| 22.3 | etage 3 gris |
| 23.1 | titre "Le piège classique" |
| 23.2 | sous-titre "Une mesure reste possible" |
| 23.3 | renvoi "vidéo 12" |
| 24.1 | scene-vide ; article-retirer ; personnage marc "Marc" turquoise gauche ; bulle marc "En colère" |
| 24.2 | batiment ; etage 1 vert ; etage 2 vert |
| 24.3 | etage 3 vert |
| 25.1 | retirer marc ; accent batiment |
| 25.2 | article "Art. 123 CP" |
| 25.3 | titre "Peine" ambre |
| 26.1 | scene-vide ; article-retirer ; batiment ; titre "La méthode" |
| 26.2 | sous-titre "Trois questions, dans l'ordre" |
| 26.3 | effacer-titres ; question-etage 1 "La loi décrit-elle l'acte ?" |
| 26.4 | question-etage 2 "Était-ce malgré tout permis ?" |
| 26.5 | question-etage 3 "Peut-on le reprocher ?" |
| 26.6 | accent batiment |
| 27.1 | scene-vide ; titre "Une question pour finir" |
| 27.2 | effacer-titres ; personnage marc "Marc" turquoise gauche ; personnage julien "Julien" rose droite |
| 27.2+3 | deplacer marc centre-gauche ; basculer julien |
| 27.2+6 | scene-vide ; batiment |
| 27.3 | etage-question 1 ; etage-question 2 ; etage-question 3 ; titre "Quel étage pose problème ?" |
| 27.4 | renvoi "vidéo 4" |
| 28.1 | scene-vide ; titre "L'étude du droit" ; sous-titre "Script et articles sur GitHub" |
| 28.2 | accent titre |
