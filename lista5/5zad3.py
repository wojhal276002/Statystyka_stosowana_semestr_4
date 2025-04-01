import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import scipy 

alfa = 1
beta = 2

alfa_daszek = []
beta_daszek = []
for i in range(10):
    daszki_a = []
    daszki_b = []
    for c in range(1000):
        n = 1000*(i+1)
        X = np.random.gamma(alfa,1/beta,n)
        daszki_a.append((((1/n)*(sum(X)))**2)/((1/n)*sum(X**2)-((1/n)*(sum(X)))**2))
        daszki_b.append(((1/n)*(sum(X)))/((1/n)*sum(X**2)-((1/n)*(sum(X)))**2))
    alfa_daszek.append(daszki_a)
    beta_daszek.append(daszki_b)

xs = np.linspace(1,10,1000)
plt.plot(xs,[alfa]*1000,label="wartość teoretyczna alfa")
plt.boxplot(alfa_daszek)
plt.legend()
plt.show()

plt.plot(xs,[beta]*1000,label="wartość teoretyczna beta")
plt.boxplot(beta_daszek)
plt.legend()
plt.show()
