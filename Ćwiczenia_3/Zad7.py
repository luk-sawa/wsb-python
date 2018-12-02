import matplotlib.pyplot as plt
import pylab as p
import numpy as np

t1 = p.arange(0, 5, 0.1)
t2 = p.arange(0, 2, 0.05)
x1 = np.cos(2*np.pi*t1)*np.exp(-t1)
x2 = np.cos(2*np.pi*t2)
plt.subplot(2, 1, 1)
plt.plot(t1, x1, marker='.')
plt.ylabel("Oscylacja tłumiona")
plt.subplot(2, 1, 2)
plt.plot(t2, x2, marker='.')
plt.ylabel("Oscylacja harmoniczna")
plt.xlabel("Czas (s)")
plt.show()
