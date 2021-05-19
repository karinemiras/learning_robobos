#!/bin/bash
#set -e
#set -x


num_terminals=20
experiments=("forageTD3e1" "forageTD3e2" "forageTD3e0" "forageTD3l1" "forageTD3l5")
runs=10
checkpoints=5
start_port=20000


possible_screens=()

# defines possible ports for screens
for port in $(seq $start_port $((${start_port}+${num_terminals}-1))); do
    possible_screens+=($port)
done


while true
	do

    printf "\n  >>>> loop ... \n"

    # discover free terminals

    active_screens=()
    free_screens=()
    active_experiments=()

   ###
    declare -a arr="$(screen -list)"
        echo "listtt"
        for ar in "${arr[@]}"; do
           echo $ar
      done


    for obj in ${arr[@]}; do

        if [[ "$obj" == *"exp_"* ]]; then
          printf "\n screen ${obj} is on\n"
          screen_port="$(cut -d'_' -f2 <<<"$obj")"
          active_experiments+=("$(cut -d'_' -f3 -<<<"$obj")_$(cut -d'_' -f4 -<<<"$obj")")
          active_screens+=($screen_port)
        fi
    done

   for possible_screen in "${possible_screens[@]}"; do
       if [[ ! " ${active_screens[@]} " =~ " ${possible_screen} " ]]; then
           free_screens+=($possible_screen)
     fi
      done

      ###
      echo "active_screens"
        for active_screen in "${active_screens[@]}"; do
           echo $active_screen
      done
       echo "active_experiments"
        for active_experiment in "${active_experiments[@]}"; do
           echo $active_experiment
      done
      echo "free_screens"
        for free_screen in "${free_screens[@]}"; do
           echo $free_screen
      done




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

                # only if not already running
                if [[ ! " ${active_experiments[@]} " =~ " ${experiment}_${run} " ]]; then
                   to_do+=("${experiment}_${run}")
                fi
             fi
         else
             # not started yet
             echo " None";
              # only if not already running
                if [[ ! " ${active_experiments[@]} " =~ " ${experiment}_${run} " ]]; then
                   to_do+=("${experiment}_${run}")
                fi
         fi

        done
    done


    # spawns N experiments (N is according to free screens)

    max_fs=${#free_screens[@]}
    to_do=("${to_do[@]:0:$max_fs}")

      ###
      echo "to_do"
        for to_d in "${to_do[@]}"; do
           echo $to_d
      done



    p=0
    for to_d in "${to_do[@]}"; do

        screen -d -m -S exp_${free_screens[$p]}_${to_d} -L -Logfile experiments/"${to_d}.log" nice -n19 python3  src/$(cut -d'_' -f1 <<<"${to_d}").py --experiment-name ${to_d} --robot-port ${free_screens[$p]};

        printf "\n >> (re)starting exp_${free_screens[$p]}_${to_d} \n\n"
        p=$((${p}+1))

    done


   sleep 3600s;

done

# screen -ls  | egrep "^\s*[0-9]+.exp_" | awk -F "." '{print $1}' |  xargs kill
# killall screen
# screen -r naaameee
# screen -list


