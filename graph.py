from random import random
import numpy as np
import matplotlib.pyplot as plt

from models.trivial import TrivialSampling
from models.autoregressive import AutoregressiveSampling
from models.polyas_urn import PolyasUrnSampling
from models.multiplicative import RandomMultiplicativeGrowthSampling

# Fixing random state for reproducibility
np.random.seed(19680801)

steps = 300
dt = 1
t = np.arange(0, steps, dt)

fig, axs = plt.subplots(4, 1)

samples = []
for i in range(0, 100):        
    rmg_sampling = TrivialSampling()
    rmg_iter = iter(rmg_sampling)
    sample = [next(rmg_iter) for _ in range(len(t))]
    samples.append(t)
    samples.append(sample)

axs[0].plot(*samples)
axs[0].set_xlim(0, steps)
axs[0].set_xlabel('time')
axs[0].set_ylabel('trivial sampling')
axs[0].grid(True)

samples = []
for i in range(0, 100):        
    random_init_y = random()*30-15
    rmg_sampling = AutoregressiveSampling(init_y=random_init_y)
    rmg_iter = iter(rmg_sampling)
    sample = [next(rmg_iter) for _ in range(len(t))]
    samples.append(t)
    samples.append(sample)

axs[1].plot(*samples)
axs[1].set_xlim(0, steps)
axs[1].set_xlabel('time')
axs[1].set_ylabel('autoregressive sampling')
axs[1].grid(True)

samples = []
for i in range(0, 100):        
    rmg_sampling = PolyasUrnSampling()
    rmg_iter = iter(rmg_sampling)
    sample = [next(rmg_iter) for _ in range(len(t))]
    samples.append(t)
    samples.append(sample)

axs[2].plot(*samples)
axs[2].set_xlim(0, steps)
axs[2].set_xlabel('time')
axs[2].set_ylabel('polyas urn sampling')
axs[2].grid(True)

samples = []
for i in range(0, 100):        
    rmg_sampling = RandomMultiplicativeGrowthSampling()
    rmg_iter = iter(rmg_sampling)
    sample = [next(rmg_iter) for _ in range(len(t))]
    samples.append(t)
    samples.append(sample)

axs[3].plot(*samples)
axs[3].set_xlim(0, steps)
axs[3].set_xlabel('time')
axs[3].set_ylabel('random multiplicative growth sampling')
axs[3].grid(True)

fig.tight_layout()
plt.show()