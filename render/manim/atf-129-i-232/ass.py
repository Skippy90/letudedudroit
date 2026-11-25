"""Texte du bas, avec remplissage progressif (karaoké) : même découpage que srt.py."""
import sys, re
sys.path.insert(0, "/home/claude/z232")
from temps import M
from srt import blocs
def fmt(t): return f"{int(t // 3600)}:{int(t // 60 % 60):02d}:{t % 60:05.2f}"
o = ["[Script Info]", "ScriptType: v4.00+", "PlayResX: 384", "PlayResY: 288", "", "[V4+ Styles]",
     "Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding",
     "Style: D,Inter,10.5,&H00E4F3FB,&H48E4F3FB,&H0006093B,&H00000000,1,0,0,0,100,100,0,0,1,0.7,0,2,10,10,4,1", "", "[Events]",
     "Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text"]
B_ = blocs()
for d, f, L in B_:
    txt = []; t = d
    for k_, (m, a_, b_) in enumerate(L):
        a_ = max(a_, t); fin_mot = L[k_ + 1][1] if k_ + 1 < len(L) else min(b_, f - 0.1)
        if a_ - t > 0.03: txt.append("{\\k%d}" % round(100 * (a_ - t)))
        txt.append("{\\kf%d}%s" % (max(1, round(100 * (max(fin_mot, a_ + 0.05) - a_))), m)); t = max(fin_mot, a_ + 0.05)
    o.append(f"Dialogue: 0,{fmt(d)},{fmt(f)},D,,0,0,0,,{' '.join(txt)}")
open(sys.argv[2], "w").write("\n".join(o) + "\n"); print(len(B_))
