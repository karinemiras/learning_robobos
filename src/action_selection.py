import numpy as np
import pygame
import time
import math


class ActionSelection:

    def __init__(self, config):
        self.config = config

        pygame.init()
        pygame.joystick.init()

        if self.config.human_interference:
            self.joystick = pygame.joystick.Joystick(0)
            self.joystick.init()

    def get_range_speed(self):
        if self.config.sim_hard == 'sim':
            range = self.config.range_speed
        else:
            range = self.config.range_speed_hard

        return range

    def normalize_move(self, var):
        range = self.get_range_speed()
        max = range
        min = -range
        return var * (max - min) + min

    def normalize_move_negative(self, var):
        range = self.get_range_speed()
        max = range
        min = -range

        old_min = -1
        old_range = 1 - old_min
        new_range = max - min
        var = (var - old_min) / old_range * new_range + min
        return var

    def normalize_millis(self, var):
        millis = var * (self.config.max_millis - self.config.min_millis) + self.config.min_millis
        return millis

    def select(self, actions):

        left, right, millis = self.robot_mode(actions)
        prop_diff = 0

        # if present, human actions overrule robot actions
        if self.is_human_active():
            left, right, millis, prop_diff = self.human_mode(left, right)

        if self.config.sim_hard == 'hard':
            left = int(left)
            right = int(right)
            millis = int(millis)

        return left, right, millis, prop_diff

    def is_human_active(self):
        if not self.config.human_interference:
            return False

        pygame.event.get()

        # if passes garbage threshold
        if abs(self.joystick.get_axis(1)) > 0.2 or abs(self.joystick.get_axis(3)) > 0.2:
            return True
        else:
            return False

    def human_mode(self, robot_left, robot_right):

        # left-directional down: -1/1 = front/back
        # the multiplication inverts it, otherwise it is confusing for human
        left_directional = self.joystick.get_axis(1) * -1

        # right-directional: -1/1 = left/right
        right_directional = self.joystick.get_axis(3)

        # move (has precedence over turn)
        if abs(left_directional) > 0.2:
            left = self.normalize_move_negative(left_directional)
            right = self.normalize_move_negative(left_directional)
        else:

            if abs(right_directional) > 0.2:

                # uses abs, because it is difficult for human to rotate backwards, and robot seems to rarely do it
                right_value = abs(right_directional)

                # move left wheel, turn right
                if right_directional > 0:
                    left = self.normalize_move_negative(right_value)
                    right = 0
                # move right wheel, turn left
                if right_directional < 0:
                    left = 0
                    right = self.normalize_move_negative(right_value)

        # uses max for human
        action_millis = 1
        millis = self.normalize_millis(action_millis)

        prop_diff = self.check_correct_action(robot_left, robot_right, left, right)

        return left, right, millis, prop_diff

    def check_correct_action(self, robot_left, robot_right, human_left, human_right):

        left_diff = abs(robot_left - human_left)
        right_diff = abs(robot_right - human_right)
        diff = left_diff+right_diff

        range = self.get_range_speed()
        prop_diff = diff / (range*2*2)

        return prop_diff

    def robot_mode(self, actions):

        action_move = actions[0]
        action_left = actions[1]
        action_right = actions[2]
        action_millis = actions[3]

        # performs actions
        choice = actions[0:3]
        choice = np.argmax(choice)

        # move
        if choice == 0:
            left = self.normalize_move(action_move)
            right = self.normalize_move(action_move)
        # move left wheel
        if choice == 1:
            left = self.normalize_move(action_left)
            right = 0
        # move right wheel
        if choice == 2:
            left = 0
            right = self.normalize_move(action_right)

        return left, right, self.normalize_millis(action_millis)



