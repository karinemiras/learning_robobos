#!/bin/bash
#set -e
#set -x


num_terminals=15
checkpoints=5
start_port=20000


experiments=("forageTD3e1" "forageTD3e2" "forageTD3e0")
runs=20


while true
	do


    # check if there are free terminals

    screens_on=0
    declare -a arr="$(screen -list)"
    for obj in ${arr[@]}; do

        if [[ "$obj" == *"exp_"* ]]; then
       printf "\n \n screen ${obj} is on"
       screens_on=$((${screens_on}+1))
    fi
    done
    start_port=$((${start_port}+${screens_on}))

    screens_left=$((${num_terminals}-${screens_on}))
    printf "\n \n ${screens_left} screens are free \n \n"



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

             # unfinished
             if [ "$value" != "$checkpoints" ]; then
               to_do+=("${experiment}_${run}")
             fi
         else
             # not started yet
             echo " None";
             to_do+=("${experiment}_${run}")
         fi

        done
    done



    # spawns N experiments (N is according to free screens)
    to_do=(${to_do[@]:0:$screens_left})
    for experiment in "${to_do[@]}"
    do

        screen -d -m -S exp_${start_port} -L -Logfile experiments/"${experiment}.log" nice -n19 python3  src/$(cut -d'_' -f1 <<<"$experiment").py --experiment-name ${experiment} --robot-port ${start_port};

        printf "\n >> running ${experiment} in screen exp_${start_port} \n\n"
        start_port=$((${start_port}+1))

    done


   sleep 1800s;

done

# screen -ls  | egrep "^\s*[0-9]+.exp_" | awk -F "." '{print $1}' |  xargs kill
# killall screen
# screen -r naaameee
# screen -list


