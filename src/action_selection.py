import numpy as np
import pygame
import time


class ActionSelection:

    def __init__(self, config):
        self.config = config

        pygame.init()
        pygame.joystick.init()

        if self.config.human_interference:
            self.joystick = pygame.joystick.Joystick(0)
            self.joystick.init()

    def normalize_move(self, var):
        if self.config.sim_hard == 'sim':
            return var * (self.config.max_speed - self.config.min_speed) + self.config.min_speed
        else:
            return var * (self.config.max_speed_hard - self.config.min_speed_hard) + self.config.min_speed_hard

    def normalize_millis(self, var):
        millis = var * (self.config.max_millis - self.config.min_millis) + self.config.min_millis

        return millis

    def max_action(self, direction):
        if self.config.sim_hard == 'sim':
            if direction == 'forward':
                return self.config.max_speed
            else:
                return self.config.min_speed
        else:
            if direction == 'forward':
                return self.config.max_speed_hard
            else:
                return self.config.min_speed_hard

    def select(self, actions):

        left, right, millis = self.robot_mode(actions)
        apply_reward = 1

        # if present, human actions overrule robot actions
        if self.is_human_active():
            left, right, millis, apply_reward = self.human_mode(left, right)

        if self.config.sim_hard == 'hard':
            left = int(left)
            right = int(right)
            millis = int(millis)

        return left, right, millis, apply_reward

    def is_human_active(self):
        if not self.config.human_interference:
            return False
        
        pygame.event.get()
        if int(self.joystick.get_button(3)) == 1 or \
                int(self.joystick.get_button(0)) == 1 or \
                int(self.joystick.get_button(2)) == 1 or \
                int(self.joystick.get_button(1)) == 1:
            return True
        else:
            return False

    def human_mode(self, robot_left, robot_right):

        # y = move forward
        if int(self.joystick.get_button(3)) == 1:
            left = self.max_action('forward')
            right = left

        # a = move backward
        elif int(self.joystick.get_button(0)) == 1:
            left = self.max_action('backward')
            right = left

        # x = move right wheel
        elif int(self.joystick.get_button(2)) == 1:
            left = 0

            # directional down: backwards wheel
            if round(self.joystick.get_axis(1)) == 1:
                right = self.max_action('backward')
            # forwards wheel
            else:
                right = self.max_action('forward')

        # b = move left wheel
        elif int(self.joystick.get_button(1)) == 1:
            right = 0

            # directional down: backwards wheel
            if round(self.joystick.get_axis(1)) == 1:
                left = self.max_action('backward')
            # forwards wheel
            else:
                left = self.max_action('forward')

        # define duration of move
        if round(self.joystick.get_axis(1)) == -1:
            # makes it positive, once joystick-directional-up returns a negative number
            action_millis = self.joystick.get_axis(1)*-1

        # uses min duration if human does not choose
        else:
            action_millis = 0

        millis = self.normalize_millis(action_millis)

        apply_reward = self.check_apply_reward(robot_left, robot_right, left, right)

        return left, right, millis, apply_reward

    def simplify_action(self, var):
        if var < 0:
            var = -1
        if var == 0:
            var = 0
        if var > 0:
            var = 1
        return var

    def check_apply_reward(self, robot_left, robot_right, human_left, human_right):

        apply_reward = -1

        robot_left = self.simplify_action(robot_left)
        robot_right = self.simplify_action(robot_right)
        human_left = self.simplify_action(human_left)
        human_right = self.simplify_action(human_right)

        if human_left == robot_left and human_right == robot_right:
            apply_reward = 1

        return apply_reward

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



