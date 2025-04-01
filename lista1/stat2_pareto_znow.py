import random
import matplotlib.pyplot as plt
import math
import numpy as np
from scipy.stats import pareto
import seaborn as sns


def pareto_simulation(sample, alpha = 3, lambd = 1):
    us = []
    for i in range(sample):
        us.append(random.uniform(0,1))
    return [lambd * ((1-u)**(-1/alpha) - 1) for u in us]

xs1 = np.linspace(0,8,1000)


simul = [1-(1/(1+x))**3 for x in xs1]
simul2 = pareto_simulation(1000)
plt.plot(xs1, simul, label="teoretyczna")
sns.ecdfplot(simul2, label="empiryczna")
plt.legend()
plt.show()
