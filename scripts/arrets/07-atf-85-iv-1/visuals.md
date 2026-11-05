# Visuels — Arrêts, vidéo 7 : Il boit, puis il conduit : où commence la faute ?

Ce fichier pilote les schémas Manim (`render/manim/video.py`). Vocabulaire des actions : `render/manim/README.md`.

Style « scène » : les faits se jouent dans une rue du canton de Genève (décor rue, enseigne « Café », puis « Taxis »), la Jaguar au trait (`picto voiture`) ; trois silhouettes sans visage : l'automobiliste (turquoise), son compagnon (bleu clair), le chauffeur de taxi (ambre pâle) ; le juge en violet dans la salle d'audience (décor tribunal). Le cycliste n'a pas de silhouette : un pictogramme vélo, puis le pictogramme danger, et l'écran se vide ; aucun choc n'est montré. Aucun nom de personne à l'écran. Frise du temps « Il boit » → « Il conduit » pour l'action libre dans sa cause, reprise de la vidéo 8. Bloc de l'arrêt à côté de l'article. L'ancien article 12 est affiché « Ancien art. 12 CP », pour ne pas le confondre avec l'art. 12 actuel.

| Moment | Actions |
| --- | --- |
| 1.1 | decor rue Café ; etiquette lieu "Genève, 1958" -3.6 1.7 |
| 1.2 | picto voiture -5.4 -1.7 ; personnage auto "L'automobiliste" turquoise centre-gauche ; placer auto -1 |
| 2.1 | etiquette-retirer lieu ; personnage compagnon "Le compagnon" bleu_clair centre-droite ; placer compagnon 2 ; etiquette lieu "Hermance" 3.6 1.7 |
| 2.2 | etiquette lieu "Les cafés" 3.6 1.7 ; picto bouteille -3.8 0.6 |
| 3.1 | etiquette lieu "Au milieu de la nuit" 3.6 1.7 ; picto lune 5.0 2.6 |
| 3.2 | etiquette ivre "Ivre" -1.6 2.2 ; accent auto |
| 3.3 | etiquette-retirer ivre ; picto-retirer bouteille ; accent compagnon |
| 4.1 | scene-vide ; decor rue ; picto voiture -5.8 -1.7 ; personnage auto "L'automobiliste" turquoise centre-gauche ; placer auto -1 ; bulle auto "Je reprends le volant" |
| 4.2 | effacer-bulle auto ; personnage chauffeur "Le chauffeur" ambre_pale droite ; placer chauffeur 3 ; picto-deplacer voiture -5.1 -1.7 |
| 5.1 | bulle chauffeur "Il va repartir" |
| 5.2 | scene-vide ; decor rue Taxis ; picto voiture -0.6 -1.7 ; personnage chauffeur "Le chauffeur" ambre_pale droite ; placer chauffeur 3 ; etiquette lieu "Garage des taxis" -3.6 1.7 |
| 6.1 | retirer chauffeur ; personnage auto "L'automobiliste" turquoise centre-gauche ; placer auto -3 ; picto-deplacer voiture 3.6 -1.7 |
| 6.2 | etiquette heure "Près de 5 h" 3.6 1.7 ; picto lune 5.0 2.6 |
| 7.1 | scene-vide ; etiquette lieu "Quai de Cologny" -3.6 1.7 ; picto voiture -2.0 0.3 ; picto velo 2.0 0.3 |
| 7.2 | picto danger 0 0.3 |
| 7.2+1.2 | scene-vide |
| 8.1 | decor rue ; picto voiture 3.2 -1.7 ; etiquette loin "Un kilomètre plus loin" 3.2 1.7 |
| 8.2 | etiquette-retirer loin ; personnage auto "L'automobiliste" turquoise gauche ; placer auto -3 ; etiquette haie "Caché derrière une haie" -1.4 1.9 |
| 9.1 | scene-vide ; personnage auto "L'automobiliste" turquoise gauche ; picto bouteille 0 0.3 ; etiquette taux "2,33 à 2,58 ‰" 3.4 0.4 |
| 10.1 | scene-vide ; decor tribunal ; personnage auto "L'automobiliste" turquoise gauche ; placer auto -1 ; personnage juge "Le juge" violet droite ; placer juge 3 ; arret "ATF 85 IV 1" ; etiquette peine "Deux ans et demi" 0.6 2.4 |
| 10.2 | etiquette peine "Homicide par négligence" 0.6 2.4 ; picto prison 0.6 1.1 |
| 11.1 | etiquette-retirer peine ; picto-retirer prison ; titre "Recours au Tribunal fédéral" |
| 11.2 | article "Art. 263 CP" ; parole auto "L'article 263 !" |
| 12.1 | effacer-parole auto ; effacer-titres ; titre "Irresponsabilité fautive" ; picto bouteille 0.6 1.1 |
| 12.2 | sous-titre "Le « délit d'ivresse »" |
| 13.1 | scene-vide ; effacer-titres ; article "Ancien art. 12 CP" ; personnage auto "L'automobiliste" turquoise gauche ; parole auto "Pas l'article 12" |
| 13.2 | effacer-parole auto ; titre "L'ancien Code pénal" ambre ; livre "Code pénal" 3.2 |
| 13.3 | livre-retirer ; mot-barre "Art. 12 actuel : l'intention" |
| 14.1 | scene-vide ; titre "Irresponsable exprès" ; personnage auto "L'automobiliste" turquoise gauche ; picto bouteille 0 0.3 ; bulle auto "Pour commettre l'infraction" |
| 15.1 | scene-vide ; article-retirer ; arret-retirer ; colonnes "Ancien art. 12" "Art. 263" ; picto voiture 0 -1.6 |
| 16.1 | scene-vide ; personnage juge "Le juge" violet droite ; titre "Une règle, un nom" |
| 16.2 | effacer-titres ; titre "Actio libera in causa" ambre ; sous-titre "L'action libre dans sa cause" |
| 17.1 | scene-vide ; frise ; point 0.7 "Il conduit" ; picto voiture 4.2 1.4 |
| 17.2 | point 0.25 "Il boit" ; zone 0.1 0.4 vert ; picto bouteille -2.4 1.4 |
| 18.1 | scene-vide ; arret "ATF 85 IV 1" ; titre "Le texte de l'époque" ; liste "Intentionnelle" ; personnage juge "Le juge" violet droite |
| 18.2 | liste-ajouter "Par négligence" ; liste-surligner 2 ; accent juge |
| 19.1 | scene-vide ; arret-retirer ; frise ; point 0.25 "Il boit" ; point 0.7 "Il conduit" |
| 19.1+3 | fleche-retour 0.7 0.25 vert ; repere 0.25 "Pouvait prévoir" |
| 20.1 | scene-vide ; titre "Pourquoi ?" ; personnage juge "Le juge" violet droite |
| 20.2 | liste "Une faute" ; picto bouteille 1.0 0.3 |
| 20.3 | liste-ajouter "Une cause" ; liste-surligner 2 |
| 21.1 | scene-vide ; personnage auto "L'automobiliste" turquoise gauche ; mot-barre "Privilégié" |
| 22.1 | scene-vide ; colonnes "Action libre" "Art. 263" ; colonne-accent 1 ; colonne-eteindre 2 ; article "Art. 263 CP" ; picto bouteille 0 -1.4 |
| 22.2 | titre "Art. 263 : les autres cas" |
| 23.1 | scene-vide ; titre "Les autres cas" ; personnage auto "L'automobiliste" turquoise gauche ; cases "Pas de dessein" "Pas prévisible" ; cocher 1 question |
| 23.2 | cocher 2 question |
| 24.1 | scene-vide ; article-retirer ; arret-retirer ; decor rue Café ; personnage auto "L'automobiliste" turquoise gauche ; placer auto -3 ; titre "Appliquons au cas" |
| 24.2 | etiquette dessein "Pas de dessein" 4.0 2.2 ; accent auto |
| 25.1 | etiquette-retirer dessein ; bulle auto "Je rentre en voiture" ; picto voiture 4.8 -1.7 |
| 25.1+3 | picto danger 4.8 0.4 |
| 26.1 | scene-vide ; decor rue Taxis ; personnage auto "L'automobiliste" turquoise gauche ; placer auto -3 ; picto voiture 4.6 -1.7 |
| 26.2 | parole auto "On m'a presque ramené" |
| 26.3 | effacer-parole auto ; parole auto "Pas prévisible" |
| 27.1 | effacer-parole auto ; mot-barre "On m'a ramené" 3.0 2.1 |
| 27.2 | titre "Il fallait demander avant" |
| 27.3 | bulle auto "Je rentrerai seul" |
| 28.1 | scene-vide ; decor rue Taxis ; personnage auto "L'automobiliste" turquoise gauche ; placer auto -3 ; picto voiture 1.6 -1.7 ; etiquette lieu "Pas chez lui" -3.6 1.7 |
| 28.2 | etiquette lieu "Garage des taxis" -3.6 1.7 ; accent auto |
| 29.1 | scene-vide ; arret "ATF 85 IV 1" ; personnage juge "Le juge" violet droite ; titre "Le Tribunal fédéral" |
| 29.2 | effacer-titres ; titre "Tenté de conduire" ambre ; picto voiture -2.0 0.3 |
| 30.1 | sous-titre "Tant qu'il n'est pas rentré" ; accent juge |
| 31.1 | scene-vide ; arret-retirer ; frise ; point 0.2 "Il boit" ; point 0.75 "Accident" ; fleche-retour 0.75 0.2 vert |
| 31.2 | scene-vide ; titre "Après l'accident" ; liste "S'arrêter" ; liste-ajouter "Secourir" ; liste-ajouter "Annoncer" ; picto voiture 3.6 0.3 |
| 32.1 | scene-vide ; cases "Intentionnelle" "Par négligence" ; cocher 1 gris ; cocher 2 vert ; personnage auto "L'automobiliste" turquoise gauche |
| 32.2 | titre "Condamnation justifiée" ; arret "ATF 85 IV 1" |
| 33.1 | scene-vide ; arret-retirer ; titre "Et aujourd'hui ?" ; livre "Code pénal" 0 -0.5 |
| 33.2 | livre-ouvrir ; article "Art. 19 CP" ; renvoi "vidéo 8" |
| 34.1 | scene-vide ; titre "Plus de dessein" ; mot-barre "Dessein" ; picto bouteille -3.0 0.3 |
| 34.2 | scene-vide ; titre "Alinéa 4" ; cases "État évitable" "Acte prévisible" ; personnage auto "L'automobiliste" turquoise gauche |
| 35.1 | effacer-titres ; titre "Négligence comprise" ; cocher 1 vert ; cocher 2 vert |
| 35.2 | sous-titre "Aussi la responsabilité restreinte" |
| 36.1 | scene-vide ; article "Art. 263 CP" ; titre "Toujours là" ; picto bouteille 0 0.3 |
| 36.2 | sous-titre "Ivresse fautive, crime ou délit" ; personnage auto "L'automobiliste" turquoise gauche |
| 37.1 | scene-vide ; article-retirer ; renvoi "vidéo 8" ; frise ; point 0.25 "Il boit" ; point 0.7 "Il conduit" |
| 37.2 | fleche-retour 0.7 0.25 vert ; repere 0.25 "Jugé responsable" |
| 38.1 | scene-vide ; article-retirer ; decor rue Taxis ; picto voiture 4.6 -1.7 ; personnage auto "L'automobiliste" turquoise gauche ; placer auto -3 ; titre "Un critère concret" |
| 38.2 | effacer-titres ; titre "Pas encore rentré : prévoir" ; bulle auto "Je reprends le volant ?" |
| 39.1 | scene-vide ; titre "Le piège classique" ; personnage auto "L'automobiliste" turquoise gauche ; bulle auto "J'étais ivre" |
| 40.1 | effacer-bulle auto ; mot-barre "Seulement l'ivresse" |
| 40.2 | effacer-titres ; titre "Il répond de l'acte" ambre |
| 40.3 | sous-titre "Homicide par négligence" ; accent auto |
| 41.1 | scene-vide ; titre "Retenons" ; personnage juge "Le juge" violet droite |
| 41.2 | liste "La faute avant l'acte" |
| 41.3 | liste-ajouter "Intention ou négligence" |
| 42.1 | scene-vide ; titre "Aujourd'hui" ; article "Art. 19 CP" ; cases "État évitable" "Acte prévisible" ; personnage juge "Le juge" violet gauche |
| 42.2 | article "Art. 263 CP" ; sous-titre "Sinon : art. 263" |
| 43.1 | scene-vide ; article-retirer ; titre "Une question pour finir" ; personnage juge "Le juge" violet gauche |
| 43.2 | effacer-titres ; titre "« On m'a ramené » : pourquoi ça échoue ?" ambre |
| 43.3 | accent juge |
| 44.1 | scene-vide ; livre "Code pénal" 0 -0.5 ; titre "L'étude du droit" ; sous-titre "Tout est dans la description" |
| 44.2 | accent titre |
