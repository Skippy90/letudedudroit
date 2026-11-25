#!/bin/bash
# usage : rendre.sh [-ql|-qh] "s_a A a" ...
cd /home/claude/z232
PY=/home/claude/letudedudroit/.venv/bin/python
Q=$1; shift
for x in "$@"; do
  set -- $x
  $PY -m manim render $Q --fps 30 --disable_caching --progress_bar none --media_dir /tmp/z232v -o $3 $1.py $2 > /tmp/z232v-$3.log 2>&1
  echo "$3 $(ls /tmp/z232v/videos/$1/*/$3.mp4 2>&1 | tail -1) $(tail -2 /tmp/z232v-$3.log | head -1 | cut -c1-200)"
done
