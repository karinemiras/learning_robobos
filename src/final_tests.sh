#!/bin/bash


#experiments=("foraging-TD" "ih_foraging-TD" )
experiments=("h_foraging-TD")
runs=21
runs=(1 2 3 7 10 11)
poses=7
repetitons=3

for experiment in ${experiments[@]}; do

     for r in ${runs[@]};
    #for r in $(seq $runs)
     do
        for p in $(seq 0 $((${poses}-1)) )
         do
               for i in $(seq $repetitons )
                do
                   echo  python3 src/final_tests.py --pos ${p} --experiment-name "${experiment}_${r}"
                done
         done
     done

 done