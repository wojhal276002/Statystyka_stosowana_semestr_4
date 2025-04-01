import requests
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import math
from scipy import stats
import numpy as np
import seaborn as sns

alfa=0.05
sigma = np.sqrt(20)

response = requests.get("http://prac.im.pwr.edu.pl/~wyloman/ss_2023_2024/lista6_zad5.txt")
soup = BeautifulSoup(response.content, 'html.parser')
str = (str(soup)).split()
str1 = [float(i) for i in str]
#mi znane, sigma nieznane
przedzial1, przedzial2 = -1*stats.norm.ppf(1-alfa/2)*sigma/np.sqrt(len(str1))+sum(str1)/len(str1),stats.norm.ppf(1-alfa/2)*sigma/np.sqrt(len(str1))+sum(str1)/len(str1)
print(przedzial1,przedzial2,'\n')
#mi nieznane, sigma nieznane
przedzial3,przedzial4 = sum(str1)/len(str1)-stats.t.ppf(1-alfa/2,len(str1)-1)*np.std(str1)/np.sqrt(len(str1)),sum(str1)/len(str1)+stats.t.ppf(1-alfa/2,len(str1)-1)*np.std(str1)/np.sqrt(len(str1))
print(przedzial3,przedzial4,'\n')
#mi nieznane, sigma nieznane
przedzial5,przedzial6 = ((len(str1)-1)*np.std(str1)**2)/stats.chi2.ppf(1-alfa/2,len(str1)-1),((len(str1)-1)*np.std(str1)**2)/stats.chi2.ppf(alfa/2,len(str1)-1)
print(przedzial5,przedzial6)