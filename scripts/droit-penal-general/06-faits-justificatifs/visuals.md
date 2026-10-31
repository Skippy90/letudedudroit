# Visuels — Vidéo 6 : Avait-il le droit de se défendre ?

Ce fichier pilote les schémas Manim (`render/manim/video.py`). Vocabulaire des actions : `render/manim/README.md`.

Colonne « Moment » : `ligne.phrase` du script, éventuellement `+secondes`. Plusieurs actions d'un même moment sont séparées par `;`.

Personnages : Yasmine turquoise, Kevin rose, Hugo bleu clair, Nadia violet.

Style « scène » : les cas se jouent à la sortie d'un bar (décor de rue, enseigne « Bar »), la bouteille de Kevin et la voiture du bébé sont des pictogrammes au trait, le fait justificatif est le bouclier de la charte, et le petit bâtiment en haut à droite suit l'étage en jeu (ambre : en examen ; vert : franchi ; gris : l'étage tombe).

Écart assumé : le couteau n'est pas dessiné (ligne 19), il est nommé par une étiquette.

| Moment | Actions |
| --- | --- |
| 1.1 | decor rue Bar ; etiquette lieu "Bienne, vendredi soir" -3.6 1.7 |
| 1.2@kevin | personnage kevin "Kevin" rose droite ; placer kevin 3 |
| 1.2@yasmine | personnage yasmine "Yasmine" turquoise gauche ; placer yasmine -1 |
| 1.2@avance | marcher kevin 1 |
| 1.2@bouteille | etiquette-retirer lieu ; picto bouteille 2.3 -0.9 |
| 2.1@lève | picto-deplacer bouteille 2.0 0.3 |
| 2.2@verre | etiquette danger "Peut blesser gravement" 1.6 1.7 |
| 2.3@seconde | etiquette-retirer danger ; etiquette sec "Une seconde" -1.6 1.7 |
| 2.4@repousse | pousser yasmine kevin |
| 2.5@tombe | etiquette-retirer sec ; chute kevin 2 ; picto-deplacer bouteille 4.4 -2.0 |
| 2.5@bras | dommage kevin |
| 3.1 | titre "Yasmine a blessé Kevin" |
| 3.2@lésions | sous-titre "Lésions corporelles" |
| 3.3@punie | effacer-titres ; titre "Punie pour s'être défendue ?" ambre |
| 4.1 | scene-vide ; batiment ; renvoi "vidéo 1" |
| 5.1@premier | fleche 1 ; etage 1 vert |
| 5.2@voulu | titre "Premier étage : franchi" |
| 6.1@deuxième | etage 2 ambre ; repere-batiment ; repere-etage 1 vert ; repere-etage 2 ambre |
| 6.2@permis | titre "Permis malgré tout ?" |
| 7.1 | scene-vide ; titre "Les faits justificatifs" ; bouclier |
| 7.2@licite | sous-titre "Ils rendent l'acte licite" |
| 7.3@deux | sous-titre "Aujourd'hui : deux" |
| 8.1@quinze | article "Art. 15 CP" ; titre "La légitime défense" |
| 8.2@repousser | sous-titre "Repousser une attaque illicite" |
| 9.1 | scene-vide ; personnage yasmine "Yasmine" turquoise gauche ; titre "Trois conditions" |
| 9.2@attaque | effacer-titres ; case "Attaque, même imminente" |
| 10.1@contraire | case "Contraire au droit" |
| 10.2@proportionnés | case "Défense proportionnée" |
| 11.1@tout | accent yasmine |
| 11.2@bouteille | cocher 1 vert |
| 11.3@autorisait | cocher 2 vert |
| 11.4@mesuré | cocher 3 vert |
| 12.1 | scene-vide ; personnage yasmine "Yasmine" turquoise gauche ; bouclier -2.6 0.6 ; titre "Justifié" ambre |
| 12.2@illicéité | repere-etage 2 gris ; sous-titre "L'illicéité tombe" |
| 12.3@punie | sous-titre "Yasmine n'est pas punie" |
| 13.1 | scene-vide ; article-retirer ; decor rue Bar ; personnage yasmine "Yasmine" turquoise gauche ; placer yasmine -1 ; personnage kevin "Kevin" rose droite ; placer kevin 1 ; picto bouteille 2.3 -0.9 |
| 13.2@tiers | personnage hugo "Hugo" bleu_clair gauche ; placer hugo -4 ; etiquette tiers "Un tiers aussi" -4.0 1.7 |
| 13.3@hugo | marcher hugo -3 |
| 13.3@défendre | accent hugo |
| 14.1 | scene-vide ; titre "Pas que le corps" ; personnage yasmine "Yasmine" turquoise gauche |
| 14.2@fédéral | arret "ATF 107 IV 12" |
| 14.2@biens | sous-titre "Aussi ses biens" ; picto telephone -3.45 0.3 |
| 14.3@voleur | effacer-titres ; titre "Contre un voleur, sur le moment" ; personnage voleur "Un voleur" ambre_pale droite |
| 15.1 | scene-vide ; arret-retirer ; personnage yasmine "Yasmine" turquoise gauche |
| 15.1@cru | bulle yasmine "Attaquée ?" |
| 15.2@putative | effacer-bulle yasmine ; titre "Légitime défense putative" |
| 15.3@erreur | sous-titre "Une question d'erreur" ; renvoi "vidéo 7" |
| 16.1 | scene-vide ; rembobiner |
| 16.2 | decor rue Bar ; personnage yasmine "Yasmine" turquoise gauche ; placer yasmine -2 ; personnage kevin "Kevin" rose droite ; placer kevin 1 |
| 16.2+1.5 | picto tension -0.8 0.6 |
| 16.2@rentre | picto-retirer tension ; marcher kevin 4 |
| 16.3@lendemain | etiquette lendemain "Le lendemain" -3.2 1.7 |
| 16.3@frapper | marcher yasmine 2 |
| 17.1@légitime | titre "Plus de légitime défense" |
| 17.2@terminée | etiquette lendemain "Attaque terminée" -3.2 1.7 |
| 17.3@venger | effacer-titres ; titre "Se venger n'est pas se défendre" ambre |
| 18.1 | scene-vide ; arret-retirer ; titre "Une affaire dramatique" |
| 18.1@fédéral | arret "ATF 122 IV 1" |
| 18.2@tué | picto lune -4.6 1.2 ; sous-titre "Un mari violent, tué dans son sommeil" |
| 18.3@attaquait | effacer-titres ; titre "Aucune attaque à ce moment" |
| 19.1 | scene-vide ; rembobiner |
| 19.2 | decor rue Bar ; personnage yasmine "Yasmine" turquoise gauche ; placer yasmine -2 ; personnage kevin "Kevin" rose droite ; placer kevin 2 ; picto bouteille 3.9 -0.9 |
| 19.2@couteau | etiquette couteau "Un couteau" -3.2 1.2 |
| 19.2@reprises | etiquette couteau "Plusieurs coups" -3.2 1.2 ; dommage kevin |
| 20.1@fédéral | arret "ATF 136 IV 49" |
| 20.1@retenue | titre "Une grande retenue" |
| 20.2@dernier | sous-titre "Le dernier moyen" |
| 20.3@plusieurs | sous-titre "Admis face à plusieurs agresseurs" |
| 21.1 | scene-vide ; arret-retirer ; batiment ; fleche 1 ; etage 1 vert |
| 21.1@limites | titre "Trop loin : un excès" |
| 21.2@seize | article "Art. 16 CP" ; sous-titre "Peine atténuée" |
| 22.1@excitation | sous-titre "Excitation ou saisissement excusable" |
| 22.2@coupable | etage 3 gris ; repere-etage 3 gris |
| 23.1 | effacer-titres ; titre "Où sommes-nous ?" |
| 23.2@licite | etage 2 vert ; repere-etage 2 vert ; sous-titre "Pas licite pour autant" |
| 23.3@troisième | etage 3 ambre ; repere-etage 3 ambre ; sous-titre "Seulement la culpabilité" |
| 24.1 | scene-vide ; article-retirer ; repere-etage 2 ambre ; repere-etage 3 neutre ; titre "L'état de nécessité" ; picto danger 0 0.3 |
| 24.2@agresseur | sous-titre "Pas d'agresseur" |
| 24.3@danger | sous-titre "Seulement un danger" |
| 25.1 | scene-vide ; decor parc ; personnage hugo "Hugo" bleu_clair gauche ; placer hugo -3 ; picto voiture 2.4 -1.7 ; etiquette lieu "Canicule" -2.6 2.45 |
| 25.1@bébé | etiquette bebe "Un bébé enfermé" 2.4 0.4 |
| 25.2@personne | accent hugo |
| 25.3@brise | marcher hugo 0 |
| 25.3@sortir | etiquette bebe "Vitre brisée, bébé sauvé" 2.4 0.4 |
| 26.1@dommage | etiquette lieu "Dommage à la propriété" -2.6 2.45 |
| 26.2@dix | scene-vide ; article "Art. 17 CP" |
| 26.2@licite | titre "Licite, à trois conditions" |
| 27.1 | scene-vide ; personnage hugo "Hugo" bleu_clair gauche ; case "Danger imminent" |
| 27.2@fédéral | arret "ATF 122 IV 1" |
| 27.2@actuel | sous-titre "Actuel et concret" |
| 27.3@impossible | case "Pas d'autre issue" |
| 27.4@prépondérants | case "Intérêt prépondérant" |
| 28.1@vie | cocher 1 vert ; cocher 2 vert ; cocher 3 vert |
| 28.2@justifié | bouclier -2.4 0.6 ; repere-etage 2 gris ; effacer-titres ; titre "Justifié" ambre |
| 29.1 | scene-vide ; batiment ; fleche 1 ; etage 1 vert ; titre "Valeur comparable" |
| 29.2@justifié | etage 2 vert ; repere-etage 2 vert ; sous-titre "Plus justifié" |
| 29.3@dix | article "Art. 18 CP" ; etage 3 ambre ; sous-titre "Peine atténuée" |
| 29.4@coupable | sous-titre "Sinon : pas coupable" |
| 30.1@sacrifie | effacer-titres ; titre "Sacrifice non exigible" |
| 30.2@coupable | etage 3 gris ; repere-etage 3 gris ; sous-titre "Pas coupable" |
| 30.3@troisième | sous-titre "Troisième étage" |
| 31.1 | scene-vide ; article-retirer ; arret-retirer ; repere-etage 2 ambre ; repere-etage 3 neutre ; titre "D'autres faits justificatifs" ; bouclier 0 0.3 |
| 31.2@quatorze | article "Art. 14 CP" ; sous-titre "Ce que la loi ordonne ou autorise" |
| 31.3@policier | effacer-titres ; personnage policier "Un policier" bleu_clair gauche ; etiquette regles "Dans les règles" 1.4 1.2 ; bouclier -2.0 0.5 |
| 32.1 | scene-vide ; article-retirer ; titre "Le piège classique" ; picto bouteille 0 0.3 |
| 32.2@agresseur | sous-titre "Face à un agresseur, tout est permis" |
| 32.3@faux | barrer |
| 33.1@proportionnée | effacer-titres ; picto-retirer bouteille ; titre "Rester proportionné" ; bouclier 3.0 0.3 |
| 33.2@gravité | liste-ajouter "Gravité de l'attaque" ; arret "ATF 136 IV 49" |
| 33.2@biens | liste-ajouter "Biens en jeu" |
| 33.2@moyen | liste-ajouter "Moyen utilisé" |
| 33.3@situation | effacer-titres ; sous-titre "Vu par la victime" |
| 34.1 | scene-vide ; arret-retirer ; frise ; zone 0.35 0.65 vert |
| 34.1@pendant | repere 0.35 "Attaque" |
| 34.2@tôt | point 0.15 "Trop tôt" |
| 34.3@tard | point 0.85 "Trop tard" |
| 34.4@punissable | titre "Peut rester punissable" |
| 35.1 | scene-vide ; arret-retirer ; titre "Retenons" ; personnage yasmine "Yasmine" turquoise droite |
| 35.2@légitime | effacer-titres ; liste-ajouter "Attaque : légitime défense" |
| 35.3@quinze | article "Art. 15 CP" ; retirer yasmine ; batiment 4.6 petit ; fleche 1 ; etage 1 vert |
| 36.1@danger | liste-ajouter "Danger : état de nécessité" |
| 36.2@dix | article "Art. 17 CP" |
| 37.1@illicéité | etage 2 gris ; repere-etage 2 gris ; sous-titre "Plus d'illicéité" |
| 37.2@culpabilité | article "Art. 16 et 18 CP" ; etage 2 vert ; etage 3 ambre ; repere-etage 2 ambre ; repere-etage 3 ambre ; sous-titre "Culpabilité seulement" |
| 37.3@attaque | effacer-titres ; titre "Attaque ? Danger ?" ambre |
| 38.1 | scene-vide ; article-retirer ; repere-etage 2 ambre ; repere-etage 3 neutre ; titre "Une question pour finir" |
| 38.2 | effacer-titres ; decor escalier ; personnage nadia "Nadia" violet gauche ; placer nadia 0 ; personnage voisin "Un voisin" ambre_pale droite ; placer voisin 4 |
| 38.2@frappera | parole voisin "Je te frapperai un jour !" |
| 38.3@lendemain | effacer-parole voisin ; etiquette lendemain "Le lendemain" -2.6 2.45 |
| 38.3@frappe | marcher nadia 2 ; pousser nadia voisin |
| 38.4@légitime | etiquette-retirer lendemain ; titre "Légitime défense ?" ambre |
| 38.5@commentaire | accent nadia |
| 39.1 | scene-vide ; repere-retirer ; livre ; titre "L'étude du droit" ; sous-titre "Tout est dans la description" |
| 39.2 | accent titre |
