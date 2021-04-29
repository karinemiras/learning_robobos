class Log:

    def __init__(self, experiment_name):
        self.experiment_name = experiment_name

    def write(self, text):
        print(text)
        #with open("experiments/{}/log.txt".format(experiment_name), "a") as logfile:
        with open("log.txt", "a") as logfile:
            logfile.write(text)