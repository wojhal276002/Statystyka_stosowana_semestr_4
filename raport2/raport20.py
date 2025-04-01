import requests
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import math
from scipy import stats
import numpy as np
import seaborn as sns


mi = 0.2
#N(0.2,sigma^2)
alfa = 0.05
response = requests.get("http://prac.im.pwr.edu.pl/~wyloman/ss_2023_2024/lista8_zad2.txt")
soup = BeautifulSoup(response.content, 'html.parser')
str = (str(soup)).split()
str1 = [float(i) for i in str]
df = len(str1)-1
Z = (df*np.std(str1,ddof=1)**2)/1.5
p_alfa = stats.chi2.ppf(1-alfa/2,df)
l_alfa = stats.chi2.ppf(alfa/2,df)
print(p_alfa,l_alfa,Z)
krytyczny_min = np.linspace(800,l_alfa,1000)
norm_min = stats.chi2.pdf(krytyczny_min,df)
krytyczny_max = np.linspace(p_alfa,1200,1000)
norm_max = stats.chi2.pdf(krytyczny_max,df)
xs = np.linspace(800,1200,1000)
chi = stats.chi2.pdf(xs,df)
plt.plot(xs,chi)
plt.fill_between(krytyczny_min,norm_min,color="red",label="obszary krytyczne")
plt.fill_between(krytyczny_max,norm_max,color="red")
plt.grid()
plt.title("Rozkład χ2 z obszarem krytycznym dla hipotezy alternatywnej  σ^2 ≠ 1.5")
plt.axvline(Z, color='black',label="statystyka testowa")
plt.legend()
plt.show()
krytyczny_l = np.linspace(800,l_alfa,1000)
chi_l = stats.chi2.pdf(krytyczny_l,df)
plt.plot(xs,chi)
plt.fill_between(krytyczny_l,chi_l,color="red",label="obszar krytyczny")
plt.grid()
plt.title("Rozkład χ2 z obszarem krytycznym dla hipotezy alternatywnej σ^2 < 1.5")
plt.axvline(Z, color='black',label="statystyka testowa")
plt.legend()
plt.show()
krytyczny_p = np.linspace(p_alfa,1200,1000)
chi_p = stats.chi2.pdf(krytyczny_p,df)
plt.plot(xs,chi)
plt.fill_between(krytyczny_p,chi_p,color="red",label="obszar krytyczny")
plt.grid()
plt.title("Rozkład χ2 z obszarem krytycznym dla hipotezy alternatywnej σ^2 > 1.5")
plt.axvline(Z, color='black',label="statystyka testowa")
plt.legend()
plt.show()
print(stats.chi2.cdf(Z,df),1-stats.chi2.cdf(Z,df))
p_value = 2*min(stats.chi2.cdf(Z,df),1-stats.chi2.cdf(Z,df))
p_value_l = stats.chi2.cdf(Z,df)
p_value_p = 1-stats.chi2.cdf(Z,df)
print(p_value,'\n',p_value_l,'\n',p_value_p)
#kiedy zwiększymy bądź zmniejszymy poziom ufności to zmienią się obszary krytyczne i (przy odpowiedniej zmianie) mogą się zmienić 
#odrzucenia hipotez (zależność p wartości i poziomu ufności będą wyglądały inaczej)
