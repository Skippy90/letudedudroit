# Visuels — Vidéo 1 : Qu'est-ce qu'une infraction ? Les trois étages

Ce fichier pilote les schémas Manim (`render/manim/video.py`). Vocabulaire des actions : `render/manim/README.md`.

Colonne « Moment » : `ligne.phrase` du script, `ligne.phrase+secondes`, ou `ligne.phrase@mot` (au moment où ce mot est prononcé dans la narration enregistrée). Plusieurs actions d'un même moment sont séparées par `;`.

Style « scène » (adopté le 30 octobre 2026) : les cas se jouent dans un décor (cage d'escalier), les personnages s'y déplacent, les mots-clés apparaissent sur le mot prononcé, un petit bâtiment en haut à droite suit le raisonnement, et des sous-titres sont incrustés au montage.

Personnages : Marc turquoise, Julien rose.

Écarts assumés avec la colonne « À l'écran » du script, pour rester dans la charte :

- lignes 21 et 22 : la balance « dans la tête de Marc » n'est pas un élément de la charte ; l'état d'esprit passe par la bulle de pensée, qui en est un ;
- ligne 26 : les trois questions s'affichent une à une à côté de leur étage, et non toutes ensemble, pour ne jamais dépasser douze mots à l'écran ;
- ligne 17 : le poing levé de Julien est dit par une étiquette, les silhouettes n'ayant pas de bras.

| Moment | Actions |
| --- | --- |
| 1.1 | decor escalier ; neige ; personnage marc "Marc" turquoise gauche ; placer marc -3 |
| 1.1@lausanne | etiquette lieu "Lausanne, un soir d'hiver" -2.6 2.45 |
| 1.2@escalier | marcher marc 0 |
| 1.2@julien | personnage julien "Julien" rose droite ; placer julien 6 |
| 1.3 | marcher marc 5 ; marcher julien 1 |
| 1.3@détestent | picto tension 2.5 2.3 ; etiquette-retirer lieu |
| 1.3@parc | picto parking -0.2 2.3 |
| 2.1 | picto-retirer tension ; picto-retirer parking ; parole julien "Encore toi !" |
| 2.2 | effacer-parole julien |
| 2.2@pousse | pousser marc julien |
| 2.3@tombe | chute julien -1 |
| 2.3@poignet | dommage julien |
| 2.4 | etiquette blessure "Fracture simple" -2.2 -0.3 |
| 3.1 | etiquette-retirer blessure |
| 3.1@infraction | titre "Infraction ?" ambre |
| 3.2 | sous-titre "Votre réponse instinctive ?" |
| 3.3 | accent titre |
| 4.1 | scene-vide ; titre "Une infraction" |
| 4.1@chose | sous-titre "Pas une seule chose" |
| 4.2 | effacer-titres ; batiment vide |
| 4.2@étages | titre "Trois étages" |
| 5.1@typicité | etage-nom 1 |
| 5.2@illicéité | etage-nom 2 |
| 5.3@culpabilité | etage-nom 3 |
| 5.4 | effacer-titres ; titre "Retenez ces trois mots" ; repere-batiment |
| 6.1 | effacer-titres ; titre "L'ordre compte" |
| 6.2@bas | fleche 1 ; etage 1 vert |
| 6.3@manque | etage 2 gris |
| 6.3@infraction | effacer-titres ; titre "Pas d'infraction, pas de peine" |
| 7.1 | scene-vide ; batiment ; etage 1 ambre ; titre "Premier étage : la typicité" ; repere-etage 1 ambre |
| 7.2 | sous-titre "La loi décrit-elle l'acte ?" |
| 8.1 | scene-vide ; livre |
| 8.1@réprime | titre "Seulement si la loi le prévoit" |
| 8.2 | article "Art. 1 CP" |
| 9.1 | effacer-titres ; livre-ouvrir |
| 9.2 | article "Art. 123 CP" |
| 9.2@corps | titre "Une atteinte au corps ou à la santé" |
| 9.2@lésions | effacer-titres ; titre "Lésions corporelles simples" |
| 10.1 | scene-vide ; article-retirer ; decor escalier ; personnage julien "Julien" rose droite ; placer julien -1 ; dommage julien |
| 10.2 | etiquette atteinte "Atteinte au corps" 2.4 1.6 ; picto coche 5.3 1.6 |
| 10.3 | titre "Les éléments objectifs" |
| 11.1 | scene-vide ; personnage marc "Marc" turquoise gauche ; titre "Le côté intérieur" |
| 11.2 | article "Art. 12 CP" ; bulle marc "Intention ?" |
| 11.2@intentionnellement | effacer-titres ; titre "Intentionnellement" ambre |
| 12.1 | effacer-titres ; titre "A-t-il voulu blesser ?" ; accent marc |
| 12.2 | bulle marc "Une poussée" |
| 12.3@chute | bulle marc "Une chute" |
| 12.3@risque | effacer-titres ; titre "Il accepte le risque" |
| 12.4 | effacer-titres ; titre "Dol éventuel" ambre |
| 12.5 | renvoi "vidéo 4" |
| 13.1 | scene-vide ; article-retirer ; batiment ; fleche 1 ; etage 1 vert ; repere-etage 1 vert |
| 13.1@typique | titre "Typique" ambre |
| 14.1 | scene-vide ; batiment ; etage 1 vert ; etage 2 ambre ; titre "Deuxième étage : l'illicéité" ; repere-etage 2 ambre |
| 14.2 | sous-titre "Était-ce malgré tout permis ?" |
| 15.1 | effacer-titres |
| 15.2 | bouclier |
| 15.3 | titre "Les faits justificatifs" |
| 16.1 | article "Art. 15 CP" ; sous-titre "La légitime défense" |
| 16.2@attaque | bouclier-repousser |
| 16.2@proportionnée | effacer-titres ; titre "De manière proportionnée" |
| 17.1 | scene-vide ; article-retirer ; rembobiner ; titre "Une seule chose change" |
| 17.2 | effacer-titres ; decor escalier ; personnage marc "Marc" turquoise gauche ; placer marc 5 ; personnage julien "Julien" rose droite ; placer julien 1 |
| 17.2@poing | etiquette geste "Julien lève le poing" 1.0 1.6 ; accent julien |
| 17.2@repoussé | etiquette-retirer geste ; pousser marc julien |
| 18.1 | chute julien -1 |
| 18.1+1 | dommage julien |
| 18.2 | scene-vide ; batiment ; etage 1 vert |
| 18.3 | bouclier |
| 18.4 | etage 2 gris |
| 18.5 | titre "Infraction" ; barrer |
| 19.1 | scene-vide ; article-retirer ; rembobiner ; decor escalier ; personnage julien "Julien" rose droite ; placer julien 1 ; parole julien "Encore toi !" |
| 19.2 | effacer-parole julien ; titre "Une remarque, pas une attaque" |
| 19.3 | sous-titre "Pas de légitime défense" |
| 19.4 | scene-vide ; batiment ; etage 1 vert ; fleche 2 ; etage 2 vert ; repere-etage 2 vert |
| 19.4@illicite | titre "Illicite" ambre |
| 20.1 | scene-vide ; titre "Troisième étage : la culpabilité" ; repere-etage 3 ambre |
| 20.2 | personnage marc "Marc" turquoise gauche |
| 20.2@personne | accent marc |
| 20.3 | sous-titre "Peut-on le lui reprocher ?" |
| 21.1 | effacer-titres ; article "Art. 19 CP" ; bulle marc "Comprendre ? Se maîtriser ?" |
| 21.1@apprécier | titre "Comprendre ce qu'il fait ?" |
| 21.1@déterminer | effacer-titres ; titre "Se maîtriser ?" |
| 21.1@punissable | effacer-titres ; titre "Sinon : pas punissable" ambre |
| 22.1 | scene-vide ; rembobiner ; personnage marc "Marc" turquoise gauche |
| 22.1@maladie | etiquette etat "Maladie psychique grave" 3.0 0.4 |
| 22.1@gestes | bulle marc "Plus aucune prise" |
| 22.2 | scene-vide ; batiment ; etage 1 vert ; etage 2 vert |
| 22.3 | etage 3 gris |
| 23.1 | titre "Le piège classique" |
| 23.1@rien | sous-titre "Pas coupable, mais pas « rien »" |
| 23.2 | effacer-titres ; titre "Une mesure reste possible" |
| 23.3 | renvoi "vidéo 12" |
| 24.1 | scene-vide ; article-retirer ; personnage marc "Marc" turquoise gauche ; bulle marc "En colère" |
| 24.2 | batiment 2.5 ; etage 1 vert ; etage 2 vert |
| 24.3 | etage 3 vert ; repere-etage 3 vert |
| 25.1 | retirer marc ; accent batiment |
| 25.2@lésions | titre "Lésions corporelles simples" ; article "Art. 123 CP" |
| 25.3 | effacer-titres ; titre "Peine" ambre |
| 26.1 | scene-vide ; article-retirer ; batiment ; titre "La méthode" |
| 26.2 | sous-titre "Trois questions, dans l'ordre" |
| 26.3 | effacer-titres ; question-etage 1 "La loi décrit-elle l'acte ?" |
| 26.4 | question-etage 2 "Était-ce malgré tout permis ?" |
| 26.5 | question-etage 3 "Peut-on le reprocher ?" |
| 26.6 | accent batiment |
| 27.1 | scene-vide ; titre "Une question pour finir" |
| 27.2 | effacer-titres ; decor escalier ; personnage marc "Marc" turquoise gauche ; placer marc 0 ; personnage julien "Julien" rose droite ; placer julien 5 |
| 27.2@bouscule | marcher marc 3 ; etiquette geste "Sans le voir" -1.8 1.6 |
| 27.2@tombe | chute julien -1 |
| 27.3 | scene-vide ; batiment ; etage-question 1 ; etage-question 2 ; etage-question 3 ; titre "Quel étage pose problème ?" |
| 27.4 | renvoi "vidéo 4" |
| 28.1 | scene-vide ; livre ; titre "L'étude du droit" ; sous-titre "Tout est dans la description" |
| 28.2 | accent titre |
