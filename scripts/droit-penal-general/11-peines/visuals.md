# Visuels — Vidéo 11 : Quelle peine ?

Ce fichier pilote les schémas Manim (`render/manim/video.py`). Vocabulaire des actions : `render/manim/README.md`.

Colonne « Moment » : `ligne.phrase` du script, éventuellement `+secondes` ou `@mot`. Plusieurs actions d'un même moment sont séparées par `;`.

Personnages (bonshommes en bâtons ; poses, visages et objets aux moments marqués) : Inès rose (comme dans la vidéo 3), le juge violet, Hugo bleu clair ; seconds rôles : la passante turquoise (la victime du vol, vidéo 3), la personne aisée ambre pâle, l'auteur et la victime de la ligne 24 (ambre pâle, turquoise), le passant ambre pâle et son amie turquoise (le piège).

Style « scène » (repris le 1er novembre 2026, enrichi le 9 novembre 2026 sur le modèle de la vidéo 10) : le vol se rappelle dans la rue de Neuchâtel, le samedi soir (décor rue de la vidéo 3) : Inès prend le téléphone de la passante et s'éloigne. Le cas se juge au tribunal : Inès entre et va à la barre, le juge monte sur l'estrade ; quand Inès tient un objet (porte-monnaie, pièces), elle se tient à côté de la barre et non derrière, pour que l'objet reste visible en main. Les trois peines sont des pictogrammes au trait : la prison pour la peine privative de liberté, les pièces pour la peine pécuniaire et l'amende. Un pense-bête « Choisir / Fixer / Sursis » en haut à droite suit les trois questions du juge (ambre : en cours ; vert : réglée). L'arrêt du Tribunal fédéral s'affiche à côté de l'article quand on en parle (ligne 15).

Objets et actions (9 novembre 2026) : le téléphone volé (pris des mains de la passante, ligne 1) ; les pièces que chacun tient selon son revenu (lignes 10 et 11 : petite pile pour Inès, grosse pile pour la personne aisée) ; l'amende impayée barrée qui mène à la prison (ligne 13) ; le porte-monnaie d'Inès (ligne 18) ; l'auteur qui remet des pièces à la victime pour réparer le dommage (lignes 24 et 35) ; la peine pécuniaire d'Inès suspendue au-dessus de sa tête (ligne 31) ; l'amende qu'Inès pose sur la barre (ligne 32). L'argent ne passe jamais au juge : il n'en est pas le destinataire.

Écarts assumés avec la colonne « À l'écran » du script, pour rester dans la charte : les calculs de jours-amende (ligne 10) et les critères (lignes 15, 22) sont des étiquettes près des personnages, sans signe de multiplication ; le choix de la peine (ligne 18) est montré par les pièces et le porte-monnaie d'Inès plutôt que par deux colonnes ; la ligne 31 montre la peine suspendue au-dessus d'Inès au lieu d'une frise ; la question finale (ligne 35) se joue au tribunal (le profil de Hugo en étiquettes, la victime remboursée), avec un rembobinage pour les trente mois, au lieu d'une frise.

