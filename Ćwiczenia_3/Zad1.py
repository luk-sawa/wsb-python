import matplotlib.pyplot as plt
import pylab as p


a = int(input("Podaj a = "))
b = int(input("Podaj b = "))
x = p.arange(-10, 10)
y = a*x+b
plt.plot(x,y)
plt.title("Wykres f(x) = a*x + b")
plt.legend(["Funkcja liniowa"])
plt.grid(True)
ax = plt.gca()
ax.spines['bottom'].set_position(('data', 0))
ax.spines['left'].set_position(('data', 0))
if (a*1+b)-(a*2+b) < 0:
    plt.text(2, 2, 'Funkcja rosnąca')
elif (a*1+b)-(a*2+b) > 0:
    plt.text(2, 2, 'Funkcja malejąca')
elif (a*1+b)-(a*2+b) == 0:
    plt.text(2, 2, 'Funkcja stała')
plt.show()
