from random import random

# autoregressive process
# x_n(t+1) = p*x_n(t) + e(t) with abs(p) < 1
# weak path dependence
# forgets initial condition over time
class AutoregressiveSampling:
    def __init__(self, init_y=30, dependence=.9, white_noise=1):
        self.init_y = init_y
        self.dependence = dependence
        self.white_noise = white_noise

    def __iter__(self):
        self.prev = self.init_y
        return self

    def __next__(self):
        new_val = self.dependence*self.prev + (random()*self.white_noise) - (self.white_noise/2)
        self.prev = new_val
        return new_val