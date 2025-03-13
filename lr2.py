import matplotlib.pyplot as plt
import numpy as np

x1 = np.linspace(1, 10, 1000)
x2 = np.linspace(0.1, 10, 1000)

y1 = x1 ** np.sin(10*x1)
y2 = np.cos(10*x2) * np.sin(3*x2)/(x2**(1/2))

plt.title("Графік функцій")
plt.xlabel("x")
plt.ylabel("Y(x)")
plt.grid()
plt.plot(x1, y1, label=r'$Y(x) = x^{\sin(10x)}$', color='r')
plt.plot(x2, y2, label=r'$Y(x) = \frac{\cos(10x) \sin(3x)}{x^{1/2}}$', color='b')
plt.show()

