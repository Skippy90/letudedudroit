# Visuels — Vidéo 2 : Pas de peine sans loi

Ce fichier pilote les schémas Manim (`render/manim/video.py`). Vocabulaire des actions : `render/manim/README.md`.

Colonne « Moment » : `ligne.phrase` du script, `ligne.phrase+secondes`, ou `ligne.phrase@mot` (au moment où ce mot est prononcé dans la narration enregistrée). Plusieurs actions d'un même moment sont séparées par `;`.

Style « scène » : les cas se jouent dans un décor (appartement, salle d'audience), les mots-clés apparaissent sur le mot prononcé, et un pense-bête en haut à droite suit les trois exigences de l'article premier (« Texte », « Précis », « Avant ») : ambre pour l'exigence dont on parle, gris quand elle manque dans l'histoire de Tom. Des sous-titres sont incrustés au montage.

Personnages : Sami bleu clair, Tom ambre pâle, la sœur de Sami rose, le juge turquoise, Nora violet.

Écarts assumés avec la colonne « À l'écran » du script, pour rester dans la charte : pas de ligne d'eau (ligne 2 : le lac passe par la bulle de pensée), pas de loupe (ligne 13 : une bande ambre parcourt les pages du livre), les cantons sont deux colonnes et non des silhouettes (lignes 35 et 36).

| Moment | Actions |
| --- | --- |
| 1.1 | decor appartement ; etiquette lieu "Fribourg, samedi matin" -2.6 2.45 |
| 1.2 | personnage sami "Sami" bleu_clair gauche ; placer sami -3 |
| 1.2@déménage | marcher sami 1 |
| 1.3@tom | etiquette-retirer lieu ; etiquette promesse "Tom a promis de venir" 1.1 1.4 |
| 1.3@cartons | accent sami |
| 2.1 | etiquette-retirer promesse ; personnage tom "Tom" ambre_pale droite ; placer tom -1 |
| 2.1@message | picto telephone -0.6 -0.6 |
| 2.1@désolé | parole tom "Désolé, je suis malade." |
| 2.2@réalité | effacer-parole tom ; picto-retirer telephone |
| 2.2@part | marcher tom -3 |
| 2.2@lac | bulle tom "Une journée au lac" |
| 3.1 | retirer tom ; personnage soeur "Sa sœur" rose centre ; placer soeur -1 |
| 3.1@déménagement | accent soeur |
| 3.2@soir | picto lune -2.6 1.3 |
| 3.2@vérité | etiquette verite "Tom était au lac" 1.1 1.4 |
| 3.3@furieux | etiquette-retirer verite ; picto tension 0.8 1.6 |
| 4.1 | picto-retirer tension ; retirer soeur ; picto telephone 2.6 -0.6 |
| 4.1@menti | parole sami "Tu m'as menti. Je porte plainte !" |
| 5.1 | scene-vide ; personnage tom "Tom" ambre_pale centre |
| 5.1@infraction | titre "Infraction ?" ambre |
| 5.2 | sous-titre "Mentir à un ami, est-ce puni ?" |
| 5.3@tête | accent tom |
| 6.1 | scene-vide ; batiment ; renvoi "vidéo 1" |
| 6.1@typicité | etage 1 ambre |
| 6.2@loi | titre "La loi décrit-elle l'acte ?" |
| 7.1 | scene-vide ; titre "La règle du premier étage" |
| 7.2@article | livre ; article "Art. 1 CP" |
| 7.3@phrase | etiquette phrase "Une seule phrase" 0 2.35 |
| 8.1 | etiquette-retirer phrase ; livre-ouvrir |
| 8.2+1.2 | titre "expressément réprimé par la loi" mot-a-mot |
| 9.1 | livre-retirer ; titre "Pas de loi, pas de peine" |
| 9.2@légalité | sous-titre "Le principe de la légalité" |
| 10.1 | effacer-titres ; colonnes "Peine" "Mesure" ; colonne-accent 1 |
| 10.1@mesure | colonne-accent 2 |
| 10.1@traitement | etiquette traitement "Par exemple, un traitement" 3.5 -0.4 |
| 10.2@douze | renvoi "vidéo 12" |
| 11.1 | scene-vide ; titre "Trois exigences" |
| 11.2@texte | liste-ajouter "1. Un texte" |
| 11.3@décrit | liste-ajouter "2. Qui décrit l'acte" |
| 11.4@existait | liste-ajouter "3. Qui existait déjà" |
| 12.1 | effacer-titres ; repere-liste "Texte" "Précis" "Avant" |
| 12.1@texte | repere-marquer 1 ambre ; titre "Un texte de loi" |
| 12.2@avis | mot-barre "L'avis du juge" 0 0.9 |
| 12.3@morale | mot-barre "La morale" 0 -0.5 |
| 12.4 | scene-vide ; personnage juge "Juge" turquoise centre |
| 12.4@inventer | titre "Il n'invente pas d'infraction" |
| 13.1 | scene-vide ; livre ; titre "Un article contre le mensonge ?" |
| 13.1@punit | livre-ouvrir |
| 13.2 | livre-chercher |
| 13.2@mentir | sous-titre "Aucune infraction « mentir »" |
| 14.1 | scene-vide ; personnage tom "Tom" ambre_pale centre |
| 14.1@blessant | etiquette blessant "Blessant" -2.6 1.2 |
| 14.2@moralement | etiquette morale "Moralement condamnable" 1.1 2.3 |
| 14.3 | scene-vide ; colonnes "Morale" "Loi pénale" |
| 14.3@loi | colonne-accent 1 ; colonne-eteindre 2 |
| 15.1 | scene-vide ; batiment |
| 15.1@texte | fleche 1 |
| 15.2@franchi | etage 1 gris ; repere-marquer 1 gris |
| 15.3 | titre "Pas d'infraction" |
| 16.1 | scene-vide ; repere-marquer 2 ambre ; titre "Le texte doit décrire l'acte" |
| 16.1@décrire | livre |
| 16.2@expressément | livre-ouvrir ; effacer-titres ; titre "« Expressément »" ambre |
| 17.1 | scene-vide ; personnage tom "Tom" ambre_pale centre ; titre "Pas le mensonge en général" |
| 17.2@certains | effacer-titres ; etiquette t307 "Faux témoignage" -3.6 1.4 |
| 17.2@précision | etiquette t146 "Escroquerie" 3.4 1.0 |
| 17.3@conditions | titre "Chacun ses conditions" |
| 18.1 | scene-vide ; rembobiner |
| 18.2 | decor tribunal ; personnage juge "Juge" turquoise droite ; placer juge 3 ; personnage tom "Tom" ambre_pale gauche ; placer tom -4 |
| 18.2@tribunal | etiquette lieu "Au tribunal" -2.6 2.45 |
| 18.2@témoin | marcher tom -1 |
| 19.1@article | etiquette temoin "Témoin" -1.6 0.3 ; article "Art. 307 CP" |
| 19.2@témoin | accent tom |
| 19.2@déposition | etiquette depo "Déposition fausse" -1.6 0.95 |
| 19.2@justice | picto coche 1.0 0.95 |
| 20.1 | scene-vide ; article-retirer ; rembobiner |
| 20.2 | decor appartement ; personnage sami "Sami" bleu_clair gauche ; placer sami -2 ; personnage tom "Tom" ambre_pale droite ; placer tom 2 |
| 20.2@habile | bulle tom "Un plan habile" |
| 20.2@argent | jetons sami tom |
| 21.1@escroquerie | effacer-bulle tom ; etiquette escroc "Escroquerie" 3.2 0.5 |
| 21.1@cent | article "Art. 146 CP" |
| 21.2@mentir | titre "Mentir ne suffit pas" |
| 22.1 | scene-vide ; personnage sami "Sami" bleu_clair gauche ; personnage tom "Tom" ambre_pale centre-gauche |
| 22.1@tromperie | case "Tromperie astucieuse" |
| 22.2@intérêts | case "Préjudice financier" ; jetons sami tom |
| 22.3@enrichir | case "Volonté de s'enrichir" |
| 23.1 | scene-vide ; article-retirer ; personnage tom "Tom" ambre_pale gauche ; cases "Tribunal" "Argent" |
| 23.1@tom | bulle tom "Au lac" |
| 23.1@tribunal | cocher 1 gris |
| 23.2@argent | cocher 2 gris |
| 23.3 | effacer-bulle tom ; repere-marquer 2 gris ; titre "Aucune description ne correspond" |
| 24.1 | scene-vide ; personnage juge "Juge" turquoise gauche ; livre |
| 24.1@interpréter | livre-ouvrir |
| 24.1@largement | etiquette interpreter "Interpréter" 0 2.2 |
| 24.2@ajouter | mot-barre "Ajouter" 4.6 0.4 |
| 24.3 | scene-vide ; colonnes "Mensonge de Tom" "Escroquerie" |
| 24.3@ressemble | titre "Ressembler ne suffit pas" |
| 25.1 | scene-vide ; cases "Tromperie astucieuse" "Préjudice financier" "Volonté de s'enrichir" ; cocher 1 vert ; cocher 2 vert |
| 25.1@description | cocher 3 gris |
| 25.2 | titre "Même proche" |
| 25.3 | titre "Même choquant" |
| 26.1 | scene-vide ; repere-marquer 3 ambre ; titre "Exister au moment de l'acte" |
| 26.1@moment | frise |
| 27.1 | effacer-titres ; titre "Pure fiction" ambre |
| 27.2@parlement | repere 0.65 "Nouvelle loi" |
| 28.1@samedi | point 0.25 "Mensonge" |
| 28.2 | fleche-retour 0.65 0.25 casse |
| 28.3 | titre "Non" ambre ; repere-marquer 3 gris |
| 29.1@article | article "Art. 2 CP" |
| 29.2@après | zone 0.65 1 vert |
| 30.1@passé | zone 0 0.65 gris |
| 30.2@avance | titre "Savoir à l'avance" |
| 31.1@exception | titre "Une exception" |
| 31.2@douce | titre "Une loi plus douce" ambre |
| 31.3@jugé | point 0.85 "Jugement" |
| 31.3@applique | fleche-retour 0.65 0.25 vert |
| 32.1 | scene-vide ; article-retirer ; titre "Le piège classique" |
| 32.2@souvent | effacer-titres ; livre ; sous-titre "« Pas dans le Code pénal, donc permis »" |
| 32.3@faux | barrer |
| 33.1 | scene-vide ; titre "D'autres lois fédérales" |
| 33.1@contiennent | livres "Code pénal" "Circulation routière" "Autres lois" |
| 33.2@article | article "Art. 333 CP" |
| 33.2@générales | accent livres |
| 34.1@circulation | livres-surligner 2 |
| 34.2@nonante | article "Art. 90 LCR" |
| 35.1 | scene-vide ; article-retirer ; colonnes "Genève" "Vaud" |
| 35.1@punir | titre "Les cantons aussi" |
| 35.2@article | article "Art. 335 CP" |
| 36.1@cantonales | titre "Règles cantonales" ambre |
| 36.2@genève | etiquette ge "Puni" -3.5 -0.5 |
| 36.2@vaud | etiquette vd "Pas forcément" 3.5 -0.5 |
| 37.1 | scene-vide ; article-retirer ; titre "Partout : il faut un texte" |
| 37.2 | effacer-titres ; livres "Code pénal" "Circulation routière" "Autres lois" |
| 38.1 | scene-vide ; decor appartement ; personnage sami "Sami" bleu_clair gauche ; placer sami -2 |
| 38.2@déçu | bulle sami "Déçu" |
| 38.3 | personnage tom "Tom" ambre_pale droite ; placer tom 1 |
| 38.3@réprime | etiquette constat "Aucun texte" 0.6 1.2 |
| 38.4@punir | etiquette peine "Pas de peine" 0.6 0.5 |
| 39.1 | scene-vide ; colonnes "Morale" "Loi pénale" |
| 39.1@bien | colonne-accent 1 |
| 39.2@occupe | colonne-eteindre 2 |
| 40.1 | scene-vide ; article "Art. 1 CP" ; titre "Les trois exigences" ; repere-marquer 1 neutre ; repere-marquer 2 neutre ; repere-marquer 3 neutre |
| 40.2 | effacer-titres ; liste-ajouter "1. Un texte" ; repere-marquer 1 ambre |
| 40.3@décrit | liste-ajouter "2. Qui décrit l'acte" ; repere-marquer 2 ambre |
| 40.4@existait | liste-ajouter "3. Qui existait déjà" ; repere-marquer 3 ambre |
| 41.1 | scene-vide ; article-retirer ; repere-retirer ; titre "Une question pour finir" |
| 41.2 | effacer-titres ; personnage nora "Nora" violet centre ; frise |
| 41.2@nora | point 0.15 "1er mars" |
| 42.1@juin | repere 0.5 "1er juin : nouvelle loi" |
| 42.2@juillet | point 0.8 "1er juillet" |
| 43.1 | questions |
| 43.2@date | accent frise |
| 43.3 | titre "Réponse en commentaire" |
| 44.1 | scene-vide ; titre "L'étude du droit" ; sous-titre "Tout est dans la description" |
| 44.2 | accent titre |
