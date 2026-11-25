"""Texte du bas, avec remplissage progressif (karaoké) : même découpage que srt.py."""
import sys, re
sys.path.insert(0, "/home/claude/a25")
from temps import M
blocs = [b.split("\n") for b in open(sys.argv[1]).read().strip().split("\n\n")]
def sec(h): a, b = h.split(","); x = a.split(":"); return int(x[0]) * 3600 + int(x[1]) * 60 + int(x[2]) + int(b) / 1000
def fmt(t): return f"{int(t // 3600)}:{int(t // 60 % 60):02d}:{t % 60:05.2f}"
o = ["[Script Info]", "ScriptType: v4.00+", "PlayResX: 384", "PlayResY: 288", "", "[V4+ Styles]",
     "Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding",
     "Style: D,Inter,10.5,&H00E4F3FB,&H48E4F3FB,&H0006093B,&H00000000,1,0,0,0,100,100,0,0,1,0.7,0,2,10,10,4,1", "", "[Events]",
     "Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text"]
for b in blocs:
    d, f = [sec(x) for x in b[1].split(" --> ")]; mots = b[2].split(); tot = sum(len(m) + 1 for m in mots); dur = max(0.3, f - d - 0.25)
    txt = " ".join("{\\kf%d}%s" % (round(100 * dur * (len(m) + 1) / tot), m) for m in mots)
    o.append(f"Dialogue: 0,{fmt(d)},{fmt(f)},D,,0,0,0,,{txt}")
open(sys.argv[2], "w").write("\n".join(o) + "\n"); print(len(blocs))
