# Visuels — Vidéo 10 : Ils étaient plusieurs

Ce fichier pilote les schémas Manim (`render/manim/video.py`). Vocabulaire des actions : `render/manim/README.md`.

Colonne « Moment » : `ligne.phrase` du script, éventuellement `+secondes`. Plusieurs actions d'un même moment sont séparées par `;`.

Personnages (bonhommes en bâtons depuis le 6 novembre 2026 ; poses et visages aux moments marqués) : Max turquoise, Jade rose, Lina violet, Noé bleu clair, Paul ambre pâle ; seconds rôles : le vendeur ambre pâle, l'homme du cas réel ambre pâle, l'informaticien bleu clair, l'ami de Paul rose.

Style « scène » (repris le 1er novembre 2026) : le cas se joue devant le magasin (décor rue, enseigne « Électronique ») ; les auteurs se tiennent devant la vitrine, les participants restent à l'écart ; un pense-bête « Coauteur / Instigateur / Complice » en haut à droite s'allume sur le rôle dont on parle ; les arrêts du Tribunal fédéral s'affichent à côté de l'article.

Objets dessinés (6 novembre 2026) : l'ordinateur, le sac de Noé (il passe de Noé à Max, l'ordinateur y entre), le CD-ROM, la caisse à outils de Paul. Écarts assumés avec la colonne « À l'écran » : pas de tableau ni de flèche entre silhouettes : les peines sont posées en étiquettes sous les silhouettes (ligne 30), l'accessoriété par une étiquette (ligne 32) ; les trois rôles de la question finale s'allument dans le pense-bête au lieu de trois cases.

