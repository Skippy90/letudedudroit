# Visuels — Arrêts, vidéo 3 : Une vignette sous film adhésif : « Je ne savais pas » ?

Ce fichier pilote les schémas Manim (`render/manim/video.py`). Vocabulaire des actions : `render/manim/README.md`.

Style « scène » : une rue d'Évian (décor rue), la traversée du lac en bateau (pictogramme des vagues), puis le poste de douane de Saint-Gingolph (décor rue, enseigne « Douane »). L'automobiliste est une silhouette sans visage turquoise (« X. », comme dans l'arrêt) ; les gardes-frontière, une silhouette bleu clair (« Douane ») ; le juge, une silhouette violette. La vignette n'a pas de pictogramme dans la charte : elle est nommée par une étiquette à côté de la voiture. Pense-bête en haut à droite pendant la réponse du Tribunal fédéral : « Lieu », « Falsification », « Intention », « Erreur » (vert : admis contre l'automobiliste ; gris : l'erreur est écartée). Bloc de l'arrêt à côté de l'article.

| Moment | Actions |
| --- | --- |
| 1.1 | decor rue ; picto voiture -3.4 -1.7 ; etiquette lieu "Évian, 2013" -3.6 1.7 |
| 1.2 | personnage x "X." turquoise centre-droite ; placer x 1 |
| 2.1 | scene-vide ; picto vagues -2.6 -1.2 ; etiquette lieu "Vers Lausanne" -2.6 0.4 ; personnage x "X." turquoise droite |
| 2.2 | etiquette vignette "Vignette" 2.0 1.7 |
| 2.3 | etiquette film "Film adhésif" 2.0 1.0 |
| 3.1 | scene-vide ; decor rue ; picto voiture -3.4 -1.7 ; personnage x "X." turquoise centre-droite ; placer x 1 ; etiquette lieu "Retour en France" -3.6 1.7 |
| 3.2 | etiquette etape "Décollée du support" 3.4 1.7 |
| 4.1 | etiquette etape "Sous film adhésif" 3.4 1.7 |
| 4.2 | etiquette etape "Bords découpés" 3.4 1.7 |
| 4.3 | etiquette etape "Sur le pare-brise" 3.4 1.7 ; picto-deplacer voiture -2.4 -1.7 |
| 5.1 | scene-vide ; decor rue Douane ; picto voiture -5.4 -1.7 ; etiquette lieu "Vers la Suisse" -3.6 1.7 |
| 5.2 | picto-deplacer voiture -2.2 -1.7 ; etiquette lieu "Saint-Gingolph (VS)" -3.6 1.7 ; personnage douane "Douane" bleu_clair droite ; placer douane 3 |
| 5.3 | accent douane ; etiquette decouverte "Vignette modifiée" -2.2 -0.3 |
| 6.1 | scene-vide ; titre "Condamné" ; article "Art. 245 CP" ; personnage x "X." turquoise gauche |
| 6.2 | picto pieces 3.2 -0.4 ; sous-titre "Peine pécuniaire avec sursis" |
| 7.1 | effacer-titres ; titre "Une vignette, un timbre ?" |
| 7.3 | picto voiture 3.2 1.0 ; sous-titre "Preuve de la redevance payée" |
| 7.4 | effacer-titres ; titre "Un timbre officiel de valeur" ; picto coche 0.4 -0.4 |
| 8.1 | scene-vide ; picto prison -2.6 -0.4 ; picto pieces 2.6 -0.4 ; titre "Aujourd'hui : cinq ans au plus" |
| 8.2 | sous-titre "À l'époque : trois ans au plus" |
| 9.1 | scene-vide ; article-retirer ; arret "ATF 141 IV 336" ; personnage x "X." turquoise gauche ; titre "Recours au Tribunal fédéral" |
| 9.2 | effacer-titres ; titre "Plusieurs arguments" |
| 9.3 | bulle x "Illicite, moi ?" |
| 10.1 | bulle x "Au pire, une amende" |
| 10.2 | effacer-titres ; titre "Erreur sur l'illicéité ?" ambre |
| 11.1 | scene-vide ; repere-liste "Lieu" "Falsification" "Intention" "Erreur" ; repere-marquer 1 ambre ; titre "D'abord, d'autres questions" ; personnage juge "Le juge" violet centre-droite |
| 11.2 | effacer-titres ; titre "Modifiée en France" ; picto voiture -3.6 -1.2 |
| 11.3 | effacer-titres ; titre "Juge suisse compétent ?" |
| 12.2 | effacer-titres ; etiquette but "Utilisation en Suisse" -3.6 0.4 |
| 12.3 | etiquette-retirer but ; titre "Rattaché à la Suisse" ; repere-marquer 1 vert |
| 12.4 | article "Art. 8 CP" ; sous-titre "Par analogie : alinéa 2" |
| 13.1 | scene-vide ; article-retirer ; repere-marquer 2 ambre ; titre "Falsification ?" ; picto voiture -3.0 -0.8 |
| 13.2 | sous-titre "Loi de l'époque" |
| 13.3 | etiquette valable "Plus valable" 1.0 0.4 |
| 14.1 | etiquette-retirer valable ; etiquette apparence "Fausse validité" 1.4 -0.6 |
| 14.2 | effacer-titres ; titre "Pas un bricolage grossier" ; repere-marquer 2 vert |
| 15.1 | scene-vide ; repere-marquer 3 ambre ; titre "L'intention" ; personnage x "X." turquoise gauche |
| 15.2 | bulle x "Protéger mon pare-brise" |
| 15.3 | picto voiture 3.6 -1.6 |
| 16.1 | effacer-bulle x ; etiquette savait "Il savait" 3.6 0.0 |
| 16.2 | effacer-titres ; titre "Il manipulait la vignette" |
| 17.1 | etiquette-retirer savait ; effacer-titres ; titre "Le motif ne change rien" |
| 17.2 | effacer-titres ; titre "Il compte pour la peine" ; repere-marquer 3 vert |
| 18.1 | scene-vide ; repere-marquer 4 ambre ; titre "L'erreur sur l'illicéité" ambre ; personnage x "X." turquoise gauche |
| 18.2 | article "Art. 21 CP" |
| 19.1 | scene-vide ; personnage x "X." turquoise gauche ; titre "Inévitable : pas coupable" |
| 19.2 | bulle x "Au moment d'agir" |
| 19.3 | effacer-bulle x ; effacer-titres ; titre "Évitable : peine atténuée" ; picto prison 3.5 -1.2 |
| 20.1 | scene-vide ; personnage x "X." turquoise gauche ; titre "Ce qu'il faut" |
| 20.2 | effacer-titres ; titre "Se croire en droit" ambre |
| 20.3 | bulle x "J'ai le droit" |
| 21.1 | effacer-bulle x ; effacer-titres ; mot-barre "Pas punissable" 3.0 0.4 |
| 21.2 | mot-barre "Pas de sanction" 3.0 -1.2 |
| 22.1 | scene-vide ; personnage x "X." turquoise gauche ; titre "Ce qu'il savait" ; bulle x "Collée directement" |
| 22.2 | bulle x "Au pire, une amende" |
| 23.1 | effacer-titres ; titre "Conscient de l'illicéité" ; picto coche 3.4 -0.4 |
| 24.1 | scene-vide ; personnage x "X." turquoise gauche ; mot-barre "L'article exact" 1.0 0.4 ; mot-barre "La sanction" 1.0 -1.2 |
| 24.2 | scene-vide ; article "Art. 245 CP" ; titre "Rien écrit au dos du support" ; picto document 0 -0.4 |
| 25.1 | scene-vide ; article-retirer ; titre "Grief rejeté" ; personnage juge "Le juge" violet centre-droite |
| 25.2 | repere-marquer 4 gris ; sous-titre "Pas d'erreur" ; accent juge |
| 26.1 | scene-vide ; repere-retirer ; titre "Une frontière nette" ; personnage x "X." turquoise gauche |
| 26.2 | retirer x ; colonnes "Ignorer l'interdit" "Ignorer la peine" ; colonne-accent 1 ; picto danger -3.5 -1.2 |
| 26.3 | colonne-accent 2 ; picto pieces 3.5 -1.2 |
| 27.1 | colonne-eteindre 2 ; effacer-titres ; titre "Pas de sanction : insuffisant" |
| 27.2 | effacer-titres ; titre "Se croire en droit" ambre |
| 28.1 | scene-vide ; titre "Autre leçon" ; personnage juge "Le juge" violet droite |
| 28.2 | effacer-titres ; titre "Une question de fait" |
| 28.3 | sous-titre "Sauf arbitraire" ; accent juge |
| 29.1 | scene-vide ; arret-retirer ; titre "Le piège classique" ; personnage x "X." turquoise gauche ; bulle x "Pas si grave" |
| 30.1 | effacer-bulle x ; effacer-titres ; mot-barre "Pas si grave, donc excusé" 1.6 -0.4 |
| 30.2 | sous-titre "Il faut se croire en droit" |
| 31.1 | scene-vide ; article "Art. 21 CP" ; titre "Retenons" ; livre "Code pénal" 4.6 |
| 31.2 | liste-ajouter "Se croire en droit" |
| 31.3 | liste-ajouter "Ignorer la peine : insuffisant" |
| 32.1 | renvoi "vidéo 7" ; accent livre |
| 33.1 | scene-vide ; article-retirer ; titre "Une question pour finir" ; personnage x "X." turquoise gauche |
| 33.2 | effacer-titres ; titre "Seulement une amende ?" ambre ; bulle x "Au pire, une amende" |
| 33.3 | effacer-titres ; titre "Pourquoi pas d'erreur ?" ambre |
| 33.4 | effacer-titres ; titre "Que savait-il de la pose ?" ambre |
| 33.5 | accent x |
| 34.1 | scene-vide ; livre "Code pénal" 0 -0.5 ; titre "L'étude du droit" ; sous-titre "Tout est dans la description" |
| 34.2 | accent titre |
