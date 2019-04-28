#!/bin/bash
FILES=../resultados/32.0/*.csv
for f in $FILES
do
  echo "Processing $f file..."
  cat $f >> consolidado.txt
  echo "\n" >> consolidado.txt
done
