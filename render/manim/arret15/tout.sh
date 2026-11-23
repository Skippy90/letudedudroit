#!/bin/bash
# Chaîne complète de la vidéo de l'arrêt 15 : sections, son, texte du bas, encodage.
# Avant : tools/alignement.py arrets/15-atf-129-i-217 (avec la phrase 28.3 telle qu'elle est dite), puis retouche_annees.py.
cd "$(dirname "$0")"; ICI=$(pwd); RACINE=$(cd ../../.. && pwd); PY=${PY:-$RACINE/.venv/bin/python}; export A15_SORTIE=${A15_SORTIE:-/tmp/a15}; S=$A15_SORTIE; V=${1:-v6}
mkdir -p "$S"; rm -f "$S"/sons-*.json
# deux rendus en parallèle ; une section peut échouer quand ils écrivent le même cache : on relance celles qui manquent
(./rendre.sh -qh "s_a A a" "s_d2 D2 d2" "s_e Ef e" "s_c C c" "s_e Fin f") &
sleep 40; ./rendre.sh -qh "s_b Bf b" "s_d1 D1 d1" "s_d3 D3 d3"; wait
for x in "s_a A a" "s_b Bf b" "s_c C c" "s_d1 D1 d1" "s_d2 D2 d2" "s_d3 D3 d3" "s_e Ef e"; do set -- $x; [ -f "$S/sons-$2.json" ] || ./rendre.sh -qh "$x"; done
cd "$S"
ffmpeg -v error -y -i "$RACINE/voice/arrets/15-atf-129-i-217/narration.wav" -af "highpass=f=70" -ar 48000 -ac 1 voix.wav
$PY "$ICI/mix.py"   # écrit voix_p.wav et bruitages.wav dans le dossier courant
ffmpeg -v error -y -i voix_p.wav -i bruitages.wav -filter_complex "[0]pan=stereo|c0=c0|c1=c0[v];[1]volume=0.22[b];[v][b]amix=inputs=2:normalize=0,volume=-1.5dB,alimiter=limit=0.89:level=disabled[o]" -map "[o]" -ar 48000 mix.wav
$PY "$ICI/srt.py" arret-15.srt && $PY "$ICI/ass.py" arret-15.srt s.ass
for x in s_a/1080p30/a s_b/1080p30/b s_c/1080p30/c s_d1/1080p30/d1 s_d2/1080p30/d2 s_d3/1080p30/d3 s_e/1080p30/e s_e/1080p30/f; do echo "file '$S/videos/$x.mp4'"; done > l.txt
ffmpeg -v error -y -f concat -safe 0 -i l.txt -c copy tout.mp4
D=$($PY -c "import sys; sys.path.insert(0,'$ICI'); from temps import *; print(round(M(FIN)+14.95,2))")
ffmpeg -v error -y -i tout.mp4 -i mix.wav -i arret-15.srt -vf "subtitles=s.ass" -map 0:v -map 1:a -map 2 -c:v libx264 -preset medium -crf 27 -tune animation -pix_fmt yuv420p -c:a aac -b:a 128k -c:s mov_text -metadata:s:s:0 language=fra -movflags +faststart -t $D "$RACINE/out/arret-15-$V.mp4"
