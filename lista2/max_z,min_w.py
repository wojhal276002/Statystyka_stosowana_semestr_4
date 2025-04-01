import numpy as np
import matplotlib.pyplot as plt
import math
import seaborn as sns

lambd_1 = 2
lambd_2 = 1

xs = np.linspace(0,5,1000)
X = np.random.exponential(0.5,1000)
Y = np.random.exponential(1,1000)
def Z(X,Y):
    lista_empir_z = []
    for i in range(1000):
        lista_empir_z.append(max(X[i],Y[i]))
    return lista_empir_z

def W(X,Y):
    lista_empir_w = []
    for i in range(1000):
        lista_empir_w.append(min(X[i],Y[i]))
    return lista_empir_w

def gest_teor_z(xs):
    lista_teor_z = []
    for i in xs:
        lista_teor_z.append(2*math.exp(-2*i)+math.exp(-i)-3*math.exp(-3*i))
    return lista_teor_z

def gest_teor_w(xs):
    lista_teor_w = []
    for i in xs:
        lista_teor_w.append(3*math.exp(-3*i))
    return lista_teor_w

def dyst_teor_z(xs):
    lista_teor_z = []
    for i in xs:
        lista_teor_z.append(1-math.exp(-2*i)-math.exp(-i)+math.exp(-3*i))
    return lista_teor_z

def dyst_teor_w(xs):
    lista_teor_w = []
    for i in xs:
        lista_teor_w.append(1-math.exp(-3*i))
    return lista_teor_w


e_z = Z(X,Y)
e_w = W(X,Y)
gest_t_z = gest_teor_z(xs)
gest_t_w = gest_teor_w(xs)
dyst_t_z = dyst_teor_z(xs)
dyst_t_w = dyst_teor_w(xs)

#gestosc_z
plt.plot(xs,gest_t_z,label="gestosc teoretyczna z")
sns.kdeplot(e_z,label="gestosc empiryczna z")
plt.legend()
plt.show()

#gestosc_w
plt.plot(xs,gest_t_w, label="gestosc teoretyczna w")
sns.kdeplot(e_w, label="gestosc empiryczna w")
plt.legend()
plt.show()

#dystrybuanta_z
plt.plot(xs,dyst_t_z, label="dystrybuanta teoretyczna z")
sns.ecdfplot(e_z,label="dystrybuanta empieyczna z")
plt.legend()
plt.show()

#dystrybuanta_w
plt.plot(xs,dyst_t_w, label="dystrybuanta teoretyczna w")
sns.ecdfplot(e_w,label="dystrybuanta empiryczna w")
plt.legend()
plt.show()
