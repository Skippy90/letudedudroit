# Visuels — Vidéo 8 : Était-il responsable ?

Ce fichier pilote les schémas Manim (`render/manim/video.py`). Vocabulaire des actions : `render/manim/README.md`.

Colonne « Moment » : `ligne.phrase` du script, éventuellement `+secondes`. Plusieurs actions d'un même moment sont séparées par `;`.

Personnages : Théo turquoise, l'agent bleu clair, le juge rose, l'expert ambre pâle, un inconnu ambre pâle, Zoé violet, son amie rose.

Style « scène » (repris le 1er novembre 2026) : le cas se joue devant l'entrée du festival (décor rue, enseigne « Festival ») et chaque variante s'y rejoue après le rembobinage ; l'expertise se joue dans la salle d'audience (décor tribunal) ; un pense-bête « Comprendre / Se retenir » en haut à droite suit les deux facultés de l'article 19 (ambre : examinée ; gris : elle manque ; vert : présente).

Écarts assumés avec la colonne « À l'écran » du script, pour rester dans la charte : le juge est une silhouette dans la salle d'audience plutôt que la pyramide (ligne 20) ; pas d'échelle dessinée, les trois situations sont une liste (lignes 6, 17 et 34) ; le traitement et le verre drogué n'ont pas de pictogramme propre : ils sont nommés par une étiquette (lignes 29 et 31), le verre est la bouteille.

