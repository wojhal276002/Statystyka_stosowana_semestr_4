import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import scipy 

mi = 1
sigma_2 = np.sqrt(2)
n = 1000

X = []
theta_1 = []
theta_2 =[]
for n in range(1000):
    X.append(np.random.normal(mi,sigma_2,7))

for c in X:
    theta_1.append(sum(c)/len(c))
    theta_2.append((2*c[0]-c[5]+c[3])/2)

xs = np.linspace(-5,5,1000)
plt.plot(xs,scipy.stats.norm.cdf(xs,1,np.sqrt(sigma_2**2/7)),label="theta_1 teor")
sns.ecdfplot(theta_1, label="theta_1 empir")
plt.plot(xs,scipy.stats.norm.cdf(xs,1,np.sqrt(3*(sigma_2)**2/2)), label="theta_2 teor")
sns.ecdfplot(theta_2, label="theta_2 empir")
plt.legend()
plt.show()