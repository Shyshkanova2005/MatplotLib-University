import matplotlib.pyplot as plt
import numpy as np

a1, b1, c1 = 13.1, 9.2, 173
a2, b2, c2 = 8.3, 21, 271
a3, b3, c3 = 3.2, -8.3, 34

def solve_system(a1, b1, c1, a2, b2, c2):
    A = np.array([[a1, b1], [a2, b2]])
    B = np.array([c1,c2])
    x, y = np.linalg.solve(A, B)
    return x,y

x1,y1 = solve_system(a1, b1, c1, a2, b2, c2)
x2,y2 = solve_system(a1, b1, c1, a3, b3, c3 )
x3,y3 = solve_system( a2, b2, c2, a3, b3, c3)

x_vals = np.linspace(-100, 100, 400)
y_vals1 = (c1 - a1 * x_vals) / b1
y_vals2 = (c2 - a2 * x_vals) / b2
y_vals3 = (c3 - a3 * x_vals) / b3


plt.plot(x_vals, y_vals1, label='f[0]', color='red', linestyle='--')
plt.plot(x_vals, y_vals2, label='f[1]', color='black', linestyle=':')
plt.plot(x_vals, y_vals3, label='f[2]', color='magenta', linestyle='-.')


plt.scatter(x1, y1, color='blue', zorder=5)
plt.scatter(x2, y2, color='red', zorder=5)
plt.scatter(x3, y3, color='green', zorder=5)

polygon = np.array([[x1, y1], [x2, y2], [x3, y3]])
plt.fill(polygon[:, 0], polygon[:, 1], color='gray', alpha=0.7)


plt.annotate('The intersection point of f[0] and f[1]', 
             xy=(x1, y1), xytext=(x1 + 10, y1 + 90),
             arrowprops=dict(facecolor='black', arrowstyle="->", linewidth=1, edgecolor='black'),
             fontsize=9, color='black')

plt.annotate('The intersection point of f[0] and f[2]', 
             xy=(x2, y2), xytext=(x2 + 10, y2 - 70), 
             arrowprops=dict(facecolor='black', arrowstyle="->", linewidth=1, edgecolor='black'),
             fontsize=9, color='black', ha='right')

plt.annotate('The intersection point of f[1] and f[2]', 
             xy=(x3, y3), xytext=(x3 - 3, y3 - 90),  
             arrowprops=dict(facecolor='black', arrowstyle="->", linewidth=1, edgecolor='black'),
             fontsize=9, color='black')

plt.text(-76, 76, '$13.1x_1  + 9.2x_2 = 173$', fontsize=9, rotation=-38, color='black')
plt.text(-78, 30, '$8.3x_1  + 21x_2 = 271$', fontsize=9, rotation=-15, color='black')
plt.text(45, 19, '$3.2x_1  - 8.3x_2 = 34$', fontsize=9, rotation=10, color='black')


plt.title("All lines in one figure")
plt.xlabel('$x_1$')
plt.ylabel('$x_2$')
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(True)
plt.legend()
plt.show()