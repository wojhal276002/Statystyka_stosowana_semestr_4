import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

theta = 2
n = 1000
thety_mm = []
thety_nw = []
for i in range(1000):
    X = np.random.exponential(1,1000)
    Y = X + theta
    theta_mm = (1/n)*sum(Y-1)
    theta_nw = min(Y)
    thety_mm.append(theta_mm)
    thety_nw.append(theta_nw)

fig, ax = plt.subplots()
ax.boxplot([thety_nw,thety_mm])
plt.show()
