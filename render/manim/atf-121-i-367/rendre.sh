#!/bin/bash
# usage : rendre.sh [-ql|-qh] "s_a A a" ...
cd /home/claude/m367
PY=/home/claude/letudedudroit/.venv/bin/python
Q=$1; shift
for x in "$@"; do
  set -- $x
  nice -n 5 $PY -m manim render $Q --fps 30 --disable_caching --progress_bar none --media_dir /tmp/m367v -o $3 $1.py $2 > /tmp/m367v-$3.log 2>&1
  echo "$3 $(ls /tmp/m367v/videos/$1/*/$3.mp4 2>&1 | tail -1) $(tail -2 /tmp/m367v-$3.log | head -1 | cut -c1-200)"
done
