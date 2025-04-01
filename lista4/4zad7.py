import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

theta = 2
X = np.random.exponential(1,1000)
Y = X + theta

xs = np.linspace(2,10,1000)
teor = 1-np.exp(theta-xs)
sns.ecdfplot(Y,label="dyst empir")
plt.plot(xs,teor,label="dyst teor")
plt.legend()
plt.show()