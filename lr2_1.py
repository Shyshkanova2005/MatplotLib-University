import matplotlib.pyplot as plt
import numpy as np

x1 = np.linspace(1, 10, 1000)
x2 = np.linspace(0.1, 10, 1000)

y1 = x1 ** np.sin(10*x1)
y2 = np.cos(10*x2) * np.sin(3*x2)/(x2**(1/2))

plt.subplot(1, 2, 1)
plt.plot(x1, y1, label='$Y(x) = x^{\sin(10x)}$', color='r')
plt.title("Y(x)=x^sin(10*x)")
plt.xlabel("x1")
plt.ylabel("Y(x1)")
plt.grid()

plt.subplot(1, 2, 2)
plt.plot(x2, y2, label='$Y(x) = \frac{\cos(10x) \sin(3x)}{x^{1/2}}$', color='b')
plt.title("Y(x)=cos(10*x)*sin(3*x)/(x^(1/2))")
plt.xlabel("x2")
plt.ylabel("Y(x2)")
plt.grid()
plt.show()



