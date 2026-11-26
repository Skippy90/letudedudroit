# FR-01 Morsang-sur-Orge — production des images

- `base.py` : briques (kit du style rouge passé au bleu du drapeau français avant chargement ; section « FRANCE »). Chemins de travail : `/home/claude/fr01`, kit commun `/home/claude/proto` (voir `docs/passation-grands-arrets.md`).
- `temps.py` : instants. `FR01_TIMINGS=timings_estimes.json` avant l'enregistrement ; ensuite le `timings.json` de l'enregistrement aligné.
- `muet.sh v1` : version muette 1080p (sections, texte du bas, piste silencieuse).
- `europe_ouest.json` : contours de la France métropolitaine et de la Suisse, extraits de world-atlas 2.0.2 (Natural Earth, domaine public), avec topojson-client.
