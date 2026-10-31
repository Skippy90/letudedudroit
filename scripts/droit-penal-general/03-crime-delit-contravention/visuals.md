# Visuels — Vidéo 3 : Crime, délit ou contravention ?

Ce fichier pilote les schémas Manim (`render/manim/video.py`). Vocabulaire des actions : `render/manim/README.md`.

Colonne « Moment » : `ligne.phrase` du script, éventuellement `+secondes`. Plusieurs actions d'un même moment sont séparées par `;`.

Personnages : Inès rose, Noah turquoise, Yann bleu clair ; la passante violet, l'ami de Yann ambre pâle.

Style « scène » : les trois cas se jouent dans la rue, chaque personnage revient dans le décor quand on classe son acte, et un pense-bête en haut à droite (« Crime », « Délit », « Contravention ») s'allume en ambre sur la catégorie dont on parle.

Écarts assumés avec la colonne « À l'écran » du script, pour rester dans la charte :

- ligne 3 : pas d'éclair rouge sur le mur (le rouge de la charte se place sur une silhouette) ; le dommage est dit par le texte ;
- lignes 11 à 13 et 17 à 23 : l'échelle des peines utilise la frise horizontale (une durée de peine est une durée) ;
- ligne 32 : pas de pile de jetons ; le plafond de l'amende est écrit.

