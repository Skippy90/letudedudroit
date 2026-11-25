"""Met à jour les minutages du kit de publication (chapitres, durée, écran de fin, points d'écoute).
usage : kit_maj.py <kit.md> <version> <durée en secondes de la vidéo finale>"""
import re, sys
sys.path.insert(0, "/home/claude/m367")
from temps import M, B, S, W

kit, version, duree = sys.argv[1], sys.argv[2], float(sys.argv[3])
CHAP = [1, 4, 10, 12, 15, 18, 20, 23, 24, 27, 30, 32, 35, 38, 39, 40, 43, 44]


def ms(t):
    t = int(t + 0.5)
    return f"{t // 60}:{t % 60:02d}"


s = open(kit, encoding="utf-8").read()
lignes = s.split("\n")
i = lignes.index("Chapitres") + 1
for k, l in enumerate(CHAP):
    titre = lignes[i + k].split(" ", 1)[1]
    lignes[i + k] = f"{'0:00' if k == 0 else ms(M(B(l)))} {titre}"
s = "\n".join(lignes)
s = re.sub(r"minimum-vital-v\d+\.mp4", f"minimum-vital-{version}.mp4", s)
s = re.sub(r"\(1080p, \d+ min \d+ s\)", f"(1080p, {int(duree) // 60} min {int(duree) % 60} s)", s)
s = re.sub(r"à partir de \d+:\d\d, sur les 15", f"à partir de {ms(duree - 15)}, sur les 15", s)
s = re.sub(r"vers \d+:\d\d, « L'aide sociale", f"vers {ms(M(S(13, 3)))}, « L'aide sociale", s)
s = re.sub(r"vers \d+:\d\d, la référence lue", f"vers {ms(M(W(45, 1, 'retrouverez')))}, la référence lue", s)
s = re.sub(r"vers \d+:\d\d, la phrase « Il admet", f"vers {ms(M(S(38, 2)))}, la phrase « Il admet", s)
open(kit, "w", encoding="utf-8").write(s)
print("\n".join(lignes[i:i + len(CHAP)]))
