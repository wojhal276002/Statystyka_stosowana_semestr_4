import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

lambd = 2
n =1000

box_plt = []
for i in range(1000):
    Y1,Y2 = np.random.exponential(1/lambd,1000), np.random.exponential(1/lambd,n)
    X = Y1-Y2
    lambd_sr = n/sum(np.abs(X))
    box_plt.append(lambd_sr)

print(box_plt)
plt.boxplot(box_plt)
plt.show()

