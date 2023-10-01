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

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

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

b = [55137.31, 55937.51, 55950.75, 57750.20, 58917.69, 58918.83, 59095.81, 59384.31, 57603.89, 58758.55]
b = np.array(b)

plt.title('Least Squares for BTC (3rd degree polynomial)')
plt.xlabel('x')
plt.ylabel('Close price')

x_axis = np.linspace(1, 15, 100)

y_axis = [0.0 for i in range(100)]
for i in range(100):
    y_axis[i] = least_squares(A, b, x_axis[i])

plt.plot(x_axis, y_axis)
plt.scatter(x, b)

x2 = [11, 12, 13, 14, 15]
y2 = [0.0 for i in range(5)]
for i in range(5):
    y2[i] = least_squares(A, b, x2[i])
plt.scatter(x2, y2)

plt.show()

for i in range(1, 16):
    print("approx", i, "=", least_squares(A, b, i))
