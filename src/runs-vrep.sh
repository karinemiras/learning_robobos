#!/bin/bash


#./vrep.app/Contents/MacOS/vrep -h ../../../scenes/robobo_food_arena.ttt -gREMOTEAPISERVERSERVICE_"${1}"_FALSE_TRUE nice -n19

./vrep.app/Contents/MacOS/vrep  ../../../scenes/robobo_food_arena.ttt -gREMOTEAPISERVERSERVICE_"${1}"_FALSE_TRUE nice -n19