| Moment | Actions |
| --- | --- |
| 1.1 | decor festival ; etiquette lieu "Près de Nyon, un soir" -3.6 1.7 |
| 1.2 | personnage theo "Théo" turquoise gauche ; placer theo -3 ; etiquette lieu "Il s'agite" -3.6 1.7 |
| 2.1 | etiquette-retirer lieu ; personnage agent "L'agent" bleu_clair droite ; placer agent 2 ; etiquette calme "« Calmez-vous »" 3.4 1.7 |
| 2.2 | etiquette-retirer calme ; marcher theo 0 |
| 2.2+0.8 | pousser theo agent |
| 2.3 | chute agent 3 |
| 2.3+0.9 | dommage agent ; etiquette blesse "Épaule blessée" 4.4 1.7 |
| 2.4 | etiquette-retirer blesse ; etiquette regard "Un regard étrange" 0.6 1.7 |
| 2.4+2 | etiquette regard "Des paroles sans suite" 0.6 1.7 |
| 3.1 | scene-vide ; batiment |
| 3.2 | etage 1 vert |
| 3.2+1.2 | etage 2 vert |
| 3.3 | etage-question 3 |
| 3.4 | personnage theo "Théo" turquoise gauche ; titre "Que se passait-il dans sa tête ?" |
| 4.1 | scene-vide ; batiment ; renvoi "vidéo 1" ; etage 1 vert ; etage 2 vert |
| 4.2 | etage 3 ambre |
| 5.1 | scene-vide ; personnage theo "Théo" turquoise gauche ; titre "Être responsable" |
| 5.2 | bulle theo "Je réponds de mes actes" |
| 6.1 | scene-vide ; article "Art. 19 CP" ; titre "Trois situations" ; livre "Code pénal" 3.8 |
| 6.2 | livre-ouvrir ; liste-ajouter "Responsable" |
| 6.2+2 | liste-ajouter "Pas du tout" |
| 6.2+4 | liste-ajouter "En partie" |
| 7.1 | scene-vide ; article-retirer ; rembobiner ; decor festival ; personnage theo "Théo" turquoise gauche ; placer theo -3 ; personnage agent "L'agent" bleu_clair droite ; placer agent 2 ; titre "La version simple" |
| 7.2 | picto tension -0.8 -0.2 ; etiquette etat "Sobre, juste énervé" -3.6 1.7 |
| 7.3 | etiquette-retirer etat ; picto-retirer tension ; bulle theo "Je comprends" |
| 7.3+1.3 | bulle theo "Je pourrais me retenir" |
| 7.4 | effacer-bulle theo ; etiquette coupable "Responsable" 0.6 1.7 |
| 7.5 | etiquette coupable "Autres conditions à examiner" 0.6 1.7 |
| 8.1 | scene-vide ; article "Art. 19 CP" ; titre "Deux facultés" ; personnage theo "Théo" turquoise gauche |
| 9.1 | case "Comprendre" |
| 9.2 | bulle theo "Interdit" |
| 10.1 | case "Se retenir" |
| 10.2 | bulle theo "Je m'arrête" |
| 11.1 | effacer-bulle theo ; effacer-titres ; titre "Une seule suffit" ; cocher 1 gris |
| 11.2 | sous-titre "Irresponsable, pas punissable" |
| 11.3 | scene-vide ; article-retirer ; repere-liste "Comprendre" "Se retenir" ; personnage theo "Théo" turquoise gauche ; titre "« au moment d'agir »" ambre |
| 11.4 | sous-titre "L'état à l'instant de l'acte" ; accent theo |
| 12.1 | scene-vide ; rembobiner ; decor festival ; personnage theo "Théo" turquoise gauche ; placer theo -3 ; personnage agent "L'agent" bleu_clair droite ; placer agent 2 ; titre "Variante 1" |
| 12.2@psychotique | etiquette crise "Crise psychotique" -3.6 1.7 |
| 12.3 | etiquette-retirer crise ; bulle theo "Un démon !" |
| 13.1 | repere-marquer 1 ambre ; effacer-titres ; effacer-bulle theo ; titre "Ne voit plus l'interdit" |
| 13.2 | repere-marquer 1 gris |
| 13.3 | etiquette irr "Irresponsable" 0.6 1.7 |
| 14.1 | scene-vide ; rembobiner ; repere-marquer 1 neutre ; decor festival ; personnage theo "Théo" turquoise gauche ; placer theo -3 ; personnage agent "L'agent" bleu_clair droite ; placer agent 2 ; titre "Variante 2" |
| 14.2@interdit | bulle theo "C'est interdit, je sais" ; repere-marquer 1 vert |
| 14.3 | effacer-bulle theo ; etiquette maitrise "Plus aucune maîtrise" 0.6 1.7 |
| 14.3+1.5 | marcher theo 0 |
| 15.1 | pousser theo agent ; repere-marquer 2 ambre |
| 15.1+1.5 | repere-marquer 2 gris |
| 15.2 | etiquette maitrise "Irresponsable aussi" 0.6 1.7 |
| 16.1 | scene-vide ; repere-marquer 1 neutre ; repere-marquer 2 neutre ; renvoi "vidéo 7" ; colonnes "Information" "Capacité" |
| 16.2 | colonne-accent 1 ; picto document -3.5 -1.3 |
| 16.3 | colonne-eteindre 1 ; colonne-accent 2 ; etiquette cap "Sa capacité même" 3.5 -1.3 |
| 17.1 | scene-vide ; personnage theo "Théo" turquoise droite ; titre "Une zone grise" |
| 17.2 | liste "Responsable" "Restreinte" "Irresponsable" ; liste-surligner 2 ; repere-marquer 1 ambre ; repere-marquer 2 ambre |
| 18.1 | article "Art. 19 CP" ; effacer-titres ; titre "Responsabilité restreinte" |
| 18.2 | sous-titre "Toujours coupable" |
| 18.3 | sous-titre "Peine atténuée" ; picto prison 1.6 -0.6 |
| 19.1 | scene-vide ; article-retirer ; personnage theo "Théo" turquoise centre ; titre "La logique" |
| 19.2 | bulle theo "À moitié maîtrisé" ; effacer-titres ; titre "Moins de reproche" |
| 20.1 | scene-vide ; repere-marquer 1 neutre ; repere-marquer 2 neutre ; decor tribunal ; personnage theo "Théo" turquoise gauche ; placer theo -1 ; personnage juge "Le juge" rose droite ; placer juge 3 ; titre "Comment savoir ?" |
| 20.2 | bulle juge "Pas psychiatre…" |
| 21.1 | effacer-bulle juge ; effacer-titres ; article "Art. 20 CP" ; etiquette expertise "Une expertise" 1.0 1.7 |
| 21.2 | etiquette enquete "Dès l'enquête" -4.4 1.7 |
| 22.1 | etiquette-retirer enquete ; etiquette-retirer expertise ; article-retirer ; arret "ATF 133 IV 145" ; titre "Pas tout seul" |
| 22.2 | effacer-titres ; livre "Psychiatrie" 1.2 -0.6 |
| 22.2+1.8 | etiquette livres "Lire ne suffit pas" 1.2 1.6 |
| 22.3 | livre-retirer ; etiquette-retirer livres ; personnage expert "L'expert" ambre_pale gauche ; placer expert -3 ; effacer-titres ; titre "Un expert" ambre |
| 23.1 | effacer-titres ; etiquette diag "Diagnostic insuffisant" -3.6 1.7 |
| 23.2 | etiquette diag "Le lien avec l'acte" -3.6 1.7 |
| 23.3 | etiquette-retirer diag ; parole expert "Sa santé" |
| 23.4 | effacer-parole expert ; etiquette juge "Le juge décide" 4.6 1.8 |
| 24.1 | scene-vide ; article-retirer ; arret-retirer ; decor festival ; personnage theo "Théo" turquoise gauche ; placer theo -3 ; picto bouteille -3.5 -1.0 ; titre "Le piège classique" |
| 24.2 | parole theo "J'avais trop bu" |
| 24.2+1.8 | effacer-parole theo |
| 24.2+2.1 | parole theo "Je ne savais plus" |
| 24.3 | effacer-parole theo ; effacer-titres ; titre "Une excuse ?" ambre |
| 25.1 | scene-vide ; article "Art. 19 CP" ; titre "Quatrième alinéa" ; picto bouteille -4.4 0.6 |
| 25.2 | frise ; point 0.25 "Il boit" |
| 25.2+3 | point 0.7 "Il frappe" |
| 26.1 | fleche-retour 0.7 0.25 vert |
| 26.2 | article "Art. 19 CP" ; effacer-titres ; titre "Évitable et prévisible ?" |
| 26.3 | effacer-titres ; titre "Alors, pleinement responsable" ambre ; repere-marquer 1 vert ; repere-marquer 2 vert |
| 27.1 | scene-vide ; repere-marquer 1 neutre ; repere-marquer 2 neutre ; personnage theo "Théo" turquoise gauche ; titre "Pas prévisible ?" ; bulle theo "Imprévisible" |
| 27.2 | effacer-bulle theo ; article "Art. 263 CP" ; sous-titre "Irresponsabilité fautive" ; picto bouteille 0 0.3 |
| 27.3 | sous-titre "Totalement irresponsable, par sa faute" |
| 27.4 | sous-titre "Un crime ou un délit" |
| 28.1 | effacer-titres ; titre "Peine pécuniaire" ; picto pieces 3.0 0.3 |
| 28.2 | picto-retirer bouteille ; picto prison 0 0.3 ; sous-titre "Seule peine : la prison ?" |
| 28.2+4 | sous-titre "Trois ans au plus" |
| 29.1 | scene-vide ; article-retirer ; decor festival ; personnage theo "Théo" turquoise gauche ; placer theo -2 ; personnage inconnu "Un inconnu" ambre_pale droite ; placer inconnu 3 ; picto bouteille -1.9 -1.0 |
| 29.1+2.5 | etiquette insu "Drogué, à son insu" 0.6 1.7 |
| 29.2 | etiquette insu "Pas fautif" 0.6 1.7 |
| 29.3 | article "Art. 263 CP" ; titre "Ni l'alinéa 4, ni 263" |
| 29.4 | scene-vide ; article-retirer ; titre "Ivresse volontaire" ; frise ; point 0.25 "Il boit" ; point 0.7 "Il frappe" |
| 29.5 | sous-titre "Conditions précises" |
| 29.6 | effacer-titres ; repere 0.25 "La faute" |
| 30.1 | scene-vide ; personnage theo "Théo" turquoise gauche ; bulle theo "Un démon !" ; repere-marquer 1 gris |
| 30.2 | titre "Pas punissable" |
| 30.3 | effacer-bulle theo ; sous-titre "Pas forcément la fin" |
| 31.1 | scene-vide ; article "Art. 19 CP" ; personnage theo "Théo" turquoise gauche ; etiquette mesure "Une mesure" 0 1.0 |
| 31.1+3 | etiquette soin "Un traitement" 0 -0.2 |
| 31.2 | repere-marquer 1 ambre ; repere-marquer 2 ambre ; etiquette soin "Aussi si restreinte" 0 -0.2 |
| 31.3 | renvoi "vidéo 1" |
| 31.4 | renvoi "vidéo 12" |
| 32.1 | scene-vide ; article-retirer ; repere-marquer 1 neutre ; repere-marquer 2 neutre ; colonnes "Peine : la faute" "Mesure : le danger" ; colonne-accent 1 ; picto prison -3.5 -1.3 |
| 32.2 | colonne-accent 2 ; picto danger 3.5 -1.3 |
| 32.3 | titre "La grande différence" |
| 33.1 | scene-vide ; titre "Retenons" ; personnage theo "Théo" turquoise gauche |
| 33.2 | cases "Comprendre" "Se retenir" ; cocher 1 vert ; cocher 2 vert ; repere-marquer 1 vert ; repere-marquer 2 vert |
| 34.1 | scene-vide ; personnage theo "Théo" turquoise droite ; repere-marquer 1 gris ; liste-ajouter "Pas de peine" |
| 34.2 | repere-marquer 1 ambre ; repere-marquer 2 ambre ; liste-ajouter "Peine atténuée" |
| 34.3 | article "Art. 20 CP" ; liste-ajouter "Un expert" |
| 34.4 | scene-vide ; article-retirer ; repere-marquer 1 neutre ; repere-marquer 2 neutre ; picto bouteille 0 0.3 ; titre "Ivresse volontaire : pas d'automatisme" |
| 34.5 | sous-titre "Plusieurs conditions à examiner" |
| 35.1 | scene-vide ; titre "Une question pour finir" |
| 35.2 | effacer-titres ; decor festival ; personnage zoe "Zoé" violet gauche ; placer zoe -2 ; bulle zoe "Agressive si je bois" |
| 35.3 | effacer-bulle zoe ; picto bouteille -1.9 -1.0 ; personnage amie "Une amie" rose droite ; placer amie 1 ; etiquette soiree "Elle boit énormément" 0.6 1.7 |
| 35.4 | etiquette-retirer soiree ; picto-retirer bouteille ; marcher zoe -1 |
| 35.4+1.2 | pousser zoe amie ; dommage amie |
| 36.1 | titre "Son ivresse l'excuse-t-elle ?" ambre ; repere-marquer 1 ambre ; repere-marquer 2 ambre |
| 36.2 | effacer-titres ; titre "Que faut-il vérifier ?" ambre |
| 36.3 | effacer-titres ; titre "Votre réponse en commentaire" ; accent zoe |
| 37.1 | scene-vide ; repere-retirer ; livre "Code pénal" 0 -0.5 ; titre "L'étude du droit" ; sous-titre "Tout est dans la description" |
| 37.2 | accent titre |
