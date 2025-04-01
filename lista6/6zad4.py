import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats

n = 1000
alfa = 0.02
kwantyl = 0.8389
sigma = 0.2
mi = 2.1
t20 = stats.t.ppf(1-0.01,20)
t50 =stats.t.ppf(1-0.01,50)
t100 = stats.t.ppf(1-0.01,100)
zn20 = 0
zn50 = 0
zn100 = 0
nzn20 = 0
nzn50 = 0
nzn100 = 0
for i in range(n):
    lista20 = np.random.normal(2.1,0.2,20)
    lista50 = np.random.normal(2.1,0.2,50)
    lista100 = np.random.normal(2.1,0.2,100)
    srednia20 = sum(lista20)/len(lista20)
    srednia50 = sum(lista50)/len(lista50)
    srednia100 = sum(lista100)/len(lista100)
    if srednia20-kwantyl*(sigma/np.sqrt(20))<=mi<=srednia20+kwantyl*(sigma/np.sqrt(20)):
        zn20+=1
    if srednia50-kwantyl*(sigma/np.sqrt(50))<=mi<=srednia50+kwantyl*(sigma/np.sqrt(50)):
        zn50+=1
    if srednia100-kwantyl*sigma/np.sqrt(100)<=mi<=srednia100+kwantyl*sigma/np.sqrt(100):
        zn100+=1
    if srednia20-t20*np.std(lista20)/np.sqrt(20)<=mi<=srednia20+t20*np.std(lista20)/np.sqrt(20):
        nzn20+=1
    if srednia50-t50*np.std(lista50)/np.sqrt(50)<=mi<=srednia50+t50*np.std(lista50)/np.sqrt(50):
        nzn50+=1
    if srednia100-t100*np.std(lista100)/np.sqrt(100)<=mi<=srednia100+t100*np.std(lista100)/np.sqrt(100):
        nzn100+=1

print(zn20,
zn50,
zn100 ,
nzn20 ,
nzn50,
nzn100)