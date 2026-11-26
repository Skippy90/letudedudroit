"""Texte du bas : une ligne entière à la fois, sans effet karaoké ; même découpage que srt.py."""
import sys, re
sys.path.insert(0, "/home/claude/fr01")
from temps import M
from srt import blocs
def fmt(t): return f"{int(t // 3600)}:{int(t // 60 % 60):02d}:{t % 60:05.2f}"
o = ["[Script Info]", "ScriptType: v4.00+", "PlayResX: 384", "PlayResY: 288", "", "[V4+ Styles]",
     "Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding",
     "Style: D,Inter,10.5,&H00E4F3FB,&H48E4F3FB,&H003F0A0A,&H00000000,1,0,0,0,100,100,0,0,1,0.7,0,2,10,10,4,1", "", "[Events]",
     "Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text"]
B_ = blocs()
for d, f, L in B_:   # une ligne entière à la fois, sans surlignage mot à mot (l'autrice n'aime pas l'effet karaoké, 25 novembre 2026)
    o.append(f"Dialogue: 0,{fmt(d)},{fmt(f)},D,,0,0,0,,{' '.join(m for m, a_, b_ in L)}")
open(sys.argv[2], "w").write("\n".join(o) + "\n"); print(len(B_))
