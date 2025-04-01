import csv
import matplotlib.pyplot as plt

rows = []
with open("/Users/wojtek/Desktop/Statystyka_stosowana_semestr_4/quakes.csv", 'r') as file:
    csvreader = csv.reader(file)
    header = next(csvreader)
    for row in csvreader:
        rows.append(float(row[4]))
#print(rows)

#plt.boxplot(rows)
#plt.show()
f = 'x y š'
for k in f:
    if k == 'š':
        f.replace(k,'s')
print(f)