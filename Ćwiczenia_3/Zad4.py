import matplotlib.pyplot as plt
import pylab as p


x1 = p.arange(0, 50, 1)
x2 = p.arange(0, 100, 5)
x3 = p.arange(0, 30, 5)
y1 = 6*x1
y2 = x2
y3 = x3*x3
plt.plot(x1, y1, ls='--', color="green", label="6x")
plt.plot(x2, y2, color="red", marker='+', label="x")
plt.plot(x3, y3, ls=':', color="blue", label="x^2")
plt.legend(loc='upper left')
plt.title("Wykres funkcji")
plt.xlabel("Oś x")
plt.ylabel("Oś y")
plt.grid(True)
plt.show()
