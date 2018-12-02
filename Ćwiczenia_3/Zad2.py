import matplotlib.pyplot as plt
import pylab as p


a = int(input("Podaj a = "))
x1 = p.arange(-10, 0, 0.5)
x2 = p.arange(0, 10, 0.5)
y1 = x1 / (-3) + a
y2 = x2 * x2 / 3
plt.plot(x1, y1, label="x/(-3)+a")
plt.plot(x2, y2, label="x^2/3")
plt.legend(loc='upper left')
plt.title("Wykres funkcji")
plt.xlabel("Oś x")
plt.ylabel("Oś y")
plt.grid(True)
ax = plt.gca()
ax.spines['bottom'].set_position(('data', 0))
ax.spines['left'].set_position(('data', 0))
plt.show()
