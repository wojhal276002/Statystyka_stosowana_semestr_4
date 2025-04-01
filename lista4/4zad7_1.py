import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

theta = 2
n = 1000
thety = []
for i in range(1000):
    X = np.random.exponential(1,1000)
    Y = X + theta
    theta_sr = min(Y)
    thety.append(theta_sr)

plt.boxplot(thety)
plt.show()
