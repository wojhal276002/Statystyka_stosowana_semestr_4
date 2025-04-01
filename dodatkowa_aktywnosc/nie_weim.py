import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def ziggurat(f, g, k,x_0, x_k, n, c):
    xs = np.linspace(x_0, x_k, k)
    samples = []
    f_min = []
    f_max = []
    for i in range(k-1):
        f_min.append(min([f(j) for j in np.linspace(xs[i], xs[i+1], 10**3)]))
        f_max.append(max([f(j) for j in np.linspace(xs[i], xs[i+1], 10**3)]))
    while len(samples) < n:
        u = np.random.uniform()
        x = np.random.uniform(x_0, x_k)
        ind = 0
        for i in range(k-1):
            if xs[i] <= x <= xs[i+1]:
                ind = i
        if ind != 0:
            if u*c*g(x) < f_min[ind]:
                samples.append(x)
            elif u*c*g(x) > f_max[ind]:
                continue
            else:
                if u*c*g(x) < f(x):
                    samples.append(x)
    return samples
def exp_cdf(x):
    return np.exp(-x)	
def normal_cdf(x):
    return np.exp(-x**2/2)/np.sqrt(2*np.pi)
samples = ziggurat(normal_cdf, lambda x: 1 / np.sqrt(2 * np.pi), 100, -4, 4, 10000, 1)
xs = np.linspace(-5,5, 100)
plt.hist(samples, density=True, bins=50)
plt.plot(xs, norm.pdf(xs, 0, 1), label="gęstość teoretyczna")
plt.title("Porównanie unormowanego histogramu z gęstością rozkładu standardowego normalnego")
plt.legend(loc='best')
plt.show()