import argparse


class Config:

    def __init__(self):

        self.parser = argparse.ArgumentParser()

        self.parser.add_argument(
            '--sim-hard',
            default='sim', type=str,
            help="sim for simulation and hard for hardware"
        )

        self.parser.add_argument(
            '--robot-ip-hard',
            default='10.15.3.116', type=str,
            help="Ip of the robot in hardware."
        )


        # simulation

        self.parser.add_argument(
            '--robot-ip',
            default='145.108.196.188', type=str,
            help="Ip of the robot in simulation."
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
            '--min-speed',
            default=-3, type=int,
            help="Minimum accelaration of the left wheels in simulation (backwards)."
        )

        self.parser.add_argument(
            '--max-speed',
            default=3, type=int,
            help="Maximum accelaration of the wheels in simulation (forward)."
        )

        self.parser.add_argument(
            '--min-speed-hard',
            default=-100, type=int,
            help="Minimum accelaration of the left wheels in hardware (backwards)."
        )

        self.parser.add_argument(
            '--max-speed-hard',
            default=100, type=int,
            help="Maximum accelaration of the wheels in hardware (forward)."
        )
