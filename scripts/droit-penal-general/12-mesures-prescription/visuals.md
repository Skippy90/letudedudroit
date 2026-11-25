# Visuels — Vidéo 12 : Quand la justice ne poursuit plus

Ce fichier pilote les schémas Manim (`render/manim/video.py`). Vocabulaire des actions : `render/manim/README.md`.

Colonne « Moment » : `ligne.phrase` du script, éventuellement `+secondes` ou `@mot` (mot tel que la transcription de la narration l'a reconnu). Plusieurs actions d'un même moment sont séparées par `;`.

Personnages (bonshommes en bâtons ; poses, visages et objets aux moments marqués) : Théo turquoise et l'agent de sécurité bleu clair (vidéo 8), Noah turquoise (vidéo 3) — Théo et Noah ne sont jamais à l'écran ensemble —, le juge rose et l'expert ambre pâle (comme dans la vidéo 8), Lina violet ; seconds rôles : l'auteur des exemples bleu clair, la victime de la plainte ambre pâle, le passant ambre pâle et son amie rose (le piège).

Style « scène » (repris le 1er novembre 2026, enrichi le 9 novembre 2026 sur le modèle des vidéos 10 et 11) : Théo revient au festival près de Nyon, le soir (décor festival de la vidéo 8) : il pousse l'agent, puis repart ; Noah revient dans la rue de Neuchâtel, le samedi soir (décor rue de la vidéo 3), devant le mur de la boulangerie couvert de son tag. Les questions sur Théo se posent au tribunal. Un pense-bête « Mesure / Prescription » en haut à droite s'allume sur l'outil dont on parle ; les délais se dessinent sur des frises (cinq ans plus cinq, les délais de l'article 97, dix ans contre onze pour Noah, trois mois pour la plainte, douze ans pour Lina).

Objets et actions (9 novembre 2026) : le rapport d'expertise que l'expert remet au juge (ligne 9) ; le cadenas de la privation de liberté, qui disparaît quand la mesure est levée (lignes 9 et 32) et qu'on barre pour le traitement ambulatoire (ligne 14) ; l'établissement adapté (ligne 12) ; le sablier du délai, qui avance le long de la frise (lignes 23 et 34) et qu'on barre quand la prescription ne court plus (lignes 25 et 26) ; la loupe de la poursuite, barrée quand l'État ne peut plus poursuivre (lignes 18, 24 et 31) ; la plainte que tient la victime (ligne 25) ; le vélo que Lina prend et emporte (ligne 35). Signes constants : `danger` pour le danger, `coeur` pour le besoin de soins, `prison` pour la peine privative de liberté, `foule` pour la société.

Traitement sobre : la crise psychotique est dite par une étiquette ; l'agent est poussé, sans chute ni blessure ; les infractions graves (meurtre, viol, brigandage) et les crimes imprescriptibles (génocide, crimes sexuels sur des enfants) ne sont que du texte.

Écarts assumés avec la colonne « À l'écran » du script, pour rester dans la charte : le bâtiment de la ligne 2 est le petit bâtiment repère en haut à droite (étage « Culpabilité » gris) ; la proportionnalité (ligne 8) est une balance entre l'atteinte et le risque plutôt que deux colonnes ; « Expertise » (ligne 9) est un document remis au juge ; la ligne 17 montre les conditions en cases plutôt qu'une case « Traitement institutionnel » ; pas de barrière devant le bâtiment (ligne 31) : un point d'interrogation sur la culpabilité, le tag toujours illicite, la loupe barrée.

