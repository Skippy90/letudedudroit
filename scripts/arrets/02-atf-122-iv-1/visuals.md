# Visuels — Arrêts, vidéo 2 : Un mari violent, tué pendant son sommeil : légitime défense ?

Ce fichier pilote les schémas Manim (`render/manim/video.py`). Vocabulaire des actions : `render/manim/README.md`.

Style « scène » : les faits se jouent dans une cage d'escalier d'immeuble, la nuit (décor escalier, faute de décor « logement » ou « chambre ») ; l'épouse est une silhouette turquoise, le mari une silhouette bleu clair, le juge une silhouette violette. Les violences sont nommées par des étiquettes, jamais dessinées ; un seul éclair de dommage, au moment de la blessure qui mène à l'hôpital. Aucune arme n'est dessinée ; l'acte n'est pas montré : la lune, puis l'écran se vide. Les autorités sont la pyramide ; le fait justificatif, le bouclier ; l'état d'esprit, la bulle. Bloc de l'arrêt à côté de l'article.

| Moment | Actions |
| --- | --- |
| 1.1 | decor escalier ; etiquette lieu "Valais, 1993" -4.4 2.4 |
| 1.2 | personnage epouse "L'épouse" turquoise centre-gauche ; placer epouse -3 ; personnage mari "Le mari" bleu_clair centre ; placer mari 2 ; etiquette enfants "Cinq enfants" 3.6 2.4 |
| 2.1 | etiquette-retirer enfants ; etiquette-retirer lieu ; accent mari ; etiquette brutal "Brutal" 0.6 2.4 |
| 2.2 | etiquette recluse "Recluse" -4.4 2.4 |
| 3.1 | etiquette-retirer brutal ; etiquette-retirer recluse ; etiquette coups "Chaque semaine" -2.0 2.4 |
| 4.1 | etiquette coups "Fin janvier" -2.0 2.4 |
| 4.2 | dommage epouse ; etiquette hopital "Hospitalisée" 3.6 2.4 |
| 5.1 | etiquette coups "Malnutrition, hématomes" -2.0 2.4 ; etiquette-retirer hopital |
| 5.2 | etiquette coups "Menaces de mort" -2.0 2.4 |
| 6.1 | etiquette-retirer coups ; picto lune -4.6 2.3 ; etiquette soir "15 mars, le soir" -1.6 2.4 |
| 6.2 | etiquette revolver "Un revolver, « pour elle »" 3.4 2.4 |
| 7.1 | etiquette-retirer soir ; etiquette revolver "Il l’aurait déjà tuée" 2.4 2.4 |
| 7.2 | etiquette revolver "L'arme sous l'oreiller" 2.4 2.4 |
| 8.1 | etiquette-retirer revolver ; bulle epouse "Il va me tuer" |
| 8.2 | etiquette dort "Il s'endort" 2.4 2.4 |
| 9.1 | effacer-bulle epouse ; etiquette dort "Vingt minutes" 2.4 2.4 |
| 9.2 | scene-vide ; picto lune 0 0.6 |
| 9.3 | picto-retirer lune |
| 10.1 | personnage epouse "L'épouse" turquoise gauche ; etiquette fille "Sa fille aînée" 0.6 1.6 |
| 10.1+2.5 | etiquette police "Police" 3.6 1.6 |
| 11.1 | scene-vide ; personnage epouse "L'épouse" turquoise gauche ; titre "Meurtre passionnel" ; pyramide ; pyramide-niveau 1 ambre |
| 11.2 | pyramide-niveau 2 ambre |
| 12.1 | retirer-pyramide ; sous-titre "Émotion violente, profond désarroi" |
| 12.2 | article "Art. 113 CP" ; picto prison 3.4 -0.4 |
| 13.1 | scene-vide ; article-retirer ; arret "ATF 122 IV 1" ; personnage epouse "L'épouse" turquoise gauche ; titre "Recours au Tribunal fédéral" |
| 13.2 | bouclier 2.6 0.2 ; bulle epouse "Une attaque ?" |
| 14.1 | effacer-titres ; titre "Une question simple" |
| 14.2 | effacer-titres ; effacer-bulle epouse ; titre "Se défendre contre un homme endormi ?" ambre |
| 15.1 | scene-vide ; titre "Légitime défense ?" ; personnage juge "Le juge" violet gauche |
| 15.2 | sous-titre "Écartée" ; accent juge |
| 16.1 | case "Attaque" ; case "Ou attaque imminente" |
| 16.2 | article "Art. 15 CP" |
| 17.1 | scene-vide ; personnage mari "Le mari" bleu_clair gauche ; picto lune -2.4 1.6 ; etiquette dort "Il dormait" -4.5 2.6 |
| 17.2 | case "Attaque" ; cocher 1 gris |
| 17.3 | case "Attaque imminente" ; cocher 2 gris |
| 18.1 | etiquette dort "Vingt minutes" -4.5 2.6 |
| 18.2 | mot-barre "Cru à une attaque" 2.6 -0.8 |
| 19.1 | scene-vide ; article-retirer ; titre "Le Tribunal fédéral continue" ; personnage juge "Le juge" violet droite |
| 19.2 | bouclier -3.0 0.2 ; sous-titre "L'examen continue" |
| 19.3 | effacer-titres ; titre "L'état de nécessité" ambre |
| 19.4 | sous-titre "Licite, ou excusé" |
| 20.1 | scene-vide ; colonnes "Attaque" "Danger" ; picto danger 0 -1.4 |
| 20.2 | colonne-accent 1 ; titre "Agression en cours ou imminente" |
| 20.3 | colonne-accent 2 ; effacer-titres ; titre "Risque d'une nouvelle agression" |
| 21.1 | effacer-titres ; titre "Un danger imminent" |
| 21.2 | sous-titre "Ni passé ni futur : actuel et concret" |
| 22.1 | scene-vide ; frise ; titre "Un danger peut durer" |
| 22.2 | effacer-titres ; titre "Doctrine allemande : danger permanent" |
| 23.1 | etiquette tyran "Tyran domestique" -3.6 0.8 |
| 23.2 | picto danger 3.6 0.8 |
| 24.1 | sous-titre "Imminence appréciée plus largement" |
| 25.1 | effacer-titres ; titre "Ici" ; point 0.15 "Coups" ; point 0.45 "Hôpital" ; point 0.7 "Menaces" |
| 25.2 | point 0.9 "Revolver" ; effacer-titres ; titre "Danger durable et imminent ?" ambre |
| 26.1 | scene-vide ; titre "Pas d'autre issue ?" ; personnage juge "Le juge" violet droite |
| 26.2 | liste-ajouter "Police" ; liste-ajouter "Juge" ; liste-ajouter "Service social" |
| 27.1 | etiquette issue "Sans issue" 1.8 1.4 |
| 27.2 | effacer-titres ; titre "Contradiction" ambre ; accent juge |
| 28.1 | effacer-titres ; etiquette-retirer issue ; titre "Aggraver le danger ?" ; picto danger 1.8 1.4 |
| 28.2 | sous-titre "Pas examiné" ; accent juge |
| 29.1 | scene-vide ; personnage mari "Le mari" bleu_clair centre-gauche ; personnage epouse "L'épouse" turquoise centre-droite ; titre "Deux vies" |
| 29.2 | sous-titre "Valeur comparable" |
| 30.1 | effacer-titres ; mot-barre "Licite" 0 -1.4 |
| 30.2 | titre "Excusé, sans faute ?" ambre |
| 31.1 | scene-vide ; titre "Arrêt cantonal annulé" ; pyramide ; pyramide-niveau 3 ambre ; personnage juge "Le juge" violet gauche |
| 31.2 | pyramide-niveau 3 neutre ; pyramide-niveau 2 ambre ; effacer-titres ; titre "Renvoi au canton" |
| 32.1 | effacer-titres ; titre "Nécessité excusable ?" |
| 32.2 | retirer-pyramide ; effacer-titres ; titre "La suite n'est pas publiée" ; accent juge |
| 33.1 | scene-vide ; titre "Aujourd'hui, dans la loi" ; livre "Code pénal" -3.6 |
| 33.2 | article "Art. 17 CP" ; bouclier 3.4 0 ; sous-titre "Licite : intérêts prépondérants" |
| 34.1 | article "Art. 18 CP" ; effacer-titres ; titre "Sinon : article 18" ; sous-titre "Danger imminent, sans autre issue" |
| 34.2 | effacer-titres ; titre "Sacrifice exigible : peine atténuée" |
| 34.3 | sous-titre "Sinon : pas de culpabilité" ; accent livre |
| 35.1 | scene-vide ; article-retirer ; arret "ATF 122 IV 1" ; colonnes "Attaque" "Danger" ; picto danger 0 -1.4 ; titre "Attaque ou danger" |
| 35.2 | renvoi "vidéo 6" ; colonne-accent 2 ; effacer-titres ; titre "Le danger imminent, défini" |
| 36.1 | scene-vide ; titre "Une limite claire" ; personnage juge "Le juge" violet gauche |
| 36.2 | mot-barre "Querelles de couple" 2.6 0.8 ; mot-barre "Remplacer un divorce" 2.6 -0.6 |
| 37.1 | scene-vide ; personnage juge "Le juge" violet gauche ; titre "Pas de justice privée" |
| 37.2 | sous-titre "Mais un martyre peut excuser" ; accent juge |
| 38.1 | scene-vide ; arret-retirer ; titre "Le piège classique" ; personnage juge "Le juge" violet gauche ; bulle juge "Légitime défense ?" |
| 38.2 | mot-barre "Pas d'attaque, rien à examiner" 2.6 -0.4 |
| 39.1 | scene-vide ; personnage juge "Le juge" violet gauche ; bulle juge "Un danger ?" |
| 39.2 | effacer-titres ; titre "Examiner l'état de nécessité" ; accent juge |
| 40.1 | scene-vide ; colonnes "Attaque" "Danger" |
| 40.2 | colonne-accent 1 |
| 40.2+1 | titre "En cours ou imminente" ; picto danger 0 -1.4 |
| 41.1 | colonne-accent 2 ; effacer-titres ; titre "Un danger qui peut durer" |
| 41.2 | effacer-titres ; titre "Deux vies : excusé, pas licite" ambre |
| 42.1 | scene-vide ; titre "Une question pour finir" ; personnage juge "Le juge" violet gauche |
| 42.2 | effacer-titres ; titre "Pourquoi pas de légitime défense ?" ambre |
| 42.3 | accent juge |
| 43.1 | scene-vide ; livre "Code pénal" 0 -0.5 ; titre "L'étude du droit" ; sous-titre "Tout est dans la description" |
| 43.2 | accent titre |
