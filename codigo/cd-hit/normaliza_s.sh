#!/usr/bin/zsh

filename="$1"
while read -r line
do
    cd $line

    total=`tail -n 10 results0.40.txt | grep finished |cut -d"f" -f1`
    cluster=`tail -n 10 results0.40.txt | grep finished |cut -d"c" -f1 | cut -d"d" -f2`
    normalizado=`bc <<< "scale=2; $cluster/$total" | sed 's/^\./0./'`
    echo $line ",0.40," $total "," $cluster "," $normalizado | sed 's/ //g' > results_$line.txt

    total=`tail -n 10 results0.45.txt | grep finished |cut -d"f" -f1`
    cluster=`tail -n 10 results0.45.txt | grep finished |cut -d"c" -f1 | cut -d"d" -f2`
    normalizado=`bc <<< "scale=2; $cluster/$total" | sed 's/^\./0./'`
    echo $line ",0.45," $total "," $cluster "," $normalizado | sed 's/ //g' >> results_$line.txt

    total=`tail -n 10 results0.50.txt | grep finished |cut -d"f" -f1`
    cluster=`tail -n 10 results0.50.txt | grep finished |cut -d"c" -f1 | cut -d"d" -f2`
    normalizado=`bc <<< "scale=2; $cluster/$total" | sed 's/^\./0./'`
    echo $line ",0.50," $total "," $cluster "," $normalizado | sed 's/ //g' >> results_$line.txt

    total=`tail -n 10 results0.55.txt | grep finished |cut -d"f" -f1`
    cluster=`tail -n 10 results0.55.txt | grep finished |cut -d"c" -f1 | cut -d"d" -f2`
    normalizado=`bc <<< "scale=2; $cluster/$total" | sed 's/^\./0./'`
    echo $line ",0.55," $total "," $cluster "," $normalizado | sed 's/ //g' >> results_$line.txt

    total=`tail -n 10 results0.60.txt | grep finished |cut -d"f" -f1`
    cluster=`tail -n 10 results0.60.txt | grep finished |cut -d"c" -f1 | cut -d"d" -f2`
    normalizado=`bc <<< "scale=2; $cluster/$total" | sed 's/^\./0./'`
    echo $line ",0.60," $total "," $cluster "," $normalizado | sed 's/ //g' >> results_$line.txt

    total=`tail -n 10 results0.70.txt | grep finished |cut -d"f" -f1`
    cluster=`tail -n 10 results0.70.txt | grep finished |cut -d"c" -f1 | cut -d"d" -f2`
    normalizado=`bc <<< "scale=2; $cluster/$total" | sed 's/^\./0./'`
    echo $line ",0.70," $total "," $cluster "," $normalizado | sed 's/ //g' >> results_$line.txt

    total=`tail -n 10 results0.75.txt | grep finished |cut -d"f" -f1`
    cluster=`tail -n 10 results0.75.txt | grep finished |cut -d"c" -f1 | cut -d"d" -f2`
    normalizado=`bc <<< "scale=2; $cluster/$total" | sed 's/^\./0./'`
    echo $line ",0.75," $total "," $cluster "," $normalizado | sed 's/ //g' >> results_$line.txt

    total=`tail -n 10 results0.80.txt | grep finished |cut -d"f" -f1`
    cluster=`tail -n 10 results0.80.txt | grep finished |cut -d"c" -f1 | cut -d"d" -f2`
    normalizado=`bc <<< "scale=2; $cluster/$total" | sed 's/^\./0./'`
    echo $line ",0.80," $total "," $cluster "," $normalizado | sed 's/ //g' >> results_$line.txt

    total=`tail -n 10 results0.85.txt | grep finished |cut -d"f" -f1`
    cluster=`tail -n 10 results0.85.txt | grep finished |cut -d"c" -f1 | cut -d"d" -f2`
    normalizado=`bc <<< "scale=2; $cluster/$total" | sed 's/^\./0./'`
    echo $line ",0.85," $total "," $cluster "," $normalizado | sed 's/ //g' >> results_$line.txt

    total=`tail -n 10 results0.90.txt | grep finished |cut -d"f" -f1`
    cluster=`tail -n 10 results0.90.txt | grep finished |cut -d"c" -f1 | cut -d"d" -f2`
    normalizado=`bc <<< "scale=2; $cluster/$total" | sed 's/^\./0./'`
    echo $line ",0.90," $total "," $cluster "," $normalizado | sed 's/ //g' >> results_$line.txt

    total=`tail -n 10 results0.95.txt | grep finished |cut -d"f" -f1`
    cluster=`tail -n 10 results0.95.txt | grep finished |cut -d"c" -f1 | cut -d"d" -f2`
    normalizado=`bc <<< "scale=2; $cluster/$total" | sed 's/^\./0./'`
    echo $line ",0.95," $total "," $cluster "," $normalizado | sed 's/ //g' >> results_$line.txt

    total=`tail -n 10 results0.65.txt | grep finished |cut -d"f" -f1`
    cluster=`tail -n 10 results0.65.txt | grep finished |cut -d"c" -f1 | cut -d"d" -f2`
    normalizado=`bc <<< "scale=2; $cluster/$total" | sed 's/^\./0./'`
    echo $line ",0.65," $total "," $cluster "," $normalizado | sed 's/ //g' >> results_$line.txt

    cd ..
done < "$filename"
