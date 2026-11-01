# Visuels — Vidéo 11 : Quelle peine ?

Ce fichier pilote les schémas Manim (`render/manim/video.py`). Vocabulaire des actions : `render/manim/README.md`.

Colonne « Moment » : `ligne.phrase` du script, éventuellement `+secondes` ou `@mot`. Plusieurs actions d'un même moment sont séparées par `;`.

Personnages : Inès rose (comme dans la vidéo 3), le juge violet, une personne aisée ambre pâle, un passant ambre pâle, Hugo bleu clair.

Style « scène » (repris le 1er novembre 2026) : le vol se rappelle devant le magasin (décor rue, enseigne « Téléphones »), puis le cas se juge au tribunal (Inès à la barre, le juge sur l'estrade). Les trois peines sont des pictogrammes au trait : la prison pour la peine privative de liberté, les pièces pour la peine pécuniaire et l'amende. Un pense-bête « Choisir / Fixer / Sursis » en haut à droite suit les trois questions du juge (ambre : en cours ; vert : réglée). L'arrêt du Tribunal fédéral s'affiche à côté de l'article quand on en parle (ligne 15).

Écarts assumés avec la colonne « À l'écran » du script, pour rester dans la charte : les calculs de jours-amende (ligne 10) et les critères (lignes 15, 22) sont des étiquettes près des personnages, sans signe de multiplication ; le choix de la peine (ligne 18) est montré par les jetons qu'Inès peut payer plutôt que par deux colonnes ; la question finale (ligne 35) se joue au tribunal (le profil de Hugo en étiquette), avec un rembobinage pour les trente mois, au lieu d'une frise.

| Moment | Actions |
| --- | --- |
| 1.1 | decor rue Téléphones ; personnage ines "Inès" rose gauche ; placer ines -3 ; renvoi "vidéo 3" |
| 1.2 | picto telephone 1.5 -1.55 ; etiquette lieu "Neuchâtel, samedi soir" -3.6 1.7 |
| 1.2+1.2 | marcher ines -1 |
| 1.2+2.4 | picto-deplacer telephone -0.6 -1.0 0.4 |
| 2.1 | scene-vide ; decor tribunal ; personnage ines "Inès" rose gauche ; placer ines -1 ; etiquette age "Vingt ans" -1.6 0.6 |
| 2.2 | etiquette age "Apprentie, jamais condamnée" -1.6 0.6 |
| 2.3 | etiquette-retirer age ; personnage juge "Le juge" violet droite ; placer juge 3 ; repere-batiment |
| 2.3+1.2 | repere-etage 1 vert ; repere-etage 2 vert ; repere-etage 3 vert ; etiquette vol "Un vol" 1.4 1.4 |
| 3.1 | etiquette-retirer vol ; titre "Une question concrète" |
| 3.2 | effacer-titres ; titre "Quelle peine ?" ambre ; accent juge |
| 3.3 | picto prison -4.2 1.4 |
| 3.4 | picto pieces -1.6 1.4 |
| 3.5 | etiquette rien "Rien du tout ?" 1.4 1.4 |
| 4.1 | scene-vide ; repere-retirer ; titre "Trois peines principales" ; picto prison -4.4 0.4 |
| 4.2 | etiquette p1 "Privative de liberté" -4.4 -0.9 |
| 4.2+1.3 | picto pieces 0 0.4 ; etiquette p2 "Pécuniaire" 0 -0.9 |
| 4.2+2.6 | picto pieces:2 4.4 0.4 ; etiquette p3 "Amende" 4.4 -0.9 |
| 5.1 | scene-vide ; personnage juge "Le juge" violet centre-droite ; titre "Deux temps" |
| 5.2 | liste-ajouter "Choisir" |
| 5.3 | liste-ajouter "Fixer" |
| 6.1 | liste-ajouter "Sursis ?" ; accent juge |
| 6.1+3.5 | effacer-titres ; repere-liste "Choisir" "Fixer" "Sursis" |
| 7.1 | scene-vide ; repere-marquer 1 ambre ; article "Art. 40 CP" ; picto prison 0 1.0 ; titre "L'enfermement" |
| 7.2 | frise ; point 0.05 "3 jours" |
| 7.2+1.2 | point 0.85 "20 ans" |
| 7.3 | repere 0.95 "À vie" |
| 8.1 | scene-vide ; article "Art. 34 CP" ; picto pieces 0 0.6 ; titre "Les jours-amende" |
| 8.2 | etiquette nombre "Nombre : la faute" -3.8 0.6 |
| 8.2+2.5 | etiquette fourchette "3 à 180" -3.8 -0.6 |
| 9.1 | effacer-titres ; etiquette montant "Montant d'un jour" 3.8 -0.6 |
| 9.2 | etiquette montant "30 à 3000 francs" 3.8 -0.6 |
| 9.3 | etiquette montant "Exception : 10 francs" 3.8 -0.6 |
| 9.4 | etiquette situation "Montant : la situation" 3.8 0.6 |
| 9.4+2.5 | picto portefeuille 3.8 -1.7 |
| 10.1 | scene-vide ; article-retirer ; titre "30 jours-amende" ; personnage ines "Inès" rose gauche |
| 10.2 | etiquette j1 "À 50 francs" -2.3 1.2 ; picto pieces -2.3 -0.2 |
| 10.2+2.2 | etiquette j1 "1500 francs" -2.3 1.2 |
| 10.3 | personnage aisee "Personne aisée" ambre_pale centre-droite ; etiquette j2 "À 1000 francs" 4.6 1.2 |
| 10.3+2.4 | picto pieces:2 4.6 -0.2 ; etiquette j2 "30 000 francs" 4.6 1.2 |
| 11.1 | etiquette-retirer j1 ; etiquette-retirer j2 ; effacer-titres ; titre "Même faute, même nombre" |
| 11.1+2 | accent aisee |
| 11.2 | effacer-titres ; titre "Même effort" ambre ; accent ines |
| 12.1 | scene-vide ; article "Art. 106 CP" ; titre "L'amende" ; renvoi "vidéo 3" ; picto parking -2.4 0.6 |
| 12.1+2 | etiquette contrav "Contraventions" -2.4 -0.6 |
| 12.2 | picto pieces 2.4 0.6 ; etiquette max "10 000 francs au plus" 2.4 -0.6 |
| 13.1 | scene-vide ; titre "Peine de substitution" ; picto prison -2.4 0.6 ; picto pieces 2.4 0.6 |
| 13.1+2.5 | etiquette duree "1 jour à 3 mois" -2.4 -0.6 |
| 13.2 | etiquette impaye "Amende impayée" 2.4 -0.6 |
| 13.2+1.5 | picto-deplacer pieces -0.4 0.6 |
| 14.1 | scene-vide ; article "Art. 139 CP" ; decor tribunal ; personnage ines "Inès" rose gauche ; placer ines -1 ; personnage juge "Le juge" violet droite ; placer juge 3 |
| 14.1+2 | picto prison -4.2 1.4 ; etiquette cinq "5 ans au plus" -4.2 0.2 |
| 14.2 | picto pieces 1.2 1.4 ; etiquette pec "Peine pécuniaire" 1.2 0.2 |
| 14.3 | accent juge |
| 15.1 | scene-vide ; article-retirer ; arret "ATF 147 IV 241" ; personnage juge "Le juge" violet centre-droite ; titre "Trois questions" |
| 15.2 | effacer-titres ; liste-ajouter "Adaptée ?" |
| 15.3 | liste-ajouter "Effets sur la vie ?" |
| 15.4 | liste-ajouter "Efficace ?" ; accent juge |
| 16.1 | scene-vide ; arret-retirer ; article "Art. 41 CP" ; titre "Un cadre" ; picto prison -3.5 0.4 ; picto pieces 3.5 0.4 |
| 16.2 | sous-titre "Préférer la prison ?" |
| 16.2+3 | etiquette deux "Deux raisons seulement" 0 -0.8 |
| 17.1 | effacer-titres ; etiquette-retirer deux ; picto-retirer pieces ; picto-deplacer prison -4.6 0.9 ; case "Détourner de récidiver" |
| 17.2 | case "Paiement impossible" |
| 17.3 | titre "Motiver en détail" ; picto document -4.6 -0.7 |
| 18.1 | scene-vide ; article-retirer ; decor tribunal ; personnage ines "Inès" rose gauche ; placer ines -1 ; personnage juge "Le juge" violet droite ; placer juge 3 ; etiquette profil "Jeune, sans antécédents" -2.2 0.6 |
| 18.1+3.5 | picto pieces 1.6 0.5 ; etiquette choix "Peine pécuniaire" 1.6 1.6 |
| 18.2 | etiquette-retirer profil ; jetons ines juge |
| 18.2+1.5 | repere-marquer 1 vert |
| 19.1 | scene-vide ; repere-marquer 2 ambre ; personnage juge "Le juge" violet centre-droite ; titre "Combien de jours ?" |
| 19.2 | article "Art. 47 CP" |
| 19.3 | effacer-titres ; titre "La culpabilité" ambre ; accent juge |
| 20.1 | liste-ajouter "Gravité" |
| 20.1+3 | liste-ajouter "Répréhensible" |
| 20.2 | liste-ajouter "Motivations" |
| 20.2+3 | liste-ajouter "Évitable ?" |
| 21.1 | scene-vide ; personnage juge "Le juge" violet centre-droite ; titre "Aussi" ; liste "Antécédents" "Situation personnelle" |
| 21.2 | liste-ajouter "Effet sur l'avenir" |
| 22.1 | scene-vide ; article-retirer ; decor tribunal ; personnage ines "Inès" rose gauche ; placer ines -1 ; personnage juge "Le juge" violet droite ; placer juge 3 ; etiquette refl "Réfléchi" -4.4 1.5 |
| 22.1+2 | picto telephone -4.4 0.4 |
| 22.2 | etiquette premier "Premier acte" -1.6 0.6 |
| 22.3 | etiquette appr "Son apprentissage" 1.7 1.5 ; accent ines |
| 22.3+2 | repere-marquer 2 vert |
| 23.1 | scene-vide ; repere-marquer 3 ambre ; personnage ines "Inès" rose gauche ; titre "Le sursis" ; picto prison 0.6 0.4 |
| 23.2 | article "Art. 42 CP" ; etiquette regle "En règle générale" 0.6 -0.9 |
| 23.3 | etiquette-retirer regle ; picto pieces 3.6 0.4 ; sous-titre "Pécuniaire, ou 2 ans au plus" |
| 24.1 | effacer-titres ; titre "Pronostic favorable" |
| 24.1+2.5 | picto coche -2.6 1.2 |
| 24.2 | sous-titre "Les antécédents" |
| 24.3 | sous-titre "Plus de 6 mois, dans les 5 ans" |
| 24.4 | sous-titre "Circonstances particulièrement favorables" |
| 24.5 | sous-titre "Réparer le dommage" |
| 25.1 | scene-vide ; article "Art. 44 CP" ; titre "Délai d'épreuve" ; frise ; point 0.1 "Jugement" |
| 25.1+1.5 | zone 0.1 0.6 vert ; sous-titre "2 à 5 ans" |
| 25.2 | point 0.6 "Fin" ; picto prison 4.6 0.6 ; etiquette jamais "Jamais exécutée" 4.6 -0.6 |
| 26.1 | article "Art. 46 CP" ; etiquette-retirer jamais ; point 0.45 "Nouvelle infraction" |
| 26.2 | zone 0.1 0.6 gris ; effacer-titres ; titre "Sursis révoqué" |
| 26.3 | sous-titre "Peine exécutée" ; accent frise |
| 27.1 | scene-vide ; article "Art. 43 CP" ; titre "Le sursis partiel" ; picto prison 0 -0.8 |
| 27.2 | picto-retirer prison ; colonnes "Exécutée" "Suspendue" ; sous-titre "1 à 3 ans" |
| 27.2+2.5 | picto prison -3.5 -0.6 |
| 28.1 | effacer-titres ; colonne-accent 1 ; etiquette moitie "Moitié au plus" -3.5 -1.9 |
| 28.2 | colonne-accent 2 ; etiquette six "6 mois au moins" 3.5 -1.9 |
| 29.1 | scene-vide ; article-retirer ; decor tribunal ; personnage ines "Inès" rose gauche ; placer ines -1 ; personnage juge "Le juge" violet droite ; placer juge 3 ; etiquette verdict "Pécuniaire avec sursis" 1.2 1.5 |
| 29.1+3 | etiquette epreuve "2 ans d'épreuve" -1.6 0.6 |
| 29.2 | picto pieces -4.4 0.8 ; repere-marquer 3 vert |
| 30.1 | scene-vide ; titre "Le piège classique" ; personnage passant "Un passant" ambre_pale gauche |
| 30.2 | effacer-titres ; parole passant "Du sursis : pas puni" |
| 30.3 | effacer-parole passant ; mot-barre "Pas puni" 2.5 0.4 |
| 31.1 | scene-vide ; personnage ines "Inès" rose gauche ; titre "Bel et bien condamnée" |
| 31.2 | retirer ines ; frise ; point 0.1 "Jugement" ; point 0.6 "Fin" ; sous-titre "La peine existe" |
| 31.3 | zone 0.1 0.6 ambre ; picto prison -1.8 0.6 ; sous-titre "Seulement suspendue" |
| 32.1 | scene-vide ; article "Art. 42 CP" ; titre "Une amende en plus" ; personnage ines "Inès" rose gauche ; personnage juge "Le juge" violet centre-droite |
| 32.1+2.5 | jetons ines juge |
| 32.2 | effacer-titres ; titre "Tout de suite sensible" |
| 33.1 | scene-vide ; article-retirer ; repere-marquer 3 neutre ; titre "Retenons" |
| 33.2 | picto prison -4.4 0.4 ; etiquette p1 "Privation de liberté" -4.4 -0.9 |
| 33.2+2 | picto pieces 0 0.4 ; etiquette p2 "Jours-amende" 0 -0.9 |
| 33.2+4.5 | picto pieces:2 4.4 0.4 ; etiquette p3 "Amende" 4.4 -0.9 |
| 34.1 | scene-vide ; repere-marquer 1 ambre ; repere-marquer 2 neutre ; personnage juge "Le juge" violet centre-droite ; titre "Choisir, puis fixer" |
| 34.1+2 | repere-marquer 1 vert ; repere-marquer 2 ambre |
| 34.2 | repere-marquer 2 vert ; repere-marquer 3 ambre ; effacer-titres ; titre "Sursis : la règle" ; sous-titre "Jusqu'à 2 ans" |
| 34.3 | sous-titre "Pronostic favorable" ; picto coche -2.6 0.6 |
| 34.4 | sous-titre "Antécédents, réparation du dommage" |
| 35.1 | scene-vide ; repere-marquer 1 neutre ; repere-marquer 2 neutre ; repere-marquer 3 neutre ; titre "Une question pour finir" |
| 35.2 | effacer-titres ; decor tribunal ; personnage hugo "Hugo" bleu_clair gauche ; placer hugo -1 ; picto prison -4.4 0.6 ; etiquette duree "2 ans" -1.6 0.6 |
| 35.3 | etiquette profil "Jamais condamné, dommage réparé" 2.6 0.6 |
| 35.4 | titre "Sursis complet ?" ; repere-marquer 3 ambre |
| 35.5 | scene-vide ; rembobiner ; decor tribunal ; personnage hugo "Hugo" bleu_clair gauche ; placer hugo -1 ; picto prison -4.4 0.6 ; etiquette duree "30 mois" -1.6 0.6 ; etiquette profil "Jamais condamné, dommage réparé" 2.6 0.6 ; titre "Et 30 mois ?" |
| 35.6 | effacer-titres ; titre "Réponse en commentaire" ; accent hugo |
| 36.1 | scene-vide ; repere-retirer ; livre "Code pénal" 0 -0.5 ; titre "L'étude du droit" ; sous-titre "Tout est dans la description" |
