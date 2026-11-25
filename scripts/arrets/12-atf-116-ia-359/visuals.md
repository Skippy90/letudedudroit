# Visuels — Arrêts, vidéo 12 : En 1990, des Suissesses ne pouvaient toujours pas voter dans leur canton

Ce fichier pilote les schémas Manim (`render/manim/video.py`). Vocabulaire des actions : `render/manim/README.md`.

Colonne « Moment » : `ligne.phrase` du script (texte de `tts.txt`, 41 lignes), éventuellement `+secondes` ou `@mot` (mot tel que la transcription de la narration l'a reconnu, par exemple `apensel` pour « Appenzell »). Plusieurs actions d'un même moment sont séparées par `;`.

Personnages (bonshommes en bâtons ; poses, visages et objets aux moments marqués) : Theresa Rohner turquoise, Ursula Baumann ambre pâle (pour les cinquante-trois recourantes), Mario Sonderegger bleu clair (pour les quarante-neuf recourants), le juge violet ; seconds rôles en rose : le gouvernement cantonal (ligne 5), le Conseil fédéral (lignes 14 et 25) ; un homme et une femme sans nom (lignes 12 et 35).

Style « scène » : la Landsgemeinde n'a pas de décor dans le moteur ; elle est rendue par la carte de la Suisse (canton AI mis en avant), une foule de citoyens et le pictogramme `main_levee`. Les femmes et les hommes recourants sont des foules à côté de leur premier nom. Le Tribunal fédéral est la salle d'audience (le juge derrière son banc) ; l'Assemblée fédérale et le Conseil fédéral, le Palais fédéral. Les dates sont sur des frises (1971, les recours de mai 1990, 1874 et 1999, 1981, 1979 contre 1981, le délai de neuf ans, l'effet pour l'avenir). Un pense-bête « Recours / Garantie / Fond / Remède » en haut à droite suit les quatre étapes de l'arrêt (lignes 17 à 32). Le bloc de l'arrêt reste en bas de la ligne 16 à la ligne 39 ; les blocs d'article : art. 16 de la constitution cantonale, art. 4 al. 2 et 74 al. 4 de la Constitution de 1874, art. 8 al. 3, 39 et 51 de la Constitution actuelle.

Objets et actions : la demande de Theresa Rohner (une enveloppe qu'elle remet au gouvernement, qui la lui rend : le refus), son recours (un document posé sur le banc du juge), le bulletin barré du refus de 1990, le bulletin que tient Mario Sonderegger (il vote déjà), la balance de l'égalité, la loupe du contrôle, la flèche du Conseil fédéral vers le peuple et les cantons, barrée (son avis ne les lie pas), le sablier du délai qui avance sur la frise, les mots barrés du remède écarté.

Sobriété : aucune arme n'est dessinée (ligne 2 : une étiquette suffit) ; aucun jugement sur le canton ni sur ses citoyens ; pas de croix suisse.

| Moment | Actions |
| --- | --- |
| 1.1 | carte cantons petite ; etiquette date "29 avril 1990" 3.2 2.6 |
| 1.1@apensel | carte-canton AI |
| 1.1@landsgemeinde | etiquette lg "Landsgemeinde" 3.2 1.6 ; foule citoyens 3.2 -0.4 24 8 |
| 1.2@populaire | etiquette lg "Assemblée populaire" 3.2 1.6 |
| 1.2@démocratie | picto main_levee 5.6 -0.4 |
| 1.3@citoyens | picto main_levee:2 0.8 -0.4 |
| 1.3@directement | etiquette lg "Démocratie directe" 3.2 1.6 |
| 1.3@décisions | picto bulletin 3.2 -2.2 0.8 |
| 2.1 | scene-vide ; foule hommes -2.8 0.4 24 8 ; etiquette part "Une particularité" 0 2.6 ; etiquette h "Hommes" -2.8 -1.0 |
| 2.1@attester | etiquette part "La preuve du droit de vote" 0 2.6 |
| 2.1@arme | etiquette arme "Une arme blanche au côté" -2.4 -2.1 |
| 2.2 | etiquette-retirer arme ; etiquette part "Les hommes seulement" 0 2.6 ; foule femmes 3.6 0.4 12 4 |
| 2.2@part | etiquette f "Femmes" 3.6 -1.0 |
| 2.2@décisions | interdit femmes |
| 3.1 | scene-vide ; picto parlement -4.4 0.4 1.3 ; etiquette gouv "Le canton propose" -4.4 -1.2 |
| 3.1@accorder | picto bulletin 0 0.4 1.3 ; relier parlement bulletin |
| 3.1@femmes | titre "Le vote des femmes ?" |
| 3.2 | foule lg 4.4 0.4 12 4 ; etiquette lg "Landsgemeinde" 4.4 -1.2 |
| 3.2@rejette | picto-retirer parlement>bulletin ; interdit bulletin ; titre "Refusé" ambre |
| 3.2@six | jauge vote -1.8 -2.3 60 "6 contre 4" |
| 4.1 | scene-vide ; frise ; point 0.1 "1971" |
| 4.1@fédéral | picto urne -4.8 1.0 |
| 4.1@sucesses | etiquette f "Les Suissesses votent" 0.4 1.0 |
| 4.2 | scene-vide ; carte cantons 0 -0.1 6.4 |
| 4.2@cantons | carte-cantons-tous ; titre "Les autres cantons : oui" |
| 4.3 | carte-canton AI |
| 4.3@dernier | etiquette ai "Le dernier" 5.0 1.0 |
| 4.3@refuser | titre "Appenzell Rhodes-Intérieures : non" ambre |
| 5.1 | scene-vide ; etiquette an "Un an plus tôt" 0 2.6 |
| 5.1@thérésa | personnage rohner "Theresa Rohner" turquoise gauche ; picto enveloppe -4.5 0 0.7 ; tenir rohner enveloppe aussitot ; personnage gouv "Le gouvernement" rose droite |
| 5.1@demandé | poser rohner enveloppe 0 -0.3 |
| 5.1@participer | prendre gouv enveloppe |
| 5.2@opposé | etiquette an "Demande refusée" 0 2.6 |
| 5.2@refus | poser gouv enveloppe -1.8 -0.3 ; visage rohner triste |
| 6.1 | scene-vide ; decor tribunal ; personnage juge "Le juge" violet droite ; placer juge 3 ; personnage rohner "Theresa Rohner" turquoise gauche ; placer rohner -3 ; picto document -4.8 0 0.7 ; tenir rohner document aussitot ; etiquette tf "Tribunal fédéral" -3.2 1.7 |
| 6.1+1.9 | marcher rohner 0 |
| 6.2+0.9 | poser rohner document 3.5 -0.45 |
| 6.2@suspendue | etiquette tf "Procédure suspendue" -3.2 1.7 ; picto sablier 1.4 1.4 0.8 |
| 6.2@scrutin | etiquette att "Jusqu'au vote de 1990" -3.2 0.6 |
| 7.1 | scene-vide ; picto bulletin 0 1.2 0.9 ; etiquette refus "Nouveau refus" 0 2.6 |
| 7.1@refus | interdit bulletin |
| 7.1@cinquante | etiquette-retirer refus ; picto-retirer bulletin ; foule femmes -3.6 1.4 20 10 ; etiquette nb "53 femmes" -3.6 2.7 |
| 7.1@saisissent | picto marteau 3.6 1.4 1.1 ; relier femmes marteau |
| 7.1@mai | etiquette date "29 mai 1990" 3.6 2.7 |
| 7.2 | picto-retirer femmes>marteau ; personnage baumann "Ursula Baumann" ambre_pale centre |
| 7.2@ursula | accent baumann |
| 8.1 | scene-vide ; frise ; point 0.8 "29 mai" ; foule femmes 3.6 1.2 20 5 ; etiquette nb "53 femmes" 3.6 2.9 |
| 8.1@seules | picto marteau 6.3 0.4 0.8 |
| 8.2@neuf | point 0.45 "20 mai" |
| 8.2@quarante | foule hommes -0.6 1.2 20 5 ; etiquette h "49 hommes" -0.6 2.9 |
| 8.2@mario | personnage sonderegger "Mario Sonderegger" bleu_clair gauche haut |
| 8.2@recours | repere 0.625 "9 jours" |
| 8.3 | picto bulletin -3.0 0.4 0.6 ; tenir sonderegger bulletin |
| 8.4 | etiquette-retirer nb ; etiquette-retirer h ; titre "Pourquoi recourir ?" |
| 8.4@personnellement | visage sonderegger surpris |
| 8.5 | accent sonderegger |
| 9.1 | scene-vide ; carte cantons 4.4 0.4 4.0 ; livre "Constitution cantonale" -2.4 0.2 |
| 9.1@article | article "Art. 16 Cst. AI" |
| 9.1@apenzell | carte-canton AI |
| 9.2 | etiquette dc "Droit cantonal" -2.4 2.4 |
| 9.2@cantonal | livre-ouvrir |
| 10.1 | scene-vide ; titre "Qui peut voter ?" |
| 10.1@landleuter | etiquette ll "« Landleute »" -3.6 1.0 ; foule ll -3.6 -0.6 8 4 |
| 10.1@ressortissant | etiquette ll "Ressortissants du canton" -3.6 1.0 |
| 10.1@suisses | etiquette ch "« Suisses »" 3.6 1.0 ; foule ch 3.6 -0.6 8 4 |
| 10.2@autorités | effacer-titres ; picto parlement 0 -0.4 1.0 |
| 10.2@interprété | picto loupe 0 -1.7 0.8 |
| 10.2@hommes | titre "Lu : les hommes seulement" ambre |
| 11.1 | scene-vide ; article-retirer ; livre "Constitution fédérale" 0 1.2 |
| 11.1@respecter | livre-ouvrir |
| 11.2 | frise |
| 11.2@mille | point 0.15 "1874" |
| 11.2@remplacée | point 0.85 "1999" |
| 11.2@nonante | zone 0.15 0.85 gris |
| 12.1 | scene-vide ; frise ; point 0.6 "1981" |
| 12.1@article | article "Art. 4 al. 2 Cst. 1874" |
| 12.1@fondamental | picto balance 0 1.3 1.5 |
| 12.1@homme | personnage homme "Un homme" bleu_clair gauche haut ; personnage femme "Une femme" ambre_pale droite haut |
| 12.1@égaux | titre "Égaux en droits" ambre |
| 13.1 | scene-vide ; article-retirer ; livre "Constitution fédérale" 0 0.4 ; titre "Une autre disposition" |
| 13.1@débat | livre-ouvrir |
| 13.2 | scene-vide ; article "Art. 74 Cst. 1874" ; frise |
| 13.2@mille | point 0.3 "1971" |
| 13.2@instauré | picto urne -2.4 1.2 |
| 13.2@féminin | etiquette fed "Vote fédéral des femmes" 2.6 1.2 |
| 13.3@alinéa | article "Art. 74 al. 4 Cst. 1874" |
| 13.3@élections | etiquette-retirer fed ; picto-retirer urne ; carte cantons 2.0 1.0 4.2 |
| 13.3@réservé | carte-cantons-tous ; titre "Le droit cantonal demeure réservé" ambre |
| 14.1 | scene-vide ; colonnes "Égalité" "Réserve" ; picto balance -3.5 -1.2 1.1 |
| 14.1@réserve | colonne-accent 2 ; carte cantons 3.5 -1.2 2.8 |
| 14.1@canton | carte-canton AI sans-nom |
| 14.2 | scene-vide ; article-retirer ; decor palais ; personnage cf "Conseil fédéral" rose gauche ; placer cf -3 |
| 14.2@mille | etiquette cf "En 1980" 0 1.9 |
| 14.2@estimait | bulle cf "Les cantons décident" |
| 14.2@femmes | parler cf |
| 15.1 | scene-vide ; picto balance -3.6 0.6 1.4 ; etiquette eg "Égalité" -3.6 -0.9 |
| 15.1@réserve | carte cantons 3.6 0.6 4.0 ; etiquette res "Réserve cantonale" 3.6 -0.9 |
| 15.1@portée | titre "Quelle portée ?" |
| 15.2 | foule femmes 0 0.6 9 3 |
| 15.2@exclusion | etiquette q "Exclues ?" 0 -0.9 |
| 15.2@électoral | titre "L'autonomie contre l'égalité ?" ambre |
| 16.1 | scene-vide ; decor tribunal ; personnage juge "Le juge" violet droite ; placer juge 3 ; etiquette date "27 novembre 1990" -3.0 1.7 |
| 16.1@tribunal | arret "ATF 116 Ia 359" |
| 16.1@décision | picto marteau 3.3 -0.4 0.8 |
| 16.2@grands | etiquette ga "Un arrêt de référence" -3.0 0.5 |
| 17.1 | scene-vide ; repere-liste "Recours" "Garantie" "Fond" "Remède" ; titre "Trois recours" |
| 17.1@juges | personnage rohner "Theresa Rohner" turquoise gauche ; foule femmes -0.4 0.6 15 5 ; foule hommes 2.6 0.6 15 5 |
| 17.1@recevabilité | repere-marquer 1 ambre |
| 17.2 | effacer-titres ; accent rohner |
| 17.2@irrecevable | etiquette irr "Irrecevable" -4.5 -2.0 ; visage rohner triste |
| 17.2@lieu | picto calendrier -4.5 2.6 0.8 |
| 17.2@annulation | etiquette ann "Pas d'annulation demandée" -0.6 2.6 |
| 17.3@admettre | etiquette-retirer ann |
| 17.3@intérêt | mot-barre "Intérêt pratique" -0.6 2.6 |
| 18.1 | scene-vide ; personnage baumann "Ursula Baumann" ambre_pale gauche ; foule femmes -0.6 0.6 30 10 |
| 18.1@cinquante | etiquette nb "53 femmes" -0.6 2.4 |
| 18.2@prive | picto urne 3.4 0.4 ; interdit urne |
| 18.2@violation | etiquette viol "Contraire à la Constitution ?" 0.4 -2.0 |
| 18.3 | etiquette-retirer viol |
| 18.3@reconnaître | picto coche 3.4 -1.2 |
| 18.3@qualité | etiquette viol "Qualité pour recourir" 0 -2.0 ; pose baumann bras-ciel content |
| 19.1 | scene-vide ; personnage sonderegger "Mario Sonderegger" bleu_clair gauche ; foule hommes -1.0 0.6 20 5 |
| 19.1@surprenant | etiquette nb "49 hommes" -1.0 2.6 |
| 19.1@recourir | picto coche 1.0 2.6 0.7 |
| 19.2@voter | picto bulletin 1.0 0.6 0.8 |
| 19.3 | picto-retirer bulletin |
| 19.3@corps | foule femmes 1.6 0.6 20 5 |
| 19.3@électoral | etiquette ce "Corps électoral" 0.3 -2.0 |
| 19.4@exclues | interdit femmes |
| 19.4@atteints | visage sonderegger inquiet ; accent sonderegger |
| 20.1 | scene-vide ; repere-marquer 1 vert ; repere-marquer 2 ambre ; titre "Autre difficulté" ; picto document 0 0.2 1.2 |
| 20.2 | scene-vide ; decor palais |
| 20.2@assemblée | etiquette af "Assemblée fédérale, 1979" 0 1.9 |
| 20.2@garantie | picto coche -5.6 0.2 0.8 |
| 20.2@seize | article "Art. 16 Cst. AI" |
| 20.3@contrôler | etiquette af "Encore contrôlable ?" 0 1.9 ; picto loupe 5.8 -1.2 0.9 |
| 21.1 | scene-vide ; frise ; point 0.3 "1979 : garantie" |
| 21.1@oui | titre "Oui" ambre |
| 21.1@égalité | picto balance 1.4 0.9 1.2 |
| 21.1@mille | point 0.65 "1981 : égalité" |
| 21.1@après | zone 0.65 1 vert |
| 21.2 | effacer-titres ; picto loupe -3.4 0.9 1.1 |
| 21.2@vérifier | titre "Contrôle possible" |
| 21.2@récent | accent frise |
| 22.1 | scene-vide ; repere-marquer 2 vert ; repere-marquer 3 ambre ; titre "Le fond" ; picto loupe 0 -1.4 0.9 |
| 22.1@deux | colonnes "Vote fédéral" "Réserve" |
| 22.2 | colonne-accent 1 ; article "Art. 74 Cst. 1874" |
| 22.2@femmes | picto urne -3.5 -1.3 |
| 22.3 | colonne-accent 2 |
| 22.3@cantons | carte cantons 3.5 -0.9 2.6 |
| 22.3@organiser | carte-cantons-tous |
| 23.1 | scene-vide ; article-retirer ; picto balance 0 0.6 1.5 ; etiquette eg "Égalité" 0 -0.9 |
| 23.1@exception | mot-barre "Exception" 3.8 0.6 |
| 23.2@soustraire | picto urne -3.8 0.6 |
| 23.2@fallu | titre "Il aurait fallu l'écrire" |
| 23.2@expressément | sous-titre "Expressément" |
| 24.1 | scene-vide ; picto balance -3.6 0.9 1.3 ; etiquette eg "Égalité" -3.6 -0.4 |
| 24.1@perdrait | jauge portee -4.6 -1.6 35 "Une part perdue" |
| 24.1@exercice | picto urne 3.4 0.9 ; relier balance urne |
| 24.2 | titre "Au cœur de la démocratie" ambre |
| 24.2@démocratique | foule citoyens 3.4 -1.2 10 5 |
| 25.1 | scene-vide ; decor palais ; personnage cf "Conseil fédéral" rose gauche ; placer cf -3 |
| 25.1@autrefois | bulle cf "Les cantons décident" |
| 25.2 | effacer-bulle cf ; foule peuple 3.6 -1.0 12 6 ; picto document -2.2 0.6 0.8 |
| 25.2@lit | interdit document |
| 25.2@peuple | etiquette const "Peuple et cantons" 1.2 1.9 |
| 25.3 | picto-retirer document ; picto enveloppe -1.4 0.4 0.8 |
| 25.3@citoyens | picto-deplacer enveloppe 1.6 0.4 0.5 |
| 25.3@mille | etiquette const "Votation de 1981" 1.2 1.9 |
| 25.3@ensemble | etiquette exp "Égalité partout" -1.4 1.0 |
| 26.1 | scene-vide ; carte cantons petite ; titre "Une vraie autonomie" |
| 26.1@autonomie | carte-cantons-tous |
| 26.2 | effacer-titres |
| 26.2@âge | case "Âge du vote" |
| 26.2@décider | cocher 1 vert |
| 26.2@étrangers | case "Étrangers" |
| 26.3 | cocher 2 vert |
| 26.3@exclure | case "Exclure les femmes" |
| 26.3@sexe | cocher 3 gris |
| 27.1 | scene-vide ; titre "Un délai ?" ; frise ; point 0.1 "1981" |
| 27.1@délai | picto sablier -4.8 0.9 1.1 |
| 27.2@laisse | sous-titre "Question ouverte" |
| 27.3 | effacer-titres |
| 27.3@neuf | point 0.85 "1990" ; picto-deplacer sablier 2.6 0.6 |
| 27.3@écoulées | repere 0.475 "Près de 9 ans" |
| 27.4@nécessaire | zone 0.1 0.85 vert |
| 27.4@largement | titre "Largement suffisant" ambre |
| 28.1 | scene-vide ; repere-marquer 3 vert ; repere-marquer 4 ambre ; decor tribunal ; personnage juge "Le juge" violet droite ; placer juge 3 |
| 28.1@comment | titre "Quel remède ?" |
| 28.2 | effacer-titres |
| 28.2@annuler | etiquette opt "Annuler le vote ?" -3.4 1.4 |
| 28.2@révision | etiquette opt2 "Réviser le texte ?" -3.4 0.2 |
| 28.3 | etiquette-retirer opt ; etiquette-retirer opt2 ; mot-barre "Annuler" -3.4 1.4 ; mot-barre "Réviser" -3.4 0.2 |
| 28.3@voix | pose juge pointe |
| 29.1 | scene-vide ; article "Art. 16 Cst. AI" ; livre "Constitution cantonale" 0 0.4 |
| 29.1@texte | livre-ouvrir |
| 29.2 | scene-vide ; colonnes "« Suisses »" "« Landleute »" ; colonne-accent 1 |
| 29.2@suissesses | foule ch -3.5 -1.0 10 5 |
| 29.3 | colonne-accent 2 |
| 29.3@gens | foule ll 3.5 -1.0 10 5 |
| 29.3@hommes | etiquette ll "Femmes et hommes" 0 2.6 |
| 30.1 | scene-vide ; livre "Constitution cantonale" -3.4 0.4 |
| 30.1@modifier | mot-barre "Modifier" 2.0 1.6 |
| 30.2@sens | etiquette sens "Un sens compatible" 1.6 0.0 |
| 30.2@constitution | picto livre 5.2 -1.4 1.1 |
| 30.3@interprétation | titre "Interprétation conforme" ambre |
| 31.1 | scene-vide ; article-retirer ; carte cantons -2.6 0.2 5.4 |
| 31.1@femmes | carte-canton AI ; personnage baumann "Ursula Baumann" ambre_pale centre-droite |
| 31.1@politiques | titre "Les droits politiques" ambre ; pose baumann bras-ciel content |
| 31.2 | carte-retirer |
| 31.2@participer | liste "Landsgemeinde" |
| 31.2@districts | liste-ajouter "Districts" |
| 31.2@communes | liste-ajouter "Communes" |
| 32.1 | scene-vide ; frise ; point 0.5 "27 novembre 1990" |
| 32.1@uniquement | zone 0.5 1 vert |
| 32.1@avenir | etiquette av "Pour l'avenir" 3.2 0.3 |
| 32.2@décisions | picto urne -4.6 0.9 |
| 32.2@conservent | picto coche -2.8 0.9 0.9 ; etiquette pa "Restent valables" -3.6 2.2 |
| 32.3@cause | picto parlement 0 1.3 1.1 |
| 32.3@cantonales | repere-marquer 4 vert |
| 33.1 | scene-vide ; repere-retirer ; foule peuple -2.8 0.2 24 8 |
| 33.1@démocratie | etiquette dd "Démocratie directe" -2.8 1.9 |
| 33.1@constitution | livre "Constitution fédérale" 3.6 0.4 |
| 33.2@décision | picto main_levee -2.8 -1.8 |
| 33.2@contrôle | picto loupe 0.7 0.4 1.0 |
| 33.2@supérieurs | titre "Même la majorité" ambre |
| 34.1 | scene-vide ; livre "Constitution cantonale" -3.6 0.4 |
| 34.1@interprétation | livre-ouvrir ; titre "Interpréter" |
| 34.2@évoluer | titre "Un sens qui évolue" |
| 34.2@société | foule soc 3.4 0.4 10 5 |
| 34.3@autrefois | etiquette hier "Hier : admise" 0 -1.8 |
| 34.3@incompatible | etiquette hier "Aujourd'hui : incompatible" 0 -1.8 |
| 35.1 | scene-vide ; etiquette auj "Aujourd'hui" 0 2.6 ; livre "Constitution fédérale" -3.6 0.4 |
| 35.1@article | article "Art. 8 al. 3 Cst." |
| 35.1@constitution | livre-ouvrir |
| 35.2 | picto balance 3.4 0.6 1.4 |
| 35.2@égaux | etiquette auj "Égaux en droit" 0 2.6 |
| 36.1 | scene-vide ; carte cantons petite |
| 36.1@régler | carte-cantons-tous |
| 36.1@trente | article "Art. 39 Cst." ; etiquette e39 "Leurs votes, leurs règles" 3.0 1.4 |
| 36.2@respecter | etiquette e39 "Dans le respect du droit fédéral" 2.6 1.4 ; livre "Constitution fédérale" 2.6 -0.6 |
| 36.2@cinquante | article "Art. 51 Cst." |
| 36.3@essentielle | titre "Essentielle, pas absolue" ambre |
| 37.1 | scene-vide ; article-retirer ; decor tribunal ; personnage juge "Le juge" violet droite ; placer juge 3 |
| 37.1@confusion | titre "Une confusion fréquente" |
| 37.2@annulé | mot-barre "Vote annulé" -3.0 1.2 |
| 37.3@réécrit | mot-barre "Texte réécrit" -3.0 -0.1 |
| 38.1@subtile | effacer-titres ; titre "Plus subtil" ambre ; pose juge pointe |
| 38.2 | scene-vide ; article "Art. 16 Cst. AI" ; livre "Constitution cantonale" -3.4 0.4 |
| 38.2@respecte | etiquette t "Son texte" -3.4 2.5 |
| 38.2@garanties | picto balance 3.4 0.6 1.3 ; etiquette g "Garanties fédérales" 3.4 2.5 |
| 38.3@reconnaître | foule femmes 0 0.4 10 5 |
| 38.3@formellement | etiquette-retirer t ; etiquette-retirer g ; titre "Sans changer un mot" ambre |
| 39.1 | scene-vide ; article-retirer ; titre "Deux principes" |
| 39.2@compétence | carte cantons petite |
| 39.2@limites | etiquette p1 "Dans les limites fédérales" 2.8 1.2 |
| 39.3@égalité | picto balance 1.4 -0.6 1.1 |
| 39.3@politiques | picto urne 4.4 -0.6 ; etiquette p2 "L'égalité pour voter aussi" 2.8 -2.0 |
| 40.1 | scene-vide ; arret-retirer ; titre "Une question pour finir" |
| 40.1@quarante | personnage sonderegger "Mario Sonderegger" bleu_clair gauche ; picto bulletin -4.5 0.5 0.6 ; tenir sonderegger bulletin aussitot |
| 40.1@qualité | etiquette q "Qualité pour recourir ?" 2.2 0.8 |
| 40.2 | effacer-titres |
| 40.2@aspect | etiquette q2 "Quel droit en jeu ?" 2.2 -0.6 |
| 40.2@jeu | visage sonderegger surpris |
| 41.1 | scene-vide ; picto stylo -2.0 0.2 1.3 ; etiquette com "Votre réponse en commentaire" 0 2.2 |
| 41.2@solution | picto livre 2.4 0.2 1.3 ; etiquette com "Dans la description" 0 2.2 |
| 41.2@arrêt | arret "ATF 116 Ia 359" |
| 41.3@étude | titre "L'étude du droit" |
