import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import norm, lognorm, pareto

n = 1000
U = []
for j in range(n):
    U.append(max(np.random.normal(0,1,1000)))


def u_norm_pdf(n,mi,sigma,x):
    return (n*(norm.cdf(x,mi,sigma))**(n-1))*((1/np.sqrt(2*np.pi)*sigma)*np.exp(-((x-mi)**2)/2*sigma**2))

def u_norm_cdf(n,mi,sigma,x):
    return (norm.cdf(x,mi,sigma))**n


xs = np.linspace(0,5,1000)
plt.title("Rozklad Normalny")
plt.plot(xs,u_norm_pdf(n,0,1,xs),label="gest teor")
sns.kdeplot(U,label="gest empir")
plt.legend()
plt.show()

plt.title("Rokzlad normalny")
plt.plot(xs,u_norm_cdf(n,0,1,xs),label="dyst teor")
sns.ecdfplot(U,label="dyst empir")
plt.legend()
plt.show()

U1 = []
for j in range(n):
    U1.append(max(np.random.lognormal(0,1,1000)))

def u_log_pdf(n,mi,sigma,x):
    return n*(1/((2*np.pi)**(1/2)*sigma*x))*np.exp((-(np.log(x)-mi)**2)/(2*sigma**2))*(norm.cdf((np.log(x)-mi)/sigma))**(n-1)

def u_log_cdf(n,mi,sigma,x):
    return (norm.cdf(np.log(x),mi,sigma))**n



xs1 = np.linspace(0,120,1000)
plt.title("Rozklad lognormalny")
plt.plot(xs1,u_log_pdf(n,0,1,xs1),label="gest teor")
sns.kdeplot(U1,label="gest empir")
plt.legend()
plt.show()

plt.title("Rozklad lognormalny")
plt.plot(xs1,u_log_cdf(n,0,1,xs1),label="dyst teor")
sns.ecdfplot(U1,label="dyst empir")
plt.legend()
plt.show()

import random
def pareto_simulation(sample, alpha = 6, lambd = 2):
    us = []
    for i in range(sample):
        us.append(random.random())
    return [lambd * ((1-u)**(-1/alpha) - 1) for u in us]
U2 = []
for j in range(n):
    U2.append(max(pareto_simulation(1000)))

def u_par_pdf(n,lambd,alpha,x):
    return n*(1 - (lambd/(lambd + x))**alpha)**(n-1)*(alpha*(lambd**alpha))/(lambd+x)**(alpha+1)

def u_par_cdf(n,lambd,alpha,x):
    return (1 - (lambd/(lambd + x))**alpha)**n



xs2 = np.linspace(0,20,1000)
plt.title("Rozklad Pareto")
plt.plot(xs2,u_par_pdf(n,2,6,xs2),label="gest teor")
sns.kdeplot(U2,label="gest empir")
plt.legend()
plt.show()

plt.title("Rozklad Pareto")
plt.plot(xs2,u_par_cdf(n,2,6,xs2),label="dyst teor")
sns.ecdfplot(U2,label="dyst empi")
plt.legend()
plt.show()