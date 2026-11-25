# Standards des vidéos « grands arrêts de droit constitutionnel »

Ce document consigne ce qui a été demandé, corrigé et validé sur les trois premières vidéos de la série (Emmen, ATF 129 I 217 ; Aînées pour le climat, ATF 146 I 145 ; Zurich, ATF 129 I 232). Il s'applique d'office à chaque nouvelle vidéo de la série : rien de ce qui suit ne doit avoir à être redemandé. Il complète le brief (`CLAUDE.md`) et la charte visuelle (`docs/charte-visuelle.md`) ; en cas de désaccord sur le style, c'est ce document qui vaut pour la série.

Dernière mise à jour : 25 novembre 2026.

## 1. Déroulement d'une vidéo

1. **L'autrice envoie son script** (PDF, deux colonnes : direction de voix, texte à enregistrer).
2. **Audit** contre l'arrêt et contre Fedlex, puis réponse courte : ce qui est faux, ce qui est à resserrer, ce qui est conforme. Chaque correction est proposée avec sa formulation de remplacement.
3. **Script revu en PDF**, dans la mise en page de l'autrice, dès qu'elle a validé les corrections. C'est ce document qu'elle lit pour enregistrer : ne pas se contenter de la pull request.
   - Livré en **PDF annoté et en Word modifiable**, avec les **liaisons à faire mises en évidence** (signe ‿ et lettres soulignées en rouge) : seulement les liaisons obligatoires ou attendues en lecture soignée, jamais les facultatives ni les simples enchaînements.
   - Séquences corrigées repérées (trait ambre), consignes de voix ajustées repérées (brun). Après toute correction, relire chaque consigne de voix : elle doit viser des mots réellement présents dans sa séquence.
   - Outil : `python tools/script_arret_annote.py arrets/<slug>` produit `script.md`, `tts.txt`, le PDF et le Word à partir de `sequences.py` (modèle : ATF 121 I 367).
4. **Pull request « script »** : `script.md`, `audit.md`, `tts.txt`, générés d'une seule source pour rester identiques.
5. **L'autrice enregistre** (voix humaine, téléphone, prises ratées comprises).
6. **Montage, images, son, contrôles** (sections 2 à 6), puis livraison : vidéo 1080p, version légère, sous-titres, miniature, kit de publication, fiche PDF.
7. **Pull request « enregistrement »**. Rien n'est publié : l'autrice met en ligne elle-même. Quand elle donne le lien et la date, mettre à jour la page du site.

Le dossier porte la référence de l'arrêt tant que le numéro dans la série n'est pas attribué.

## 2. Vérification juridique

