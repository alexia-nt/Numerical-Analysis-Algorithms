import numpy as np
import matplotlib.pyplot as plt


def form(a, b, c, d, t):
    y = a + b*t + c*(t**2) + d*(t**3)
    return y


# υπολογισμός 2ης νόρμας διανύσματος
def norm2(x):
    n = len(x)
    sum = 0
    for i in range(n):
        sum = sum + x[i]**2
    norm = np.sqrt(sum)
    return norm


def least_squares(A, b, t):
    AT_A = np.matmul(AT, A)
    AT_b = np.matmul(AT, b)
    x = np.linalg.solve(AT_A, AT_b)

    new_b = np.matmul(A, x)
    r = b - np.matmul(A, x)
    norm = norm2(r)

    return form(x[0], x[1], x[2], x[3], t)


x = [-3, -2.7, -2.1, -1.2, -0.4, 0, 0.9, 1.4, 2.5, 3.1]

A = [[0.0]*4 for i in range(10)]
for i in range(10):
    for j in range(4):
        if j == 0:
            A[i][j] = 1.0
        elif j == 1:
            A[i][j] = x[i]
        elif j == 2:
            A[i][j] = x[i]**2
        else:
            A[i][j] = x[i]**3

A = np.array(A)
AT = np.transpose(A)

b = [-0.1411, -0.4274, -0.8632, -0.9320, -0.3894, 0, 0.7833, 0.9854, 0.5985, 0.0416]
b = np.array(b)

x_axis = np.linspace(-np.pi, np.pi, 200)

y_axis = [0.0 for i in range(200)]
for i in range(200):
    y_axis[i] = abs(np.sin(x_axis[i]) - least_squares(A, b, x_axis[i]))

plt.title('Least Squares Interpolation Error')
plt.xlabel('x')
plt.ylabel('error')

plt.plot(x_axis, y_axis)
plt.show()

approx = least_squares(A, b, 3)
print("approx of sin(2)=", approx)
print("sin(2)=", np.sin(3))
