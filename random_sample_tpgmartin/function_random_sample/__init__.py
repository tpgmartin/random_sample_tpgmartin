from numpy import random

def sample_from_distribution(sample_size, distribution, parameters):

    distributions = ["binomial", "normal", "poisson"]

    distribution = distribution.lower()
    if distribution not in distributions:
        return "distribution must be one of binomial, normal, or poisson"

    if distribution == "binomial":
        try:
            prob = parameters["prob"]
            trials = parameters["trials"]
            sample = random.binomial(trials, prob, sample_size)
        except KeyError:
            return "Must pass parameter dictionary with 'prob' and 'trials' values"

    if distribution == "normal":
        try:
            mean = parameters["mean"]
            std = parameters["std"]
            sample = random.normal(mean, std, sample_size)
        except KeyError:
            return "Must pass parameter dictionary with 'mean' and 'std' values"

    if distribution == "poisson":
        try:
            mean = parameters["mean"]
            sample = random.poisson(mean, sample_size)
        except KeyError:
            return "Must pass parameter dictionary with 'mean' value"
    
    return sample