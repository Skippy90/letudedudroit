#!/bin/bash
# Chaîne complète de l'arrêt 25 : rendu des sections, son, texte du bas, encodage. usage : tout.sh v1 [son]
cd /home/claude/a25; PY=/home/claude/letudedudroit/.venv/bin/python; V=${1:-v1}; N=/home/claude/letudedudroit/voice/arrets/25-atf-146-i-145
SEC=("s_a A a" "s_b Bf b" "s_c C c" "s_d1 D1 d1" "s_d2 D2 d2" "s_e Es e" "s_f Ff f")
rm -f /tmp/a25/enc.fin
if [ "$2" != "son" ]; then
  rm -f /tmp/a25/sons-*.json
  (./rendre.sh -qh "${SEC[0]}" "${SEC[2]}" "${SEC[4]}" "${SEC[6]}" "s_f Fin fin" > /tmp/a25/hq1.log 2>&1) &
  sleep 40; ./rendre.sh -qh "${SEC[1]}" "${SEC[3]}" "${SEC[5]}" > /tmp/a25/hq2.log 2>&1; wait
  for x in "${SEC[@]}"; do set -- $x; [ -f /tmp/a25/sons-$2.json ] || ./rendre.sh -qh "$x" >> /tmp/a25/hq3.log 2>&1; done
fi
: > /tmp/a25/l.txt; for x in "${SEC[@]}" "s_f Fin fin"; do set -- $x; echo "file '$(ls /tmp/a25/videos/$1/1080p30/$3.mp4)'" >> /tmp/a25/l.txt; done
cd son && ffmpeg -v error -y -i $N/narration.wav -af "highpass=f=70" -ar 48000 -ac 1 voix.wav && $PY mix.py > /tmp/a25/mix.log 2>&1 && ffmpeg -v error -y -i voix_p.wav -i bruitages.wav -filter_complex "[0]pan=stereo|c0=c0|c1=c0[v];[1]volume=0.22[b];[v][b]amix=inputs=2:normalize=0,volume=-1.5dB,alimiter=limit=0.89:level=disabled[o]" -map "[o]" -ar 48000 mix.wav
cd .. && $PY srt.py /tmp/a25/arret-25.srt && $PY ass.py /tmp/a25/arret-25.srt /tmp/a25/s.ass
cd /tmp/a25 && ffmpeg -v error -y -f concat -safe 0 -i l.txt -c copy tout.mp4
D=$($PY -c "import sys; sys.path.insert(0,'/home/claude/a25'); from temps import *; print(round(M(FIN)+14.95,2))")
ffmpeg -v error -y -i tout.mp4 -i /home/claude/a25/son/mix.wav -i arret-25.srt -vf "subtitles=s.ass" -map 0:v -map 1:a -map 2 -c:v libx264 -preset medium -crf 27 -tune animation -pix_fmt yuv420p -c:a aac -b:a 128k -c:s mov_text -metadata:s:s:0 language=fra -movflags +faststart -t $D arret-25-$V.mp4 \
 && ffmpeg -v error -y -i arret-25-$V.mp4 -map 0:v -map 0:a -map 0:s -vf scale=1280:720 -c:v libx264 -preset medium -crf 28 -tune animation -pix_fmt yuv420p -c:a aac -b:a 96k -c:s mov_text -movflags +faststart arret-25-$V-leger.mp4 && echo FINI > enc.fin
