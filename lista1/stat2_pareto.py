import random
import matplotlib.pyplot as plt
import math
import numpy as np
from scipy.stats import pareto


def pareto_simulation(sample, alpha = 3, lambd = 1):
    us = []
    for i in range(sample):
        us.append(random.uniform(0,1))
    return [lambd * ((1-u)**(-1/alpha) - 1) for u in us]

xs1 = np.linspace(0,1000,1000)

simul = pareto_simulation(1000)
plt.plot(xs1, simul)
plt.show()