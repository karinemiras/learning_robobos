#!/bin/bash


experiment="foraging-TD"
runs=20
poses=7
repetitons=3

for r in $(seq $runs)
 do
    for p in $(seq 0 $((${poses}-1)) )
     do
           for i in $(seq $repetitons )
            do
               echo "python3 src/final_tests.py --pos ${p} --experiment-name ${experiment}_${r}"
            done
     done
 done


