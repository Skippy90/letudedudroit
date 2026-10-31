# Visuels — Vidéo 5 : Coupable de n'avoir rien fait

Ce fichier pilote les schémas Manim (`render/manim/video.py`). Vocabulaire des actions : `render/manim/README.md`.

Colonne « Moment » : `ligne.phrase` du script, éventuellement `+secondes`. Plusieurs actions d'un même moment sont séparées par `;`.

Personnages : Clara turquoise, Timéo rose, Maël bleu clair, Lucas violet.

Style « scène » : le cas se joue à la piscine (chaise haute de la surveillante, bassin au premier plan : Timéo n'en dépasse que par la tête). Un pense-bête en haut à droite rappelle les quatre sources de la position de garant (« Loi », « Contrat », « Communauté », « Risque ») : ambre pour la source dont on parle, vert si elle fonde l'obligation, gris si elle manque. Il ne s'allume pas pour la question finale, dont la réponse est dans la description.

Écart assumé : pas d'obstacle dessiné dans le Rhône (lignes 17 et 18) ; la plaque est dite par une étiquette, l'eau par le pictogramme des vagues.

| Moment | Actions |
| --- | --- |
| 1.1 | decor piscine ; etiquette lieu "Yverdon, un dimanche d'été" -2.6 2.45 |
| 1.2@clara | personnage clara "Clara" turquoise gauche ; placer clara -2 |
| 1.2@surveillante | etiquette role "Surveillante de baignade" -3.2 1.7 |
| 1.3@payée | etiquette role "Payée pour surveiller" -3.2 1.7 |
| 2.1@téléphone | etiquette-retirer lieu ; etiquette-retirer role ; picto telephone -2.3 -0.9 |
| 2.2@timéo | personnage timeo "Timéo" rose droite ; placer timeo 3 |
| 2.2@débat | etiquette debat "Se débat dans l'eau" 4.6 1.0 ; accent timeo |
| 3.1@maël | personnage mael "Maël" bleu_clair centre ; placer mael 0 |
| 3.1@voit | etiquette voit "Voit tout" 0 1.0 |
| 3.2@rien | accent mael |
| 4.1@sorti | etiquette-retirer voit ; etiquette debat "Sorti à temps" 4.6 1.0 |
| 4.2@hôpital | etiquette debat "Deux jours à l'hôpital" 4.6 1.0 |
| 5.1@rien | picto-retirer telephone ; etiquette-retirer debat ; titre "Ils n'ont rien fait" |
| 5.2@geste | sous-titre "Aucun geste" |
| 5.3@coupable | effacer-titres ; titre "Coupable sans agir ?" ambre |
| 6.1 | scene-vide ; titre "Jusqu'ici : des actes" |
| 6.2@marc | sous-titre "Pousser, frapper un ballon" ; personnage marc "Marc" turquoise gauche ; personnage julien "Julien" rose centre-gauche ; picto ballon 3.0 -0.6 |
| 6.2@poussait | pousser marc julien |
| 7.1@omission | effacer-titres ; retirer marc ; retirer julien ; picto-retirer ballon ; personnage clara "Clara" turquoise centre ; picto telephone 0.95 0.2 ; titre "L'omission" ambre |
| 7.2@agir | sous-titre "Ne pas agir alors qu'on aurait dû" |
| 7.3@piscine | sous-titre "Piscine, crèche, montagne" ; picto vagues 3.5 0.2 |
| 8.1 | effacer-titres ; retirer clara ; picto-retirer telephone ; picto-retirer vagues ; livre |
| 8.1@onze | article "Art. 11 CP" |
| 8.2@passif | livre-ouvrir ; titre "Un comportement passif" |
| 8.2@obligation | sous-titre "contraire à une obligation d'agir" |
| 9.1 | scene-vide ; article-retirer ; decor piscine ; personnage clara "Clara" turquoise gauche ; placer clara -2 ; personnage mael "Maël" bleu_clair centre ; placer mael 0 ; personnage timeo "Timéo" rose droite ; placer timeo 3 |
| 9.1@obligation | titre "Qui devait agir ?" |
| 9.2 | accent clara |
| 9.3 | accent mael |
| 9.4 | accent clara ; accent mael |
| 10.1 | scene-vide ; titre "Le Tribunal fédéral" ; personnage clara "Clara" turquoise gauche |
| 10.1@fédéral | arret "ATF 134 IV 255" |
| 10.2@obligation | sous-titre "Pas n'importe quelle obligation" |
| 10.3@garant | effacer-titres ; titre "Une position de garant" ambre |
| 11.1@garant | personnage clara "Clara" turquoise gauche ; etiquette oblige "Obligée de protéger" -0.9 1.0 |
| 11.2@vie | etiquette bien "La vie, la santé" 3.2 -0.2 |
| 12.1 | scene-vide ; arret-retirer ; titre "Quatre sources" ; personnage clara "Clara" turquoise centre |
| 12.2 | sous-titre "Une par une" |
| 13.1@loi | effacer-titres ; retirer clara ; liste-ajouter "1. La loi" ; picto parlement 3.4 0.0 |
| 13.2@parents | etiquette ex "Les parents" 3.4 1.3 |
| 14.1@contrat | liste-ajouter "2. Un contrat" |
| 14.2@surveillante | etiquette ex "La surveillante" 3.4 1.3 ; picto-retirer parlement ; picto document 3.4 0.0 |
| 15.1@communauté | liste-ajouter "3. Communauté de risques" |
| 15.2@cordée | etiquette ex "La cordée" 3.4 1.3 ; picto-retirer document ; picto corde 3.4 0.0 |
| 16.1@création | liste-ajouter "4. Risque créé" |
| 16.2@danger | etiquette ex "Le danger créé" 3.4 1.3 ; picto-retirer corde ; picto danger 3.4 0.0 |
| 16.2@mal | etiquette-retirer ex ; picto-retirer danger ; repere-liste "Loi" "Contrat" "Communauté" "Risque" |
| 17.1 | scene-vide ; personnage fonct "Un fonctionnaire" ambre_pale gauche ; titre "Un cas réel" |
| 17.1@fédéral | arret "ATF 134 IV 255" |
| 17.2@plaque | effacer-titres ; picto vagues 0.6 -0.7 ; etiquette x "Plaque dans le Rhône" 0.2 0.4 |
| 18.1@risque | repere-marquer 4 ambre ; etiquette x "Danger pour les bateaux" 0.2 0.4 |
| 18.2@retirer | etiquette x "Retirer la plaque" 0.2 0.4 |
| 18.3@garant | repere-marquer 4 vert ; titre "Garant" ambre |
| 19.1 | scene-vide ; repere-marquer 4 neutre ; titre "Deux sortes de devoirs" ; personnage clara "Clara" turquoise gauche ; personnage fonct "Un fonctionnaire" ambre_pale centre |
| 19.2@protection | effacer-titres ; retirer clara ; retirer fonct ; colonnes "Protection" "Surveillance" ; colonne-accent 1 ; picto vagues -3.5 -1.4 |
| 20.1@surveillance | colonne-accent 2 ; picto danger 3.5 -1.4 |
| 20.2@clara | etiquette c1 "Clara" -3.5 -0.4 |
| 20.3@fonctionnaire | etiquette c2 "Le fonctionnaire" 3.5 -0.4 |
| 21.1 | scene-vide ; arret-retirer ; decor piscine ; personnage clara "Clara" turquoise gauche ; placer clara -2 ; picto telephone -2.3 -0.9 |
| 21.2@engagée | repere-marquer 2 ambre ; etiquette c "Engagée" -3.2 1.7 |
| 21.2@poste | etiquette c "À son poste" -3.2 1.7 |
| 22.1@prise | etiquette c "Prise de poste effective" -3.2 1.7 ; arret "ATF 141 IV 249" |
| 22.2@garante | repere-marquer 2 vert ; etiquette c "Garante" -3.2 1.7 |
| 23.1@maël | arret-retirer ; repere-marquer 2 neutre ; personnage mael "Maël" bleu_clair centre ; placer mael 0 |
| 23.2@loi | repere-marquer 1 gris |
| 23.2@contrat | repere-marquer 2 gris |
| 23.2@risque | repere-marquer 3 gris ; repere-marquer 4 gris |
| 23.3@garant | etiquette m "Pas garant" 0 1.0 |
| 24.1 | scene-vide ; repere-marquer 1 neutre ; repere-marquer 2 vert ; repere-marquer 3 neutre ; repere-marquer 4 neutre ; personnage clara "Clara" turquoise gauche ; titre "Encore deux conditions" |
| 24.2@agi | effacer-titres ; case "Accident évité ?" |
| 25.1@hypothèse | titre "Par hypothèse" ; arret "ATF 117 IV 130" |
| 25.2@sauvé | sous-titre "Sauvé à temps ?" |
| 26.1@équivalence | effacer-titres ; arret-retirer ; case "Équivalence" |
| 26.2@geste | titre "Comme un geste" |
| 27.1@remplies | cocher 1 vert ; cocher 2 vert |
| 27.1@blessures | titre "Clara répond des blessures" |
| 27.2@atténuer | effacer-titres ; sous-titre "Peine atténuable" |
| 28.1 | scene-vide ; renvoi "vidéo 4" ; colonnes "Négligence" "Intention" ; picto telephone -3.5 -1.4 |
| 28.3@négligence | colonne-accent 1 |
| 28.3@plainte | etiquette p "Sur plainte" -3.5 -0.4 |
| 28.4@exprès | colonne-accent 2 |
| 28.5@grave | etiquette g "Bien plus grave" 3.5 -0.4 |
| 29.1 | scene-vide ; titre "Le piège classique" |
| 29.2@maël | effacer-titres ; personnage mael "Maël" bleu_clair gauche ; sous-titre "Pas garant, rien à se reprocher" |
| 29.3@subtil | barrer |
| 30.1@infraction | effacer-titres ; titre "Pour tous" |
| 30.2@omission | etiquette o "Omission de prêter secours" -0.2 0.4 |
| 30.2@cent | article "Art. 128 CP" |
| 31.1@mort | etiquette o "Danger de mort imminente" -0.2 0.4 |
| 31.2@exiger | etiquette o "Si on peut l'exiger" -0.2 0.4 |
| 31.3@blessée | etiquette o "Ou sa propre victime" -0.2 0.4 |
| 32.1 | scene-vide ; article-retirer ; decor piscine ; personnage mael "Maël" bleu_clair centre ; placer mael 0 ; personnage timeo "Timéo" rose droite ; placer timeo 2 |
| 32.1+2.5 | accent timeo |
| 32.2@aide | etiquette aide "Au moins appeler à l'aide" -2.2 1.7 |
| 33.1 | scene-vide ; personnage mael "Maël" bleu_clair gauche |
| 33.2@blessures | case "Les blessures" ; cocher 1 gris |
| 33.3@secours | case "Secours omis" ; cocher 2 vert |
| 33.4@trois | sous-titre "3 ans au plus" |
| 34.1 | scene-vide ; article-retirer ; titre "Retenons" ; picto vagues 2.2 -1.0 |
| 34.2@crime | effacer-titres ; liste-ajouter "Omission punissable" |
| 34.3@garant | liste-ajouter "Garant seulement" |
| 35.1@loi | repere-marquer 1 ambre |
| 35.1@contrat | repere-marquer 2 ambre |
| 35.1@communauté | repere-marquer 3 ambre |
| 35.1@risque | repere-marquer 4 ambre |
| 36.1@secours | liste-ajouter "Sinon : porter secours" |
| 36.2 | scene-vide ; repere-marquer 1 neutre ; repere-marquer 2 neutre ; repere-marquer 3 neutre ; repere-marquer 4 neutre ; titre "Devait-il agir ?" ; personnage mael "Maël" bleu_clair centre |
| 36.3@pourquoi | sous-titre "Et pourquoi ?" |
| 37.1 | scene-vide ; titre "Une question pour finir" |
| 37.2 | effacer-titres ; decor parc ; personnage lucas "Lucas" violet gauche ; placer lucas -1 ; picto feu -0.4 -1.9 |
| 37.3@part | marcher lucas -4 |
| 37.3@étend | etiquette feu "Le feu s'étend" -0.4 1.0 |
| 38.1@garant | etiquette-retirer feu ; titre "Lucas était-il garant ?" ambre |
| 38.2@sources | sous-titre "Quelle source ?" |
| 38.3@commentaire | accent lucas |
| 39.1 | scene-vide ; repere-retirer ; livre ; titre "L'étude du droit" ; sous-titre "Tout est dans la description" |
| 39.2 | accent titre |
