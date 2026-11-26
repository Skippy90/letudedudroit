#!/bin/bash
# usage : rendre.sh [-ql|-qh] "s_a A a" ...   (FR01_TIMINGS : instants de la narration, estimés avant l'enregistrement)
cd /home/claude/fr01
export FR01_TIMINGS=${FR01_TIMINGS:-/tmp/fr01v/timings_estimes.json}
PY=/home/claude/letudedudroit/.venv/bin/python
Q=$1; shift
for x in "$@"; do
  set -- $x
  nice -n 5 $PY -m manim render $Q --fps 30 --disable_caching --progress_bar none --media_dir /tmp/fr01v -o $3 $1.py $2 > /tmp/fr01v-$3.log 2>&1
  echo "$3 $(ls /tmp/fr01v/videos/$1/*/$3.mp4 2>&1 | tail -1) $(grep -c 'DEPASSEMENT\|INTROUVABLE' /tmp/fr01v-$3.log) $(grep -h 'Error\|DEPASSEMENT\|INTROUVABLE' /tmp/fr01v-$3.log | head -3 | cut -c1-200)"
done
