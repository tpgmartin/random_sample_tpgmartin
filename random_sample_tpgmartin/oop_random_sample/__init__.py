import numpy as np
from prettytable import PrettyTable

class Distribution(object):

    def __init__(self, sample_size):
        self.sample = None
        self.sample_size = sample_size

    def summarise(self):

        if self.sample is None:
            return "Need to call `draw()` method first"

        mean = np.round(np.mean(self.sample), decimals=2)
        std = np.round(np.std(self.sample), decimals=2)
        min = np.round(np.min(self.sample), decimals=2)
        max = np.round(np.max(self.sample), decimals=2)

        summary = PrettyTable(["Statistic", "Value"])
        summary.add_row(["mean", mean])
        summary.add_row(["std", std])
        summary.add_row(["min", min])
        summary.add_row(["max", max])

        print(summary)

class Binomial(Distribution):

    def __init__(self, sample_size, prob, trials):
        super(Binomial, self).__init__(sample_size)
        self.prob = prob
        self.trials = trials

    def draw(self):
        self.sample = np.random.binomial(self.trials, self.prob, self.sample_size)
        print("New sample: {}".format(self.sample))

class Normal(Distribution):

    def __init__(self, sample_size, mean, std):
        super(Normal, self).__init__(sample_size)
        self.mean = mean
        self.std = std

    def draw(self):
        self.sample = np.random.normal(self.mean, self.std, self.sample_size)
        print("New sample: {}".format(self.sample))

class Poisson(Distribution):

    def __init__(self, sample_size, mean):
        super(Poisson, self).__init__(sample_size)
        self.mean = mean

    def draw(self):
        self.sample = np.random.poisson(self.mean, self.sample_size)
        print("New sample: {}".format(self.sample))
