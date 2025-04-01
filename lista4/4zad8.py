import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

mi = 0
sigma = 1
n = 1000
def mediana(wekt_1):
    wekt = sorted(wekt_1)
    if len(wekt)%2 == 0:
        return (wekt[(len(wekt)//2)-1]+wekt[(len(wekt)//2)])/2
    else:
        return wekt[(len(wekt))//2]

mi1s = []
mi2s = []
e1s = []
e2s = []
for i in range(100):
    X = np.random.normal(mi,sigma,2*n+1)
    mi_1 = (1/(2*n+1))*sum(X)
    mi_2 = mediana(X)
    e_1 = (mi_1-mi)**2
    e_2 = (mi_2-mi)**2
    mi1s.append(mi_1)
    mi2s.append(mi_2)
    e1s.append(e_1)
    e2s.append(e_2)

plt.boxplot(mi1s)
plt.show()

plt.boxplot(mi2s)
plt.show()

print("e_1",sum(e1s)/len(e1s),"\n","e_2",sum(e2s)/len(e2s))


