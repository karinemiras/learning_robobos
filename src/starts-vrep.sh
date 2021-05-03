#!/bin/bash


num_terminals=4
start_port=19996


for i in $(seq $num_terminals)
 do

     echo ""
     screen -d -m -S port_${start_port} ../learning_robobos/src/runs-vrep.sh $start_port;

     start_port=$((${start_port}+1))

 done


 # from VREP root run:
 # ../learning_robobos/src/starts-vrep.sh
