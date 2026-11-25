# Arrêt 15 (ATF 129 I 217, Emmen) : scènes du « style rouge »

Vidéo écrite scène par scène, hors du moteur `video.py` : chaque section est une classe Manim calée sur la narration (`voice/arrets/15-atf-129-i-217/timings.json`). Les briques communes du style sont dans `../style_rouge/` (`proto.py`, `suite.py`, `kit.py`, reprises de l'arrêt 12) ; celles propres à cette vidéo dans `base.py`. La charte du style : `docs/charte-visuelle.md`, section « Style rouge ».

## Fichiers

| Fichier | Rôle |
| --- | --- |
| `temps.py` | Instants des phrases (`S`, `E`, `W` pour un mot, `B` pour la frontière avant une ligne) et temps de la vidéo `M(t)` : cartons de partie, deux pauses de réflexion, silences trop longs raccourcis |
| `base.py` | Personnages (`acteur`, habits aux couleurs des drapeaux, `visage`), objets (`passeport`, `cadenas`, `tampon`), classe `Sec15` : caméra, décor, `marche`, `saut`, `son` |
| `s_a.py` … `s_e.py` | Les sections : ouverture (lignes 1 à 3), faits (4 à 14), textes et question (15 à 18), réponse (19 à 36, en trois fichiers), à retenir (37 à 45) et écran de fin muet de 15 s (script, fiche, licence, puis place des éléments YouTube) |
| `mix.py` | Voix (trous de silence comblés par le ton de la pièce, pauses), bruitages calculés, dont ceux notés par les scènes avec `self.son(...)` |
| `srt.py`, `ass.py` | Texte du bas : sous-titres, puis version à remplissage progressif incrustée dans l'image |
| `retouche_annees.py` | Trois retouches de la narration montée (voir `voice/arrets/15-atf-129-i-217/montage.txt`) |
| `fiche15.py` | Fiche de cours en PDF (deux pages), composée de phrases du script audité ; écrit `out/arrets--15-atf-129-i-217--fiche.pdf` |
| `mini2.py` | Miniature (`MiniA` : le score 8 sur 8, 0 sur 38) |
| `rendre.sh`, `tout.sh`, `revue.sh` | Rendu d'une section, chaîne complète, planches-contact de contrôle |

## Refaire la vidéo

1. Aligner la voix : `tools/alignement.py arrets/15-atf-129-i-217`, avec dans `tts.txt` la phrase 3 de la ligne 28 telle qu'elle est dite à l'enregistrement (avec les années), puis remettre le texte final et lancer `retouche_annees.py`.
2. `./tout.sh v6` : rend les sections en 1080p, mixe, incruste le texte et écrit `out/arret-15-v6.mp4`. Les fichiers de travail vont dans `$A15_SORTIE` (par défaut `/tmp/a15`). Compter une demi-heure sur deux cœurs.
3. Contrôle : `./revue.sh <vidéo> 4` produit des planches horodatées, une image toutes les quatre secondes.

Aperçu d'une section en 480p : `./rendre.sh -ql "s_b Bf b"`.

## Limites connues

- Les positions sont écrites à la main : tout ajout se contrôle sur les planches (les chevauchements ne sont pas détectés automatiquement).
- Les bruitages sont calculés, jamais écoutés par l'agent : à valider à l'oreille.
- `../style_rouge/proto.py` et `suite.py` contiennent aussi les scènes de l'arrêt 12, qui attendent leur propre module `temps` (non versionné ici).
