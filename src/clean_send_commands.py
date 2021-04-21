#!/usr/bin/env python3
from __future__ import print_function

import time
import numpy as np

import robobo
import cv2
import sys
import signal
import prey
import random

def terminate_program(signal_number, frame):
    print("Ctrl-C received, terminating program")
    sys.exit(1)

def main():
    #signal.signal(signal.SIGINT, terminate_program)

   # rob = robobo.HardwareRobobo(camera=True).connect(address="10.15.3.116")
    rob = robobo.SimulationRobobo().connect(address='192.168.0.105', port=19997)

    rob.play_simulation()
    # Following code moves the robot
    for i in range(100):
        print('\n'+str(i))
        left = random.randint(0, 20)
        right = random.randint(0, 20)
           # print("robobo is at {}".format(rob.position()))
        try:

            rob.move(10, 10, 3000)
            print(left, right)
        except Exception as error:
          print(error)
        print("ROB Irs: {}".format(np.log(np.array(rob.read_irs())) / 10))


if __name__ == "__main__":
    main()
