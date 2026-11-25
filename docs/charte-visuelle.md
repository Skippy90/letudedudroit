# Charte visuelle — L'étude du droit

Un vocabulaire graphique fixe remplace le visage : le spectateur doit reconnaître la chaîne en une seconde et comprendre un schéma sans lire. Tout ce qui suit s'applique à chaque vidéo, sans exception, et devient le gabarit de code (Manim pour les schémas, Remotion pour l'habillage et les shorts).

## Vocabulaire graphique

| Élément | Représentation à l'écran |
| --- | --- |
| Une personne | Bonhomme en bâtons articulé, au trait de sa couleur, avec un visage simple (deux yeux, une bouche, des sourcils) ; expressions : neutre, content, triste, inquiet, surpris, fâché. Chaque personnage du cas garde sa couleur du début à la fin (depuis novembre 2026 ; l'ancien style « silhouette sans visage » reste disponible avec PERSONNAGES=silhouettes) |
| La loi | Bloc rectangulaire avec le numéro d'article à l'intérieur (« Art. 123 CP »), toujours centré en bas de l'image |
| L'infraction | Bâtiment à trois étages : Typicité en bas, Illicéité au milieu, Culpabilité en haut ; vert quand l'étage est franchi, gris quand il manque |
| Le temps et les délais | Frise horizontale où les délais se dessinent en direct |
| Les autorités | Pyramide à trois niveaux : autorité de première instance, autorité de recours cantonale, Tribunal fédéral |
| L'argent | Jetons qui se déplacent d'une silhouette à l'autre |
| Un fait justificatif | Bouclier |
| L'état d'esprit de l'auteur | Bulle de pensée au-dessus de la silhouette |
| Une variante du cas | Icône de rembobinage, puis le changement s'anime |

## Couleurs et typographie

- Fond sombre uni (noir, adopté le 30 octobre 2026 à la place du bleu nuit) ; texte et traits en blanc cassé ; le rouge suisse de la marque comme accent, pour ce qui est important à l'instant (les mots-clés s'écrivent en blanc sur une pastille rouge, comme le logo) ; vert pour « condition remplie », gris pour « condition manquante », ambre pour le dommage. Grille adoptée le 31 octobre 2026 ; l'ancienne (accent ambre, dommage rouge) reste disponible avec `THEME=ambre`.
- Valeurs de départ (à ajuster une fois rendues) : fond `#0B0B0B` (blocs `#1F1F22`), texte `#F2EFE6`, accent rouge suisse `#DA291C`, vert `#4CAF7D`, gris `#6B7280`, dommage ambre `#E3A52F`.
- Une seule famille de caractères, sans empattement, lisible sur téléphone : rien en dessous de l'équivalent de 28 points sur une image 1920 × 1080.
- Jamais plus de douze mots affichés en même temps, hors bloc d'article et hors sous-titres.

## Style « scène » (adopté le 30 octobre 2026)

Ajouts au vocabulaire graphique, validés sur le prototype de la vidéo 1 :

| Élément | Représentation à l'écran |
| --- | --- |
| Le lieu du cas | Décor au trait fin, blanc cassé très atténué, habillé de détails encore plus pâles (fenêtres, mobilier, trottoir, ciel du soir) depuis le 6 novembre 2026. Les vidéos déjà rendues gardent leurs décors et silhouettes d'origine : on ne les refait pas, l'évolution de la chaîne reste visible. (cage d'escalier, appartement, rue, parc, piscine, salle d'audience ; d'autres à venir : poste de police) ; il situe la scène sans concurrencer les silhouettes |
| Ce qui se passe | Les bonhommes bougent dans le décor : ils marchent (jambes et bras alternent), poussent, tombent, et changent de pose (`pose <id> tend|pointe|bras-ciel|assis|recule|debout [expression]`) ou de visage (`visage <id> <expression>`) au moment où la voix le dit. Sur un sujet grave (violence, maladie, décès), le visage reste neutre ou triste, jamais content |
| Un mot-clé | Étiquette courte en blanc sur pastille rouge, posée près de ce dont elle parle, qui apparaît au moment exact où le mot est prononcé |
| Un objet ou une idée simple | Pictogramme au trait (panneau « P » de parking, ligne brisée rouge de la tension entre deux personnes) |
| Où en est le raisonnement | Petit bâtiment à trois étages en haut à droite, présent du moment où les trois étages sont posés jusqu'à la fin ; ses étages suivent le cas principal (rouge : étage en cours d'examen ; vert : franchi) |
| Une liste de conditions qui structure toute la vidéo | Pense-bête en haut à droite, une case et un mot par condition (vidéo 2 : « Texte », « Précis », « Avant ») ; il remplace le petit bâtiment quand la vidéo ne suit pas les trois étages ; mêmes couleurs (rouge : condition examinée ; gris : elle manque dans le cas ; vert : remplie) |
| Un arrêt du Tribunal fédéral | Bloc « ATF … » au cadre rouge, en bas, à côté du bloc d'article, affiché pendant qu'on parle de cette jurisprudence |
| Une idée sans personnage | Pictogramme au trait plutôt qu'un écran de texte seul : prison (peine privative de liberté), pièces (argent), document (contrat), danger, édifice à colonnes (la loi votée), corde (cordée) |
| Ce qui est dit | Sous-titres incrustés en bas de l'image, sept mots au plus, coupés de préférence à la ponctuation, calés sur la voix ; police Inter, blanc cassé, même échelle que les plus petits textes |

