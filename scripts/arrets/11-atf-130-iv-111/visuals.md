# Visuels — Arrêts, vidéo 11 : Une réunion sur invitation : est-ce « en public » ?

Ce fichier pilote les schémas Manim (`render/manim/video.py`). Vocabulaire des actions : `render/manim/README.md`.

Style « scène » : la réunion a lieu dans une cabane en forêt ; aucun décor de cabane n'existe, le décor « parc » (un arbre, une haie) sert de lisière, et l'étiquette dit « Une cabane en forêt ». Silhouettes sans visage : X., l'organisateur (turquoise), Y., l'orateur (bleu clair), deux invités (ambre pâle et rose) qui représentent l'assistance. Le juge (violet) apparaît dans la salle d'audience (décor tribunal). Aucun propos, aucun symbole du milieu n'est montré : la conférence n'est désignée que par « Une conférence ». Le cercle « privé » et le cercle « public » sont rendus par deux colonnes « Privé » / « Public ». Bloc de l'arrêt à côté de l'article.

| Moment | Actions |
| --- | --- |
| 1.1 | decor parc ; etiquette lieu "Septembre 1999" -4.2 2.6 |
| 1.1+2.5 | etiquette cabane "Une cabane en forêt" 2.8 2.6 |
| 1.2 | etiquette lieu "Canton de Berne" -4.2 2.6 |
| 2.1 | etiquette-retirer lieu ; etiquette-retirer cabane ; personnage x "X." turquoise gauche ; placer x -3 |
| 2.2 | picto document -2.8 0.6 ; etiquette invit "Invitation écrite" -4.2 2.6 |
| 3.1 | etiquette-retirer invit ; picto-retirer document ; personnage y "Y." bleu_clair centre ; placer y 1 ; etiquette role "L'orateur" 1.6 2.6 |
| 3.2 | etiquette role "Une conférence" 1.6 2.6 |
| 4.1 | etiquette role "Pas membre" 1.6 2.6 ; accent y |
| 4.2 | etiquette-retirer role ; personnage inv1 "Invité" ambre_pale centre-droite ; placer inv1 2 |
| 5.1 | etiquette entree "Contrôle à l'entrée" 3.8 2.6 ; picto document 4.4 1.2 |
| 5.2 | picto-retirer document ; personnage inv2 "Invité" rose droite ; placer inv2 3 |
| 6.1 | etiquette-retirer entree ; etiquette nombre "40 à 50 personnes" 2.4 2.6 |
| 6.2 | accent inv1 ; accent inv2 |
| 7.1 | scene-vide ; arret "ATF 130 IV 111" ; personnage x "X." turquoise gauche ; personnage y "Y." bleu_clair centre-droite ; titre "Discrimination raciale ?" |
| 7.2 | etiquette yreproche "Minimiser ?" 2.2 2.4 ; accent y |
| 7.3 | etiquette xreproche "Propagande ?" -4.5 2.4 ; accent x |
| 8.1 | etiquette-retirer xreproche ; etiquette-retirer yreproche ; article "Art. 261bis CP" |
| 8.2 | effacer-titres ; titre "Publiquement" ambre ; sous-titre "Crimes contre l'humanité minimisés" |
| 9.1 | scene-vide ; titre "Le mot clé" ; colonnes "Privé" "Public" ; picto prison 3.5 -1.2 |
| 9.2 | colonne-accent 1 ; sous-titre "En principe : pas punissable" |
| 10.1 | scene-vide ; article-retirer ; decor tribunal ; personnage x "X." turquoise gauche ; placer x -1 ; personnage juge "Le juge" violet droite ; placer juge 3 ; etiquette verdict "Acquittés" 0.6 2.4 |
| 10.2 | etiquette verdict "Juin 2003 : confirmé" 0.6 2.4 ; accent juge |
| 11.1 | scene-vide ; colonnes "Privé" "Public" ; colonne-accent 1 ; titre "Pas publique" ; picto document -3.5 -1.2 |
| 11.2 | sous-titre "Le contenu n'est pas examiné" |
| 12.1 | scene-vide ; decor tribunal ; personnage juge "Le juge" violet droite ; placer juge 3 ; titre "Recours au Tribunal fédéral" |
| 12.2 | effacer-titres ; titre "Fermée, donc privée ?" ambre ; accent juge |
| 13.1 | scene-vide ; titre "La définition habituelle" ; personnage juge "Le juge" violet droite |
| 13.2 | liste "Nombre indéterminé" |
| 14.1 | liste-ajouter "Cercle large, sans liens" ; liste-surligner 2 |
| 15.1 | scene-vide ; titre "Le nombre comptait" ; picto document 0 0.3 |
| 15.2 | etiquette lettre "432 : public" -3.2 0.3 |
| 15.3 | etiquette livre "7 : privé" 3.2 0.3 |
| 16.1 | etiquette-retirer lettre ; etiquette-retirer livre ; effacer-titres ; titre "Pas de seuil fixe" ; mot-barre "Seuil : 20" 3.6 0.3 |
| 17.1 | scene-vide ; livre "Code pénal" 0 -0.5 ; titre "Une question de méthode" |
| 17.2 | effacer-titres ; titre "Un sens par article" |
| 18.1 | livre-ouvrir ; livre-chercher ; effacer-titres ; titre "Quel bien protégé ?" ambre |
| 19.1 | scene-vide ; article "Art. 261bis CP" ; titre "La dignité" ; personnage inv1 "Invité" ambre_pale centre |
| 19.2 | sous-titre "Race, ethnie, religion" ; accent inv1 |
| 19.3 | effacer-titres ; titre "Et la paix publique" |
| 20.1 | scene-vide ; colonnes "Privé" "Public" ; colonne-accent 1 ; titre "Le législateur" ; picto parlement 0 -1.2 |
| 20.2 | sous-titre "Pas d'enquête pénale" |
| 21.1 | effacer-titres ; titre "Changement de jurisprudence" ambre |
| 21.2 | colonne-accent 2 ; effacer-titres ; titre "Public : tout ce qui n'est pas privé" |
| 22.1 | scene-vide ; titre "Le nombre ne décide plus" ; mot-barre "Compter" 0 0.3 ; personnage inv1 "Invité" ambre_pale gauche ; personnage inv2 "Invité" rose droite |
| 22.2 | sous-titre "Souvent dû au hasard" |
| 23.1 | scene-vide ; titre "Ce qui est privé" ; liste "Famille" "Amis" ; personnage inv1 "Invité" ambre_pale centre-droite ; personnage inv2 "Invité" rose droite |
| 23.2 | liste-ajouter "Confiance particulière" ; liste-surligner 3 |
| 24.1 | scene-vide ; personnage inv1 "Invité" ambre_pale gauche ; personnage inv2 "Invité" rose droite ; titre "Le nombre peut jouer" |
| 24.2 | deplacer inv1 centre-gauche ; deplacer inv2 centre-droite ; effacer-titres ; titre "Plus proches, cercle plus large" |
| 25.1 | scene-vide ; personnage x "X." turquoise centre-gauche ; personnage y "Y." bleu_clair centre-droite ; etiquette tete "Tête-à-tête : privé" 0 2.4 |
| 26.1 | scene-vide ; titre "Pas suffisant pour être privé" ; personnage inv1 "Invité" ambre_pale centre-droite ; personnage inv2 "Invité" rose droite |
| 26.2 | mot-barre "Mêmes idées" -3.6 0.8 |
| 26.3 | mot-barre "Entrée contrôlée" -3.6 -0.6 |
| 27.1 | scene-vide ; titre "Empêcher que ces idées s'étendent" ambre ; article "Art. 261bis CP" ; personnage inv1 "Invité" ambre_pale centre-gauche ; personnage inv2 "Invité" rose centre-droite |
| 28.1 | scene-vide ; article-retirer ; arret-retirer ; decor parc ; personnage x "X." turquoise gauche ; placer x -3 ; personnage y "Y." bleu_clair centre ; placer y 1 |
| 28.2 | personnage inv1 "Invité" ambre_pale centre-droite ; placer inv1 2 ; personnage inv2 "Invité" rose droite ; placer inv2 3 ; etiquette groupes "Différents groupes" 2.4 2.6 |
| 28.3 | etiquette groupes "Pas tous connus" 2.4 2.6 |
| 29.1 | etiquette groupes "Pas tous liés" 2.4 2.6 ; accent inv1 |
| 29.2 | etiquette groupes "Pas un cercle de confiance" 2.4 2.6 ; accent inv2 |
| 30.1 | scene-vide ; cases "Réunion fermée" "Mêmes convictions" ; personnage juge "Le juge" violet gauche |
| 30.2 | cocher 1 gris ; cocher 2 gris ; titre "Pas privée" |
| 30.3 | effacer-titres ; titre "Donc publique" ambre ; accent cases |
| 31.1 | scene-vide ; decor tribunal ; personnage juge "Le juge" violet droite ; placer juge 3 ; titre "Recours admis" ; arret "ATF 130 IV 111" |
| 31.2 | sous-titre "L'acquittement ne tient plus" ; accent juge |
| 32.1 | effacer-titres ; titre "Le contenu : pas tranché" ambre |
| 32.2 | sous-titre "Non examiné par la cour bernoise" |
| 33.1 | scene-vide ; arret-retirer ; mot-barre "Combien ?" -3.6 0.3 ; personnage inv1 "Invité" ambre_pale centre-droite |
| 33.2 | titre "Quels liens ?" ambre ; personnage inv2 "Invité" rose droite |
| 34.1 | scene-vide ; personnage inv1 "Invité" ambre_pale centre-gauche ; personnage inv2 "Invité" rose centre-droite ; etiquette inconnus "Inconnus, mêmes idées" 0 2.4 |
| 34.2 | etiquette inconnus "Porte fermée : rien ne change" 0 2.4 |
| 35.1 | scene-vide ; article "Art. 261bis CP" ; titre "Le texte actuel" ; livre "Code pénal" -3 |
| 35.2 | etiquette orientation "+ orientation sexuelle" 2.6 0.3 |
| 35.3 | effacer-titres ; titre "Absente du texte de l'arrêt" |
| 36.1 | scene-vide ; article-retirer ; titre "Le piège classique" ; personnage x "X." turquoise gauche ; bulle x "Porte fermée, donc privé" |
| 37.1 | effacer-bulle x ; mot-barre "Porte fermée" |
| 37.2 | effacer-titres ; titre "Les liens comptent" ambre |
| 37.3 | sous-titre "Pas la porte ni le nombre" |
| 38.1 | scene-vide ; titre "Retenons" ; personnage juge "Le juge" violet droite |
| 38.2 | article "Art. 261bis CP" ; liste "Public : tout sauf le privé" |
| 39.1 | scene-vide ; personnage juge "Le juge" violet droite ; liste "Famille, amis, confiance" |
| 39.2 | liste-ajouter "Le nombre seul ne décide pas" ; liste-surligner 2 |
| 40.1 | scene-vide ; article-retirer ; titre "Une question pour finir" ; personnage juge "Le juge" violet gauche |
| 40.2 | effacer-titres ; titre "Contrôle à l'entrée : privé ?" ambre |
| 40.3 | accent juge |
| 41.1 | scene-vide ; livre "Code pénal" 0 -0.5 ; titre "L'étude du droit" ; sous-titre "Tout est dans la description" |
| 41.2 | accent titre |
