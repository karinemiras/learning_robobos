#!/bin/bash

runs=4
num_terminals=4
checkpoints=4
start_port=19996

experiments=("forageTD3e0" "forageTD3e1" "forageTD3e2")

while true
	do

    to_do=()

    for i in $(seq $runs)
    do
        run=$(($i))

        for experiment in "${experiments[@]}"
        do

         echo ""
         file="experiments/${experiment}_${run}/log.txt";

         #check if experiments status
         if [[ -f "$file" ]]; then

           value=$(grep "SAVED checkpoint" $file|tail -n1|sed -E "s/\SAVED checkpoint ([0-9]+).*/\1/g");

            echo $file;
            echo $value;

            if [ "$value" != "$checkpoints" ]; then

              to_do+=("${experiment}_${run}")
             fi
          else
             echo "$file"
             echo "None";
             to_do+=("${experiment}_${run}")
          fi

        done
    done


    # selects num_terminals unfinished experiments to spawn
    to_do=(${to_do[@]:0:$num_terminals})
    for experiment in "${to_do[@]}"
    do

         screen -d -m -S exp_${start_port}  python3  src/"$(cut -d'_' -f1 <<<"$experiment").py --experiment-name ${experiment} --robot-port ${start_port} > experiments/full_log_${experiment}.txt"
         start_port=$((${start_port}+1))
    done

    sleep 1800s;

done


# killall screen
# screen -r naaameee
# screen -list


