#!/usr/bin/bash
filename="$1"
while read -r line
do
    dir=`echo $line | cut -d"." -f1`
    mkdir $dir
    name="$line"
    echo "Name read from file - $name"
    cp $line $dir
    cd $dir
    cd-hit -i $line -o db95 -c 0.95 -n 5 -T 0 > results0.95.txt
    cd-hit -i $line -o db90 -c 0.9 -n 5 -T 0 > results0.90.txt
    cd-hit -i $line -o db85 -c 0.85 -n 5 -T 0 > results0.85.txt
    cd-hit -i $line -o db80 -c 0.8 -n 5 -T 0 > results0.80.txt
    cd-hit -i $line -o db75 -c 0.75 -n 5 -T 0 > results0.75.txt
    cd-hit -i $line -o db70 -c 0.7 -n 4  -T 0 > results0.70.txt
    cd-hit -i $line -o db65 -c 0.65 -n 4  -T 0 > results0.65.txt
    cd-hit -i $line -o db60 -c 0.6 -n 4  -T 0 > results0.60.txt
    cd-hit -i $line -o db55 -c 0.55 -n 3  -T 0 > results0.55.txt
    cd-hit -i $line -o db50 -c 0.5 -n 3  -T 0 > results0.50.txt
    cd-hit -i $line -o db45 -c 0.45 -n 2  -T 0 > results0.45.txt
    cd-hit -i $line -o db40 -c 0.4 -n 2  -T 0 > results0.40.txt
    cd ..
done < "$filename"
