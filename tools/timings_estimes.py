"""Estime des timings de narration à partir de tts.txt (environ 2,6 mots par seconde).

Usage : python tools/timings_estimes.py <matiere>/<numero-slug> <fichier de sortie>
Sert à prévisualiser les schémas avant de générer la vraie narration (variable TIMINGS).
"""

import json
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent

slug, sortie = sys.argv[1], sys.argv[2]
blocs = (RACINE / "scripts" / slug / "tts.txt").read_text(encoding="utf-8").strip().split("\n\n")
t, lignes = 0.0, []
for n, bloc in enumerate(blocs, 1):
    debut, phrases = t, []
    for phrase in bloc.split("\n"):
        d = max(0.8, len(phrase.split()) / 2.6)
        phrases.append({"texte": phrase, "debut": round(t, 3), "fin": round(t + d, 3)})
        t += d + 0.15
    lignes.append({"ligne": n, "debut": round(debut, 3), "fin": round(t, 3), "phrases": phrases})
    t += 0.45
Path(sortie).write_text(json.dumps({"voix": "estimation", "duree": round(t, 2), "lignes": lignes}), encoding="utf-8")
