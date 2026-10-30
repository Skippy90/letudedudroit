# Marque — L'étude du droit

La marque est en blanc sur rouge suisse : le nom « L'étude du droit » et le symbole, le bâtiment à trois étages des vidéos réduit à un toit et trois étages (blanc, de plus en plus transparent vers le bas). Le rouge est réservé à la marque : les schémas des vidéos et les miniatures gardent le bleu nuit de la charte.

## Fichiers

| Fichier | Usage | Taille |
| --- | --- | --- |
| `symbole.svg`, `png/symbole-1024.png` | Symbole blanc sur pastille rouge, coins arrondis | 1024 × 1024 |
| `profil.svg`, `png/profil-800.png` | Photo de profil YouTube : symbole et nom sur deux lignes, en blanc sur rouge (tient dans le cercle) | 800 × 800 |
| `png/profil-1080.png` | Photo de profil Instagram, TikTok | 1080 × 1080 |
| `banniere-youtube.svg`, `png/banniere-youtube-2560x1440.png` | Bannière YouTube : symbole, nom et signature ; tout tient dans la zone visible partout (1546 × 423 au centre) | 2560 × 1440 |
| `logo-horizontal.svg`, `png/logo-horizontal-1600x512.png` | Symbole + nom + signature : documents, présentations, site | 1600 × 512 |
| `png/filigrane-150.png` | Filigrane YouTube (Studio → Personnalisation → Branding) | 150 × 150 |

Miniatures : `tools/miniature.py <slug> <seconde>` génère `scripts/<slug>/miniature.png` (1280 × 720) au gabarit de la chaîne, à partir du titre du script et d'une image des schémas.

Ouverture et fin des vidéos : le symbole s'y construit (étages de bas en haut, puis le toit) — `render/remotion/src/Video.tsx`.

## Nom et signature

- Nom : **L'étude du droit** (apostrophe typographique ’ dans les visuels). Handle sans accent ni apostrophe : `letudedudroit`.
- Signature : **Le droit suisse, une notion à la fois.**

## Couleurs

| Nom | Valeur | Rôle |
| --- | --- | --- |
| Rouge suisse | `#DA291C` | Fond de la marque : profil, bannière, logo, filigrane, ouverture et fin des vidéos |
| Blanc | `#FFFFFF` | Nom, symbole, signature sur le rouge |
| Bleu nuit | `#0F1B2D` | Schémas des vidéos et miniatures (charte visuelle) |
| Ambre | `#E3A52F` | Dernier mot du titre des miniatures |

Le rouge de la marque n'entre pas dans les schémas : là, le rouge (`#D9534F`) reste réservé au dommage. Ouverture et fin passent en douceur du rouge au bleu nuit des schémas. Pas de croix suisse ni d'armoiries : le rouge et le blanc suffisent, sans laisser croire à une chaîne officielle.

## Typographie

Inter, sans empattement : extra-gras (800) pour le nom et les titres, demi-gras (500 à 600) pour la signature et les sous-titres.

## Règles

- Le symbole en blanc sur rouge (ou rouge sur blanc si le fond est clair) ; jamais déformé, jamais d'autres couleurs.
- Marge autour du symbole : au moins la hauteur d'un étage.
- Taille minimale : 48 px de côté (le filigrane fait 150 px).
- Miniatures : la question en grand, le dernier mot en ambre, sur bleu nuit ; la scène du cas en dessous ; la pastille rouge du symbole en bas à gauche.
