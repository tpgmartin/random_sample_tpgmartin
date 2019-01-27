from random_sample_tpgmartin.function_random_sample import sample_from_distribution
from random_sample_tpgmartin.oop_random_sample import *

print("Function approach")

# No distribution specified
wrong_distribution = sample_from_distribution(10, "uniform", {})
print(wrong_distribution)

# Good example with binomial distribution
good_binomial_distribution = sample_from_distribution(10, "binomial", {"prob":0.1, "trials":10})
print(good_binomial_distribution)

# Bad example with binomial distribution
bad_binomial_distribution = sample_from_distribution(10, "binomial", {})
print(bad_binomial_distribution)

# Good example with normal distribution
good_normal_distribution = sample_from_distribution(10, "normal", {"mean":0, "std":1})
print(good_normal_distribution)

# Bad example with normal distribution
bad_normal_distribution = sample_from_distribution(10, "normal", {})
print(bad_normal_distribution)

# Good example with poisson distribution
good_poisson_distribution = sample_from_distribution(10, "poisson", {"mean":10})
print(good_poisson_distribution)

# Bad example with poisson distribution
bad_poisson_distribution = sample_from_distribution(10, "poisson", {})
print(bad_poisson_distribution)

print('---------------\n')
print("OOP approach")

binomial_distribution = Binomial(10, 0.1, 10)
binomial_distribution.draw()
binomial_distribution.summarise()

normal_distribution = Normal(10, 0, 1)
normal_distribution.draw()
normal_distribution.summarise()

poisson_distribution = Poisson(10, 10)
poisson_distribution.draw()
poisson_distribution.summarise()