# Visuels — Vidéo 1 : La carte de la procédure

Ce fichier pilote les schémas Manim (`render/manim/video.py`). Vocabulaire des actions : `render/manim/README.md`.

Colonne « Moment » : `ligne.phrase` du script, éventuellement `+secondes`. Plusieurs actions d'un même moment sont séparées par `;`.

Personnages du fil rouge : Nina rose, Tom turquoise, Malik bleu clair ; la procureure violet.

Écarts assumés avec la colonne « À l'écran » du script, pour rester dans la charte : la carte est une frise du temps à cinq repères (la charte n'a pas d'autre schéma d'étapes) ; dans les sections 1 à 5, l'étape en cours s'affiche en titre plutôt qu'en coloriant son repère ; le scooter n'est pas dessiné ; « Recours » (ligne 7) est un sous-titre.

| Moment | Actions |
| --- | --- |
| 1.1 | titre "L'affaire du scooter" |
| 1.2 | personnage nina "Nina" rose gauche ; dommage nina |
| 1.3 | personnage malik "Malik" bleu_clair droite ; sous-titre "Contrôlé au guidon" |
| 1.4 | parole malik "Je l'ai acheté" |
| 2.1 | scene-vide ; titre "Et maintenant ?" |
| 2.2 | effacer-titres ; titre "Qui va enquêter ?" |
| 2.3 | effacer-titres ; titre "Qui va décider ?" |
| 2.4 | effacer-titres ; titre "Combien de temps ?" |
| 3.1 | effacer-titres ; titre "Il faut une carte" ambre |
| 3.2 | sous-titre "Du début à la fin" |
| 3.3 | effacer-titres ; titre "La carte de la procédure" |
| 3.4 | sous-titre "Chaque étape en détail ensuite" |
| 4.1 | scene-vide ; titre "Cinq étapes" |
| 4.2 | frise |
| 5.1 | repere 0.06 "Signalement" |
| 5.2 | repere 0.28 "Police" |
| 6.1 | repere 0.5 "Instruction" |
| 6.2 | repere 0.72 "Clôture" |
| 7.1 | repere 0.94 "Tribunal" |
| 7.2 | sous-titre "Puis, les recours" |
| 8.1 | effacer-titres ; zone 0.28 0.5 ambre |
| 8.2 | titre "La procédure préliminaire" ambre |
| 8.3 | article "Art. 299 CPP" |
| 9.1 | sous-titre "Avant le procès" |
| 10.1 | scene-vide ; article-retirer ; titre "Étape 1 : le signalement" |
| 11.1 | personnage tom "Tom" turquoise gauche ; sous-titre "Une dénonciation" |
| 11.2 | parole tom "J'ai vu quelque chose" |
| 11.3 | article "Art. 301 CPP" |
| 12.1 | personnage nina "Nina" rose centre ; effacer-titres ; titre "Une plainte" |
| 12.2 | parole nina "On m'a volé mon scooter" ; effacer-parole tom |
| 13.1 | personnage malik "Malik" bleu_clair droite ; effacer-parole nina ; effacer-titres ; titre "L'initiative de la police" |
| 13.2 | sous-titre "Un contrôle" ; article "Art. 15 CPP" |
| 14.1 | scene-vide ; article-retirer ; titre "Une précision importante" |
| 14.2 | effacer-titres ; colonnes "D'office" "Sur plainte" ; colonne-accent 1 |
| 14.3 | titre "Le vol : d'office" |
| 15.1 | colonne-accent 2 ; effacer-titres ; titre "D'autres : sur plainte" |
| 15.2 | renvoi "vidéos 7 et 8" |
| 16.1 | scene-vide ; titre "Étape 2 : la police enquête" |
| 16.2 | sous-titre "Elle établit les faits" |
| 17.1 | effacer-titres ; cases "Traces et preuves" "Interroger" "Arrêter" ; cocher 1 vert |
| 17.2 | cocher 2 vert |
| 17.3 | cocher 3 vert |
| 17.4 | article "Art. 306 CPP" |
| 18.1 | scene-vide ; personnage nina "Nina" rose gauche ; titre "La police entend" |
| 18.2 | personnage tom "Tom" turquoise centre ; bulle tom "Un jeune homme" |
| 18.3 | personnage malik "Malik" bleu_clair droite ; accent malik |
| 19.1 | scene-vide ; personnage malik "Malik" bleu_clair gauche ; titre "Malik : le prévenu" ambre |
| 19.2 | article "Art. 111 CPP" |
| 19.3 | sous-titre "Il a des droits" |
| 19.4 | effacer-titres ; cases "Se taire" "Un avocat" ; cocher 1 vert ; cocher 2 vert |
| 19.5 | article "Art. 158 CPP" |
| 19.6 | renvoi "vidéo 11" |
| 20.1 | scene-vide ; titre "La police n'agit pas seule" |
| 20.2 | sous-titre "Sous les instructions du ministère public" |
| 20.3 | article "Art. 15 CPP" |
| 21.1 | effacer-titres ; titre "Infraction grave : informer sans retard" |
| 21.2 | sous-titre "Rapport et dossier au ministère public" |
| 21.3 | article "Art. 307 CPP" |
| 22.1 | scene-vide ; article-retirer ; titre "Étape 3 : l'instruction" |
| 22.2 | personnage procureure "La procureure" violet gauche ; sous-titre "Conduite par le ministère public" |
| 23.1 | effacer-titres ; titre "Un rôle central" ambre |
| 23.2 | cases "Diriger" "Poursuivre" "Accuser" ; cocher 1 vert ; cocher 2 vert |
| 23.3 | cocher 3 vert |
| 23.4 | article "Art. 16 CPP" |
| 24.1 | scene-vide ; titre "Soupçons suffisants" ; sous-titre "Ouverture de l'instruction" |
| 24.2 | article "Art. 309 CPP" |
| 25.1 | effacer-titres ; titre "Conditions manifestement absentes ?" |
| 25.2 | sous-titre "Non-entrée en matière" |
| 25.3 | article "Art. 310 CPP" |
| 26.1 | scene-vide ; article-retirer ; titre "Établir les faits, les qualifier" |
| 26.2 | effacer-titres ; cases "Entendre" "Réunir les preuves" "Mesures de contrainte" |
| 27.1 | scene-vide ; colonnes "À charge" "À décharge" ; titre "Avec le même soin" |
| 27.2 | article "Art. 6 CPP" |
| 28.1 | scene-vide ; personnage malik "Malik" bleu_clair droite ; bulle malik "Je l'ai acheté" ; titre "Cela aussi doit être vérifié" |
| 29.1 | scene-vide ; article-retirer ; personnage nina "Nina" rose gauche ; titre "Et Nina ?" |
| 29.2 | effacer-titres ; titre "Partie plaignante" ambre |
| 29.3 | cases "Consulter le dossier" "Proposer des preuves" "Demander réparation" |
| 29.4 | article "Art. 118 CPP" |
| 29.5 | renvoi "vidéo 5" |
| 30.1 | scene-vide ; personnage malik "Malik" bleu_clair gauche ; titre "Et une détention ?" |
| 30.2 | effacer-titres ; titre "Tribunal des mesures de contrainte" ; article "Art. 13 CPP" |
| 30.3 | renvoi "vidéo 20" |
| 31.1 | scene-vide ; article-retirer ; titre "Étape 4 : la clôture" |
| 31.2 | sous-titre "Trois issues possibles" |
| 32.1 | effacer-titres ; liste "1. Classement" |
| 32.2 | titre "Pas de soupçon suffisant" |
| 32.3 | article "Art. 319 CPP" |
| 33.1 | effacer-titres ; titre "Comme un acquittement" |
| 34.1 | effacer-titres ; liste-ajouter "2. Ordonnance pénale" ; liste-surligner 2 |
| 34.2 | titre "Condamné sans procès" ; article "Art. 352 CPP" |
| 35.1 | scene-vide ; cases "Faits admis ou établis" "Peine modeste" ; cocher 1 vert |
| 35.2 | cocher 2 vert ; titre "Six mois au plus, par exemple" |
| 36.1 | scene-vide ; liste "1. Classement" "2. Ordonnance pénale" "3. Mise en accusation" ; liste-surligner 3 |
| 36.2 | titre "Soupçons suffisants" |
| 36.3 | sous-titre "Renvoi devant le tribunal" |
| 36.4 | article "Art. 324 CPP" |
| 37.1 | effacer-titres ; titre "Le but de la procédure préliminaire" ; accent liste |
| 37.2 | article "Art. 299 CPP" |
| 38.1 | scene-vide ; article-retirer ; titre "Étape 5 : le procès" |
| 38.2 | sous-titre "Seulement les faits de l'acte d'accusation" |
| 38.3 | article "Art. 9 CPP" |
| 39.1 | scene-vide ; titre "Le tribunal juge" |
| 39.2 | colonnes "Acquittement" "Condamnation" |
| 39.3 | article "Art. 351 CPP" |
| 40.1 | scene-vide ; article-retirer ; titre "Contester le jugement" |
| 40.2 | pyramide ; pyramide-niveau 2 ambre ; sous-titre "L'appel" |
| 40.3 | article "Art. 398 CPP" |
| 41.1 | pyramide-niveau 3 ambre |
| 41.2 | effacer-titres ; titre "Tout un module" |
| 42.1 | scene-vide ; article-retirer ; titre "Combien de temps ?" |
| 42.2 | sous-titre "Pas de durée unique" |
| 42.3 | effacer-titres ; titre "Mais une exigence" |
| 43.1 | effacer-titres ; titre "Sans délai, sans retard injustifié" |
| 43.2 | sous-titre "Célérité" ; article "Art. 5 CPP" |
| 44.1 | effacer-titres ; titre "Détenu : en priorité" ambre |
| 44.2 | sous-titre "Chaque jour compte" |
| 45.1 | scene-vide ; article-retirer ; titre "La prescription" ; frise |
| 45.2 | point 0.05 "Le vol" |
| 45.3 | repere 0.9 "15 ans" ; zone 0.05 0.9 ambre |
| 46.1 | article "Art. 97 CP" |
| 46.2 | renvoi "Droit pénal général, vidéo 12" |
| 47.1 | scene-vide ; article-retirer ; titre "Le piège classique" |
| 47.2 | sous-titre "Toute affaire finit au tribunal" |
| 48.1 | barrer |
| 48.2 | effacer-titres ; titre "Classement ou ordonnance pénale" ; sous-titre "Sans procès" |
| 49.1 | effacer-titres ; titre "Une vraie condamnation" ambre |
| 49.2 | frise ; point 0.1 "Notification" ; repere 0.45 "10 jours" ; zone 0.1 0.45 ambre |
| 49.3 | article "Art. 354 CPP" |
| 50.1 | effacer-titres ; titre "Opposition à temps" ; sous-titre "Le tribunal peut être saisi" |
| 50.2 | effacer-titres ; titre "L'accès à un juge" |
| 50.3 | renvoi "vidéos 23 et 24" |
| 51.1 | scene-vide ; article-retirer ; titre "Retenons" |
| 51.2 | frise ; repere 0.06 "Signalement" ; repere 0.28 "Police" ; repere 0.5 "Instruction" ; repere 0.72 "Clôture" ; repere 0.94 "Tribunal" |
| 52.1 | scene-vide ; personnage procureure "La procureure" violet gauche ; titre "Au centre de tout" |
| 52.2 | liste "Classer" "Ordonnance pénale" "Accuser" |
| 53.1 | scene-vide ; titre "Une question pour finir" |
| 53.2 | effacer-titres ; personnage malik "Malik" bleu_clair gauche ; titre "Une ordonnance pénale" |
| 53.3 | bulle malik "Au tiroir" |
| 54.1 | effacer-titres ; frise ; point 0.1 "Notification" ; point 0.7 "2 semaines" ; questions |
| 54.2 | titre "Encore un procès ?" |
| 55.1 | scene-vide ; titre "Réponse dans la description" |
| 55.2 | effacer-titres ; titre "Prochaine vidéo : les principes" ; renvoi "vidéo 2" |
| 55.3 | effacer-titres ; titre "L'étude du droit" |
