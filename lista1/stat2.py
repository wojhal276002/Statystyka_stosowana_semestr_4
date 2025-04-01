import requests
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import math
from scipy.stats import norm, lognorm, pareto
import numpy as np
import seaborn as sns

response = requests.get("http://prac.im.pwr.edu.pl/~wyloman/ss_2023_2024/dane_lista1.txt")
soup = BeautifulSoup(response.content, 'html.parser')
str = (str(soup)).split()
str1 = [float(i) for i in str]

x_var = range(1,1001)
y_var = [math.exp(float(i)) for i in str]

fig, (ax1,ax2) = plt.subplots(1, 2)
fig.set_figheight(5)
fig.set_figwidth(12)
xs1 = np.linspace(-3,3,1000)
xs2 = np.linspace(0,12,1000)

ax1.plot(xs1, norm.pdf(xs1))

ax2.plot(xs2, norm.pdf(xs2))
sns.kdeplot(xs1)
sns.kdeplot(xs2)
plt.show()