- Lois : ouvrir Fedlex avec le navigateur intégré (le shell et la recherche web ne l'atteignent pas), noter l'état et la date de consultation, citer le texte exact dans l'audit.
- Arrêt : lire le texte original. Si seul un miroir est accessible (servat.unibe.ch), le dire dans l'audit et laisser la relecture sur bger.ch à l'autrice.
- Tout ce qui s'affiche à l'écran reprend le script ou un article vérifié. Aucun chiffre inventé pour « faire vrai » (pas de pourcentage de vote fictif).
- Ne jamais prêter à une partie un motif que l'arrêt ne rapporte pas : distinguer ce que disent les faits, ce que soutient l'autorité et ce qu'apprécie le Tribunal.
- L'audit donne pour chaque correction son fondement (considérant, page, courte citation) et traite à part les points que l'autrice demande de vérifier.
- Institutions cantonales : nom officiel français à la première occurrence (« Conseil-exécutif bernois »), forme courante ensuite.
- Une phrase de l'autrice sans source est signalée, avec l'état réel de la pratique ; elle décide de la garder ou de la couper.
- « Cour EDH » pour la Cour, « CEDH » pour la Convention. Strasbourg n'est pas l'Union européenne : jamais d'étoiles.
- Partis et personnes : le parti auteur est nommé, jamais son logo ; les particuliers ne sont pas nommés. La chaîne ne prend pas position.

## 3. La voix

### Montage
- `tools/alignement.py` retrouve chaque phrase et garde la dernière bonne prise. Le moteur de transcription local tronque parfois le dernier mot d'un passage court : l'alignement peut alors déborder sur le passage voisin.
- **Contrôles obligatoires avant tout rendu** (`tools/controle_voix.py`) :
  1. aucune coupe ne mord sur un passage de voix voisin (fin d'une prise écartée, début de la phrase suivante) ;
  2. aucun son à niveau de voix dans les silences entre deux phrases ;
  3. la narration montée, retranscrite, redonne le texte, séquence par séquence ; les passages douteux sont retranscrits à part, sur un extrait plus long ;
  4. les passages que la machine ne peut pas trancher sont donnés à l'autrice avec leur minutage, dans la vidéo.
- Une prise ratée sans rechange : proposer de réenregistrer **la phrase d'avant, la phrase, la phrase d'après** (on ne garde que celle du milieu), ou une coupe si le sens reste complet. Pour montrer un passage, envoyer un extrait audio de l'enregistrement brut, avec des minutages en minutes et secondes, en précisant s'il s'agit de l'enregistrement ou de la vidéo.
- On ne synthétise jamais la voix de l'autrice.

### Qualité du son
- **Timbre de référence : la voix traitée de la vidéo 25** (`render/manim/atf-129-i-232/son/ref25.npy`, spectre par tiers d'octave). Chaque nouvelle voix est égalisée vers cette référence (±8 dB au plus) ; l'écart moyen visé est inférieur à 1,5 dB. À l'intérieur d'une vidéo, les parties enregistrées à des moments différents sont d'abord ramenées au même timbre.
- **Niveau** : chaque séquence au même niveau, vidéo finale entre −15 et −16 LUFS.
- **Pas de limiteur qui pompe** : monter la narration assez bas pour que le limiteur du montage ne touche presque rien (`reglages.json`, `{"niveau": -22}` pour un enregistrement faible), donner le niveau au mixage, limiteur doux sur les seules crêtes (1 % d'échantillons retouchés au plus).
- **Rythme** (« sinon c'est soporifique ») : silences resserrés (0,38 s dans une séquence, 0,7 s entre deux séquences, 0,95 s avant un carton de partie), voix accélérée de 5 % sans changer la hauteur, une pause de réflexion après la question finale.
- **Bruitages** discrets (mixés à 0,22) ; jamais de son strident (le « zip » est banni, remplacé par un souffle).
- Dire ce que la mesure montre, et rappeler que le résultat ne peut pas être écouté par l'agent : c'est l'oreille de l'autrice qui tranche.

## 4. L'image

### Principes
- Style rouge : fond rouge de la marque, formes crème et encre, **des icônes en couleur** (voir la palette).
- **Chaque phrase fait apparaître ou bouger quelque chose.** Aucun écran vide plus d'une seconde et demie, aucun plan fixe de plus de quatre secondes.
- **La narration est en images jusqu'à la fin.** Les séquences de portée, de droit actuel, de synthèse et la question finale sont des petites scènes avec personnages, pas des listes de texte.
- Jamais plus de douze mots affichés à la fois, hors texte d'article.
- Rien ne sort du cadre, rien ne se chevauche : contrôler chaque section sur une planche-contact avant le rendu final, puis des images de la vidéo finale.

### Personnages : toujours un visage, toujours une réaction
| Personnage | Dessin | Brique |
| --- | --- | --- |
| Personne qui demande la naturalisation (ou requérante) | robe d'une couleur fixe par personnage | `candidat` |
| Personne naturalisée | une croix suisse apparaît sur son maillot ; la personne refusée n'a rien et son visage est triste | `maillot_ch` |
| Corps électoral | maillot aux couleurs du canton (Zurich : bleu et blanc), drapeau du canton et drapeau suisse à côté du groupe | `electeurs(..., drapeaux=True)`, `colorer_foule` |
| Juge | robe noire, rabat blanc, toque | `juge` |
| Agent de l'administration | silhouette claire, col sombre | `agent` |
| Parti politique | trois militants à écharpe derrière une banderole à son nom, jamais le logo | `parti`, `militant` |
| La Terre (climat) | varie selon le récit : contente, inquiète, malade (poche de glace et thermomètre médical sur le front), chaude | `terre` |

- **Émotions cohérentes avec le récit** : à chaque décision, les personnages concernés réagissent (content et petit saut quand on gagne, triste quand on perd, surpris devant un coup de théâtre, perplexe devant une question ouverte, muet pour un vote secret). Un personnage suit son affaire d'une instance à l'autre et change de visage à chaque étape.
- **Les personnages interagissent avec le texte** : le juge montre du doigt le passage de l'article, la requérante parle, l'agent examine le dossier à la loupe, les électeurs reçoivent l'information.
- **Tout personnage à l'écran a un rôle lisible** : une étiquette sous lui (« Une autorité », « Tribunal fédéral ») ou une action claire. Jamais de silhouette posée là sans raison, jamais d'étiquette ou de tampon par-dessus un personnage. Quand une instance « répond », c'est son personnage qui apparaît (un juge pour le Tribunal fédéral), pas une étiquette seule.

### Cantons et drapeaux
- Les couleurs d'un canton sont réservées à son identité (maillots des électeurs, drapeau). **Les objets génériques restent neutres** : le bandeau de l'urne est menthe, pas bleu, pour ne pas être lu comme zurichois ou lucernois.
- Deux cantons peuvent avoir les mêmes couleurs (Zurich et Lucerne : bleu et blanc). Dès que deux cantons sont comparés, chaque drapeau porte le nom du canton à côté (`drapeau_nomme`).
- Chaque drapeau est vérifié sur une source avant d'être dessiné. Zurich : tranché, bleu côté hampe en bas, blanc en haut au vent (`drapeau_zh`). Lucerne : coupé, blanc en haut, bleu en bas (`drapeau_lu`). Une commune (Emmen) est située par le drapeau de son canton, nommé.

### Institutions, textes et décisions
| Élément | Dessin | Brique |
| --- | --- | --- |
| Parlement | hémicycle et tribune | `ic_parlement` |
| Autorité de surveillance, conseil | membres à une table | `ic_district` |
| Gouvernement cantonal | hôtel du gouvernement, drapeau | `ic_gouvernement` |
| Tribunal fédéral | temple à colonnes | `tribunal`, `ic_tf` |
| Cour de Strasbourg | bâtiment à deux tours rondes, sans étoiles ; « Conseil de l'Europe : 46 États, dont la Suisse » une fois | `cour` |
| Parcours de procédure | une carte illustrée par instance, avec date et décision | `station` |
| Constitution fédérale | cahier clair, bandeau sombre, croix suisse | `constit` |
| Loi fédérale hors code | livret crème, bandeau sombre, croix suisse | `loi` |
| Code (CO, CC, CP) | livre jaune | `code` |
| Traité | couverture bleu nuit et or, emblème (balance pour la Convention) | `traite` |
| Article cité | page avec son texte exact ; le passage dit est encadré au moment où il est dit | `page`, `cadre_autour` |
| Droit fondamental | carte avec une image qui porte l'émotion : arbre pour la vie, foyer pour la vie privée et familiale, fiche sous cadenas pour les données | `carte_droit`, `icone_vie`, `icone_foyer`, `donnees` |
| **Décision** | feuille à en-tête (« DÉCISION », « ARRÊT DU TRIBUNAL FÉDÉRAL »), dispositif en tampon vert ou rouge, sceau à ruban | `decision`, `arret_tf`, `verdict` |
| Initiative, acte invalidé | page, tampon « INVALIDE » | `initiative`, `tampon` |
| Dossier d'une personne | chemise ambre à onglet, feuille à en-tête, portrait agrafé ; les rubriques apparaissent une à une | `fiche` (dossier du candidat), `dossier` (petite icône) |

### Palette des icônes
Dossier ambre, cadenas doré, loupe à verre bleu, urne à bandeau menthe, fenêtres éclairées, passeport rouge à croix blanche, pastille verte pour oui, croix rouge pour non, pastille ambre pour une question ouverte, robes menthe, ambre, lilas et ciel.

## 5. Le texte du bas et les sous-titres

- Une ligne à la fois, **42 caractères au plus**, coupée de préférence après une ponctuation, **jamais sur un petit mot** (« à la », « de », « qui »), jamais avec une ponctuation en tête de ligne.
- Le surlignage suit les mots tels qu'ils sont dits (instants des mots, pas un calcul au prorata sur la phrase).
- Chiffres arabes pour les dates, les articles et les nombres ; orthographe et tournures du texte de l'autrice.
- Le fichier `.srt` livré est le même découpage.

## 6. Contrôles avant de livrer

| Contrôle | Seuil |
| --- | --- |
| Coupes de montage | aucune ne mord sur un passage voisin |
| Silences | aucun son à niveau de voix entre deux phrases |
| Texte | retranscription conforme, passages douteux listés avec leur minutage |
| Calage son-image | écart constant d'un bout à l'autre (0,13 à 0,16 s) |
| Niveau | −15 à −16 LUFS |
| Timbre | écart moyen à la référence inférieur à 1,5 dB |
| Scènes | aucun « DEPASSEMENT », aucun « MOT INTROUVABLE » dans les journaux de rendu |
| Images | planche-contact de chaque section, images de la vidéo finale aux endroits modifiés |
| Chapitres | recalculés à chaque changement de durée, dix secondes au moins entre deux |

## 7. Miniature, kit de publication, fiche

- **Miniature** : **une idée différente pour chaque vidéo**, jamais le gabarit de la précédente. Ce qui reste commun : les couleurs de la marque, un seul objet ou une seule idée, peu de mots et très gros, lisible en tout petit, sobre, exacte en droit, les références en bas. Exemples : Aînées, deux panneaux « NON. » / « OUI. » avec la Terre sur la couture (Tribunal fédéral en rouge, Strasbourg en brun) ; Zurich, un bulletin de vote « Peut-elle devenir suisse ? » frappé du tampon « INVALIDE ». Source : une page HTML photographiée (`miniature/m.html`).
- **Kit** (`publication.md`) : trois titres, description, chapitres, sources avec liens Fedlex et bger, ce que disent les articles, réponse à la question finale, commentaire à épingler, mots-clés, réglages, points à vérifier avant de publier. Mention de la licence CC BY-SA 4.0 et de la voix humaine.
- **Fiche de cours** : deux pages au plus, tirée du texte du script.
- Fichiers livrés avec un numéro de version dans le nom ; une version « légère » pour regarder, la version 1080p pour YouTube.

## 8. Ce qui est automatisé, et où

- Briques graphiques : `render/manim/atf-129-i-232/base.py`, section « STANDARDS GRANDS ARRÊTS » (à extraire dans `render/manim/commun/` à la prochaine vidéo, sans changer les noms).
- Texte du bas et sous-titres : `srt.py`, `ass.py`.
- Son : `son/egaliser.py` (timbre de référence, niveau, limiteur doux), `son/mix.py` (rythme, bruitages).
- Contrôles de la voix : `tools/controle_voix.py`.
- Chaîne complète : `tout.sh <version>` ; `tout.sh <version> son` pour ne refaire que le son et l'encodage.

Toute nouvelle demande récurrente de l'autrice est ajoutée ici le jour même, avec la brique ou le contrôle qui l'applique.
- Reprise par une autre session ou un autre modèle : `docs/passation-grands-arrets.md` (état des pull requests, chaîne de production, chemins à adapter, erreurs à surveiller) ; outils `tools/transcrire_secours.py` et `tools/extrait_audio.py`.