| Moment | Actions |
| --- | --- |
| 1.1 | decor rue ; personnage ines "Inès" rose gauche ; placer ines -0.25 ; personnage passante "La passante" turquoise centre-droite ; placer passante 1 ; picto telephone 1.2 -1.4 ; tenir passante telephone aussitot ; renvoi "vidéo 3" |
| 1.2 | etiquette lieu "Neuchâtel, samedi soir" -3.6 1.7 |
| 1.2@volé | rejoindre ines passante ; prendre ines telephone |
| 1.2@samedi | marcher ines -4 ; visage passante surpris |
| 2.1 | scene-vide ; decor tribunal ; personnage ines "Inès" rose gauche ; placer ines -3 ; etiquette age "Vingt ans" -4.4 1.0 |
| 2.2 | etiquette-retirer age ; marcher ines -1 |
| 2.2@jamais | etiquette age "Apprentie, jamais condamnée" -1.6 0.6 |
| 2.3 | etiquette-retirer age ; personnage juge "Le juge" violet droite ; placer juge 4 |
| 2.3+0.5 | marcher juge 3 |
| 2.3@trois | repere-batiment |
| 2.3@étages | repere-etage 1 vert ; repere-etage 2 vert ; repere-etage 3 vert |
| 2.3@vol | etiquette vol "Un vol" 1.4 1.4 |
| 3.1 | etiquette-retirer vol ; titre "Une question concrète" ; parler juge |
| 3.2 | effacer-titres ; titre "Quelle peine ?" ambre ; visage ines inquiet |
| 3.3 | picto prison -4.2 1.4 |
| 3.4 | picto pieces -1.6 1.4 |
| 3.5 | etiquette rien "Rien du tout ?" 1.4 1.4 |
| 4.1 | scene-vide ; repere-retirer ; titre "Trois peines principales" ; livre "Code pénal" 0 0.2 |
| 4.1+2 | livre-ouvrir |
| 4.2 | livre-retirer |
| 4.2@privative | picto prison -4.4 0.4 ; etiquette p1 "Privative de liberté" -4.4 -0.9 |
| 4.2@pécuniaire | picto pieces 0 0.4 ; etiquette p2 "Pécuniaire" 0 -0.9 |
| 4.2@amende | picto pieces:2 4.4 0.4 ; etiquette p3 "Amende" 4.4 -0.9 |
| 5.1 | scene-vide ; personnage juge "Le juge" violet centre ; titre "Deux temps" |
| 5.2 | liste-ajouter "Choisir" ; picto prison -2.4 0.5 ; picto pieces 2.4 0.5 |
| 5.2@genre | tourner juge gauche |
| 5.2+1.8 | tourner juge droite |
| 5.3 | liste-ajouter "Fixer" |
| 5.3@durée | picto sablier -2.4 -1.0 0.8 |
| 5.3@montant | picto billet 2.4 -1.0 |
| 6.1 | liste-ajouter "Sursis ?" ; tourner juge gauche |
| 6.1@exécutée | accent juge |
| 6.1@suspendue | effacer-titres ; repere-liste "Choisir" "Fixer" "Sursis" |
| 7.1 | scene-vide ; repere-marquer 1 ambre ; article "Art. 40 CP" ; picto prison 0 1.0 ; titre "L'enfermement" |
| 7.1@enfermement | picto cadenas 1.2 0.8 0.8 |
| 7.2 | frise ; point 0.05 "3 jours" |
| 7.2@vingt | point 0.85 "20 ans" |
| 7.3 | repere 0.95 "À vie" |
| 8.1 | scene-vide ; article "Art. 34 CP" ; titre "Les jours-amende" ; personnage juge "Le juge" violet centre |
| 8.1@jour | picto calendrier -3.8 1.0 ; picto pieces 3.8 1.0 |
| 8.2 | tourner juge gauche ; etiquette nombre "Nombre : la faute" -3.8 -0.2 |
| 8.2@trois | etiquette nombre "3 à 180, selon la faute" -3.8 -0.2 |
| 9.1 | effacer-titres ; tourner juge droite |
| 9.1@montant | etiquette montant "Montant d'un jour" 3.8 -0.2 |
| 9.2 | etiquette montant "30 à 3000 francs" 3.8 -0.2 |
| 9.3 | etiquette montant "Exception : 10 francs" 3.8 -0.2 |
| 9.4 | etiquette montant "Selon la situation" 3.8 -0.2 |
| 9.4@revenu | picto billet 2.6 -1.4 0.8 |
| 9.4@fortune | picto tirelire 3.8 -1.4 0.8 |
| 9.4@charges | picto document 5.0 -1.4 0.8 |
| 10.1 | scene-vide ; article-retirer ; titre "30 jours-amende" ; personnage ines "Inès" rose gauche |
| 10.2 | etiquette j1 "À 50 francs" -2.3 1.2 ; picto pieces -2.6 -0.3 0.8 |
| 10.2@cela | tenir ines pieces ; etiquette j1 "1500 francs" -2.3 1.2 |
| 10.3 | personnage aisee "Personne aisée" ambre_pale centre-droite ; etiquette j2 "À 1000 francs" 4.6 1.2 |
| 10.3+2.4 | picto pieces:2 4.6 0.0 1.6 |
| 10.3@feront | tenir aisee pieces:2 ; etiquette j2 "30 000 francs" 4.6 1.2 |
| 11.1 | etiquette-retirer j1 ; etiquette-retirer j2 ; effacer-titres ; titre "Même faute, même nombre" |
| 11.1@sacrifice | visage ines inquiet ; visage aisee inquiet |
| 11.2 | effacer-titres ; titre "Même effort" ambre ; picto balance -1.2 0.7 |
| 12.1 | scene-vide ; article "Art. 106 CP" ; titre "L'amende" ; renvoi "vidéo 3" ; picto voiture -5.6 1.0 |
| 12.1@contraventions | picto parking -2.4 0.6 ; etiquette contrav "Contraventions" -2.4 -0.6 |
| 12.2 | picto pieces 2.4 0.6 |
| 12.2@dix | etiquette max "10 000 francs au plus" 2.4 -0.6 |
| 13.1 | scene-vide ; titre "Peine de substitution" ; picto prison -2.4 0.6 |
| 13.1@jour | etiquette duree "1 jour à 3 mois" -2.4 -0.6 |
| 13.2 | picto pieces 2.4 0.6 ; etiquette impaye "Amende impayée" 2.4 -0.6 |
| 13.2@paie | interdit pieces |
| 13.2@faute | relier pieces prison |
| 14.1 | scene-vide ; article "Art. 139 CP" ; decor tribunal ; personnage ines "Inès" rose gauche ; placer ines -1 ; personnage juge "Le juge" violet droite ; placer juge 3 ; visage ines inquiet |
| 14.1@cinq | picto prison -4.2 1.4 ; etiquette cinq "5 ans au plus" -4.2 0.2 |
| 14.2 | tourner juge -4.2 |
| 14.2+4 | parler juge |
| 14.2@pécuniaire | picto pieces 1.2 1.4 ; etiquette pec "Peine pécuniaire" 1.2 0.2 |
| 14.3 | accent juge ; tourner juge 1.2 |
| 15.1 | scene-vide ; article-retirer ; arret "ATF 147 IV 241" ; personnage juge "Le juge" violet centre-droite ; titre "Trois questions" |
| 15.2 | effacer-titres ; liste-ajouter "Adaptée ?" |
| 15.2@adaptée | picto balance -0.4 1.3 0.7 |
| 15.3 | liste-ajouter "Effets sur la vie ?" |
| 15.3@sociale | foule soc -0.4 0.2 3 |
| 15.4 | liste-ajouter "Efficace ?" |
| 15.4@efficace | picto cible -0.4 -0.9 0.7 ; accent juge |
| 16.1 | scene-vide ; arret-retirer ; article "Art. 41 CP" ; titre "Un cadre" ; personnage juge "Le juge" violet centre ; picto prison -3.5 0.4 ; picto pieces 3.5 0.4 |
| 16.2 | sous-titre "Préférer la prison ?" ; tourner juge gauche |
| 16.2@deux | etiquette deux "Deux raisons" 0 -1.8 |
| 16.2+7 | accent juge |
| 17.1 | effacer-titres ; etiquette-retirer deux ; retirer juge ; picto-retirer pieces ; picto-deplacer prison -4.6 0.9 ; case "Détourner de récidiver" |
| 17.2 | case "Paiement impossible" |
| 17.2@pécuniaire | picto pieces -4.6 -0.8 |
| 17.2@exécutée | interdit pieces |
| 17.3 | titre "Motiver en détail" ; picto document 2.2 -1.5 |
| 17.3@détail | picto stylo 3.3 -1.5 |
| 18.1 | scene-vide ; article-retirer ; decor tribunal ; personnage ines "Inès" rose gauche ; placer ines -2 ; personnage juge "Le juge" violet droite ; placer juge 3 |
| 18.1@jeune | etiquette profil "Jeune, sans antécédents" -3.0 0.4 |
| 18.1@salaire | picto portefeuille -2.4 -1.2 ; tenir ines portefeuille |
| 18.1@paraît | picto pieces 1.6 0.5 ; etiquette choix "Peine pécuniaire" 1.6 1.6 ; parler juge |
| 18.2 | etiquette-retirer profil ; accent ines ; visage ines content |
| 18.2@payer | repere-marquer 1 vert |
| 19.1 | scene-vide ; repere-marquer 2 ambre ; personnage juge "Le juge" violet centre-droite ; titre "Combien de jours ?" ; picto calendrier 4.4 0.4 |
| 19.2 | article "Art. 47 CP" |
| 19.3 | effacer-titres ; titre "La culpabilité" ambre ; picto-retirer calendrier ; picto balance 4.4 0.4 |
| 20.1 | liste-ajouter "Gravité" ; tourner juge gauche |
| 20.1@répréhensible | liste-ajouter "Répréhensible" |
| 20.2 | liste-ajouter "Motivations" |
| 20.2@aurait | liste-ajouter "Évitable ?" |
| 21.1 | scene-vide ; personnage juge "Le juge" violet centre-droite ; titre "Aussi" ; liste "Antécédents" "Situation personnelle" ; picto document 4.4 0.4 |
| 21.2 | liste-ajouter "Effet sur l'avenir" ; accent juge |
| 22.1 | scene-vide ; article-retirer ; decor tribunal ; personnage ines "Inès" rose gauche ; placer ines -1 ; personnage juge "Le juge" violet droite ; placer juge 3 ; etiquette refl "Réfléchi" -4.4 1.5 |
| 22.1@objet | picto telephone -4.4 0.4 |
| 22.1@valeur | etiquette val "Valeur moyenne" -4.4 -0.5 |
| 22.2 | etiquette premier "Jamais condamnée" -1.6 0.6 |
| 22.3 | etiquette-retirer refl ; picto ecole 1.7 0.3 0.8 ; etiquette appr "Son apprentissage" 1.7 1.5 ; visage ines inquiet |
| 22.3@apprentissage | repere-marquer 2 vert |
| 23.1 | scene-vide ; repere-marquer 3 ambre ; personnage ines "Inès" rose gauche ; titre "Le sursis" ; picto prison 0.6 0.2 |
| 23.2 | article "Art. 42 CP" |
| 23.2@suspend | picto-deplacer prison 0.6 1.0 ; etiquette regle "En règle générale" 0.6 -0.9 |
| 23.3 | etiquette-retirer regle ; picto pieces 3.6 1.0 ; sous-titre "Pécuniaire, ou 2 ans au plus" |
| 24.1 | effacer-titres ; titre "Pronostic favorable" ; tourner ines droite |
| 24.1@nécessaire | picto coche -2.6 1.2 ; visage ines content |
| 24.2 | sous-titre "Les antécédents" ; picto document -2.6 -0.4 0.8 |
| 24.3 | scene-vide ; titre "Déjà condamné" ; frise ; point 0.9 "L'acte" |
| 24.3@six | point 0.4 "Plus de 6 mois" ; picto prison -1.4 0.7 |
| 24.3@cinq | repere 0.15 "5 ans avant" ; zone 0.15 0.9 gris |
| 24.4 | effacer-titres ; titre "Circonstances particulièrement favorables" |
| 24.5 | scene-vide ; titre "Réparer le dommage" ; personnage auteur "L'auteur" ambre_pale gauche ; picto pieces -3.4 -0.3 ; personnage victime "La victime" turquoise centre-droite ; visage victime triste |
| 24.5+0.5 | tenir auteur pieces |
| 24.5@sursis | sous-titre "Sinon, refus possible" |
| 24.5@effort | donner auteur victime pieces ; visage victime content |
| 25.1 | scene-vide ; article "Art. 44 CP" ; titre "Délai d'épreuve" ; frise ; point 0.1 "Jugement" |
| 25.1@délai | zone 0.1 0.6 vert ; sous-titre "2 à 5 ans" |
| 25.2 | point 0.6 "Fin" ; picto prison 4.6 0.6 |
| 25.2@jamais | etiquette jamais "Jamais exécutée" 4.6 -0.6 |
| 26.1 | article "Art. 46 CP" ; etiquette-retirer jamais |
| 26.1@crime | point 0.45 "Nouvelle infraction" ; picto danger -0.8 0.6 0.8 |
| 26.2 | zone 0.1 0.6 gris ; effacer-titres ; titre "Sursis révoqué" |
| 26.3 | sous-titre "Peine exécutée" ; picto cadenas 5.8 0.6 0.8 |
| 27.1 | scene-vide ; article "Art. 43 CP" ; titre "Le sursis partiel" ; picto prison 0 -0.8 |
| 27.2 | picto-retirer prison ; colonnes "Exécutée" "Suspendue" ; sous-titre "1 à 3 ans" |
| 27.2@exécuter | picto prison -3.5 -0.6 |
| 27.2@partie | picto prison:2 3.5 -0.6 |
| 28.1 | effacer-titres ; colonne-accent 1 ; etiquette moitie "Moitié au plus" -3.5 -1.9 |
| 28.2 | colonne-accent 2 ; etiquette six "6 mois au moins" 3.5 -1.9 |
| 29.1 | scene-vide ; article-retirer ; decor tribunal ; personnage ines "Inès" rose gauche ; placer ines -1 ; personnage juge "Le juge" violet droite ; placer juge 3 ; visage ines inquiet |
| 29.1@prononce | parler juge ; etiquette verdict "Pécuniaire avec sursis" 1.2 1.5 |
| 29.1@délai | picto sablier -4.4 0.8 0.8 ; etiquette epreuve "2 ans d'épreuve" -1.6 0.6 |
| 29.2 | picto-retirer sablier ; picto pieces -4.4 0.8 |
| 29.2@paiera | interdit pieces ; visage ines content ; repere-marquer 3 vert |
| 30.1 | scene-vide ; decor rue Café jour ; titre "Le piège classique" ; personnage passant "Un passant" ambre_pale gauche ; placer passant -3 ; personnage amie "Son amie" turquoise centre-gauche ; placer amie -2 |
| 30.2 | effacer-titres ; parler passant amie ; parole passant "Du sursis : pas puni" |
| 30.3 | effacer-parole passant ; mot-barre "Pas puni" 4.2 1.2 ; visage amie surpris |
| 31.1 | scene-vide ; personnage ines "Inès" rose gauche ; titre "Bel et bien condamnée" ; picto pieces -3.4 0.3 0.7 |
| 31.2 | sous-titre "La peine existe" |
| 31.2@suspendue | picto-deplacer pieces -4.5 2.2 0.4 ; visage ines inquiet |
| 31.3 | sous-titre "Seulement suspendue" ; picto sablier -2.4 0.7 0.8 |
| 31.3@délai | etiquette delai "Délai d'épreuve" 0.6 0.7 |
| 32.1 | scene-vide ; article "Art. 42 CP" ; decor tribunal ; personnage ines "Inès" rose gauche ; placer ines -0.3 ; personnage juge "Le juge" violet droite ; placer juge 3 ; titre "Une amende en plus" |
| 32.1@ajouter | parler juge |
| 32.1@amende | picto pieces 0.3 -1.4 ; tenir ines pieces |
| 32.1@payée | poser ines pieces -1.3 -1.0 |
| 32.2 | effacer-titres ; titre "Tout de suite sensible" ; visage ines triste |
| 33.1 | scene-vide ; article-retirer ; repere-marquer 3 neutre ; titre "Retenons" |
| 33.2@privation | picto prison -4.4 0.4 ; etiquette p1 "Privation de liberté" -4.4 -0.9 |
| 33.2@pécuniaire | picto pieces 0 0.4 ; etiquette p2 "Jours-amende" 0 -0.9 |
| 33.2@contraventions | picto pieces:2 4.4 0.4 ; etiquette p3 "Amende" 4.4 -0.9 |
| 34.1 | scene-vide ; repere-marquer 1 ambre ; repere-marquer 2 neutre ; personnage juge "Le juge" violet centre-droite ; titre "Choisir, puis fixer" ; picto prison -2.0 0.4 ; picto pieces -0.2 0.4 |
| 34.1@puis | repere-marquer 1 vert ; repere-marquer 2 ambre ; picto-retirer prison ; tourner juge gauche |
| 34.2 | repere-marquer 2 vert ; repere-marquer 3 ambre ; picto-retirer pieces ; effacer-titres ; titre "Sursis : la règle" ; sous-titre "Jusqu'à 2 ans" |
| 34.3 | sous-titre "Pronostic favorable" ; picto coche -2.6 0.6 |
| 34.4 | sous-titre "Antécédents, réparation du dommage" ; picto pieces -0.4 0.4 |
| 35.1 | scene-vide ; repere-marquer 1 neutre ; repere-marquer 2 neutre ; repere-marquer 3 neutre ; titre "Une question pour finir" |
| 35.2 | effacer-titres ; decor tribunal ; personnage hugo "Hugo" bleu_clair gauche ; placer hugo 0 ; picto pieces 0.4 -1.4 ; tenir hugo pieces aussitot ; personnage victime "La victime" turquoise droite ; placer victime 1.5 |
| 35.2@deux | picto prison -4.6 1.3 ; etiquette duree "2 ans" -4.6 0.35 |
| 35.3 | etiquette profil "Jamais condamné" 1.6 1.2 |
| 35.3@et | donner hugo victime pieces ; etiquette profil2 "Dommage réparé" 1.6 0.4 |
| 35.4 | etiquette-retirer profil ; etiquette-retirer profil2 ; titre "Sursis complet ?" ; repere-marquer 3 ambre ; visage hugo inquiet |
| 35.5 | scene-vide ; rembobiner ; decor tribunal ; personnage hugo "Hugo" bleu_clair gauche ; placer hugo 0 ; personnage victime "La victime" turquoise droite ; placer victime 1.5 ; picto pieces 2.0 -1.4 ; tenir victime pieces aussitot ; picto prison -4.6 1.3 ; etiquette duree "30 mois" -4.6 0.35 ; titre "Et 30 mois ?" |
| 35.6 | effacer-titres ; titre "Réponse en commentaire" ; accent hugo |
| 36.1 | scene-vide ; repere-retirer ; livre "Code pénal" 0 -0.5 ; titre "L'étude du droit" ; sous-titre "Tout est dans la description" |