| Moment | Actions |
| --- | --- |
| 1.1 | decor rue ; etiquette lieu "Neuchâtel, samedi soir" -3.6 1.6 |
| 1.2 | personnage ines "Inès" rose gauche ; placer ines -3 ; personnage noah "Noah" turquoise centre ; placer noah 1 ; personnage yann "Yann" bleu_clair droite ; placer yann 3 |
| 2.1 | etiquette-retirer lieu ; personnage passante "Une passante" violet centre-gauche ; placer passante -1 ; accent ines |
| 2.1@téléphone | picto telephone -0.75 -0.9 |
| 2.2@neuf | etiquette neuf "Un modèle tout neuf" -3.8 1.7 |
| 2.3@éloigne | picto-retirer telephone ; etiquette-retirer neuf ; retirer passante ; marcher ines -4 ; bulle ines "Le garder" |
| 3.1 | effacer-bulle ines ; accent noah |
| 3.1@mur | picto tag 1.3 0.4 |
| 3.2@francs | etiquette prix "Environ 2 000 francs" 0.6 1.7 |
| 4.1 | etiquette-retirer prix ; personnage ami "Un ami" ambre_pale droite ; placer ami 4 |
| 4.1@gifle | pousser yann ami |
| 4.2@blessé | etiquette blesse "Pas blessé" 5.6 1.0 |
| 5.1 | etiquette-retirer blesse ; titre "Trois actes interdits" |
| 5.2@poids | sous-titre "Le même poids ?" |
| 5.3@crime | effacer-titres ; etiquette q1 "Crime ?" -4.4 1.0 |
| 5.4@délit | etiquette q2 "Délit ?" -0.6 1.0 |
| 5.5@contravention | etiquette q3 "Contravention ?" 4.4 1.0 |
| 5.6@intuition | accent ines ; accent noah ; accent yann |
| 6.1 | scene-vide ; batiment ; renvoi "vidéo 1" |
| 6.2@typique | etage 1 vert |
| 6.2@illicite | etage 2 vert |
| 6.2@coupable | etage 3 vert |
| 7.1 | scene-vide ; personnage ines "Inès" rose gauche ; personnage noah "Noah" turquoise centre ; personnage yann "Yann" bleu_clair droite ; titre "Pas toutes égales" |
| 7.2@catégories | titre "Trois catégories" |
| 8.1@crimes | retirer ines ; retirer noah ; retirer yann ; liste-ajouter "1. Crime" ; livre "Code pénal" 3.8 |
| 8.2@délits | liste-ajouter "2. Délit" |
| 8.3@contraventions | liste-ajouter "3. Contravention" |
| 9.1@impression | mot-barre "Impression" -0.2 0.9 |
| 9.2@colère | mot-barre "Colère" -0.2 -0.3 |
| 9.3@règle | effacer-titres ; livre-retirer ; repere-liste "Crime" "Délit" "Contravention" |
| 9.3@loi | titre "Une règle écrite" ambre |
| 10.1 | scene-vide ; livre |
| 10.1@dix | article "Art. 10 CP" |
| 10.2@critère | livre-ouvrir ; titre "Le critère" |
| 10.2@passible | sous-titre "La peine possible" |
| 11.1@lourde | effacer-titres ; titre "La peine la plus lourde" |
| 11.2@gestes | titre "Deux gestes" |
| 11.3@trouve | sous-titre "1. Trouver l'article" ; livre-chercher |
| 11.4@lit | sous-titre "2. Lire la peine maximale" |
| 12.1 | scene-vide ; frise ; repere 0.5 "3 ans" |
| 12.1@plus | repere-marquer 1 ambre ; zone 0.5 1 ambre ; titre "Plus de 3 ans : crime" |
| 13.1@délit | repere-marquer 1 neutre ; repere-marquer 2 ambre |
| 13.1@au | zone 0 0.5 vert ; titre "3 ans au plus : délit" |
| 14.1@article | article "Art. 103 CP" |
| 14.2@contravention | repere-marquer 2 neutre ; repere-marquer 3 ambre ; titre "Amende : contravention" |
| 15.1 | scene-vide ; repere-marquer 3 neutre ; article-retirer ; liste-ajouter "Peine privative de liberté" ; picto prison 2.6 1.0 |
| 15.2@pécuniaire | liste-ajouter "Peine pécuniaire" ; picto pieces 2.6 -0.1 |
| 15.3@amende | liste-ajouter "Amende" ; liste-surligner 3 ; picto pieces:2 2.6 -1.2 |
| 15.4@onze | renvoi "vidéo 11" |
| 16.1 | scene-vide ; decor rue ; personnage ines "Inès" rose gauche ; placer ines -3 |
| 16.2@téléphone | marcher ines -2 ; picto telephone -2.35 -0.9 |
| 16.2@vol | etiquette vol "Un vol" -3.2 1.7 |
| 16.3@article | article "Art. 139 CP" |
| 17.1 | scene-vide ; frise ; repere 0.5 "3 ans" |
| 17.1@cinq | point 0.83 "Vol : 5 ans" |
| 18.1@plus | zone 0.5 1 ambre |
| 18.2@crime | repere-marquer 1 ambre ; titre "Un crime" |
| 19.1 | scene-vide ; repere-marquer 1 neutre ; decor rue ; personnage ines "Inès" rose gauche ; placer ines -2 ; picto telephone -2.35 -0.9 |
| 19.1@neuf | etiquette neuf "Tout neuf" -3.2 1.7 |
| 19.2@faible | etiquette neuf "Faible valeur ?" -4.7 1.7 |
| 19.2@article | article "Art. 172ter CP" |
| 19.2@amende | etiquette amende "Amende, sur plainte" -0.1 1.7 |
| 20.1@contravention | repere-marquer 3 ambre ; titre "Alors : contravention" |
| 20.2@prévue | accent titre |
| 21.1 | scene-vide ; repere-marquer 3 neutre ; article-retirer ; decor rue ; personnage noah "Noah" turquoise centre ; placer noah 2 ; picto tag 1.3 0.4 |
| 21.2@dommage | etiquette dommage "Dommage à la propriété" -2.6 1.7 |
| 21.3@article | article "Art. 144 CP" |
| 22.1 | scene-vide ; frise ; repere 0.5 "3 ans" |
| 22.1@trois | point 0.5 "Au plus" ; zone 0 0.5 vert |
| 22.2@délit | repere-marquer 2 ambre ; titre "Un délit" |
| 22.3@dommage | sous-titre "Tout petit dommage : amende" |
| 23.1@considérable | effacer-titres ; point 0.83 "Considérable : 5 ans" |
| 23.2@crime | titre "Alors : un crime" |
| 24.1 | scene-vide ; repere-marquer 2 neutre ; article-retirer ; decor rue ; personnage yann "Yann" bleu_clair centre ; placer yann 2 ; personnage ami "Un ami" ambre_pale droite ; placer ami 3 |
| 24.2@gifle | pousser yann ami |
| 24.2@voies | etiquette vdf "Voies de fait" 0 1.7 |
| 24.3@article | article "Art. 126 CP" |
| 25.1 | scene-vide ; personnage yann "Yann" bleu_clair gauche |
| 25.1@amende | case "Amende" ; cocher 1 vert |
| 25.2@privative | case "Peine privative de liberté" ; cocher 2 gris |
| 25.3@contravention | repere-marquer 3 ambre ; titre "Une contravention" |
| 25.4@plainte | scene-vide ; personnage yann "Yann" bleu_clair gauche ; personnage noah "Noah" turquoise centre ; titre "Sur plainte" |
| 25.5@noah | accent noah |
| 26.1 | scene-vide ; repere-marquer 3 neutre ; article-retirer ; decor rue ; personnage ines "Inès" rose gauche ; placer ines -3 ; personnage noah "Noah" turquoise centre ; placer noah 0 ; personnage yann "Yann" bleu_clair droite ; placer yann 3 |
| 26.1@crime | etiquette c1 "Crime" -4.8 0.0 ; repere-marquer 1 ambre |
| 26.1@délit | etiquette c2 "Délit" 0 0.0 ; repere-marquer 2 ambre |
| 26.1@contravention | etiquette c3 "Contravention" 4.8 0.0 ; repere-marquer 3 ambre |
| 26.2@rue | etiquette lieu "Même rue" -2.6 2.45 |
| 26.3@niveaux | accent ines ; accent noah ; accent yann |
| 27.1 | scene-vide ; repere-marquer 1 neutre ; repere-marquer 2 neutre ; repere-marquer 3 neutre ; personnage ines "Inès" rose gauche ; personnage noah "Noah" turquoise centre-gauche ; personnage yann "Yann" bleu_clair centre ; titre "Pas qu'une étiquette" |
| 27.2@différemment | sous-titre "Des règles différentes" |
| 28.1@tentative | retirer ines ; retirer noah ; retirer yann ; effacer-titres ; titre "1. La tentative" |
| 28.2 | effacer-titres ; decor rue ; personnage yann "Yann" bleu_clair centre-droite ; placer yann 1 ; personnage ami "Un ami" ambre_pale droite ; placer ami 3 |
| 28.2@essayé | bulle yann "Une gifle ?" |
| 28.2@toucher | marcher yann 2 |
| 29.1@contravention | effacer-bulle yann ; repere-marquer 3 ambre ; etiquette tentative "Tentative" 1.6 1.0 |
| 29.1@expressément | etiquette loi "Seulement si prévu" -2.6 2.45 |
| 29.2@article | article "Art. 105 CP" |
| 30.1@rien | etiquette-retirer loi ; etiquette tentative "Rien pour les voies de fait" -0.8 1.7 |
| 30.2@puni | scene-vide ; personnage yann "Yann" bleu_clair centre ; titre "Yann : pas puni" |
| 30.3@crimes | sous-titre "Crimes et délits : autrement" |
| 30.4@neuf | renvoi "vidéo 9" |
| 31.1 | scene-vide ; titre "2. Pas de sursis" ; picto prison 0 0.2 |
| 31.1@contraventions | sous-titre "pour les contraventions" |
| 31.2@sursis | effacer-titres ; picto-retirer prison ; personnage yann "Yann" bleu_clair gauche ; bulle yann "Se tenir tranquille" ; renvoi "vidéo 11" |
| 32.1 | scene-vide ; titre "3. Un plafond" ; picto pieces 0 0.3 |
| 32.2@dix | sous-titre "Dix mille francs au plus" |
| 32.3@article | article "Art. 106 CP" ; accent titre |
| 33.1 | scene-vide ; article-retirer ; titre "La prescription" |
| 33.2@délai | frise |
| 34.1@contravention | repere-marquer 3 ambre |
| 34.1@ans | repere 0.15 "3 ans" ; point 0.15 "Yann" |
| 34.2@article | article "Art. 109 CP" |
| 35.1@noah | repere-marquer 3 neutre ; repere-marquer 2 ambre |
| 35.1@ans | repere 0.5 "10 ans" ; point 0.5 "Noah" |
| 35.2@inès | repere-marquer 2 neutre ; repere-marquer 1 ambre |
| 35.2@ans | repere 0.75 "15 ans" ; point 0.75 "Inès" |
| 35.3@article | article "Art. 97 CP" |
| 35.4@grave | accent frise ; renvoi "vidéo 12" |
| 36.1 | scene-vide ; repere-marquer 1 neutre ; article-retirer ; titre "Le piège classique" ; personnage juge "Juge" turquoise gauche |
| 36.2@prononcée | sous-titre "La peine prononcée décide" |
| 36.3@faux | barrer |
| 37.1 | scene-vide ; rembobiner ; decor rue ; personnage ines "Inès" rose gauche ; placer ines -2 |
| 37.1@pécuniaire | etiquette prononcee "Peine pécuniaire" -3.2 1.7 |
| 37.2@crime | repere-marquer 1 ambre ; titre "Son vol reste un crime" |
| 38.1 | scene-vide ; colonnes "Prévue" "Prononcée" ; picto parlement -3.5 -0.6 ; picto document 3.5 -0.6 |
| 38.1@maximum | colonne-accent 1 |
| 38.2@juge | colonne-eteindre 2 |
| 39.1@passible | article "Art. 10 CP" ; titre "« passible »" ambre |
| 39.2@possible | sous-titre "La peine possible" |
| 40.1 | scene-vide ; repere-retirer ; article-retirer ; titre "Retenons" ; frise bas ; repere 0.5 "3 ans" |
| 40.2@crime | effacer-titres ; liste-ajouter "Plus de 3 ans : crime" ; zone 0.5 1 ambre |
| 41.1@délit | liste-ajouter "3 ans au plus : délit" ; zone 0 0.5 vert |
| 41.2@contravention | liste-ajouter "Amende : contravention" |
| 42.1 | scene-vide ; titre "La catégorie change" ; personnage ines "Inès" rose gauche |
| 42.1@tentative | effacer-titres ; case "Tentative" |
| 42.1@sursis | case "Sursis" |
| 42.1@prescription | case "Prescription" |
| 42.2@réflexe | titre "Le réflexe" |
| 42.3 | sous-titre "Trouver l'article, lire la peine" |
| 43.1 | scene-vide ; titre "Une question pour finir" |
| 43.2 | sous-titre "Seulement une peine pécuniaire" ; picto pieces -4.0 0.3 |
| 43.3 | cases "Crime" "Délit" "Contravention" ; cocher 1 question ; cocher 2 question ; cocher 3 question |
| 43.4@commentaire | accent cases |
| 44.1 | scene-vide ; livre ; titre "L'étude du droit" ; sous-titre "Tout est dans la description" |
| 44.2 | accent titre |
