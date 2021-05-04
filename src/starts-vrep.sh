#!/bin/bash


num_terminals=2
start_port=20000


for i in $(seq $num_terminals)
 do

     echo "";
     screen -d -m -S sim_${start_port} ../learning_robobos/src/runs-vrep.sh $start_port;
     sleep 1s;

     start_port=$((${start_port}+1));

 done


 # from VREP root run:
 # ../learning_robobos/src/starts-vrep.sh
