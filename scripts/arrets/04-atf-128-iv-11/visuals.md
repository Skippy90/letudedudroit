# Visuels — Arrêts, vidéo 4 : Vingt mille francs pour un CD-ROM : qui a décidé qui ?

Ce fichier pilote les schémas Manim (`render/manim/video.py`). Vocabulaire des actions : `render/manim/README.md`.

Style « scène » : les faits se jouent dans une rue de Genève (décor rue, enseigne « Boucherie », puis « Café ») ; trois silhouettes sans visage : Z., l'informaticien (turquoise), Y., l'ami de son père (ambre pâle), X., le recourant (bleu clair) ; le juge en violet. Le CD-ROM est figuré par le pictogramme `document` (pas de pictogramme de disque dans la charte), le voilier par les vagues. Pense-bête en haut à droite, à partir de la ligne 13 : les trois questions « Décidé », « Vol », « Punissable ». Bloc de l'arrêt à côté de l'article.

| Moment | Actions |
| --- | --- |
| 1.1 | decor rue Étude ; etiquette lieu "Genève, 1999" -3.6 1.7 |
| 1.2 | personnage x "X." bleu_clair droite ; placer x 3 ; picto document -4.0 -0.4 |
| 2.1 | etiquette-retirer lieu ; etiquette cd "CD-ROM" -4.0 1.0 |
| 2.2 | personnage z "Z." turquoise centre-gauche ; placer z -1 ; etiquette role "Informaticien indépendant" -3.6 1.9 |
| 3.1 | scene-vide ; personnage z "Z." turquoise gauche ; picto vagues 2.2 -0.6 ; bulle z "L'Atlantique en voilier" |
| 3.2 | picto pieces 4.6 -0.6 ; etiquette fin "Financement ?" 4.0 1.2 |
| 4.1 | scene-vide ; decor rue Boucherie ; personnage z "Z." turquoise centre-gauche ; placer z -2 ; personnage y "Y." ambre_pale centre-droite ; placer y 3 ; etiquette date "2 juin 1999" -3.6 1.7 |
| 4.2 | etiquette-retirer date ; bulle y "X. pourrait aider" |
| 5.1 | effacer-bulle y ; etiquette cd "Un CD-ROM sur X." -3.6 1.7 ; marcher z -3 |
| 5.2 | etiquette-retirer cd ; bulle y "Une copie contre 20 000 francs" |
| 6.1 | effacer-bulle y ; personnage x "X." bleu_clair centre ; placer x 1 |
| 6.2 | scene-vide ; decor rue Café ; personnage z "Z." turquoise centre-gauche ; placer z -2 ; personnage x "X." bleu_clair droite ; placer x 3 ; etiquette echange "Une copie contre de l'argent" -3.6 1.9 |
| 6.3 | bulle z "Besoin d'argent" |
| 7.1 | etiquette-retirer echange ; effacer-bulle z ; etiquette decide "Décidé" -3.6 1.9 ; accent z |
| 8.1 | scene-vide ; personnage z "Z." turquoise gauche ; etiquette date "8 juin" 3.8 1.7 ; bulle z "Je me ravise" |
| 8.2 | picto telephone 1.6 -0.6 ; etiquette etude "L'Étude est prévenue" 3.8 0.2 |
| 9.1 | etiquette-retirer date ; etiquette etude "Plainte" 3.8 0.2 ; effacer-bulle z ; picto-retirer telephone |
| 9.2 | etiquette etude "Sous contrôle de la police" -0.6 1.9 ; personnage x "X." bleu_clair droite ; jetons x z |
| 9.3 | etiquette etude "X. interpellé" -0.6 1.9 ; accent x |
| 10.1 | scene-vide ; titre "Tentative d'instigation à vol" ; arret "ATF 128 IV 11" ; personnage x "X." bleu_clair gauche |
| 10.2 | personnage y "Y." ambre_pale centre-gauche |
| 10.3 | personnage juge "Le juge" violet droite ; accent juge |
| 11.1 | scene-vide ; titre "Instiguer : décider autrui" ; personnage x "X." bleu_clair gauche ; personnage z "Z." turquoise droite |
| 11.2 | article "Art. 24 CP" |
| 12.1 | bulle x "Pas un vol" |
| 12.2 | etiquette donnees "Des données ?" 0 0.2 |
| 13.1 | scene-vide ; article-retirer ; titre "Trois questions" ; personnage juge "Le juge" violet gauche |
| 13.2 | repere-liste "Décidé" "Vol" "Punissable" ; repere-marquer 1 ambre |
| 13.3 | repere-marquer 1 neutre ; repere-marquer 2 ambre |
| 13.4 | repere-marquer 2 neutre ; repere-marquer 3 ambre |
| 14.1 | scene-vide ; repere-marquer 3 neutre ; repere-marquer 1 ambre ; titre "Susciter la décision" ; personnage juge "Le juge" violet centre-droite ; renvoi "vidéo 10" |
| 15.1 | scene-vide ; personnage x "X." bleu_clair gauche ; personnage z "Z." turquoise centre-droite ; etiquette lien "Causalité" -1.2 0.2 |
| 15.1+2 | accent z |
| 16.1 | scene-vide ; personnage juge "Le juge" violet centre-droite ; liste-ajouter "Une demande" ; liste-ajouter "Une suggestion" |
| 16.2 | mot-barre "Une occasion" -3.4 -1.0 |
| 17.1 | scene-vide ; personnage z "Z." turquoise gauche ; bulle z "Déjà décidé" ; mot-barre "Instigation" 2.6 -0.4 |
| 18.1 | scene-vide ; personnage z "Z." turquoise gauche ; bulle z "Pourquoi pas ?" ; titre "Disposé n'est pas décidé" |
| 18.2 | bulle z "Pas encore décidé" |
| 19.1 | scene-vide ; arret-retirer ; decor rue Café ; personnage z "Z." turquoise centre-gauche ; placer z -2 ; personnage x "X." bleu_clair droite ; placer x 3 ; etiquette proteste "Pas de protestation" -3.6 1.9 |
| 19.2 | bulle z "Intéressant" |
| 20.1 | effacer-bulle z ; etiquette proteste "Fin de la discussion" -3.6 1.9 |
| 20.2 | etiquette-retirer proteste ; etiquette paie "X. accepte de payer" -0.6 1.9 ; accent x |
| 21.1 | jetons x z |
| 21.2 | etiquette paie "Déterminant" -0.6 1.9 ; repere-marquer 1 vert |
| 22.1 | scene-vide ; arret "ATF 128 IV 11" ; repere-marquer 2 ambre ; titre "L'intention" ; personnage x "X." bleu_clair gauche |
| 22.2 | bulle x "Le décider ?" |
| 22.3 | sous-titre "Le dol éventuel suffit" |
| 23.1 | effacer-titres ; bulle x "Sans payer, pas de copie" |
| 23.2 | effacer-bulle x ; personnage z "Z." turquoise centre-droite ; etiquette besoin "Besoin d'argent" -1.0 1.2 |
| 24.1 | scene-vide ; titre "Vouloir un vol ?" ; personnage x "X." bleu_clair gauche |
| 24.2 | bulle x "Une copie, pas l'original" |
| 25.1 | effacer-titres ; effacer-bulle x ; titre "Rien ne l'établit" ; personnage juge "Le juge" violet centre-droite |
| 25.2 | effacer-titres ; bulle x "Peu importe à qui" |
| 25.3 | picto document -1.2 -1.0 ; repere-marquer 2 vert |
| 26.1 | scene-vide ; article "Art. 139 CP" ; picto document -2.0 -0.4 ; etiquette chose "Chose mobilière" -2.0 1.2 |
| 26.2 | titre "C'est un vol" ; picto pieces 2.0 -0.4 |
| 27.1 | scene-vide ; titre "Et les données ?" ; personnage z "Z." turquoise gauche |
| 27.2 | article "Art. 143 CP" ; mot-barre "Soustraction de données" 2.4 -0.4 |
| 27.3 | etiquette acces "Accès autorisé" -1.6 1.4 |
| 27.4 | effacer-titres ; etiquette-retirer acces ; titre "Remettre la copie : non" |
| 28.1 | scene-vide ; article-retirer ; personnage x "X." bleu_clair gauche ; personnage z "Z." turquoise centre-droite ; picto document 0.6 -0.6 ; etiquette copie "Remettre la copie" -1.2 1.7 |
| 28.1+2 | picto-deplacer document -3.2 -0.6 0.4 |
| 29.1 | scene-vide ; repere-marquer 3 ambre ; titre "Si l'auteur n'agit pas ?" ; personnage z "Z." turquoise gauche |
| 29.2 | sous-titre "Commise ou tentée" |
| 30.1 | effacer-titres ; titre "Tentative d'instigation" ; article "Art. 24 CP" ; bulle z "Je me ravise" |
| 30.2 | effacer-bulle z ; sous-titre "Seulement pour un crime" |
| 31.1 | scene-vide ; article "Art. 139 CP" ; titre "Le vol est un crime" ; picto prison -2.0 -0.4 |
| 31.2 | etiquette peine "Cinq ans au plus" 1.4 -0.4 |
| 32.1 | scene-vide ; article-retirer ; titre "Recours rejeté" ; personnage juge "Le juge" violet centre-droite |
| 32.2 | repere-marquer 3 vert ; accent juge |
| 33.1 | scene-vide ; arret-retirer ; personnage y "Y." ambre_pale gauche ; bulle y "L'idée de l'échange" |
| 33.2 | effacer-bulle y ; personnage x "X." bleu_clair centre-droite ; titre "Il a fait basculer Z." ; accent x |
| 34.1 | scene-vide ; titre "Pas besoin de résistance" ; personnage z "Z." turquoise gauche ; bulle z "Pourquoi pas ?" |
| 35.1 | scene-vide ; titre "La limite : la décision" ; frise ; repere 0.6 "Décidé" |
| 35.2 | zone 0 0.6 vert ; point 0.3 "Intéressé" |
| 35.3 | zone 0.6 1 gris |
| 36.1 | scene-vide ; titre "Le piège classique" ; sous-titre "Il était partant" ; personnage z "Z." turquoise gauche ; personnage x "X." bleu_clair centre-droite |
| 37.1 | barrer |
| 37.2 | effacer-titres ; titre "Intéressé n'est pas décidé" ; accent x |
| 38.1 | scene-vide ; repere-retirer ; titre "Retenons" ; personnage x "X." bleu_clair droite |
| 38.2 | liste-ajouter "Faire naître la décision" |
| 38.3 | liste-ajouter "Tentative : crime seulement" |
| 39.1 | scene-vide ; titre "Une question pour finir" ; personnage juge "Le juge" violet droite |
| 39.2 | rembobiner |
| 39.3 | scene-vide ; personnage z "Z." turquoise gauche ; personnage x "X." bleu_clair droite ; picto document -2.0 -0.6 |
| 39.4 | bulle z "Déjà décidé" |
| 39.5 | jetons x z |
| 39.6 | titre "Instigateur ?" ambre |
| 39.7 | accent titre |
| 40.1 | scene-vide ; arret-retirer ; livre "Code pénal" 0 -0.5 ; titre "L'étude du droit" ; sous-titre "Tout est dans la description" |
| 40.2 | accent titre |