Les silhouettes placées dans un décor sont réduites de 20 % pour tenir sur les marches ; leur nom garde sa taille.

## Style rouge : droit constitutionnel et grands arrêts (adopté le 23 novembre 2026)

Utilisé pour les arrêts 12 (Appenzell) et 15 (Emmen). Le fond noir reste celui du droit pénal ; le rouge signale la Constitution. Code : `render/manim/style_rouge/` et, pour l'arrêt 15, `render/manim/arret15/`.

| Élément | Règle |
| --- | --- |
| Couleurs | Fond rouge de la marque en dégradé (`#DA291C` vers `#B81F15`), panneaux `#96170F` et `#74110B`, texte et formes crème `#FBF3E4`, encre `#3B0906`. Mot-clé : texte rouge sur pastille crème. Étiquette discrète : texte crème sur bandeau encre |
| Structure | Fil conducteur en bas (« Les faits · Les textes · La question · La réponse · À retenir ») et carton plein écran à chaque partie, en fondu |
| Personnages | Silhouettes pleines, tête crème pour tous, avec un visage simple : neutre, content, triste, perplexe, surpris, décidé, bouche cousue. L'expression change au moment où la voix le dit |
| Origine d'un personnage | Quand l'origine compte pour le raisonnement, l'habit porte les couleurs du drapeau, avec une légende à l'écran. Jamais d'autre signe distinctif (ni accessoire, ni trait physique, ni cliché). Si la source ne nomme qu'un ensemble (« ex-Yougoslavie »), on le dit dans l'audit |
| Jeu des personnages | Ils jouent les faits : ils marchent en sautillant, franchissent une porte ou butent dessus, sautent de joie, reculent. Une scène jouée remplace un tableau chaque fois que c'est possible |
| Ton | Une pointe de malice est permise sur la procédure et le raisonnement, jamais sur les personnes concernées ni sur un passage sensible (propos haineux, violence) : leur contenu n'est ni cité ni montré |
| Textes de loi | Page crème avec la référence en tête ; texte officiel exact, coupes marquées « […] », ajout entre crochets ; un résumé ne porte jamais de guillemets |
| Vie de l'image | Caméra qui avance lentement sur chaque plan (3 % au plus) et revient au changement de plan ; grandes formes pâles qui glissent dans le fond ; léger va-et-vient des personnages. Rien ne doit sortir du cadre à l'avancée maximale |
| Texte du bas | Le texte lu, sur une ligne, qui se remplit au fil de la voix ; chiffres en chiffres |
| Son | Voix sans traitement autre qu'un filtre des graves ; les silences entre deux prises sont comblés par le ton de la pièce ; bruitages courts et discrets liés aux gestes (bulletin, porte, joie, déception). Pas de musique sans validation à l'oreille |
| Contrôle | Planches-contact horodatées avant chaque livraison ; aucun chevauchement de texte toléré, même bref |

Les règles générales restent valables : douze mots au plus à l'écran hors texte de loi et texte du bas, une idée par plan, schémas construits devant le spectateur.

## Texture de l'image (adoptée le 1er novembre 2026)

Appliquée au montage (`tools/assembler.py`), sur les schémas seulement (l'ouverture et la fin gardent le rouge exact) ; les sous-titres restent nets :
halo doux autour des éléments clairs (blanc, rouge de la marque), vignette légère sur les bords, grain fin animé.
Les couleurs de la charte ne changent pas. `TEXTURE=0` rend sans texture.

## Ouverture et carte de fin

Ouverture (4 s) : les trois barres du logo traversent l'écran, le logo se construit, puis le titre de la vidéo.
Fin (6 s) : logo, bouton « S'abonner » cliqué, vidéo suivante annoncée (si son script existe), GitHub et licence ;
le bas de l'écran reste libre pour l'écran de fin YouTube. Bruitages synthétisés en code, sans licence à gérer.

## Règles d'animation

1. Chaque phrase du script fait apparaître ou bouger quelque chose ; aucun plan fixe de plus de quatre secondes.
2. L'article cité apparaît en bas au moment précis où il est prononcé, et reste affiché tant qu'on en parle.
3. Les schémas se construisent devant le spectateur ; on ne montre jamais un schéma déjà complet.
4. Un renvoi à une autre vidéo s'affiche en petit, en bas à droite, sous la forme « vidéo N ».
5. Les shorts reprennent les mêmes éléments en format vertical (1080 × 1920) : question en haut, réponse en une phrase au centre, article en bas.

## Marque

Symbole, bannière, photos de profil, filigrane, gabarit des miniatures et règles d'usage : `docs/marque/README.md`. Le symbole reprend le bâtiment à trois étages ; il se construit dans l'ouverture et la fin de chaque vidéo.
