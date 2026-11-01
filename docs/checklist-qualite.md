# Checklist qualité — avant de publier une vidéo

Tous les problèmes rencontrés sur les vidéos 1 à 4, transformés en points de contrôle.
**Auto** : vérifié par un outil (`make video`, `make paquet`). **Œil** : à regarder. **Juriste** : relecture humaine.

## 1. Droit

| ✓ | Point | Déjà arrivé | Contrôle |
|---|---|---|---|
| [ ] | Chaque article cité ouvert sur Fedlex, date de consultation notée dans l'audit | règle de départ | Agent + Juriste |
| [ ] | Le cas pratique est cohérent avec la qualification (montants, valeur, intention) | v3 : tag « quelques dizaines de francs » → contravention (art. 172ter), pas délit ; téléphone sans valeur | Juriste (PDF de vérification → GPT, puis relectrice) |
| [ ] | La formule de la loi est respectée, pas seulement l'idée (« vise » = intention) | v3 : art. 172ter « si l'objet n'avait qu'une faible valeur » → « si Inès n'avait visé… » | Juriste |
| [ ] | Les tiers et cas particuliers ne sont pas oubliés | v2 : art. 146 « ou d'un tiers » ; « enrichir quelqu'un d'autre » | Juriste |
| [ ] | Dates et entrée en vigueur exactes | v2 : nouvelle loi « entre en vigueur le 1er juin » | Juriste |
| [ ] | Arrêts du TF pertinents cités à l'écran et dans la description | v2 : ATF absents | Œil + Auto (liste de la description) |
| [ ] | Droit cantonal signalé comme tel ; « ici » quand une exception existe | v3 : art. 126 al. 2 (poursuite d'office) | Juriste |
| [ ] | Aucun « À VÉRIFIER » restant dans le script et l'audit | — | Auto (`make check`) |

## 2. Voix

| ✓ | Point | Déjà arrivé | Contrôle |
|---|---|---|---|
| [ ] | Aucun mot juridique manquant ou changé (numéros d'article, « au plus ») | v3 : « article cent » au lieu de « cent trois » ; « trois ans **ou** plus » | Auto (transcription complète comparée aux sous-titres) + écoute des passages signalés |
| [ ] | Aucun faux départ ni prise ratée restée dans le montage | v4 : « Pas d'intention, pas d'impr— » puis reprise | Auto (même comparaison) |
| [ ] | Début de phrase non coupé | v1/v4 : « Sofia » coupé | Auto (`alignement.py`, extension 1 s) + Œil |
| [ ] | Volume homogène entre une reprise et le reste | v2, v3 : reprises plus faibles (+4 à +8 dB) | Agent (mesure du volume) + écoute |
| [ ] | Voix configurée ou enregistrement humain seulement | règle de départ | Agent |

## 3. Sous-titres

| ✓ | Point | Déjà arrivé | Contrôle |
|---|---|---|---|
| [ ] | Les sous-titres disent exactement ce que la voix dit | v1–v5 : petites reformulations à l'enregistrement ; v4 « et il se dit » | Auto (comparaison) ; écarts restants écoutés |
| [ ] | `tts.txt` et `script.md` synchronisés après chaque changement | v1–v5 | Agent |

## 4. Images

| ✓ | Point | Déjà arrivé | Contrôle |
|---|---|---|---|
| [ ] | Aucun texte qui en chevauche un autre | v2 : colonnes sur le livre ouvert ; v4 : titre et sous-titre collés | Auto (`alertes-visuels.txt`) + Œil (planche toutes les 3 s) |
| [ ] | Rien sur l'enseigne ou les traits du décor | v3 : tag et étiquettes sur « Boulangerie » | Auto (contrôle de l'enseigne) + Œil |
| [ ] | Bulle de pensée du bon côté, jamais sur un personnage | v2 : bulle sur Tom au lac | Auto |
| [ ] | Nom de personnage lisible, sous sa silhouette | v2 : nom de Nora barré par la frise ; v4 : nom d'Adam resté sur le poteau en sortant de la haie | Auto (frise) + Œil |
| [ ] | Livre, schéma ou bloc jamais collé au titre/sous-titre | v3, v4 : livre « Code pénal » sous « Tout est dans la description » | Œil |
| [ ] | Icône de retour en arrière sur écran vide, avant le décor | v3 (5:32), v4 : icône sur l'enseigne | Auto (le moteur la joue avant le décor) |
| [ ] | Le bloc d'article à l'écran = l'article que la voix cite | v3 : « Art. 109 CP » pendant l'art. 97 ; « Art. 144 CP » pendant l'art. 172ter | Auto (`tools/verifier_articles.py`) |
| [ ] | Le remplacement d'un titre ou d'une étiquette ne superpose pas l'ancien et le nouveau | v2 : étiquettes en fondu croisé | Auto (fondu successif) |
| [ ] | Charte : fond noir, accent rouge marque, vert/gris, ambre = dommage ; ≥ 28 pt ; ≤ 12 mots | changement de grille v2 | Auto (12 mots) + Œil |
| [ ] | Pas de plan texte seul trop long ; vidéo assez illustrée | v2 « pauvre en visuels » | Auto (« Texte seul : N s ») + Œil |
| [ ] | Animation pas en retard de plus de 0,5 s sur la voix | v3, v4 | Auto (alerte) |

## 5. Publication

| ✓ | Point | Déjà arrivé | Contrôle |
|---|---|---|---|
| [ ] | Description sans note interne (« lignes 24 et 25 », « le script dit… ») | v3 | Auto (`make paquet` refuse) |
| [ ] | Liste des articles et des ATF avec liens Fedlex / bger | v2 : ATF absents | Auto |
| [ ] | Chapitres recalculés après tout changement de durée | v3 (4:00 → 4:01) | Auto (`make paquet`) |
| [ ] | Lien GitHub vers la bonne version du script (PR fusionnée) | v2, v3 : main montre l'ancien script | Agent → décision de la narratrice |
| [ ] | Miniature à la nouvelle charte | v2 | Œil |
| [ ] | Commentaire épinglé = question finale | v3 | Auto (`make paquet`) |
| [ ] | « Contenu synthétique » : oui seulement pour une voix de synthèse | — | Auto (`youtube.json`) |
| [ ] | Rien n'est envoyé à YouTube sans instruction explicite | règle de départ | Agent |

## Ordre des contrôles

1. Rendu : `make video SLUG=…` (alertes visuelles, articles à l'écran).
2. Voix : transcription complète comparée aux sous-titres ; écouter chaque écart.
3. Œil : planche d'images toutes les 3 s.
4. Juriste : PDF de vérification (`tools/script_pdf.py`) → GPT → relectrice ; corrections → nouveau rendu.
5. `make paquet SLUG=… TAGS="…"` → upload.
