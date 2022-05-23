from random import random

# random multiplicative growth
# standard model of the evolution of asset prices in finance and cell populations in biology
# sometimes called "equation of life"
# x_n(t+1) = 
#   1.5*x_n(t) with p = 1/2
#   0.6*x_n(t) with p = 1/2
class RandomMultiplicativeGrowthSampling:
    def __init__(self, init_y=1, growth_factor=1.5, decay_factor=0.6, p=.5):
        self.init_y = init_y
        self.growth_factor = growth_factor
        self.decay_factor = decay_factor
        self.p = p

    def __iter__(self):
        self.prev = self.init_y
        return self

    def __next__(self):
        if random() > self.p:
            new_val = self.prev*self.growth_factor
        else:
            new_val = self.prev*self.decay_factor
        self.prev = new_val
        return new_val