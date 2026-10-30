# Visuels — Vidéo 4 : Le voulait-il vraiment ?

Ce fichier pilote les schémas Manim (`render/manim/video.py`). Vocabulaire des actions : `render/manim/README.md`.

Colonne « Moment » : `ligne.phrase` du script, éventuellement `+secondes`. Plusieurs actions d'un même moment sont séparées par `;`.

Personnages : Léo turquoise, Adam rose, Sofia violet.

Style « scène » : chaque version de l'histoire se rejoue dans le parc (arbre, poteau, haie au premier plan), le ballon part du pied de Léo, et un pense-bête en haut à droite (« Intention », « Négligence ») s'allume en ambre sur l'attitude retenue, en gris quand aucune ne l'est.

| Moment | Actions |
| --- | --- |
| 1.1 | decor parc ; etiquette lieu "Sion, mercredi après-midi" -2.6 2.45 |
| 1.2 | personnage leo "Léo" turquoise gauche ; placer leo -3 ; picto ballon -4.1 -2.1 |
| 1.2@football | marcher leo -2 |
| 2.1 | personnage adam "Adam" rose droite ; placer adam 2 |
| 2.1@ballon | etiquette-retirer lieu ; picto-deplacer ballon -1.0 -1.2 0.6 |
| 2.2@groupe | etiquette groupe "Le groupe d'à côté" 3.2 1.7 |
| 2.2@touche | picto-deplacer ballon 2.7 -0.6 0.5 ; dommage adam |
| 3.1@blessé | etiquette-retirer groupe ; etiquette blesse "Blessé" 3.2 1.7 |
| 3.2@geste | etiquette cause "Le tir de Léo" -3.2 1.7 |
| 4.1 | etiquette-retirer cause ; etiquette-retirer blesse ; titre "Une question décide de tout" |
| 4.2@blesser | bulle leo "Blesser Adam ?" |
| 4.3@malgré | sous-titre "Ou malgré lui ?" |
| 5.1 | scene-vide ; batiment ; renvoi "vidéo 1" |
| 5.1@typicité | etage 1 ambre |
| 5.2@geste | titre "Le geste" |
| 5.2@tête | sous-titre "et la tête" |
| 6.1 | scene-vide ; personnage leo "Léo" turquoise droite ; bulle leo "?" |
| 6.1@douze | article "Art. 12 CP" |
| 6.2@intention | liste-ajouter "Intention" |
| 6.2@négligence | liste-ajouter "Négligence" |
| 7.1@énorme | accent liste |
| 7.2@intentionnellement | liste-surligner 1 ; titre "Punissable en principe" |
| 8.1 | effacer-titres ; effacer-bulle leo ; retirer leo ; repere-liste "Intention" "Négligence" |
| 8.1@versions | titre "Cinq versions" |
| 8.2@voulu | sous-titre "Du plus voulu au plus involontaire" |
| 9.1 | scene-vide ; article-retirer ; decor parc ; personnage leo "Léo" turquoise gauche ; placer leo -3 ; personnage adam "Adam" rose droite ; placer adam 2 ; picto ballon -4.1 -2.1 ; titre "Version 1" |
| 9.2@veut | picto tension 0 0.4 |
| 9.3@vise | picto-retirer tension ; bulle leo "Lui faire mal" |
| 9.3@exprès | picto-deplacer ballon 2.7 -0.6 0.5 |
| 9.3@mal | dommage adam |
| 10.1 | scene-vide ; personnage leo "Léo" turquoise gauche ; article "Art. 12 CP" |
| 10.1@conscience | case "Conscience" |
| 10.1@volonté | case "Volonté" |
| 11.1@conscience | cocher 1 vert |
| 11.2@volonté | cocher 2 vert |
| 12.1@intention | repere-marquer 1 ambre ; titre "Intention" |
| 12.2@dol | sous-titre "Dol direct" |
| 13.1 | scene-vide ; article-retirer ; decor parc ; personnage leo "Léo" turquoise gauche ; placer leo -3 ; picto ballon -4.1 -2.1 ; titre "Version 2" |
| 13.2@personne | personnage adam "Adam" rose droite ; placer adam 2 |
| 13.3@impressionner | bulle leo "Impressionner" |
| 14.1@groupe | accent adam |
| 14.2@pis | bulle leo "Tant pis" |
| 15.1@souhaite | etiquette souhait "Pas souhaité" 3.2 1.7 |
| 15.2@accepte | etiquette accepte "Mais accepté" -0.4 1.7 ; picto-deplacer ballon 2.7 -0.6 0.5 |
| 16.1 | scene-vide ; article "Art. 12 CP" ; titre "Seconde phrase" |
| 16.2@possible | sous-titre "Possible et accepté : intention" |
| 17.1@dol | effacer-titres ; repere-marquer 1 ambre ; titre "Dol éventuel" ambre |
| 17.2@accommode | sous-titre "Il s'en accommode" |
| 18.1@intention | personnage leo "Léo" turquoise gauche ; case "Intention" ; cocher 1 vert |
| 18.2@puni | accent leo |
| 19.1 | scene-vide ; article-retirer ; repere-marquer 1 neutre ; decor parc ; personnage leo "Léo" turquoise gauche ; placer leo -3 ; picto ballon -4.1 -2.1 ; titre "Version 3" |
| 19.2@groupe | personnage adam "Adam" rose droite ; placer adam 2 |
| 19.3@raté | bulle leo "Un risque" |
| 20.1@précision | bulle leo "Je suis précis" |
| 20.2@rien | bulle leo "Rien n'arrivera" |
| 20.3@touche | effacer-bulle leo ; picto-deplacer ballon 2.7 -0.6 0.5 ; dommage adam |
| 21.1 | scene-vide ; personnage leo "Léo" turquoise gauche ; case "Accepte le résultat" |
| 21.1@accepte | cocher 1 gris |
| 21.2@confiance | titre "Confiance mal placée" |
| 21.3@intention | sous-titre "Plus de l'intention" |
| 22.1@négligence | repere-marquer 2 ambre ; effacer-titres ; titre "Négligence consciente" ambre |
| 22.2@risque | sous-titre "Risque vu, issue espérée" |
| 23.1 | scene-vide ; repere-marquer 2 neutre ; decor parc ; personnage leo "Léo" turquoise gauche ; placer leo -3 ; picto ballon -4.1 -2.1 ; titre "Version 4" |
| 23.2@regarde | etiquette regard "Ne regarde pas" -4.8 1.7 |
| 23.3@groupe | personnage adam "Adam" rose droite ; placer adam 3 |
| 23.3@haie | accent adam |
| 24.1@rendu | etiquette regard "Risque pas vu" -4.8 1.7 |
| 24.2@vérifier | etiquette verifier "Aurait dû vérifier" -0.4 1.7 ; picto-deplacer ballon 5.0 -0.4 0.6 |
| 25.1 | scene-vide ; article "Art. 12 CP" ; titre "Imprévoyance coupable" |
| 25.2@précautions | sous-titre "Précautions non prises" |
| 26.1@versions | repere-marquer 2 ambre ; effacer-titres ; titre "Négligence" ambre |
| 26.2@compte | effacer-titres ; liste-ajouter "Ne pas se rendre compte" |
| 26.3@tient | liste-ajouter "Ne pas en tenir compte" |
| 27.1 | scene-vide ; article-retirer ; repere-marquer 2 neutre ; decor parc ; personnage leo "Léo" turquoise gauche ; placer leo -3 ; picto ballon -4.1 -2.1 ; titre "Version 5" |
| 27.2@regardé | bulle leo "Parc vide" |
| 27.3@ballon | effacer-bulle leo ; picto-deplacer ballon 0.45 -0.6 0.4 |
| 27.3@rebondit | personnage adam "Adam" rose droite ; placer adam 4 |
| 27.3@file | marcher adam 2 ; picto-deplacer ballon 2.7 -0.6 -0.3 |
| 28.1@précautions | etiquette precautions "Précautions prises" -3.2 1.7 |
| 28.2@intention | repere-marquer 1 gris ; repere-marquer 2 gris |
| 28.3@accident | titre "Un accident" |
| 29.1 | scene-vide ; repere-marquer 1 neutre ; repere-marquer 2 neutre ; personnage leo "Léo" turquoise gauche ; bulle leo "?" |
| 29.1@lire | titre "Lire dans sa tête ?" |
| 29.2 | effacer-bulle leo ; sous-titre "Impossible" |
| 29.3@déduit | effacer-titres ; titre "Le juge déduit" ambre |
| 30.1 | scene-vide ; titre "Les indices" |
| 30.2@risque | liste-ajouter "Risque connu" |
| 30.3@imprudence | liste-ajouter "Imprudence grave" |
| 31.1@mobiles | liste-ajouter "Mobiles" |
| 31.2@agi | liste-ajouter "Manière d'agir" |
| 31.3@indices | accent liste |
| 32.1 | scene-vide ; titre "Une frontière délicate" |
| 32.2@voiture | sous-titre "Course mortelle : dol éventuel" ; repere-marquer 1 ambre |
| 32.3@légère | effacer-titres ; titre "Pas à la légère" ambre |
| 33.1 | scene-vide ; repere-marquer 1 neutre ; titre "Le piège classique" |
| 33.2@négligence | sous-titre "Négligence toujours punie" |
| 33.3 | barrer |
| 34.1 | scene-vide ; repere-marquer 2 ambre ; livre ; article "Art. 12 CP" |
| 34.1@expressément | livre-ouvrir ; titre "Seulement si la loi le prévoit" |
| 35.1 | scene-vide ; decor parc ; personnage adam "Adam" rose droite ; placer adam 2 ; dommage adam ; titre "Les blessures" |
| 35.2@cent | article "Art. 125 CP" |
| 35.2@négligence | etiquette blessure "Lésions par négligence" -2.8 1.1 ; picto coche 0.9 1.1 |
| 35.3@plainte | effacer-titres ; sous-titre "Sur plainte, d'office si grave" |
| 36.1 | scene-vide ; rembobiner ; decor rue ; personnage leo "Léo" turquoise gauche ; placer leo -3 ; picto ballon -4.1 -2.1 |
| 36.1@vitre | picto-deplacer ballon 4.6 -1.0 0.5 ; etiquette vitre "Vitre de voiture" 4.4 1.7 |
| 36.2@cent | article "Art. 144 CP" |
| 36.2@intentionnelle | etiquette version "Intentionnel seulement" -2.6 2.45 |
| 37.1 | scene-vide ; case "Dommage par négligence" ; cocher 1 gris |
| 37.2@infraction | titre "Pas d'infraction" |
| 37.3@réparation | sous-titre "Seulement une réparation" |
| 38.1 | scene-vide ; article-retirer ; repere-marquer 2 neutre ; batiment ; renvoi "vidéo 1" |
| 38.2@étage | titre "Quel étage ?" |
| 39.1 | fleche 1 ; etage 1 gris |
| 39.2@intentionnellement | article "Art. 123 CP" ; sous-titre "Pas d'intention" |
| 40.1 | article "Art. 125 CP" ; repere-marquer 2 ambre ; effacer-titres ; titre "Imprévoyance coupable ?" |
| 40.1@plainte | sous-titre "Et plainte de Julien" |
| 41.1 | scene-vide ; article-retirer ; repere-marquer 2 neutre ; titre "L'échelle" |
| 41.2@vouloir | liste-ajouter "Vouloir : intention" ; repere-marquer 1 ambre |
| 41.3@possible | liste-ajouter "Accepter : dol éventuel" |
| 42.1@risque | liste-ajouter "Espérer : négligence" ; repere-marquer 2 ambre |
| 42.2@voir | liste-ajouter "Ignorer : négligence" |
| 43.1 | scene-vide ; repere-marquer 1 neutre ; titre "Si la loi le dit" ambre |
| 43.2@intentionnel | sous-titre "Sinon, seul l'intentionnel" ; repere-marquer 2 neutre ; repere-marquer 1 ambre |
| 44.1 | scene-vide ; repere-marquer 1 neutre ; titre "Une question pour finir" |
| 44.2 | effacer-titres ; decor rue ; personnage sofia "Sofia" violet gauche ; placer sofia -2 ; etiquette vite "Bien trop vite" -3.2 1.7 |
| 44.3@renverser | bulle sofia "Un risque" |
| 44.4@freiner | bulle sofia "Je freinerai" |
| 44.5 | etiquette-retirer vite ; titre "Intention ou négligence ?" ambre |
| 44.6@commentaire | accent sofia |
| 45.1 | scene-vide ; repere-retirer ; titre "L'étude du droit" ; sous-titre "Tout est dans la description" |
| 45.2 | accent titre |
