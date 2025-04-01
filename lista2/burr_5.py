import random
import matplotlib.pyplot as plt
import math
import numpy as np
from scipy.stats import pareto,burr
import seaborn as sns

def burr_simulation(sample, alpha=3, lambd=1, T=2):
    us = []
    for i in range(sample):
        us.append(random.uniform(0,1))
    return [((lambd * ((1-u)**(-1/alpha) - 1))**1/T) for u in us]

def density(simulation,alpha=3,lambd=1,T=2):
    return [T*s**(T-1)*(lambd**alpha*alpha)/((s**T+lambd)**(alpha+1)) for s in simulation]


xs1 = np.linspace(0,8,1000)
c = burr_simulation(1000)
dens = density(c)
plt.plot(xs1, burr.pdf(xs1, c=2, d=0.5))
sns.distplot(dens, hist=False)
plt.show()