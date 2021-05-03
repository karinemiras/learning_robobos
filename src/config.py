import argparse

class Config:

    def __init__(self):

        self.parser = argparse.ArgumentParser()

        self.parser.add_argument(
            '--robot-ip',
            default='192.168.0.100', type=str,
            help="Ip of the robot."
        )

        self.parser.add_argument(
            '--robot-port',
            default=19997, type=int,
            help="Port of the robot."
        )

        self.parser.add_argument(
            '--train-or-test',
            default='train', type=str,
            help="If it is running as training or testing: 'train' or 'test'."
        )

        self.parser.add_argument(
            '--episode-train-time',
            default=200000, type=int,
            help="Maximum duration of an episode while training."
        )

        self.parser.add_argument(
            '--episode-test-time',
            default=300000, type=int,
            help="Maximum duration of an episode while testing."
        )

        self.parser.add_argument(
            '--checkpoints',
            default=4, type=int,
            help="N stages of training, so that experiments are saved after each stage."
        )


        self.parser.add_argument(
            '--checkpoint-timesteps',
            default=5000, type=int,
            help="Number of total time steps in each training stage."
        )

        self.parser.add_argument(
            '--experiment-name',
            default='default_experiment', type=str,
            help="Name of the current experiment."
        )

        self.parser.add_argument(
            '--min-millis',
            default=500, type=int,
            help="Minimum duration of actions."
        )

        self.parser.add_argument(
            '--max-millis',
            default=500, type=int,
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