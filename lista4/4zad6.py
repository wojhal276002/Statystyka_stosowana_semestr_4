import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

alfa = 4
x_0 = 1
n = 1000

def pareto(alfa,x_0):
    X = np.random.uniform(0,1,1000)
    return x_0*((1-X)**(-1/alfa))

alfy = []
x_zera = []
for c in range(1000):
    X = pareto(alfa,x_0)
    x0_sr = min(X)
    alfa_sr = n/sum(np.log(X)-n*np.log(x_0))
    x_zera.append(x0_sr)
    alfy.append(alfa_sr)


plt.boxplot(x_zera)
plt.show()
print(alfy)
plt.boxplot(alfy)
plt.show()


        