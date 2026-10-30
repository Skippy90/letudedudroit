# Visuels — Vidéo 2 : Les grands principes du procès pénal

Ce fichier pilote les schémas Manim (`render/manim/video.py`). Vocabulaire des actions : `render/manim/README.md`.

Colonne « Moment » : `ligne.phrase` du script, éventuellement `+secondes`. Plusieurs actions d'un même moment sont séparées par `;`.

Personnages : Nina rose, Tom turquoise, Malik bleu clair (fil rouge) ; le policier ambre pâle.

Écarts assumés avec la colonne « À l'écran » du script, pour rester dans la charte et sous douze mots : les six principes s'affichent en mots courts (« Dignité », « Vérité »…) ; les méthodes interdites (ligne 10) forment une liste sous le titre « Méthodes interdites », sans barrer chaque mot ; le mot « Doute sérieux » (ligne 33) est un titre au-dessus des deux colonnes.

| Moment | Actions |
| --- | --- |
| 1.1 | personnage malik "Malik" bleu_clair droite ; titre "Au poste de police" |
| 1.2 | sous-titre "Depuis deux heures" |
| 1.3 | effacer-titres ; parole malik "Je l'ai acheté" |
| 2.1 | effacer-parole malik ; personnage policier "Le policier" ambre_pale gauche ; parole policier "Avoue, et tu rentres ce soir" |
| 2.1+3 | effacer-parole policier ; parole policier "Sinon, tu dors en cellule" |
| 3.1 | effacer-parole policier ; bulle malik "Je suis fatigué" |
| 3.2 | effacer-bulle malik ; parole malik "D'accord, j'avoue" |
| 3.3 | effacer-parole malik ; titre "Cet aveu vaut-il quelque chose ?" |
| 3.4 | effacer-titres ; titre "Avait-il le droit ?" |
| 4.1 | scene-vide ; titre "Les grands principes" ambre |
| 4.2 | sous-titre "Les règles de base" |
| 4.3 | effacer-titres ; frise ; repere 0.06 "Signalement" ; repere 0.28 "Police" ; repere 0.5 "Instruction" ; repere 0.72 "Clôture" ; repere 0.94 "Tribunal" ; zone 0.06 0.94 ambre |
| 5.1 | scene-vide ; livre "Code de procédure pénale" ; titre "Dès les premiers articles" |
| 5.2 | effacer-titres ; titre "Six principes" |
| 6.1 | livre-retirer ; effacer-titres ; liste "1. Dignité" |
| 6.2 | liste-ajouter "2. Vérité" |
| 6.3 | liste-ajouter "3. Poursuivre" |
| 7.1 | liste-ajouter "4. Accusation" |
| 7.2 | liste-ajouter "5. Innocence" |
| 7.3 | liste-ajouter "6. Pas deux fois" |
| 8.1 | scene-vide ; titre "Principe 1 : la dignité" ambre |
| 8.2 | sous-titre "À tous les stades de la procédure" |
| 8.3 | article "Art. 3 CPP" |
| 9.1 | effacer-titres ; cases "Bonne foi" "Traitement équitable" "Droit d'être entendu" ; cocher 1 vert |
| 9.2 | cocher 2 vert ; cocher 3 vert |
| 10.1 | scene-vide ; titre "Méthodes interdites" |
| 10.2 | liste "Contrainte" "Force" "Menaces" |
| 10.3 | liste-ajouter "Promesses" ; liste-ajouter "Tromperie" |
| 10.4 | article "Art. 140 CPP" |
| 11.1 | sous-titre "Même avec son accord" |
| 12.1 | scene-vide ; personnage policier "Le policier" ambre_pale gauche ; personnage malik "Malik" bleu_clair droite ; titre "Revenons au policier" |
| 12.2 | effacer-titres ; parole policier "Avoue, et tu rentres" |
| 12.3 | titre "Une promesse" |
| 12.4 | effacer-parole policier ; parole policier "Sinon, la cellule" |
| 12.5 | effacer-titres ; titre "Une menace" |
| 12.6 | effacer-parole policier ; effacer-titres ; titre "Les deux sont interdites" ambre |
| 13.1 | scene-vide ; titre "Aveu inexploitable" |
| 13.2 | sous-titre "Preuves inexploitables" ; renvoi "vidéo 15" |
| 14.1 | scene-vide ; article-retirer ; titre "Une autre garantie" |
| 14.2 | personnage malik "Malik" bleu_clair droite ; effacer-titres ; titre "Pas obligé de s'accuser" |
| 14.3 | cases "Se taire" "Ne pas collaborer" ; cocher 1 vert ; cocher 2 vert |
| 14.4 | article "Art. 113 CPP" |
| 15.1 | scene-vide ; titre "Une limite" |
| 15.2 | sous-titre "Mesures de contrainte : il s'y soumet" |
| 15.3 | effacer-titres ; titre "La procédure continue" |
| 16.1 | scene-vide ; article-retirer ; titre "Principe 2 : chercher la vérité" ambre |
| 16.2 | sous-titre "Tous les faits utiles" |
| 16.3 | effacer-titres ; titre "La maxime de l'instruction" |
| 16.4 | article "Art. 6 CPP" |
| 17.1 | scene-vide ; personnage malik "Malik" bleu_clair droite ; titre "Pas à Malik de prouver" |
| 17.2 | personnage nina "Nina" rose gauche ; sous-titre "Ni à Nina" |
| 17.3 | effacer-titres ; titre "Le travail de l'État" |
| 18.1 | scene-vide ; colonnes "À charge" "À décharge" ; titre "Avec un soin égal" |
| 18.2 | effacer-titres ; titre "Chercher aussi le vendeur" ; renvoi "vidéo 1" |
| 19.1 | scene-vide ; article-retirer ; titre "Principe 3 : poursuivre" ambre |
| 19.2 | sous-titre "Les autorités doivent agir" |
| 19.3 | article "Art. 7 CPP" |
| 20.1 | effacer-titres ; titre "Pas de choix libre" |
| 20.2 | sous-titre "Seulement si la loi le prévoit" |
| 21.1 | effacer-titres ; titre "Des exceptions" |
| 21.2 | sous-titre "Renvoi au Code pénal" ; article "Art. 8 CPP" |
| 22.1 | effacer-titres ; titre "Faute et conséquences peu importantes" |
| 22.2 | article "Art. 52 CP" |
| 23.1 | scene-vide ; titre "Le dommage réparé" |
| 23.2 | rembobiner ; personnage malik "Malik" bleu_clair droite ; personnage nina "Nina" rose gauche ; jetons malik nina |
| 23.3 | article "Art. 53 CP" |
| 24.1 | scene-vide ; titre "Conditions strictes" |
| 24.2 | effacer-titres ; cases "Faits admis" "Peine modeste" "Intérêts faibles" ; cocher 1 vert |
| 24.3 | cocher 2 vert ; titre "Un an avec sursis, par exemple" |
| 24.4 | cocher 3 vert |
| 25.1 | scene-vide ; article-retirer ; titre "Principe 4 : l'accusation" ambre |
| 25.2 | sous-titre "Le tribunal juge ce dont il est saisi" |
| 25.3 | effacer-titres ; titre "Un acte d'accusation" ; sous-titre "Des faits précis, une personne déterminée" |
| 25.4 | article "Art. 9 CPP" |
| 26.1 | effacer-titres ; titre "Protéger le prévenu" |
| 26.2 | sous-titre "Savoir ce qu'on lui reproche" |
| 26.3 | effacer-titres ; titre "Lié par les faits de l'accusation" |
| 27.1 | effacer-titres ; titre "Sauf l'ordonnance pénale" ; renvoi "vidéo 1" |
| 28.1 | scene-vide ; article-retirer ; titre "Principe 5 : l'innocence" ambre |
| 28.2 | effacer-titres ; titre "Présumé innocent" ambre ; sous-titre "Jusqu'au jugement entré en force" |
| 28.3 | article "Art. 10 CPP" |
| 29.1 | article "Art. 32 Cst." ; sous-titre "Aussi dans la Constitution" |
| 30.1 | scene-vide ; titre "Entré en force ?" ; frise ; point 0.1 "Jugement" ; point 0.45 "Délai de recours" |
| 30.2 | point 0.85 "Entré en force" ; zone 0.1 0.45 ambre |
| 30.3 | effacer-titres ; titre "Avant : toujours présumé innocent" |
| 31.1 | scene-vide ; titre "Pour le juge" |
| 31.2 | sous-titre "Libre appréciation des preuves" |
| 31.3 | effacer-titres ; titre "Doutes insurmontables" ; sous-titre "La version favorable au prévenu" |
| 31.4 | article "Art. 10 CPP" |
| 32.1 | effacer-titres ; titre "In dubio pro reo" ambre |
| 32.2 | sous-titre "Le doute profite à l'accusé" |
| 33.1 | scene-vide ; titre "Un doute sérieux" ambre |
| 33.2 | colonnes "Simple probabilité" "Certitude absolue" ; colonne-eteindre 1 |
| 33.3 | colonne-eteindre 2 |
| 34.1 | scene-vide ; personnage tom "Tom" turquoise gauche ; personnage malik "Malik" bleu_clair droite ; bulle tom "Un jeune homme" |
| 34.2 | titre "Doute sérieux : pas de vol retenu" |
| 35.1 | scene-vide ; titre "Aussi hors du tribunal" |
| 35.2 | sous-titre "L'information du public" |
| 35.3 | article "Art. 74 CPP" |
| 36.1 | personnage malik "Malik" bleu_clair droite ; effacer-titres ; titre "Le voleur" ; barrer |
| 37.1 | scene-vide ; article-retirer ; titre "Principe 6 : pas deux fois" ambre |
| 37.2 | sous-titre "Condamné ou acquitté, entré en force" |
| 37.3 | effacer-titres ; titre "Plus de poursuite pour la même infraction" |
| 37.4 | article "Art. 11 CPP" |
| 38.1 | effacer-titres ; titre "Ne bis in idem" ambre |
| 38.2 | sous-titre "Pas deux fois pour la même chose" |
| 38.3 | effacer-titres ; titre "Pas de menace permanente" |
| 39.1 | effacer-titres ; titre "Deux cas réservés" |
| 39.2 | cases "Reprise après classement" "Révision" ; cocher 1 question |
| 39.3 | cocher 2 question |
| 39.4 | renvoi "vidéos 22 et 33" |
| 40.1 | scene-vide ; titre "Deux autres règles" |
| 40.2 | sous-titre "Indépendance" ; article "Art. 4 CPP" |
| 40.3 | effacer-titres ; titre "Célérité" ; article "Art. 5 CPP" ; renvoi "vidéo 1" |
| 41.1 | scene-vide ; article-retirer ; titre "Le piège classique" |
| 41.2 | sous-titre "Au moindre doute, tout s'arrête" |
| 42.1 | barrer |
| 42.2 | scene-vide ; titre "Un doute sérieux" ; sous-titre "Pas un doute théorique" |
| 42.3 | effacer-titres ; titre "La règle vise le juge qui tranche" |
| 43.1 | scene-vide ; personnage procureure "La procureure" violet droite ; titre "Le procureur, lui…" |
| 43.2 | effacer-titres ; titre "Classer ou accuser ?" ; sous-titre "En principe : accuser" |
| 44.1 | scene-vide ; titre "Selon le Tribunal fédéral" |
| 44.2 | sous-titre "Classer : punissabilité clairement absente" |
| 44.3 | effacer-titres ; colonnes "Condamnation" "Acquittement" ; titre "Aussi probables : accuser" |
| 45.1 | scene-vide ; titre "In dubio pro duriore" ambre |
| 45.2 | sous-titre "Dans le doute : le procès" |
| 45.3 | effacer-titres ; titre "Puis le tribunal applique le doute" |
| 46.1 | scene-vide ; titre "Retenons" |
| 46.2 | liste "1. Dignité" "2. Vérité" "3. Poursuivre" |
| 46.3 | accent liste |
| 46.4 | liste-ajouter "4. Accusation" ; liste-ajouter "5. Innocence" ; liste-ajouter "6. Pas deux fois" |
| 47.1 | scene-vide ; personnage nina "Nina" rose gauche ; personnage tom "Tom" turquoise centre ; personnage malik "Malik" bleu_clair droite |
| 47.2 | titre "La vérité, sans abus" |
| 48.1 | scene-vide ; titre "Une question pour finir" |
| 48.2 | effacer-titres ; personnage malik "Malik" bleu_clair droite ; titre "Acquitté" |
| 48.3 | sous-titre "Jugement entré en force" |
| 49.1 | scene-vide ; frise ; point 0.1 "Acquittement" ; point 0.5 "6 mois" ; point 0.85 "Nouveau témoin" |
| 49.2 | titre "Un nouveau procès ?" ; questions |
| 49.3 | sous-titre "Votre réponse en commentaire" |
| 50.1 | scene-vide ; titre "Réponse dans la description" |
| 50.2 | effacer-titres ; titre "Prochaine vidéo : les autorités" ; renvoi "vidéo 3" |
| 50.3 | effacer-titres ; titre "L'étude du droit" |
