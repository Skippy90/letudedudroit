#!/bin/bash
# Version muette de FR-01 (avant l'enregistrement) : images calées sur les instants estimés, texte du bas, piste son silencieuse.
# usage : muet.sh v1
cd /home/claude/fr01; PY=/home/claude/letudedudroit/.venv/bin/python; V=${1:-v1}
export FR01_TIMINGS=/tmp/fr01v/timings_estimes.json
SEC=("s_a A a" "s_b B b" "s_c C1 c1" "s_c C2 c2" "s_d D1 d1" "s_d D2 d2" "s_e E1 e1" "s_e E2 e2" "s_f Ff f")
rm -f /tmp/fr01v/muet.fin
if [ "$2" != "enc" ]; then
(./rendre.sh -qh "${SEC[0]}" "${SEC[2]}" "${SEC[3]}" "${SEC[6]}" "${SEC[7]}" > /tmp/fr01v/hq1.log 2>&1) &
sleep 30; ./rendre.sh -qh "${SEC[1]}" "${SEC[4]}" "${SEC[5]}" "${SEC[8]}" "s_f Fin fin" > /tmp/fr01v/hq2.log 2>&1; wait
fi
for x in "${SEC[@]}" "s_f Fin fin"; do set -- $x; [ -f /tmp/fr01v/videos/$1/1080p30/$3.mp4 ] || ./rendre.sh -qh "$x" >> /tmp/fr01v/hq3.log 2>&1; done
: > /tmp/fr01v/l.txt; for x in "${SEC[@]}" "s_f Fin fin"; do set -- $x; echo "file '/tmp/fr01v/videos/$1/1080p30/$3.mp4'" >> /tmp/fr01v/l.txt; done
$PY srt.py /tmp/fr01v/fr01.srt && $PY ass.py /tmp/fr01v/fr01.srt /tmp/fr01v/s.ass
cd /tmp/fr01v && ffmpeg -v error -y -f concat -safe 0 -i l.txt -c copy tout.mp4
ffmpeg -v error -y -i tout.mp4 -f lavfi -i anullsrc=r=48000:cl=stereo -i fr01.srt -vf "subtitles=s.ass" -map 0:v -map 1:a -map 2 -t $(ffprobe -v error -show_entries format=duration -of csv=p=0 tout.mp4) -c:v libx264 -preset medium -crf 27 -tune animation -pix_fmt yuv420p -c:a aac -b:a 64k -c:s mov_text -metadata:s:s:0 language=fra -movflags +faststart fr01-muet-$V.mp4 \
 && ffmpeg -v error -y -i fr01-muet-$V.mp4 -map 0:v -map 0:a -vf scale=1280:720 -c:v libx264 -preset medium -crf 28 -tune animation -pix_fmt yuv420p -c:a copy -movflags +faststart fr01-muet-$V-leger.mp4 && echo FINI > muet.fin
