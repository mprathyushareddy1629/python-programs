import matplotlib.pyplot as plt
import csv

x = []
y = []

with open('example.csv') as csvfile:
    plots = csv.reader(csvfile)
    for row in plots:
        x.append(int(row[0]))
        y.append(int(row[1]))

plt.plot(x,y,color='green', linestyle='dashed')
plt.xlabel('x')
plt.ylabel('y')
plt.show()