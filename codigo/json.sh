#!/bin/bash
#FILES=../resultados/*.txt
FILES=../../temp/*.txt
for f in $FILES
do
  echo "Processing $f file..."
  # take action on each file. $f store current file name
  python3 resultToJson.py $f
done
