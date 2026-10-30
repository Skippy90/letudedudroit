# Marque — L'étude du droit

Le symbole est le bâtiment à trois étages des vidéos, réduit à l'essentiel : un toit et trois étages. De bas en haut, vert (condition remplie), blanc cassé, ambre (l'étage en cours d'examen). Il dit en un coup d'œil ce que fait la chaîne : raisonner étage par étage.

## Fichiers

| Fichier | Usage | Taille |
| --- | --- | --- |
| `symbole.svg`, `png/symbole-1024.png` | Symbole seul, coins arrondis | 1024 × 1024 |
| `profil.svg`, `png/profil-800.png` | Photo de profil YouTube (rognée en cercle) | 800 × 800 |
| `png/profil-1080.png` | Photo de profil Instagram, TikTok | 1080 × 1080 |
| `banniere-youtube.svg`, `png/banniere-youtube-2560x1440.png` | Bannière YouTube : symbole, nom et signature ; tout tient dans la zone visible partout (1546 × 423 au centre) | 2560 × 1440 |
| `logo-horizontal.svg`, `png/logo-horizontal-1600x512.png` | Symbole + nom + signature : documents, présentations, site | 1600 × 512 |
| `png/filigrane-150.png` | Filigrane YouTube (Studio → Personnalisation → Branding) | 150 × 150 |

Miniatures : `tools/miniature.py <slug> <seconde>` génère `scripts/<slug>/miniature.png` (1280 × 720) au gabarit de la chaîne, à partir du titre du script et d'une image des schémas.

Ouverture et fin des vidéos : le symbole s'y construit (étages de bas en haut, puis le toit) — `render/remotion/src/Video.tsx`.

## Nom et signature

- Nom : **L'étude du droit** (apostrophe typographique ’ dans les visuels). Handle sans accent ni apostrophe : `letudedudroit`.
- Signature : **Le droit suisse, une notion à la fois.**

## Couleurs (celles de la charte visuelle)

| Nom | Valeur | Rôle dans la marque |
| --- | --- | --- |
| Bleu nuit | `#0F1B2D` | Fond de tout |
| Blanc cassé | `#F2EFE6` | Nom, toit, textes |
| Ambre | `#E3A52F` | Signature, mot-clé du titre des miniatures, étage du haut |
| Vert | `#4CAF7D` | Étage du bas |
| Surface | `#1B2B44` | Blocs (articles, étages des vidéos) |

Le rouge (`#D9534F`) reste réservé au dommage dans les vidéos : jamais dans la marque.

## Typographie

Inter, sans empattement : extra-gras (800) pour le nom et les titres, demi-gras (500 à 600) pour la signature et les sous-titres.

## Règles

- Le symbole sur fond bleu nuit uniquement ; jamais déformé, jamais recoloré.
- Marge autour du symbole : au moins la hauteur d'un étage.
- Taille minimale : 48 px de côté (le filigrane fait 150 px).
- Miniatures : la question en grand, le dernier mot en ambre ; la scène du cas en dessous ; le symbole en bas à gauche.
