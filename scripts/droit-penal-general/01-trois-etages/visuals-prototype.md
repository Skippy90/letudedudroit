| Moment | Actions |
| --- | --- |
| 1.1 | decor escalier ; neige ; personnage marc "Marc" turquoise gauche ; placer marc -3 |
| 1.1@hiver | etiquette lieu "Un soir d'hiver" -2.6 2.45 |
| 1.1@lausanne | etiquette lieu "Lausanne, un soir d'hiver" -2.6 2.45 |
| 1.2@escalier | marcher marc 0 |
| 1.2@julien | personnage julien "Julien" rose droite ; placer julien 6 |
| 1.3 | marcher marc 5 ; marcher julien 1 |
| 1.3@détestent | picto tension 2.5 2.3 ; etiquette-retirer lieu |
| 1.3@parc | picto parking -0.2 2.3 |
| 2.1 | picto-retirer tension ; picto-retirer parking ; parole julien "Encore toi !" |
| 2.2 | effacer-parole julien |
| 2.2@pousse | pousser marc julien |
| 2.3@tombe | chute julien -1 |
| 2.3@poignet | dommage julien |
| 2.4 | etiquette blessure "Fracture simple" -2.2 -0.3 |
| 3.1 | etiquette-retirer blessure |
| 3.1@infraction | titre "Infraction ?" ambre |
| 3.2 | sous-titre "Votre réponse instinctive ?" |
| 3.3 | accent titre |
| 4.1 | scene-vide ; titre "Une infraction" |
| 4.1@chose | sous-titre "Pas une seule chose" |
| 4.2 | effacer-titres ; batiment vide |
| 4.2@étages | titre "Trois étages" |
| 5.1@typicité | etage-nom 1 |
| 5.2@illicéité | etage-nom 2 |
| 5.3@culpabilité | etage-nom 3 |
| 5.4 | effacer-titres ; titre "Retenez ces trois mots" ; repere-batiment |
| 6.1 | effacer-titres ; titre "L'ordre compte" |
| 6.2@bas | fleche 1 ; repere-etage 1 ambre |
| 6.3 | etage 1 gris ; repere-etage 1 gris ; sous-titre "Pas d'infraction, pas de peine" |
