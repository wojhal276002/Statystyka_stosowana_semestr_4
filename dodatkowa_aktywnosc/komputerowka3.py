import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import random

theta = 2
n = 1000
thety_mm = []
thety_nw = []
def komputerowka_simulation(sample, theta):
    us = []
    for i in range(sample):
        us.append(random.uniform(0,1))
    return us
for i in range(1000):
    empir = komputerowka_simulation(n,theta)
    Y = []
    for p in empir:
        Y.append((np.sqrt(abs(-(theta**2)/p))))
    theta_mm = sum(Y)/(2*n)
    theta_nw = min(Y)
    thety_mm.append(theta_mm)
    thety_nw.append(theta_nw)

fig, ax = plt.subplots()
ax.boxplot([thety_nw,thety_mm])
plt.show()
#pierwszy nw pozniej mm