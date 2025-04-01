import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import random

n=1000
theta = 2
M =1000
def komputerowka_simulation(sample, theta):
    us = []
    for i in range(sample):
        us.append(random.uniform(0,1))
    return us
U = []
for i in range(M):
    empir = komputerowka_simulation(n,theta)
    nowa = []
    for p in empir:
        nowa.append((np.sqrt(abs(-(theta**2)/p))))
    U.append(max(nowa))
xs = np.linspace(0,3000,1000)
teor = (1-(theta**2)/(xs**2))**n
print(teor)
sns.ecdfplot(U,label="dyst empir")
plt.plot(xs,teor,label="dyst teor")
plt.title("Dyst teor vs dyst empir")
plt.legend()
plt.show()

    