# Visuels — Vidéo 9 : Il a essayé, mais…

Ce fichier pilote les schémas Manim (`render/manim/video.py`). Vocabulaire des actions : `render/manim/README.md`.

Colonne « Moment » : `ligne.phrase` du script, éventuellement `+secondes`. Plusieurs actions d'un même moment sont séparées par `;`.

Personnages : Simon turquoise, Mia violet ; dans les exemples sans nom, « Quelqu'un » rose, « Un complice » ambre pâle, « L'auteur » rose.

Style « scène » (repris le 1er novembre 2026) : le cas se joue devant le kiosque (décor rue, enseigne « Kiosque »), la patrouille est la voiture au trait, le chemin du crime reste la frise horizontale, et un pense-bête « Idée / Préparation / Tentative / Résultat » en haut à droite suit l'étape dont on parle (ambre : en examen ; gris : pas punissable ou pas atteinte ; vert : tentative punissable).

Écarts assumés avec la colonne « À l'écran » : le pied-de-biche, la porte, la caisse et le coffre-fort ne sont pas dessinés ; ils sont nommés par des étiquettes. Le deuxième alinéa de l'article 22 est signalé par une étiquette au-dessus du bloc d'article.

| Moment | Actions |
| --- | --- |
| 1.1 | decor rue Kiosque ; etiquette lieu "La Chaux-de-Fonds" -3.6 1.7 ; personnage simon "Simon" turquoise gauche ; placer simon -3 |
| 1.2 | etiquette-retirer lieu ; bulle simon "De l'argent" |
| 1.3 | bulle simon "Le kiosque" ; etiquette nuit "Une nuit" 4.6 1.7 |
| 2.1 | effacer-bulle simon ; etiquette-retirer nuit ; etiquette jour "Lundi : pied-de-biche" -3.6 1.7 |
| 2.2 | etiquette jour "Mardi : repérage" -3.6 1.7 ; marcher simon -2 |
| 2.3 | etiquette jour "Mercredi, deux heures" -3.6 1.7 ; picto lune 5.6 1.6 ; marcher simon 0 |
| 3.1 | etiquette-retirer jour ; etiquette force "Il force la porte" 0 1.7 |
| 3.2 | picto voiture 4.4 -1.9 ; etiquette police "Une patrouille" 4.4 -0.6 |
| 3.3 | etiquette-retirer force ; marcher simon -3 ; etiquette jour "Les mains vides" -3.6 1.7 |
| 4.1 | scene-vide ; titre "Rien volé" ; personnage simon "Simon" turquoise gauche |
| 4.2 | sous-titre "Puni quand même ?" ; picto prison 3.5 0.3 |
| 4.3 | effacer-titres ; titre "À partir de quand ?" ; accent simon |
| 5.1 | scene-vide ; frise ; titre "Le chemin du crime" ; repere-liste "Idée" "Préparation" "Tentative" "Résultat" |
| 5.2 | point 0.1 "Idée" ; repere-marquer 1 ambre |
| 5.3 | point 0.35 "Préparation" ; repere-marquer 1 neutre ; repere-marquer 2 ambre |
| 5.4 | point 0.6 "Exécution" ; repere-marquer 2 neutre ; repere-marquer 3 ambre |
| 5.5 | point 0.85 "Résultat" ; repere-marquer 3 neutre ; repere-marquer 4 ambre |
| 6.1 | effacer-titres ; titre "Consommée" ; sous-titre "Tout est réuni" |
| 6.2 | sous-titre "Souvent : un résultat" ; accent frise |
| 6.3 | zone 0.75 1 gris ; repere-marquer 4 gris ; sous-titre "Jamais atteint" |
| 7.1 | effacer-titres ; titre "Où commence le punissable ?" ; questions |
| 8.1 | scene-vide ; repere-marquer 1 ambre ; titre "L'idée seule" ; personnage simon "Simon" turquoise gauche ; bulle simon "Le kiosque" |
| 8.2 | etiquette jamais "Jamais punie" 2.0 0.3 ; repere-marquer 1 gris |
| 9.1 | scene-vide ; repere-marquer 2 ambre ; decor rue Kiosque ; personnage simon "Simon" turquoise gauche ; placer simon -3 ; etiquette prep "Pas punie, en principe" -2.6 1.7 |
| 9.2 | etiquette prep "Pied-de-biche, repérage" -2.6 1.7 ; marcher simon -1 |
| 9.2+2 | etiquette prep "Pas encore voler" -2.6 1.7 |
| 10.1 | scene-vide ; titre "Des exceptions" ; livre "Code pénal" 0 -0.3 |
| 10.2 | article "Art. 260bis CP" ; livre-ouvrir ; sous-titre "Certains actes préparatoires" |
| 10.3 | livre-retirer ; effacer-titres ; titre "Crimes très graves" ; liste "Meurtre" "Brigandage" "Incendie intentionnel" ; picto danger 4.5 -0.8 |
| 11.1 | mot-barre "Vol" 2.0 0.0 |
| 11.2 | scene-vide ; article-retirer ; repere-marquer 2 gris ; decor rue Kiosque ; personnage simon "Simon" turquoise gauche ; placer simon -3 ; etiquette prep "Achats, repérages : impunis" -2.6 1.7 |
| 12.1 | scene-vide ; frise ; zone 0 0.45 gris ; repere-marquer 3 ambre ; titre "Le passage à l'acte" |
| 12.2 | arret "ATF 131 IV 100" ; effacer-titres ; titre "Dernier pas décisif" ambre ; repere 0.55 "Le seuil" |
| 12.3 | sous-titre "Mène à l'infraction" |
| 13.1 | zone 0.55 1 ambre ; effacer-titres ; titre "Ni trop tôt, ni trop loin" |
| 13.2 | effacer-titres ; titre "Lien étroit" ; sous-titre "Temps et lieu" |
| 14.1 | scene-vide ; arret-retirer ; decor rue Kiosque ; personnage simon "Simon" turquoise gauche ; placer simon 0 ; etiquette force "Il force la porte" 0 1.7 |
| 14.2 | etiquette force "Le seuil est franchi" 0 1.7 |
| 14.3 | etiquette force "Tentative de vol" 0 1.7 ; accent simon |
| 15.1 | scene-vide ; article "Art. 22 CP" ; titre "La tentative" ; personnage simon "Simon" turquoise gauche |
| 15.2 | sous-titre "Pas jusqu'au bout" |
| 15.2+3.5 | sous-titre "Ou pas de résultat" |
| 16.1 | scene-vide ; colonnes "Arrêté en route" "Résultat manqué" |
| 16.2 | colonne-accent 1 ; picto voiture -3.5 -1.3 |
| 16.3 | colonne-accent 2 ; picto danger 3.5 -1.3 |
| 16.4 | etiquette alarme "Caisse bloquée" 3.5 -0.3 |
| 17.1 | scene-vide ; repere-marquer 3 vert ; titre "Punissable" ; personnage simon "Simon" turquoise gauche ; picto prison 3.5 0.3 |
| 17.2 | sous-titre "Peine atténuée possible" ; accent simon |
| 18.1 | scene-vide ; renvoi "vidéo 3" ; titre "Les contraventions" ; picto pieces 0 0.3 |
| 18.2 | sous-titre "Si la loi le prévoit" ; picto-deplacer pieces -3.5 0.3 ; picto parlement 3.5 0.3 |
| 18.3 | scene-vide ; titre "Crimes et délits" ambre ; picto prison 0 0.3 |
| 19.1 | scene-vide ; renvoi "vidéo 4" ; personnage simon "Simon" turquoise gauche |
| 19.2 | titre "Pas de tentative par négligence" |
| 19.3 | effacer-titres ; titre "Vouloir le résultat" ; bulle simon "Voler" |
| 20.1 | scene-vide ; rembobiner ; article-retirer ; decor rue Kiosque ; personnage simon "Simon" turquoise gauche ; placer simon -3 ; etiquette var "Changeons l'histoire" -3.6 1.7 |
| 20.2@kiosque | etiquette-retirer var ; marcher simon 0 ; etiquette caisse "La caisse" 1.5 1.7 |
| 20.2+2.5 | etiquette caisse "Caisse vide" 1.5 1.7 |
| 20.3 | etiquette soir "Vidée le soir même" -3.6 1.7 |
| 21.1 | scene-vide ; titre "Ne pouvait pas réussir" ; personnage simon "Simon" turquoise gauche |
| 21.2 | article "Art. 22 CP" ; case "Tentative" |
| 21.3 | cocher 1 vert |
| 21.4 | effacer-titres ; titre "Pas de butin ? Peu importe" |
| 21.5 | effacer-titres ; titre "Décider et passer à l'acte" ; bulle simon "Voler" |
| 22.1 | scene-vide ; titre "Une seule exception" ; personnage quelqu "Quelqu'un" rose gauche |
| 22.2 | effacer-titres ; titre "Grave défaut d'intelligence" ; etiquette alinea "Deuxième alinéa" 0 -1.9 |
| 23.1 | etiquette-retirer alinea ; effacer-titres ; bulle quelqu "Une formule magique" ; etiquette coffre "Un coffre-fort" 3.5 0.3 |
| 23.2 | effacer-bulle quelqu ; etiquette-retirer coffre ; case "Tentative" ; cocher 1 gris |
| 24.1 | scene-vide ; rembobiner ; article-retirer ; decor rue Kiosque ; personnage simon "Simon" turquoise gauche ; placer simon -3 ; etiquette var "Dernière version" -3.6 1.7 |
| 24.2@forcer | etiquette-retirer var ; marcher simon 0 ; etiquette force "Il force la porte" 0.6 1.7 |
| 24.3 | etiquette rue "Personne ne passe" -4.4 1.7 |
| 24.4 | etiquette-retirer force ; etiquette-retirer rue ; bulle simon "Le kiosquier" |
| 24.5 | effacer-bulle simon ; marcher simon -3 ; etiquette rentre "Il rentre chez lui" -3.6 1.7 |
| 25.1 | etiquette rentre "Il renonce de lui-même" -3.6 1.7 ; accent simon |
| 25.2 | article "Art. 23 CP" ; etiquette-retirer rentre ; titre "Le désistement" ; etiquette dsi "De sa propre initiative" 0 1.7 |
| 26.1 | scene-vide ; personnage simon "Simon" turquoise centre-gauche ; titre "Peine atténuée" ; picto prison 3.5 0.3 |
| 26.1+2.5 | picto-retirer prison ; sous-titre "Ou aucune peine" |
| 26.2 | effacer-titres ; titre "Faire marche arrière" ; deplacer simon gauche |
| 26.3 | effacer-titres ; titre "Aussi à plusieurs" ; personnage complice "Un complice" ambre_pale centre-droite |
| 26.4 | effacer-titres ; titre "Aider à l'empêcher" ; accent complice |
| 26.5 | renvoi "vidéo 10" |
| 27.1 | scene-vide ; article "Art. 23 CP" ; titre "Empêcher la consommation" ; personnage auteur "L'auteur" rose gauche ; picto feu 3.0 0.0 |
| 27.2 | sous-titre "Il éteint le feu" |
| 27.2+2.5 | picto-retirer feu ; picto coche 3.0 0.0 |
| 27.3 | sous-titre "Selon les faits" ; accent auteur |
| 28.1 | scene-vide ; article-retirer ; decor rue Kiosque ; personnage simon "Simon" turquoise gauche ; placer simon 0 ; titre "« De sa propre initiative »" ambre |
| 28.2 | picto voiture 4.4 -1.9 ; etiquette police "La police" 4.4 -0.6 |
| 28.2+2 | effacer-titres ; marcher simon -3 ; mot-barre "Désistement" 0.2 2.0 |
| 28.3 | etiquette ratee "Tentative ratée" -3.6 1.7 |
| 29.1 | scene-vide ; titre "Le piège classique" ; personnage simon "Simon" turquoise gauche |
| 29.2 | effacer-titres ; titre "Rien pris, rien à craindre" |
| 29.3 | barrer |
| 30.1 | scene-vide ; frise ; zone 0 0.45 gris ; repere 0.55 "Le seuil" ; zone 0.55 1 ambre ; point 0.7 "Il force la porte" |
| 30.2 | titre "Tentative punissable" ; repere-marquer 3 vert ; zone 0.85 1 gris |
| 31.1 | scene-vide ; decor rue Kiosque ; personnage simon "Simon" turquoise gauche ; placer simon -3 ; etiquette acquis "Reste acquis" -3.6 1.7 |
| 31.2 | article "Art. 144 CP" ; etiquette porte "Porte abîmée" 1.4 1.7 |
| 31.2+3 | etiquette acquis "Dommage à la propriété" -3.6 1.7 |
| 32.1 | scene-vide ; article-retirer ; titre "Retenons" ; frise |
| 32.2 | point 0.1 "Idée" ; point 0.35 "Préparation" ; zone 0 0.45 gris ; repere-marquer 1 gris ; repere-marquer 2 gris |
| 32.3 | repere 0.55 "Dernier pas" ; zone 0.55 1 ambre ; repere-marquer 3 ambre |
| 32.4 | effacer-titres ; titre "Crimes et délits" ; repere-marquer 3 vert |
| 32.5 | effacer-titres ; titre "Vouloir le résultat" ; repere-marquer 4 ambre |
| 33.1 | scene-vide ; article "Art. 23 CP" ; repere-marquer 4 gris ; titre "Renoncer de soi-même" ; personnage simon "Simon" turquoise gauche ; picto prison 3.5 0.3 |
| 33.1+3.5 | sous-titre "Peine atténuée, voire supprimée" |
| 33.2 | effacer-titres ; picto-retirer prison ; titre "Où est l'acte ?" ; repere-marquer 1 ambre ; repere-marquer 2 ambre ; repere-marquer 3 ambre ; repere-marquer 4 ambre |
| 34.1 | scene-vide ; article-retirer ; repere-marquer 1 neutre ; repere-marquer 2 neutre ; repere-marquer 3 neutre ; repere-marquer 4 neutre ; titre "Une question pour finir" |
| 34.2 | effacer-titres ; decor rue ; personnage mia "Mia" violet gauche ; placer mia -3 ; picto voiture 4.0 -1.6 ; bulle mia "Rayer sa voiture" |
| 34.3 | effacer-bulle mia ; marcher mia 1 ; etiquette cle "Elle commence à griffer" -0.4 1.7 |
| 34.4 | etiquette cle "De sa propre initiative" -0.4 1.7 ; accent mia |
| 34.5 | etiquette cle "Elle repart" -0.4 1.7 ; marcher mia -3 |
| 34.6 | etiquette cle "Aucune trace" -0.4 1.7 |
| 35.1 | etiquette-retirer cle ; article "Art. 23 CP" ; titre "Que dit l'article 23 ?" |
| 35.2 | sous-titre "Forcément impunie ?" ; repere-marquer 3 ambre |
| 35.3 | effacer-titres ; titre "Votre réponse en commentaire" ; accent mia |
| 36.1 | scene-vide ; article-retirer ; repere-retirer ; livre "Code pénal" 0 -0.5 ; titre "L'étude du droit" ; sous-titre "Tout est dans la description" |
| 36.2 | accent titre |
