#!/usr/bin/env python3
import neat

import cv2
import numpy as np
import os
import time
import visualize

import robobo
from config import Config

class EA:

    def __init__(self, config):

        # params

        self.config = config
        self.max_food = 7

        self.robot = False
        while not self.robot:
            self.robot = robobo.SimulationRobobo().connect(address=self.config.robot_ip, port=self.config.robot_port)
            time.sleep(1)

    def get_infrared(self):

        irs = np.asarray(self.robot.read_irs()).astype(np.float32)

        irs[irs != 0] = 1

        back   = max(irs[0], irs[1], irs[2])
        front1 = max(irs[3], irs[4], irs[5])
        front2 = max(irs[5], irs[6], irs[7])

        sensors = [back, front1, front2]

        return sensors

    def detect_color(self):

        image = self.robot.get_image_front()
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

        # mask of green
        mask = cv2.inRange(hsv, (36, 25, 25), (70, 255, 255))

        if cv2.countNonZero(mask) > 0:
            y = np.where(mask == 255)[0]
            x = np.where(mask == 255)[1]
            avg_y = sum(y) / len(y) / 127
            avg_x = sum(x) / len(x) / 127

        else:
            avg_y = 0
            avg_x = 0

        # if green detected, returns average positions of y and x
        return avg_y, avg_x

    def eval_genomes(self, genomes, config):

        for genome_id, genome in genomes:

            net = neat.nn.FeedForwardNetwork.create(genome, config)

            current_step = 0
            collected_food = 0

            self.robot.stop_world()
            while self.robot.is_simulation_running():
                pass

            self.robot.set_position()

            self.robot.play_simulation()
            while self.robot.is_simulation_stopped():
                pass

            self.robot.set_phone_tilt(-100)

            #print('train', self.config.episode_train_steps)
            while current_step < self.config.episode_train_steps and collected_food < self.max_food:
                sensors = self.get_infrared()
                color_y, color_x = self.detect_color()

                inputs = sensors+[ color_y, color_x]
                #print(inputs)

                actions = net.activate(inputs)
                #print(current_step, actions)

                action_left = actions[0]
                action_right = actions[1]

                left = action_left * (self.config.max_left - self.config.min_left) + self.config.min_left
                right = action_right * (self.config.max_right - self.config.min_right) + self.config.min_right

                #print(left, right)
                self.robot.move(left, right)

                collected_food = self.robot.collected_food()

                genome.fitness = collected_food

                current_step = current_step+1
            print('fit', collected_food)


    def run(self):

        local_dir = os.path.dirname(__file__)
        config_file = os.path.join(local_dir, 'config-feedforward')

        # Load configuration.

        config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
                             neat.DefaultSpeciesSet, neat.DefaultStagnation,
                             config_file)

        # Create the population, which is the top-level object for a NEAT run.
        p = neat.Population(config)

        # Add a stdout reporter to show progress in the terminal.
        p.add_reporter(neat.StdOutReporter(True))
        stats = neat.StatisticsReporter()
        p.add_reporter(stats)
        p.add_reporter(neat.Checkpointer(5))

        # Run for up to 300 generations.
        winner = p.run(self.eval_genomes, 100)

        # Display the winning genome.
        print('\nBest genome:\n{!s}'.format(winner))

        # # Show output of the most fit genome against training data.
        # print('\nOutput:')
        # winner_net = neat.nn.FeedForwardNetwork.create(winner, config)
        # for xi, xo in zip(xor_inputs, xor_outputs):
        #     output = winner_net.activate(xi)
        #     print("input {!r}, expected output {!r}, got {!r}".format(xi, xo, output))
        #
        # node_names = {-1: 'A', -2: 'B', 0: 'A XOR B'}
        # visualize.draw_net(config, winner, True, node_names=node_names)
        visualize.plot_stats(stats, ylog=False, view=True)
        visualize.plot_species(stats, view=True)

        # p = neat.Checkpointer.restore_checkpoint('neat-checkpoint-4')
        # p.run(eval_genomes, 10)


config = Config()
config = config.parser.parse_args()

EA(config).run()