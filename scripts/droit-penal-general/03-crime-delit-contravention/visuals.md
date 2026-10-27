# Visuels — Vidéo 3 : Crime, délit ou contravention ?

Ce fichier pilote les schémas Manim (`render/manim/video.py`). Vocabulaire des actions : `render/manim/README.md`.

Colonne « Moment » : `ligne.phrase` du script, éventuellement `+secondes`. Plusieurs actions d'un même moment sont séparées par `;`.

Personnages : Inès rose, Noah turquoise, Yann bleu clair.

Écarts assumés avec la colonne « À l'écran » du script, pour rester dans la charte :

- ligne 3 : pas d'éclair rouge sur le mur (le rouge de la charte se place sur une silhouette) ; le dommage est dit par le texte ;
- lignes 11 à 13 et 17 à 23 : l'échelle des peines utilise la frise horizontale (une durée de peine est une durée) ;
- ligne 32 : pas de pile de jetons ; le plafond de l'amende est écrit.

| Moment | Actions |
| --- | --- |
| 1.1 | titre "Samedi soir, à Neuchâtel" |
| 1.2 | personnage ines "Inès" rose gauche ; personnage noah "Noah" turquoise centre ; personnage yann "Yann" bleu_clair droite |
| 2.1 | effacer-titres ; accent ines |
| 2.2 | bulle ines "Un téléphone neuf" |
| 2.3 | bulle ines "Le garder" |
| 3.1 | effacer-bulle ines ; accent noah ; titre "Un tag" |
| 3.2 | sous-titre "Quelques dizaines de francs" |
| 4.1 | effacer-titres ; accent yann ; titre "Une gifle" |
| 4.2 | sous-titre "Personne n'est blessé" |
| 5.1 | scene-vide ; titre "Trois actes interdits" |
| 5.2 | sous-titre "Le même poids ?" |
| 5.3 | effacer-titres ; case "Crime ?" |
| 5.4 | case "Délit ?" |
| 5.5 | case "Contravention ?" |
| 5.6 | accent cases |
| 6.1 | scene-vide ; batiment ; renvoi "vidéo 1" |
| 6.2 | etage 1 vert ; etage 2 vert ; etage 3 vert |
| 7.1 | scene-vide ; titre "Pas toutes égales" |
| 7.2 | titre "Trois catégories" |
| 8.1 | liste-ajouter "1. Crime" |
| 8.2 | liste-ajouter "2. Délit" |
| 8.3 | liste-ajouter "3. Contravention" |
| 9.1 | mot-barre "Impression" |
| 9.2 | mot-barre "Colère" |
| 9.3 | titre "Une règle écrite" ambre |
| 10.1 | scene-vide ; article "Art. 10 CP" ; titre "Le critère" |
| 10.2 | sous-titre "La peine dont l'infraction est passible" |
| 11.1 | effacer-titres ; frise |
| 11.2 | titre "Deux gestes" |
| 11.3 | sous-titre "1. Trouver l'article" |
| 11.4 | sous-titre "2. Lire la peine maximale" |
| 12.1 | effacer-titres ; repere 0.5 "3 ans" ; zone 0.5 1 ambre ; titre "Plus de 3 ans : crime" |
| 13.1 | zone 0 0.5 vert ; titre "3 ans au plus : délit" |
| 14.1 | article "Art. 103 CP" |
| 14.2 | titre "Amende : contravention" |
| 15.1 | scene-vide ; article-retirer ; liste-ajouter "Peine privative de liberté" |
| 15.2 | liste-ajouter "Peine pécuniaire" |
| 15.3 | liste-ajouter "Amende" ; liste-surligner 3 |
| 15.4 | renvoi "vidéo 11" |
| 16.1 | scene-vide ; personnage ines "Inès" rose gauche |
| 16.2 | titre "Un vol" |
| 16.3 | article "Art. 139 CP" |
| 17.1 | frise ; repere 0.5 "3 ans" ; point 0.83 "5 ans" |
| 18.1 | zone 0.5 1 ambre |
| 18.2 | titre "Un crime" |
| 19.1 | scene-vide ; rembobiner ; titre "Un téléphone neuf" |
| 19.2 | article "Art. 172ter CP" ; titre "Faible valeur ?" |
| 20.1 | sous-titre "Amende : contravention" |
| 20.2 | accent titre |
| 21.1 | scene-vide ; article-retirer ; personnage noah "Noah" turquoise gauche |
| 21.2 | titre "Dommage à la propriété" |
| 21.3 | article "Art. 144 CP" |
| 22.1 | frise ; repere 0.5 "3 ans" ; point 0.5 "Au plus" |
| 22.2 | zone 0 0.5 vert ; titre "Un délit" |
| 23.1 | point 0.83 "Considérable : 5 ans" |
| 23.2 | sous-titre "Alors : un crime" |
| 24.1 | scene-vide ; article-retirer ; personnage yann "Yann" bleu_clair gauche |
| 24.2 | titre "Des voies de fait" |
| 24.3 | article "Art. 126 CP" |
| 25.1 | case "Amende" ; cocher 1 vert |
| 25.2 | case "Peine privative de liberté" ; cocher 2 gris |
| 25.3 | sous-titre "Une contravention" |
| 25.4 | effacer-titres ; titre "Sur plainte" |
| 25.5 | accent titre |
| 26.1 | scene-vide ; article-retirer ; personnage ines "Inès" rose gauche ; personnage noah "Noah" turquoise centre ; personnage yann "Yann" bleu_clair droite |
| 26.2 | titre "Crime, délit, contravention" |
| 26.3 | sous-titre "Trois niveaux" |
| 27.1 | scene-vide ; titre "Pourquoi c'est important" |
| 27.2 | sous-titre "Des règles différentes" |
| 28.1 | effacer-titres ; titre "La tentative" |
| 28.2 | rembobiner ; personnage yann "Yann" bleu_clair gauche ; bulle yann "Une gifle ?" |
| 29.1 | article "Art. 105 CP" ; mot-barre "Tentative" |
| 29.2 | accent titre |
| 30.1 | sous-titre "Rien pour les voies de fait" |
| 30.2 | scene-vide ; titre "Yann ne serait pas puni" |
| 30.3 | sous-titre "Crimes et délits : autrement" |
| 30.4 | renvoi "vidéo 9" |
| 31.1 | scene-vide ; titre "Pas de sursis" ; sous-titre "pour les contraventions" |
| 31.2 | renvoi "vidéo 11" |
| 32.1 | article "Art. 106 CP" ; titre "Un plafond" |
| 32.2 | sous-titre "Dix mille francs au plus" |
| 32.3 | accent titre |
| 33.1 | scene-vide ; article-retirer ; titre "La prescription" |
| 33.2 | frise |
| 34.1 | repere 0.15 "3 ans" |
| 34.2 | article "Art. 109 CP" ; point 0.15 "Contravention" |
| 35.1 | repere 0.5 "10 ans" ; point 0.5 "Délit" |
| 35.2 | repere 0.75 "15 ans" ; point 0.75 "Vol" |
| 35.3 | article "Art. 97 CP" |
| 35.4 | renvoi "vidéo 12" |
| 36.1 | scene-vide ; article-retirer ; titre "Le piège classique" |
| 36.2 | sous-titre "La peine prononcée décide" |
| 36.3 | barrer |
| 37.1 | scene-vide ; rembobiner ; personnage ines "Inès" rose gauche ; case "Crime" |
| 37.2 | cocher 1 vert ; titre "Toujours un crime" |
| 38.1 | scene-vide ; colonnes "Prévue" "Prononcée" |
| 38.2 | colonne-accent 1 ; colonne-eteindre 2 |
| 39.1 | article "Art. 10 CP" ; titre "« passible »" ambre |
| 39.2 | sous-titre "La peine possible" |
| 40.1 | scene-vide ; article-retirer ; titre "Retenons" |
| 40.2 | liste-ajouter "Plus de 3 ans : crime" |
| 41.1 | liste-ajouter "3 ans au plus : délit" |
| 41.2 | liste-ajouter "Amende : contravention" |
| 42.1 | scene-vide ; cases "Tentative" "Sursis" "Prescription" |
| 42.2 | titre "Le réflexe" |
| 42.3 | sous-titre "Trouver l'article, lire la peine" |
| 43.1 | scene-vide ; titre "Une question pour finir" |
| 43.2 | sous-titre "Seulement une peine pécuniaire" |
| 43.3 | cases "Crime" "Délit" "Contravention" ; cocher 1 question ; cocher 2 question ; cocher 3 question |
| 43.4 | accent cases |
| 44.1 | scene-vide ; titre "L'étude du droit" ; sous-titre "Script et articles sur GitHub" |
| 44.2 | accent titre |