| Moment | Actions |
| --- | --- |
| 1.1 | decor rue Électronique ; etiquette lieu "Martigny, samedi" -3.6 1.7 |
| 1.2 | etiquette ordi "L'ordinateur" 0.6 1.7 ; picto ordinateur 0.5 -1.5 |
| 1.3 | etiquette-retirer lieu ; personnage lina "Lina" violet gauche ; placer lina -4 ; personnage noe "Noé" bleu_clair gauche ; placer noe -2 ; personnage max "Max" turquoise centre-gauche ; placer max -1 ; personnage jade "Jade" rose droite ; placer jade 1 ; picto sac -2.4 -1.3 ; tenir noe sac aussitot |
| 2.1 | accent lina ; etiquette idee "L'idée" -6.0 1.0 ; rejoindre max lina |
| 2.2 | etiquette-retirer idee ; parler lina max ; parole lina "Je te le rachète" |
| 2.2+1.8 | picto pieces -6.4 1.3 |
| 2.2+2.8 | picto-deplacer pieces -5.1 1.2 0.6 |
| 3.1 | effacer-parole lina ; etiquette-retirer ordi ; picto-retirer pieces ; marcher max -1 ; etiquette ensemble "Organisé à deux" 1.6 1.7 ; personnage vendeur "Vendeur" ambre_pale droite ; placer vendeur 3 |
| 3.1+1.4 | donner noe max sac |
| 3.2 | etiquette-retirer ensemble ; marcher noe -2 |
| 3.2+0.3 | parler jade vendeur ; etiquette q "Des questions" 4.0 1.7 |
| 3.3 | etiquette-retirer q ; etiquette sac "Dans un sac" -1.6 1.7 ; prendre max ordinateur |
| 3.3+1.8 | ranger ordinateur sac |
| 3.4 | etiquette-retirer sac ; etiquette ensemble "Partager la revente" 1.6 1.7 ; accent max ; visage max content ; visage jade content |
| 3.5 | etiquette-retirer ensemble ; etiquette rien "Il ne voit rien" 4.8 1.0 |
| 4.1 | etiquette-retirer rien ; etiquette noe "Le sac de Noé" -3.4 1.7 ; accent noe |
| 4.1+2.5 | etiquette noe "Il savait pourquoi" -3.4 1.7 |
| 5.1 | retirer vendeur ; etiquette-retirer noe ; etiquette sac "Une seule main" -1.6 1.7 |
| 5.2 | etiquette-retirer sac ; titre "Qui répond du vol ?" ; visage max inquiet ; visage jade inquiet |
| 5.3 | sous-titre "Et comment ?" |
| 6.1 | effacer-titres ; titre "Deux familles" |
| 6.2 | etiquette auteurs "Auteurs" 0 1.7 |
| 6.3 | etiquette part "Participants" -5.4 1.7 |
| 7.1 | effacer-titres ; etiquette auteurs "Seul ou coauteurs" 0.5 1.7 |
| 7.2 | etiquette part "Instigateur, complice" -4.5 1.7 |
| 8.1 | etiquette-retirer auteurs ; etiquette-retirer part ; repere-liste "Coauteur" "Instigateur" "Complice" |
| 8.2 | accent max |
| 9.1 | scene-vide ; personnage max "Max" turquoise gauche ; personnage jade "Jade" rose centre-gauche ; repere-marquer 1 ambre |
| 9.2 | picto document 2.2 -0.4 ; etiquette art "Pas d'article" 2.2 0.9 |
| 9.3 | arret "ATF 135 IV 152" ; etiquette art "Le Tribunal fédéral" 2.2 0.9 ; picto-retirer document ; picto parlement 2.2 -0.4 |
| 10.1 | etiquette-retirer art ; picto-retirer parlement ; titre "Coauteur" |
| 10.1+2.5 | sous-titre "Intention, rôle déterminant" |
| 10.2 | effacer-titres ; titre "Coauteur" ; case "Décision" |
| 10.2+2 | case "Organisation" |
| 10.2+4 | case "Exécution" |
| 11.1 | sous-titre "Un participant principal" |
| 11.2 | effacer-titres ; titre "Contribution essentielle" ambre |
| 12.1 | cocher 1 vert ; accent max |
| 12.2 | cocher 2 vert |
| 12.3 | cocher 3 vert ; accent jade |
| 13.1 | scene-vide ; article "Art. 139 CP" ; decor rue Électronique ; personnage max "Max" turquoise gauche ; placer max -3 ; personnage jade "Jade" rose droite ; placer jade 4 ; etiquette coaut "Coauteurs du vol" 0.6 1.7 ; repere-marquer 1 vert |
| 13.2 | etiquette main "Seul Max a pris" -4.6 1.0 |
| 13.3 | etiquette-retirer main ; etiquette coaut "L'infraction entière" 0.6 1.7 ; accent jade ; visage jade surpris |
| 14.1 | etiquette-retirer coaut ; bulle max "Ensemble" ; bulle jade "Ensemble" |
| 14.2 | etiquette coaut "Par leurs actes" 0.6 1.7 |
| 15.1 | scene-vide ; article-retirer ; arret-retirer ; repere-marquer 2 ambre ; decor rue Électronique ; personnage lina "Lina" violet gauche ; placer lina -4 ; personnage max "Max" turquoise droite ; placer max 2 |
| 15.2 | etiquette pas "Pas au magasin" -5.0 1.0 |
| 15.3 | rejoindre max lina ; parler lina max ; bulle max "Voler ?" ; visage max surpris |
| 16.1 | article "Art. 24 CP" ; etiquette-retirer pas ; etiquette decide "Décider autrui" -2.0 1.7 |
| 16.1+4 | etiquette decide "Crime ou délit" -2.0 1.7 |
| 16.2 | etiquette instig "L'instigatrice" -5.2 1.0 |
| 17.1 | scene-vide ; arret "ATF 128 IV 11" ; personnage lina "Lina" violet gauche ; personnage max "Max" turquoise centre-droite ; titre "Susciter la décision" |
| 17.2 | effacer-titres ; parler lina max ; parole lina "Je te le rachète" ; jetons lina max |
| 18.1 | effacer-parole lina ; titre "Une occasion ne suffit pas" |
| 18.2 | effacer-titres ; titre "Influence directe" ; accent lina |
| 18.3 | effacer-titres ; titre "Une autre limite" |
| 18.4 | scene-vide ; rembobiner ; decor rue Électronique ; personnage max "Max" turquoise gauche ; placer max -3 ; bulle max "Déjà décidé" ; personnage lina "Lina" violet droite ; placer lina 4 |
| 18.5 | mot-barre "Instigation" 0.6 1.9 ; visage lina surpris ; visage max content |
| 19.1 | scene-vide ; arret-retirer ; personnage lina "Lina" violet gauche ; titre "La sanction" ; repere-marquer 2 vert |
| 19.2 | sous-titre "La peine de l'auteur" ; picto prison 2.2 0.0 |
| 19.3 | sous-titre "Mêmes limites légales" ; accent lina |
| 19.4 | sous-titre "Peine fixée pour chacun" |
| 20.1 | effacer-titres ; article "Art. 24 CP" ; titre "Plus loin encore" |
| 20.2 | effacer-titres ; titre "Tenter de décider, punissable" ; etiquette al2 "Alinéa 2" 0 -1.6 |
| 21.1 | scene-vide ; arret "ATF 128 IV 11" ; personnage homme "Un homme" ambre_pale gauche ; titre "Un cas réel" |
| 21.2 | personnage info "L'informaticien" bleu_clair centre-droite ; etiquette cas "Vingt mille francs" -1.2 2.2 ; jetons homme info |
| 21.3 | effacer-titres ; etiquette cas "Copie d'un CD-ROM" -1.2 2.2 ; picto cd -2.0 -0.5 |
| 22.1 | etiquette-retirer cas ; bulle info "Je me ravise" ; visage info inquiet |
| 22.1+2.5 | picto telephone 3.5 0.0 |
| 22.2 | etiquette cas "Aucun vol" -3.6 2.45 |
| 22.3 | effacer-bulle info ; etiquette-retirer cas ; titre "Tentative d'instigation à vol" ; accent homme ; visage homme triste |
| 23.1 | scene-vide ; arret-retirer ; article-retirer ; repere-marquer 3 ambre ; decor rue Électronique ; personnage noe "Noé" bleu_clair gauche ; placer noe -3 ; personnage max "Max" turquoise droite ; placer max 3 ; etiquette sac "Le sac" -4.8 1.0 ; picto sac -3.85 -1.3 ; tenir noe sac aussitot |
| 23.2 | etiquette ni "Ni l'idée, ni le plan" 0.6 1.7 |
| 23.3 | etiquette ni "Il a aidé" 0.6 1.7 ; accent noe |
| 24.1 | article "Art. 25 CP" ; etiquette ni "Prêter assistance" 0.6 1.7 |
| 24.2 | etiquette ni "Crime ou délit" 0.6 1.7 |
| 24.3 | etiquette sac "Le complice" -4.8 1.0 |
| 25.1 | scene-vide ; arret "ATF 132 IV 49" ; personnage noe "Noé" bleu_clair gauche ; titre "Deux conditions" |
| 25.2 | case "Contribution causale" |
| 25.3 | sous-titre "Sans l'aide, autre déroulement" ; accent noe |
| 26.1 | effacer-titres ; case "Sait et accepte" |
| 26.2 | bulle noe "Pour un vol" ; accent cases |
| 26.3 | scene-vide ; personnage noe "Noé" bleu_clair gauche ; renvoi "vidéo 4" ; titre "Le dol éventuel suffit" |
| 26.4 | effacer-titres ; titre "Les grands traits suffisent" ; picto document 2.2 0.0 |
| 27.1 | scene-vide ; personnage noe "Noé" bleu_clair gauche ; cases "Contribution causale" "Sait et accepte" ; titre "Sac utilisé" ; picto sac -3.2 -0.5 ; tenir noe sac aussitot |
| 27.2 | effacer-titres ; titre "Vol facilité" ; cocher 1 vert |
| 27.3 | effacer-titres ; titre "Noé savait" ; cocher 2 vert |
| 27.4 | accent cases |
| 27.5 | effacer-titres ; titre "Complice du vol" ; repere-marquer 3 vert ; visage noe triste |
| 28.1 | scene-vide ; arret-retirer ; personnage noe "Noé" bleu_clair gauche ; titre "Plus doux" |
| 28.2 | article "Art. 25 CP" ; picto prison 2.0 -0.2 ; etiquette att "Peine atténuée" 2.0 1.1 |
| 29.1 | scene-vide ; article-retirer ; repere-marquer 1 neutre ; repere-marquer 2 neutre ; repere-marquer 3 neutre ; titre "Le piège classique" ; personnage max "Max" turquoise centre |
| 29.2 | effacer-titres ; titre "Seul le voleur est coupable" |
| 29.3 | retirer max ; personnage noe "Noé" bleu_clair centre-gauche ; bulle noe "Un peu aidé" |
| 29.3+1 | visage noe content |
| 29.4 | barrer ; visage noe surpris |
| 30.1 | scene-vide ; personnage jade "Jade" rose gauche ; personnage max "Max" turquoise centre-gauche ; etiquette auteur "Peine de l'auteur" -3.35 -2.0 |
| 30.2 | personnage lina "Lina" violet centre ; etiquette auteur "Peine de l'auteur" -2.25 -2.0 |
| 30.3 | personnage noe "Noé" bleu_clair centre-droite ; etiquette att "Peine atténuée" 2.2 -2.0 |
| 31.1 | scene-vide ; titre "Qui tient l'objet ?" ; personnage max "Max" turquoise gauche |
| 31.2 | barrer |
| 31.2+1.5 | effacer-titres ; titre "Le rôle de chacun" ambre ; personnage lina "Lina" violet centre-droite |
| 32.1 | scene-vide ; titre "Une dernière précision" ; personnage max "Max" turquoise centre-droite |
| 32.2 | arret "ATF 144 IV 265" ; personnage noe "Noé" bleu_clair gauche ; etiquette acc "Dépend de l'auteur" -1.2 0.5 |
| 32.3 | etiquette acc "Accessoires" -1.2 0.5 |
| 32.4 | effacer-titres ; retirer max ; titre "Pas d'infraction, pas de complice" |
| 32.5 | effacer-titres ; etiquette-retirer acc ; article "Art. 105 CP" ; titre "Contravention" ; sous-titre "Si la loi le prévoit" |
| 32.6 | renvoi "vidéo 3" ; accent noe |
| 33.1 | scene-vide ; article-retirer ; arret-retirer ; titre "Retenons" |
| 33.2 | personnage max "Max" turquoise gauche ; personnage jade "Jade" rose centre-gauche ; etiquette r "Rôle déterminant" -3.35 -2.0 |
| 33.3 | etiquette r "Chacun est auteur" -3.35 -2.0 ; repere-marquer 1 vert |
| 33.4 | retirer max ; retirer jade ; personnage lina "Lina" violet centre ; etiquette r "Fait naître la décision" 0 -2.0 |
| 33.5 | etiquette r "Peine de l'auteur" 0 -2.0 ; repere-marquer 2 vert |
| 34.1 | retirer lina ; personnage noe "Noé" bleu_clair centre ; etiquette r "Peine atténuée" 0 -2.0 ; repere-marquer 3 vert |
| 34.2 | etiquette-retirer r ; effacer-titres ; titre "Quel rôle, et quand ?" ; retirer noe ; personnage max "Max" turquoise gauche ; personnage jade "Jade" rose centre-gauche ; personnage lina "Lina" violet centre ; personnage noe "Noé" bleu_clair centre-droite |
| 35.1 | scene-vide ; repere-marquer 1 neutre ; repere-marquer 2 neutre ; repere-marquer 3 neutre ; titre "Une question pour finir" |
| 35.2 | effacer-titres ; decor rue Garage ; personnage paul "Paul" ambre_pale gauche ; placer paul -4 ; personnage ami "L'ami" rose droite ; placer ami 1 ; picto voiture 4.2 -1.5 |
| 35.3 | parler paul ami ; bulle paul "Pour un cambriolage" |
| 35.4 | effacer-bulle paul ; etiquette cambr "Les outils, le trajet" 0.6 1.7 ; picto outils 2.6 -1.6 ; prendre ami outils |
| 35.4+2 | marcher ami 2 |
| 35.4+3.4 | retirer ami ; picto-retirer outils ; picto-deplacer voiture 5.6 -1.5 |
| 35.5 | etiquette cambr "Cambriolage commis" 0.6 1.7 |
| 36.1 | etiquette-retirer cambr ; titre "Quel rôle ?" ; repere-marquer 1 ambre ; repere-marquer 2 ambre ; repere-marquer 3 ambre ; visage paul inquiet |
| 36.2 | effacer-titres ; titre "Quelle peine ?" |
| 36.3 | sous-titre "Votre réponse en commentaire" ; accent paul |
| 37.1 | scene-vide ; repere-retirer ; livre "Code pénal" 0 -0.5 ; titre "L'étude du droit" ; sous-titre "Tout est dans la description" |
| 37.2 | accent titre |
