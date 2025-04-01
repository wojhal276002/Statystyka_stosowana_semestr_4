import random
import math
import numpy
import matplotlib.pyplot as plt

N_range = range(50,2000,50)
N = [i for i in range(50,2000,50)]
print(N)

srednie = []
for c in N:
    srednia_diff = 0
    for i in range(100):
        x = numpy.random.normal(2,3,c)
        suma = 0
        for w in x:
            suma += abs(w-2)
        emp = suma/len(x)
        teo = math.sqrt(2/math.pi)*3
        diff = abs(emp-teo)
        srednia_diff += diff
    srednie_wart = srednia_diff/100
    srednie.append(srednie_wart)

plt.scatter(N_range, srednie)
plt.show()
