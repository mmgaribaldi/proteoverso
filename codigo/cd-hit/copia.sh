#!/usr/bin/zsh

filename="$1"
while read -r line
do
    cd $line
    cp results_$line.txt /home/mgaribaldi/Work/proteoverso/resultados/results_$line.csv
    cd ..
done < "$filename"
