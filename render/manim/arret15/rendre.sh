#!/bin/bash
# Rend des sections. Usage : rendre.sh [-ql|-qh] "s_a A a" "s_b Bf b" ...  (fichier, classe, nom de sortie)
cd "$(dirname "$0")"; PY=${PY:-../../../.venv/bin/python}; S=${A15_SORTIE:-/tmp/a15}; mkdir -p "$S"
Q=$1; shift
for x in "$@"; do
  set -- $x
  A15_SORTIE=$S $PY -m manim render $Q --fps 30 --disable_caching --progress_bar none --media_dir "$S" -o $3 $1.py $2 > "$S/rendu-$3.log" 2>&1
  echo "$3 $(ls "$S"/videos/$1/*/$3.mp4 2>&1 | tail -1)"
done
