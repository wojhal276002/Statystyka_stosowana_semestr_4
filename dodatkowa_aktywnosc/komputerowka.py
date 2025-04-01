import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import random

n=1000
theta = 2
def komputerowka_simulation(sample):
    us = []
    for i in range(sample):
        us.append(random.uniform(0,1))
    return us
empir = komputerowka_simulation(n)
nowa = []
for p in empir:
    nowa.append(np.sqrt((theta**2)/(1-p)))
xs = np.linspace(2,100,1000)
teor = 1-(theta**2)/(xs**2)
print(teor)
sns.ecdfplot(nowa,label="dyst empir")
plt.plot(xs,teor,label="dyst teor")
plt.title("Dyst teor vs dyst empir")
plt.legend()
plt.show()
