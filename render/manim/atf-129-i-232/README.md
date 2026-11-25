# ATF 129 I 232 — Zurich : le peuple peut-il choisir qui devient suisse ?

Scènes Manim de la vidéo, dans le « style rouge », sur la chaîne de montage de l'arrêt 25 (`render/manim/arret25/`).

- `temps.py` : instants des phrases (`voice/arrets/atf-129-i-232-zurich/timings.json`) et temps de la vidéo (cinq cartons de partie, une pause de réflexion après la question finale, silences resserrés, voix accélérée de 5 % sans changement de hauteur).
- `base.py` : briques communes, plus celles de cette vidéo : `constit` (Constitution fédérale), `candidat`, `electeurs`, `initiative`, `station` et `verdict` (le parcours des quatre décisions), `ligne_coche`, `bulle_pensee`.
- `s_a.py` à `s_f.py` : une section par fichier (séquences 1–3, 4–11, 12–15, 16–23, 24–30, 31–39, 40–45) ; `Fin` : écran de fin muet de 15 secondes.
- `son/egaliser.py` : même niveau de voix pour chaque séquence, limiteur doux ; `son/mix.py` : pauses, ton de pièce, bruitages ; `srt.py` et `ass.py` : sous-titres ; `fiche232.py` : fiche de cours ; `miniature/` : miniature (page HTML photographiée).
- `tout.sh v1` : rendu des sections, son, sous-titres, encodage (1080p et version légère).

Les chemins de travail (`/home/claude/z232`, `/home/claude/proto`, `/tmp/z232v`) sont ceux de la session de montage : à adapter avant de relancer la chaîne depuis le dépôt.
