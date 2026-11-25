"""Sous-titres en fichier (.srt) d'une vidéo rendue, pour YouTube (et donc pour la recherche Google).

Usage : python tools/sous_titres_srt.py <matiere>/<numero-slug> [sortie.srt]

Part des sous-titres incrustés (render/remotion/public/<slug>/sous-titres.ass) : mêmes morceaux, même minutage que
la vidéo envoyée. Les balises de style sont retirées.
"""

import re
import subprocess
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent


def srt(slug: str, cible: Path) -> Path:
    ass = RACINE / "render/remotion/public" / slug.replace("/", "--") / "sous-titres.ass"
    if not ass.exists():
        sys.exit(f"Pas de sous-titres pour {slug} : lancer d'abord make assemble")
    brut = subprocess.run(["ffmpeg", "-v", "error", "-i", str(ass), "-f", "srt", "-"], capture_output=True, text=True,
                          check=True).stdout
    propre = re.sub(r"</?font[^>]*>|</?[biu]>", "", brut)
    cible.write_text(propre, encoding="utf-8")
    return cible


if __name__ == "__main__":
    s = sys.argv[1]
    sortie = Path(sys.argv[2]) if len(sys.argv) > 2 else RACINE / "out" / f"{s.replace('/', '--')}.fr.srt"
    print(f"Sous-titres : {srt(s, sortie)}")
