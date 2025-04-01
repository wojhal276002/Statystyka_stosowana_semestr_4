import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

a = 2
n = 1000
alista_mm = []
alista_nw = []
for i in range(1000):
    X = []
    for p in range(n):
        X.append(np.random.uniform(0,1))
    Y = [x**(1/(a+1)) for x in X]
    a_nw = (-n/sum(np.log(Y))) - 1
    a_mm = ((1-2*(1/n)*sum(Y))/((1/n)*sum(Y)-1))
    alista_mm.append(a_mm)
    alista_nw.append(a_nw)

fig, ax = plt.subplots()
ax.boxplot([alista_nw,alista_mm])
plt.show()