| Moment | Actions |
| --- | --- |
| 1.1 | titre "Deux histoires pour finir" ; livre "Code pénal" 0 -0.5 |
| 1.2 | scene-vide ; decor festival ; etiquette lieu "Près de Nyon, un soir" -3.6 1.7 ; renvoi "vidéo 8" |
| 1.3 | personnage theo "Théo" turquoise gauche ; placer theo -3 ; personnage agent "L'agent" bleu_clair droite ; placer agent 1 |
| 1.3+0.6 | marcher theo -1 |
| 1.3@poussé | pousser theo agent |
| 1.3@psychotique | etiquette lieu "Crise psychotique" -2.6 2.1 |
| 2.1 | repere-batiment ; repere-etage 1 vert ; repere-etage 2 vert |
| 2.1@irresponsable | repere-etage 3 gris |
| 2.1@punissable | picto prison -5.6 1.3 |
| 2.1+2.1 | interdit prison |
| 2.2 | etiquette-retirer lieu ; titre "Le laisser repartir ?" ; visage agent inquiet |
| 2.2@laisser | marcher theo -4 |
| 3.1 | scene-vide ; repere-retirer ; decor rue ; etiquette lieu "Neuchâtel, samedi soir" -3.6 1.7 ; personnage noah "Noah" turquoise centre-droite ; placer noah 2 ; renvoi "vidéo 3" |
| 3.2 | accent noah |
| 3.2@mur | picto tag 0.5 -0.05 1.5 |
| 3.2+2.2 | etiquette-retirer lieu ; marcher noah -3 |
| 3.3@onze | etiquette onze "Onze ans plus tard" 3.6 1.7 |
| 4.1 | scene-vide ; frise ; point 0.03 "Le tag" ; picto tag -5.3 0.7 |
| 4.1@poursuivre | point 0.95 "Découverte" ; repere 0.95 "11 ans" |
| 4.1@temps | titre "Encore poursuivable ?" |
| 4.2 | scene-vide ; repere-liste "Mesure" "Prescription" ; colonnes "La mesure" "La prescription" |
| 4.2@mesure | colonne-accent 1 ; repere-marquer 1 ambre ; picto danger -3.5 -1.3 |
| 4.2@prescription | colonne-accent 2 ; repere-marquer 2 ambre ; picto sablier 3.5 -1.3 |
| 5.1 | scene-vide ; repere-marquer 2 neutre ; renvoi "vidéo 8" ; personnage theo "Théo" turquoise centre |
| 5.2@peine | picto prison -3.6 0.6 ; tourner theo gauche |
| 5.2@faute | etiquette peine "Peine : la faute" -3.6 -0.7 |
| 5.3@mesure | tourner theo droite ; picto danger 3.0 0.6 |
| 5.3@danger | etiquette mesure "Mesure : un danger" 3.7 -0.7 |
| 5.3@soins | picto coeur 4.6 0.6 ; etiquette mesure "Mesure : danger ou soins" 3.7 -0.7 |
| 6.1 | scene-vide ; article "Art. 56 CP" ; titre "Trois conditions" ; livre "Code pénal" -3.8 |
| 6.1@nécessaires | livre-ouvrir |
| 6.2 | livre-retirer ; case "Peine insuffisante" ; picto prison -4.6 0.9 |
| 6.2@danger | picto danger -2.6 0.9 |
| 7.1 | case "Traitement ou sécurité" |
| 7.1@traitement | picto coeur -4.6 -0.6 |
| 7.1@sécurité | foule public -2.6 -0.5 6 3 |
| 7.2 | effacer-titres ; picto-retirer prison ; picto-retirer danger ; picto-retirer coeur ; picto-retirer public ; case "Mesure précise remplie" ; livre "Code pénal" -3.8 |
| 7.2@remplies | cocher 1 vert ; cocher 2 vert ; cocher 3 vert |
| 8.1 | scene-vide ; titre "Proportionnée" ; picto balance 0 0.5 1.5 |
| 8.2 | personnage auteur "L'auteur" bleu_clair gauche ; picto cadenas -2.4 0.6 |
| 8.2@personne | etiquette atteinte "L'atteinte" -2.4 1.7 |
| 8.2+2.4 | etiquette atteinte "Pas excessive" -2.4 1.7 |
| 8.3@risque | picto danger 2.8 0.6 ; etiquette risque "Risque de récidive" 2.8 1.7 |
| 8.3@gravité | etiquette risque "Récidive et gravité" 2.8 1.7 |
| 9.1 | scene-vide ; article-retirer ; decor tribunal ; personnage juge "Le juge" rose droite ; placer juge 1.5 ; personnage expert "L'expert" ambre_pale gauche ; placer expert -3.5 ; picto document -5.3 -1.6 ; tenir expert document aussitot |
| 9.1+0.6 | marcher expert 0.5 |
| 9.1@fonde | donner expert juge document |
| 9.2 | scene-vide ; article "Art. 56 CP" ; personnage auteur "L'auteur" bleu_clair gauche ; picto cadenas -2.4 0.6 ; etiquette cond "Conditions plus remplies" 2.4 1.0 |
| 9.2@levée | picto-retirer cadenas ; visage auteur content ; etiquette cond "Mesure levée" 2.4 1.0 |
| 10.1 | scene-vide ; article-retirer ; repere-marquer 1 ambre ; titre "Plusieurs mesures" ; livre "Code pénal" 4.5 |
| 10.1+1.2 | livre-ouvrir |
| 10.2 | liste "1. Traitement institutionnel" "2. Traitement ambulatoire" "3. Internement" |
| 10.2@principales | accent liste |
| 11.1 | effacer-titres ; liste-surligner 1 ; article "Art. 59 CP" |
| 11.2 | livre-retirer ; personnage auteur "L'auteur" bleu_clair droite |
| 11.2@grave | etiquette trouble "Grave trouble mental" 4.3 -1.8 ; visage auteur triste |
| 12.1 | scene-vide ; personnage auteur "L'auteur" bleu_clair gauche ; visage auteur triste |
| 12.1@liée | case "Lien avec le trouble" |
| 12.1@détourner | case "Éviter la récidive" |
| 12.2 | scene-vide ; personnage auteur "L'auteur" bleu_clair gauche ; picto maison 2.0 0.4 1.8 |
| 12.2@établissement | etiquette lieu "Établissement adapté" 2.0 -1.2 ; deplacer auteur centre-gauche |
| 12.2@adapté | picto coeur 3.7 1.3 0.7 |
| 13.1 | scene-vide ; titre "Privation de liberté" ; frise ; point 0.05 "Début" ; picto cadenas -5.4 0.6 |
| 13.1@cinq | repere 0.45 "5 ans" ; zone 0.05 0.45 ambre |
| 13.2@juge | picto marteau 0.2 0.6 |
| 13.2@prolonger | zone 0.45 0.85 gris |
| 13.2@cinq | repere 0.85 "+ 5 ans" |
| 13.2@risque | picto danger 4.2 0.6 ; etiquette risque "Si le risque demeure" 4.2 1.7 |
| 14.1 | scene-vide ; article "Art. 63 CP" ; liste "1. Traitement institutionnel" "2. Traitement ambulatoire" "3. Internement" ; liste-surligner 2 ; personnage auteur "L'auteur" bleu_clair droite |
| 14.2 | accent auteur |
| 14.2@troubles | etiquette trouble "Troubles mentaux" 0.6 2.3 |
| 14.2@addictions | etiquette trouble "Troubles, addictions" 0.6 2.3 ; picto bouteille 2.6 -0.4 1.5 |
| 14.3 | picto-retirer bouteille |
| 14.3@soigné | picto coeur 2.6 1.0 ; visage auteur content |
| 14.3@enfermé | picto cadenas 2.6 -0.5 |
| 14.3+2.9 | interdit cadenas |
| 15.1 | retirer auteur ; picto-retirer coeur ; picto-retirer cadenas ; etiquette-retirer trouble ; article "Art. 64 CP" ; liste-surligner 3 |
| 15.1+1 | picto cadenas 3.8 0.4 1.4 |
| 15.2 | etiquette lourde "La plus lourde" 3.8 1.7 |
| 15.3@grave | etiquette lourde "Infraction grave" 3.8 1.7 |
| 15.3@meurtre | etiquette ex "Meurtre, viol, brigandage" 3.8 -1.2 |
| 16.1 | scene-vide ; personnage auteur "L'auteur" bleu_clair gauche |
| 16.1@risque | picto danger -2.0 0.6 |
| 16.1@sérieux | etiquette serieux "Risque sérieux" 2.4 1.0 |
| 16.1@genre | etiquette genre "Du même genre" 2.4 0.0 |
| 16.2@conditions | etiquette-retirer genre ; picto document 2.4 -0.6 ; etiquette serieux "Conditions précises" 2.4 1.0 |
| 16.3 | scene-vide ; frise ; picto prison -3.3 0.6 |
| 16.3@exécutée | zone 0.05 0.5 gris ; point 0.27 "Peine" |
| 16.4 | zone 0.5 0.95 ambre ; point 0.72 "Internement" ; picto cadenas 2.6 0.6 |
| 16.4@protéger | foule societe 5.3 0.9 6 3 |
| 17.1 | scene-vide ; article-retirer ; decor tribunal ; personnage theo "Théo" turquoise gauche ; placer theo -0.3 ; personnage juge "Le juge" rose droite ; placer juge 3 ; renvoi "vidéo 8" |
| 17.1@institutionnel | titre "Traitement institutionnel ?" ; parler juge |
| 17.2@psychotique | etiquette crise "Crise psychotique" -4.0 1.5 |
| 17.2@prouve | effacer-titres ; etiquette crise "Une crise ne suffit pas" -3.4 1.5 ; visage theo inquiet |
| 17.3 | scene-vide ; personnage theo "Théo" turquoise gauche ; picto document -2.2 0.9 |
| 17.3@expertise | picto loupe -2.2 -0.4 |
| 17.3@trouble | case "Grave trouble mental" |
| 17.3@lié | case "Lié à l'acte" |
| 17.3@risque | case "Récidive" |
| 17.3@soins | case "Soins utiles" |
| 18.1 | scene-vide ; repere-marquer 1 neutre ; repere-marquer 2 ambre ; decor rue ; personnage noah "Noah" turquoise droite ; placer noah 3.5 ; picto tag 0.5 -0.05 1.5 |
| 18.2 | etiquette presc "La prescription" -3.6 1.7 |
| 18.2@délai | picto sablier -2.6 -0.3 |
| 18.2@poursuivre | picto loupe -2.6 -1.6 |
| 18.2@auteur | interdit loupe |
| 19.1 | etiquette-retirer presc ; picto-retirer sablier ; picto-retirer loupe ; etiquette e "Pourquoi une telle règle ?" -3.0 1.7 |
| 19.2 | etiquette-retirer e |
| 19.2@profs | picto document -2.6 -0.8 ; etiquette e "Preuves perdues" -3.6 1.7 |
| 19.2@perdent | interdit document |
| 19.2@souvenirs | etiquette e "Souvenirs effacés" -3.6 1.7 ; bulle noah "Ce soir-là ?" |
| 19.2@punir | effacer-bulle noah ; etiquette e "Moins besoin de punir" -3.6 1.7 |
| 20.1 | scene-vide ; article "Art. 97 CP" ; frise |
| 20.1@peine | titre "Selon la peine maximale" |
| 20.2 | repere 0.95 "30 ans" |
| 20.2@maximale | picto prison 5.4 0.6 |
| 20.2@vie | etiquette pm "Prison à vie" 5.0 -0.5 |
| 21.1 | effacer-titres ; repere 0.62 "15 ans" |
| 21.1@dépasse | etiquette pm "Plus de 3 ans" 1.44 -0.5 |
| 21.2 | repere 0.44 "10 ans" |
| 21.2@trois | etiquette pm "Peine de 3 ans" -0.72 -0.5 |
| 21.3 | repere 0.27 "7 ans" |
| 21.3@autre | etiquette pm "Autre peine" -2.76 -0.5 |
| 22.1 | repere 0.1 "3 ans" |
| 22.1@contraventions | etiquette pm "Contraventions" -4.6 -0.5 |
| 22.1@vidéo | renvoi "vidéo 3" |
| 23.1 | scene-vide ; frise ; titre "Dès l'acte" ; picto sablier -5.4 0.7 |
| 23.1@jour | point 0.05 "L'acte" |
| 23.1@agi | picto-deplacer sablier 0 0.7 |
| 23.2 | article "Art. 98 CP" |
| 24.1 | scene-vide ; article-retirer ; decor rue ; personnage noah "Noah" turquoise droite ; placer noah 3.5 ; picto tag 0.5 -0.05 1.5 |
| 24.1@coûterait | bulle noah "Environ 2000 francs" |
| 24.2 | effacer-bulle noah ; etiquette e "Pas de moindre importance" -3.0 1.7 |
| 24.3 | etiquette e "Dommage à la propriété" -3.0 1.7 ; article "Art. 144 CP" |
| 24.3@trois | picto prison -2.6 -0.6 ; etiquette p "3 ans au plus" -2.6 0.7 |
| 24.4 | picto-retirer prison ; picto sablier -2.6 -0.6 |
| 24.4@dix | etiquette p "Délai : 10 ans" -2.6 0.7 |
| 24.5 | scene-vide ; frise ; point 0.03 "Le tag" ; picto tag -5.0 0.7 ; repere 0.86 "10 ans" |
| 24.5@onze | point 0.943 "Découverte" ; etiquette onze "11 ans plus tard" 4.9 0.8 |
| 24.5@prescrit | zone 0.86 1 gris ; titre "Prescrit" ambre |
| 24.6 | picto loupe 0.2 0.8 |
| 24.6@poursuivie | interdit loupe |
| 25.1 | scene-vide ; article-retirer ; decor tribunal ; personnage juge "Le juge" rose droite ; placer juge 3 ; titre "Une règle importante" |
| 25.2 | effacer-titres ; accent juge |
| 25.2@jugement | parler juge ; etiquette j "Jugement de première instance" -2.4 1.7 |
| 25.2@prescription | picto sablier -2.4 0.2 |
| 25.2@plus | interdit sablier |
| 25.3 | etiquette j "Appel : plus de prescription" -2.4 1.7 |
| 25.3@acquérir | accent juge |
| 25.4 | scene-vide ; titre "Autre délai : la plainte" |
| 25.4@confondre | personnage victime "La victime" ambre_pale centre-droite haut |
| 25.4@plainte | picto document 1.4 0.4 1.4 ; tenir victime document |
| 25.5 | frise ; point 0.1 "Connaît l'auteur" |
| 25.5@trois | repere 0.4 "3 mois" ; zone 0.1 0.4 ambre |
| 25.6 | article "Art. 31 CP" |
| 26.1 | scene-vide ; article-retirer ; titre "Crimes imprescriptibles" ambre ; picto sablier 3.8 0.4 1.4 |
| 26.1@jamais | interdit sablier |
| 26.2 | picto-retirer sablier ; article "Art. 101 CP" ; livre "Code pénal" 3.8 |
| 26.2@énumère | livre-ouvrir |
| 27.1@génocide | liste-ajouter "Génocide" |
| 27.1@humanité | liste-ajouter "Contre l'humanité" |
| 27.1@guerre | liste-ajouter "De guerre" |
| 27.2@sexuels | liste-ajouter "Sexuels : enfants < 12 ans" |
| 28.1 | scene-vide ; foule societe -4.6 0.9 8 4 |
| 28.1@temps | frise ; point 0.05 "L'acte" |
| 28.1@jamais | zone 0.05 1 vert |
| 28.1@juger | picto marteau 4.6 0.6 |
| 29.1 | scene-vide ; titre "Prescription de la peine" ; picto prison 0 0.6 |
| 29.1@article | article "Art. 99 CP" |
| 29.2 | picto-retirer prison ; frise ; point 0.05 "Jugement" ; picto marteau -5.4 0.6 |
| 29.2@exécutée | picto sablier -3.0 0.6 |
| 29.2@délai | picto-deplacer sablier -1.0 0.6 |
| 29.3@cinq | repere 0.45 "5 ans" |
| 29.3@pécuniaire | picto pieces 2.6 0.6 ; etiquette pec "Peine pécuniaire" 2.6 -0.5 |
| 30.1 | scene-vide ; article-retirer ; repere-marquer 2 neutre ; decor rue Café jour ; titre "Le piège classique" ; personnage passant "Un passant" ambre_pale gauche ; placer passant -3.5 ; personnage amie "Son amie" rose centre-gauche ; placer amie -2.5 |
| 30.2 | effacer-titres ; parler passant amie |
| 30.2@prescrit | parole passant "Prescrit, donc innocent" |
| 30.3 | effacer-parole passant ; mot-barre "Donc innocent" 3.6 1.6 ; visage amie surpris |
| 31.1 | scene-vide ; repere-marquer 2 ambre ; batiment |
| 31.1+2.2 | etage-question 3 |
| 31.2 | picto tag 4.7 -0.4 |
| 31.2@illicite | etiquette illic "Toujours illicite" 4.7 0.6 |
| 31.3@perdu | picto loupe -4.7 -0.4 ; etiquette pours "Plus de poursuite" -4.7 0.6 |
| 31.3@poursuivre | interdit loupe |
| 32.1 | scene-vide ; repere-marquer 2 neutre ; repere-marquer 1 ambre ; personnage auteur "L'auteur" bleu_clair gauche ; picto cadenas -2.4 0.6 |
| 32.1@déguisée | mot-barre "Peine déguisée" 3.4 1.2 |
| 32.2@levée | picto-retirer cadenas ; visage auteur content |
| 32.2@conditions | etiquette cond "Conditions plus réunies" 3.4 -0.6 ; deplacer auteur centre-gauche |
| 33.1 | scene-vide ; titre "Retenons" ; personnage auteur "L'auteur" bleu_clair gauche |
| 33.2@danger | picto danger -1.6 0.6 |
| 33.2@soins | picto coeur 0.2 0.6 |
| 33.2@faute | etiquette sansf "Même sans faute" 3.4 0.6 |
| 33.3@proportionnée | etiquette-retirer sansf ; picto balance 2.6 0.6 ; etiquette fin "Proportionnée" 2.6 -0.7 |
| 33.3@remplies | etiquette fin "Puis levée" 2.6 -0.7 |
| 34.1 | scene-vide ; repere-marquer 1 neutre ; repere-marquer 2 ambre ; article "Art. 97 CP" ; frise ; point 0.03 "L'acte" |
| 34.1@limite | picto sablier -5.4 0.7 |
| 34.1@poursuivre | picto-deplacer sablier -1.0 0.7 |
| 34.2 | repere 0.1 "3 ans" ; repere 0.27 "7 ans" |
| 34.2@grave | repere 0.44 "10 ans" ; repere 0.62 "15 ans" |
| 34.2@délai | repere 0.95 "30 ans" ; titre "Plus grave, plus long" |
| 34.3 | picto-retirer sablier ; picto sablier 5.4 0.7 |
| 34.3@jamais | interdit sablier |
| 35.1 | scene-vide ; article-retirer ; repere-marquer 2 neutre ; titre "Une question pour finir" |
| 35.2 | effacer-titres ; decor rue Boulangerie jour ; personnage lina "Lina" violet gauche ; placer lina -3 ; picto velo -2.4 -1.85 |
| 35.2@vole | prendre lina velo |
| 35.2@mille | bulle lina "Vaut 1000 francs" |
| 35.3 | effacer-bulle lina ; marcher lina 2 ; etiquette d "Découverts 12 ans plus tard" -3.0 1.7 |
| 35.4 | scene-vide ; repere-marquer 2 ambre ; frise ; point 0.05 "Le vol" ; picto velo -3.8 0.6 ; point 0.95 "Découverte" ; repere 0.95 "12 ans" |
| 35.4@poursuivre | titre "Encore poursuivable ?" ambre ; questions |
| 35.5 | sous-titre "Votre réponse en commentaire" |
| 36.1 | scene-vide ; repere-retirer ; titre "Droit pénal général" ; sous-titre "Dernière vidéo" |
| 36.1+1.5 | batiment -2.5 |
| 36.2 | effacer-titres ; personnage juge "Le juge" rose droite |
| 36.2@premier | etage 1 vert |
| 36.2@étage | etage 2 vert |
| 36.2@peine | etage 3 vert ; picto prison 1.6 0.3 |
| 36.3 | titre "Merci" ambre ; visage juge content |
| 36.3@ici | accent batiment |
| 37.1 | scene-vide ; livre "Code pénal" 0 -0.5 ; titre "L'étude du droit" ; sous-titre "Tout est dans la description" |
| 37.2 | accent titre |
