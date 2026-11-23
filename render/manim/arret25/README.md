# Arrêt 25 — Les Aînées pour le climat (ATF 146 I 145 et Cour EDH, 9 avril 2024)

Scènes Manim de la vidéo, dans le « style rouge » (voir `docs/charte-visuelle.md` et `render/manim/style_rouge/`, apportés par la pull request de l'arrêt 15).

- `temps.py` : instants des phrases (`voice/arrets/25-atf-146-i-145/timings.json`) et temps de la vidéo (cartons de partie, deux pauses de réflexion, silences resserrés).
- `base.py` : briques communes, plus celles de cette vidéo : `ainee` (robe de couleur fixe par personnage, chignon, canne), `juge`, `thermometre`, `terre`, `soleil`, `enveloppe`, `nuage`, `cour` (Strasbourg), fil conducteur à cinq parties.
- `s_a.py` à `s_f.py` : une section par fichier (lignes 1–3, 4–13, 14–18, 19–26, 27–35, 36–43, 44–50) ; `Fin` : écran de fin muet de 15 secondes.
- `son/mix.py` : pauses, ton de pièce, bruitages calculés ; `srt.py` et `ass.py` : sous-titres ; `mini.py` : miniature ; `fiche25.py` : fiche de cours en PDF.
- `tout.sh v1` : rendu des sections, son, sous-titres, encodage (1080p et version légère).

Les chemins de travail (`/home/claude/a25`, `/home/claude/proto`, `/tmp/a25`) sont ceux de la session de montage : à adapter avant de relancer la chaîne depuis le dépôt.
