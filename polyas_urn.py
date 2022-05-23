from random import random

# polya's urn
# we have an urn with a red and green ball initially
# each turn, sample a random ball and add another ball of the same color
# after many rounds, what is the fraction of green balls to total balls?
class PolyasUrnSampling:
    def __init__(self, green=1, red=1):
        self.green = green
        self.red = red

    def __iter__(self):
        self.green = 1
        self.red = 1
        return self

    def __next__(self):
        total = self.green + self.red
        drawn = random() < self.green/total
        if drawn:
            self.green += 1
        else:
            self.red += 1
        return self.green/(total+1)