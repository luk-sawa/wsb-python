import matplotlib.pyplot as plt
import pylab as p
import random


names = p.arange(0, 12, 1)
values1 = []
values2 = []
for name in names:
    values1.append(round(random.uniform(0, 1), 2))
    values2.append(round(random.uniform(0, -1), 2))
plt.figure(1, figsize=(9, 3))
plt.bar(names, values1)
plt.bar(names, values2)
plt.show()
