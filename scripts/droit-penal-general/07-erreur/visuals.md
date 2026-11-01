# Visuels — Vidéo 7 : Je ne savais pas

Ce fichier pilote les schémas Manim (`render/manim/video.py`). Vocabulaire des actions : `render/manim/README.md`.

Colonne « Moment » : `ligne.phrase` du script, éventuellement `+secondes`. Plusieurs actions d'un même moment sont séparées par `;`.

Personnages : Élodie turquoise, le propriétaire ambre pâle, Arthur bleu clair, l'automobiliste rose, Sam violet.

Style « scène » (repris le 1er novembre 2026) : le cas se joue devant l'université (décor rue, enseigne « Université »), les vélos sont dessinés au trait (picto `velo`), un pense-bête « Faits / Droit » en haut à droite s'allume sur l'erreur dont on parle, les arrêts du Tribunal fédéral s'affichent à côté de l'article.

Écart assumé avec la colonne « À l'écran » : la vignette n'est pas dessinée ; elle est nommée par une étiquette.

| Moment | Actions |
| --- | --- |
| 1.1 | decor rue Université ; etiquette lieu "Genève, mardi soir" -3.6 1.7 |
| 1.2 | personnage elodie "Élodie" turquoise gauche ; placer elodie -3 |
| 2.1 | etiquette-retirer lieu ; picto velo 1.0 -1.85 ; picto velo:2 4.4 -1.85 |
| 2.1@cadenas | etiquette meme "Même modèle, même cadenas" 0.6 1.7 |
| 2.2 | bulle elodie "Mon vélo" |
| 2.2@part | effacer-bulle elodie ; marcher elodie -2 ; picto-deplacer velo -5.2 -1.85 |
| 3.1 | etiquette-retirer meme ; etiquette pas "Pas son vélo" -2.0 1.7 |
| 3.2 | etiquette sien "Le sien" 4.4 -0.6 |
| 3.3 | etiquette-retirer pas ; etiquette cadenas "Cadenas bon marché" -2.0 1.7 |
| 4.1 | etiquette-retirer cadenas ; etiquette-retirer sien ; picto-retirer velo:2 ; personnage proprio "Le propriétaire" ambre_pale droite ; placer proprio 3 ; etiquette plainte "Plainte" 4.8 1.7 |
| 4.2 | article "Art. 139 CP" |
| 4.3 | etiquette-retirer plainte ; titre "Un vol ?" |
| 4.4 | bulle elodie "Je ne savais pas" |
| 5.1 | scene-vide ; article-retirer ; titre "« Je ne savais pas »" |
| 5.2 | colonnes "Les faits" "Le droit" |
| 6.1 | colonne-accent 1 ; picto velo -3.5 -1.3 |
| 6.2 | effacer-titres ; titre "Ce qu'on faisait" |
| 6.3 | article "Art. 13 CP" ; sous-titre "Erreur sur les faits" |
| 7.1 | effacer-titres ; colonne-accent 2 ; titre "Le droit d'agir" ; picto parlement 3.5 -1.3 |
| 7.2 | article "Art. 21 CP" ; sous-titre "Erreur sur l'illicéité" |
| 8.1 | scene-vide ; article-retirer ; batiment ; renvoi "vidéo 1" ; repere-liste "Faits" "Droit" |
| 8.2 | accent batiment |
| 9.1 | scene-vide ; decor rue Université ; personnage elodie "Élodie" turquoise gauche ; placer elodie -2 ; picto velo -5.2 -1.85 |
| 9.3 | bulle elodie "Mon vélo" ; repere-marquer 1 ambre |
| 10.1 | article "Art. 139 CP" ; etiquette autrui "Chose d'autrui ?" 0.6 1.7 |
| 10.2 | etiquette autrui "Son vélo, croit-elle" 0.6 1.7 |
| 11.1 | scene-vide ; article "Art. 13 CP" ; titre "Jugée d'après ce qu'elle croyait" ; personnage elodie "Élodie" turquoise gauche |
| 11.2 | sous-titre "Appréciation erronée des faits" |
| 11.3 | effacer-titres ; titre "Si c'est favorable" |
| 12.1 | scene-vide ; decor rue Université ; personnage elodie "Élodie" turquoise gauche ; placer elodie -2 ; picto velo -5.2 -1.85 ; titre "Comme si c'était son vélo" |
| 12.2 | etiquette pasvol "Pas un vol" 0.6 1.7 |
| 12.3 | etiquette-retirer pasvol ; personnage juge "Le juge" bleu_clair droite ; placer juge 3 ; bulle juge "Plausible ?" |
| 12.4 | effacer-titres ; etiquette indices "Couleur, modèle, cadenas" -2.4 1.7 |
| 13.1 | scene-vide ; batiment |
| 13.2 | etage 1 gris ; renvoi "vidéo 4" |
| 13.3 | titre "La typicité tombe" |
| 14.1 | scene-vide ; article "Art. 13 CP" ; titre "Second alinéa" ; personnage elodie "Élodie" turquoise gauche |
| 14.2 | sous-titre "Erreur évitable : négligence" |
| 15.1 | effacer-titres ; retirer elodie ; titre "Si la loi la punit" |
| 15.2 | case "Vol par négligence" ; cocher 1 gris ; article "Art. 139 CP" |
| 15.3 | sous-titre "Pas punissable" |
| 16.1 | scene-vide ; rembobiner ; article-retirer ; decor rue Université ; personnage elodie "Élodie" turquoise gauche ; placer elodie -2 ; picto velo -5.2 -1.85 ; titre "L'erreur inverse" |
| 16.2 | bulle elodie "Je le vole" |
| 16.3 | etiquette sien "C'était le sien" 0.6 1.7 |
| 16.4 | renvoi "vidéo 9" ; effacer-titres ; titre "La tentative" |
| 17.1 | scene-vide ; renvoi "vidéo 6" ; personnage elodie "Élodie" turquoise gauche ; bulle elodie "Il m'attaque ?" ; bouclier 3.5 0.3 |
| 17.2 | titre "Jugée d'après sa croyance" |
| 18.1 | scene-vide ; repere-marquer 1 neutre ; repere-marquer 2 ambre ; personnage arthur "Arthur" bleu_clair gauche |
| 18.2 | titre "Il sait ce qu'il fait" |
| 18.3 | bulle arthur "C'est permis" |
| 19.1 | scene-vide ; article "Art. 21 CP" ; titre "Ne pouvait pas savoir" ; personnage arthur "Arthur" bleu_clair gauche |
| 19.2 | sous-titre "Pas coupable" |
| 20.1 | scene-vide ; batiment |
| 20.2 | etage 1 vert ; etage 2 vert |
| 20.3 | etage 3 ambre |
| 21.1 | scene-vide ; titre "Erreur évitable ?" ; personnage arthur "Arthur" bleu_clair gauche |
| 21.2 | sous-titre "Peine atténuée" ; picto pieces 3.5 0.3 |
| 21.3 | effacer-titres ; titre "Coupable, mais moins" |
| 22.1 | scene-vide ; titre "Le Tribunal fédéral" ; arret "ATF 141 IV 336" ; personnage arthur "Arthur" bleu_clair gauche |
| 22.2 | sous-titre "Se croire en droit" |
| 22.3 | effacer-titres ; mot-barre "Pas puni ?" |
| 23.1 | scene-vide ; titre "Plus loin encore" ; arret "ATF 104 IV 217" ; personnage arthur "Arthur" bleu_clair gauche |
| 23.2 | sous-titre "Un vague sentiment suffit" |
| 23.3 | effacer-titres ; titre "Pas besoin d'être juriste" |
| 24.1 | scene-vide ; rembobiner ; arret "ATF 141 IV 336" ; personnage auto "L'automobiliste" rose gauche ; picto voiture 4.2 0.2 ; titre "Un cas réel" |
| 24.2 | etiquette vignette "Vignette décollée" 4.2 1.7 |
| 24.3 | etiquette vignette "Film adhésif" 4.2 1.7 |
| 25.1 | effacer-titres ; etiquette-retirer vignette ; titre "Il plaide l'erreur" |
| 25.2 | bulle auto "Au pire, une amende" |
| 26.1 | effacer-bulle auto ; titre "Erreur refusée" |
| 26.2 | etiquette pare "Sur le pare-brise" 4.2 1.7 |
| 26.3 | effacer-titres ; titre "Il savait" |
| 27.1 | scene-vide ; titre "Le numéro de l'article ?" ; picto document 0 0.3 |
| 27.2 | sous-titre "Inutile pour savoir qu'on fait mal" |
| 28.1 | scene-vide ; arret-retirer ; repere-marquer 2 neutre ; titre "Le piège classique" ; picto document 0 0.0 |
| 28.2 | sous-titre "Nul n'est censé ignorer la loi" |
| 28.3 | effacer-titres ; titre "L'erreur ne compte jamais ?" |
| 29.1 | barrer |
| 29.2 | scene-vide ; article "Art. 21 CP" ; titre "L'erreur est admise" ; repere-marquer 2 ambre |
| 29.3 | sous-titre "Si l'on ne pouvait pas savoir" |
| 30.1 | scene-vide ; article-retirer ; repere-marquer 2 neutre ; repere-marquer 1 ambre ; batiment ; etage 1 gris |
| 30.2 | titre "L'erreur sur les faits" |
| 31.1 | scene-vide ; colonnes "Les faits" "Le droit" |
| 31.2 | colonne-accent 1 ; picto velo -3.5 -1.3 |
| 31.3 | colonne-accent 2 ; picto parlement 3.5 -1.3 |
| 31.4 | titre "Quel étage ?" |
| 32.1 | scene-vide ; titre "Retenons" ; repere-marquer 1 ambre ; personnage elodie "Élodie" turquoise gauche |
| 32.2 | article "Art. 13 CP" ; sous-titre "Les faits : ce qu'on croyait" |
| 32.3 | effacer-titres ; titre "Évitable : négligence" |
| 33.1 | retirer elodie ; personnage arthur "Arthur" bleu_clair gauche ; repere-marquer 1 neutre ; repere-marquer 2 ambre ; article "Art. 21 CP" ; sous-titre "Le droit : pas coupable" |
| 33.2 | effacer-titres ; titre "Évitable : peine atténuée" |
| 33.3 | sous-titre "Le juge établit ce qu'on croyait" |
| 34.1 | scene-vide ; repere-marquer 2 neutre ; article-retirer ; titre "Une question pour finir" |
| 34.2 | effacer-titres ; decor rue Université ; personnage sam "Sam" violet gauche ; placer sam -2 ; picto portefeuille 0.4 -2.0 |
| 34.3 | etiquette autrui "À quelqu'un d'autre" 0.6 1.7 |
| 34.4 | bulle sam "Trouvé, c'est gagné" |
| 35.1 | etiquette-retirer autrui ; titre "Faits ou droit ?" ; repere-marquer 1 ambre ; repere-marquer 2 ambre |
| 35.2 | effacer-titres ; titre "Une excuse ?" |
| 35.3 | accent sam |
| 36.1 | scene-vide ; repere-retirer ; livre "Code pénal" 0 -0.5 ; titre "L'étude du droit" ; sous-titre "Tout est dans la description" |
