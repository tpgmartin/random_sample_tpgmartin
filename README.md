# Random Sample tpgmartin

This package provides two ways of generating a random sample from one of the following distributions: binomial, normal, poisson. You can either generate a sample from a given distribution using a function, or to create an object for a given distribution and generate a sample from there.

Check the file `example.py` for specific use instances.

## Installation

* Clone this repo
* `cd` into the directory
* Run `pip install .` or `pip install -e .` to create a symlink

## Function Random Sample

The function `sample_from_distribution` returns a sample from a given random distribution as specified by the positional arguments passed to it. In all cases the function expects,

* Sample size - the number of samples to return from the distribution
* The name of the distribution - either binomial, normal, or poisson
* The parameters for the distribution - this is a dictionary, and is specific to each distribution
    * Binomial distributions expect probability of success and number of trials
    * Normal distributions expect the mean and standard deviation
    * Poisson distributions expect the expectation value (mean)

The following code snippet shows the precise parameters required.

```
from random_sample_tpgmartin import sample_from_distribution

binomial = sample_from_distribution(10, "binomial", {"prob":0.1, "trials":10})
print(binomial)

normal = sample_from_distribution(10, "normal", {"mean":0, "std":1})
print(normal)

poisson = sample_from_distribution(10, "poisson", {"mean":10})
print(poisson)
```

## OOP Random Sample

To create an distribution class instance import the classes from `oop_random_sample` and call them as follows. Each distribution requires different positional arguments,

* Binomial distribution class requires sample size, probability of success, and number of trials in that order
* Normal distribution class requires sample size, mean, and standard deviation in that order
* Poisson distribution class requires sample size and expectation value (mean) in that order

Once created, a sample is generated for a given distribution by invoking `draw()` and a summary table is printed to the console with `summarise()`. The summary table contains the mean, standard deviation, minimum and maximum values of the last obtained sample for that distribution.

```
from random_sample_tpgmartin.oop_random_sample import *

binomial = Binomial(10, 0.1, 10)
binomial.draw()
binomial.summarise()

normal = Normal(10, 0, 1)
normal.draw()
normal.summarise()

poisson = Poisson(10, 10)
poisson.draw()
poisson.summarise()
```

## Dependencies

* `numpy`
* `tabulate`
