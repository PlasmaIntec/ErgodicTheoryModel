from math import floor
from random import random

# trivial sampling
# x_n(t) ~ X for all n and t
# no dynamic dependence on initial condition
# time and ensemble averages constructed identically
class TrivialSampling:
    def __init__(self, bias=.5):
        self.bias = bias

    def __iter__(self):
        return self

    def __next__(self):
        return floor(random()/self.bias)