import numpy as np
import matplotlib.pyplot as plt
import math

mi = 0
sigma = 1
dlugosc = np.linspace(1000,10000,10)

lista = []
lista_var = []
for n in dlugosc:
    exponenty = []
    for i in range(1000):
        x = np.random.normal(mi,sigma,int(n))
        nowe_x = np.exp(x)
        exponenty.append(sum(nowe_x)/n)
    lista.append(exponenty)
    lista_var.append(np.var(exponenty))
teor = []
wartosc = np.exp((1/2)*(sigma**2+2*mi))
for j in range(11):
    teor.append(wartosc)
print(teor)
plt.boxplot(lista)
plt.plot(teor)
plt.show()

plt.plot(dlugosc,lista_var)
plt.show()



