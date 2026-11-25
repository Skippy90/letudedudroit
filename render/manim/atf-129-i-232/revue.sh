#!/bin/bash
# revue.sh fichier.mp4 pas sortie-prefixe [colonnes] : planches-contact horodatées
f=$1; pas=${2:-3}; out=${3:-/tmp/z232v/revue}; c=${4:-4}
rm -f ${out}-*.jpg
ffmpeg -v error -y -i "$f" -vf "fps=1/$pas:start_time=$(echo "$pas/2"|bc -l),scale=640:-1,drawtext=text='%{pts\:hms}':x=8:y=8:fontsize=22:fontcolor=yellow:box=1:boxcolor=black@0.6,tile=${c}x4" -q:v 4 ${out}-%02d.jpg
ls ${out}-*.jpg; ffprobe -v error -show_entries format=duration -of csv=p=0 "$f"
