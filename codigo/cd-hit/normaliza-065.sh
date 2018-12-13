#!/usr/bin/zsh

filename="$1"
while read -r line
do
    cd $line

    total=`tail -n 10 results0.65.txt | grep finished |cut -d"f" -f1`
    cluster=`tail -n 10 results0.65.txt | grep finished |cut -d"c" -f1 | cut -d"d" -f2`
    normalizado=`bc <<< "scale=2; $cluster/$total" | sed 's/^\./0./'`
    echo $line ",0.65," $total "," $cluster "," $normalizado | sed 's/ //g' >> results_$line.txt

    cd ..
done < "$filename"
