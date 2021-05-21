#!/bin/bash
#set -e
#set -x


experiments=("env1TD3e0" "env1TD3l1" "env1TD3l5" "env2TD3e0" "env2TD3l1" "env2TD3l5" "env3TD3e0" "env3TD3l1" "env3TD3l5")
runs=20
checkpoints=3


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

