import argparse


class Config:

    def __init__(self):

        self.parser = argparse.ArgumentParser()

        # simulation

        self.parser.add_argument(
            '--robot-ip',
            default='145.108.196.188', type=str,
            help="Ip of the robot."
        )

        self.parser.add_argument(
            '--robot-port',
            default=19997, type=int,
            help="Port of the robot."
        )

        # experimental setup

        self.parser.add_argument(
            '--episode-train-steps',
            default=100, type=int,
            help="Maximum number of steps of an episode while training."
        )

        self.parser.add_argument(
            '--episode-validation-steps',
            default=130, type=int,
            help="Maximum duration of an episode while validating (during training)."
        )

        self.parser.add_argument(
            '--episode-test-steps',
            default=170, type=int,
            help="Maximum duration of an episode while making final tests."
        )

        self.parser.add_argument(
            '---validation-freq',
            default=1000, type=int,
            help="After how many steps the policy should be validation."
        )

        self.parser.add_argument(
            '---number-validations',
            default=5, type=int,
            help="Number of episodes to repeat the validation of the policy during training."
        )

        self.parser.add_argument(
            '--train-or-test',
            default='train', type=str,
            help="If it is running as training or (final) testing: 'train' or 'test'."
        )

        self.parser.add_argument(
            '---number-tests',
            default=3, type=int,
            help="Number of episodes to repeat the test of the policy after training."
        )

        self.parser.add_argument(
            '--training-timesteps',
            default=30000, type=int,
            help="Number of total time steps in the training."
        )

        self.parser.add_argument(
            '--checkpoint-timesteps',
            default=5000, type=int,
            help="After how many time steps sabes checkpoint."
        )

        self.parser.add_argument(
            '--experiment-name',
            default='default_experiment', type=str,
            help="Name of the current experiment."
        )

        # states and actions

        self.parser.add_argument(
            '--min-millis',
            default=500, type=int,
            help="Minimum duration of actions."
        )

        self.parser.add_argument(
            '--max-millis',
            default=1000, type=int,
            help="Maximum duration of actions."
        )

        self.parser.add_argument(
            '--min-left',
            default=-3, type=int,
            help="Minimum accelaration of left wheel (backwards)."
        )

        self.parser.add_argument(
            '--max-left',
            default=3, type=int,
            help="Maximum accelaration of left wheel (forward)."
        )

        self.parser.add_argument(
            '--min-right',
            default=-3, type=int,
            help="Minimum accelaration of right wheel (backwards)."
        )

        self.parser.add_argument(
            '--max-right',
            default=3, type=int,
            help="Maximum accelaration of right wheel (forward)."
        )