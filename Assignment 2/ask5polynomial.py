import numpy as np
import matplotlib.pyplot as plt

n = 10
x = [-3,      -2.7,     -2.1,   -1.2,    -0.4,    0, 0.9,    1.4,    2.5,    3.1]
y = [-0.1411, -0.4274, -0.8632, -0.9320, -0.3894, 0, 0.7833, 0.9854, 0.5985, 0.0416]


def calc_L(i, xp):
    l = 1
    for j in range(n):
        if j == i:
            continue
        l = l * ((xp-x[j]) / (x[i]-x[j]))
    return l


def lagrange_interpolation(xp):
    p = 0
    for i in range(n):
        p = p + y[i]*calc_L(i, xp)
    return p


x_axis = np.linspace(-np.pi, np.pi, 200)

y_axis = [0.0 for i in range(200)]
for i in range(200):
    y_axis[i] = abs(np.sin(x_axis[i]) - lagrange_interpolation(x_axis[i]))

plt.title('Polynomial Interpolation Error')
plt.xlabel('x')
plt.ylabel('error')

plt.ylim(0, 0.0001)

plt.plot(x_axis, y_axis)
plt.show()

xp = 2
yp = lagrange_interpolation(xp)
print("approx of sin(2) =", yp)
print("sin(2) =", np.sin(2))
