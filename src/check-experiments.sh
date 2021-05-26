#!/bin/bash
#set -e
#set -x


experiments=("envseenTD3l1" "envseenTD3l3" "envseenTD3l5" "envmseenTD3l1" "envmseenTD3l3" "envmseenTD3l5" "envmseentTD3l1" "envmseentTD3l3" "envmseentTD3l5")
runs=10
checkpoints=6


# discover unfinished experiments

to_do=()
for i in $(seq $runs)
do
    run=$(($i))

    for experiment in "${experiments[@]}"
    do

     printf  "\n${experiment}_${run} \n"
     file="experiments/${experiment}_${run}/log.txt";

     #check experiments status
     if [[ -f "$file" ]]; then

         value=$(grep "SAVED checkpoint" $file|tail -n1|sed -E "s/\SAVED checkpoint ([0-9]+).*/\1/g");
         echo " ${value} "

     else
         # not started yet
         echo " None";
     fi

    done
done

