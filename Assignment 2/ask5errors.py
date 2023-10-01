import numpy as np
from math import sqrt
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


def cubic_interp1d(x0, x, y):
    """
    Interpolate a 1-D function using cubic splines.
      x0 : a float or an 1d-array
      x : (N,) array_like
          A 1-D array of real/complex values.
      y : (N,) array_like
          A 1-D array of real values. The length of y along the
          interpolation axis must be equal to the length of x.

    Implement a trick to generate at first step the cholesky matrice L of
    the tridiagonal matrice A (thus L is a bidiagonal matrice that
    can be solved in two distinct loops).

    additional ref: www.math.uh.edu/~jingqiu/math4364/spline.pdf
    """
    x = np.asfarray(x)
    y = np.asfarray(y)

    # remove non finite values
    # indexes = np.isfinite(x)
    # x = x[indexes]
    # y = y[indexes]

    # check if sorted
    if np.any(np.diff(x) < 0):
        indexes = np.argsort(x)
        x = x[indexes]
        y = y[indexes]

    size = len(x)

    xdiff = np.diff(x)
    ydiff = np.diff(y)

    # allocate buffer matrices
    Li = np.empty(size)
    Li_1 = np.empty(size-1)
    z = np.empty(size)

    # fill diagonals Li and Li-1 and solve [L][y] = [B]
    Li[0] = sqrt(2*xdiff[0])
    Li_1[0] = 0.0
    B0 = 0.0 # natural boundary
    z[0] = B0 / Li[0]

    for i in range(1, size-1, 1):
        Li_1[i] = xdiff[i-1] / Li[i-1]
        Li[i] = sqrt(2*(xdiff[i-1]+xdiff[i]) - Li_1[i-1] * Li_1[i-1])
        Bi = 6*(ydiff[i]/xdiff[i] - ydiff[i-1]/xdiff[i-1])
        z[i] = (Bi - Li_1[i-1]*z[i-1])/Li[i]

    i = size - 1
    Li_1[i-1] = xdiff[-1] / Li[i-1]
    Li[i] = sqrt(2*xdiff[-1] - Li_1[i-1] * Li_1[i-1])
    Bi = 0.0 # natural boundary
    z[i] = (Bi - Li_1[i-1]*z[i-1])/Li[i]

    # solve [L.T][x] = [y]
    i = size-1
    z[i] = z[i] / Li[i]
    for i in range(size-2, -1, -1):
        z[i] = (z[i] - Li_1[i-1]*z[i+1])/Li[i]

    # find index
    index = x.searchsorted(x0)
    np.clip(index, 1, size-1, index)

    xi1, xi0 = x[index], x[index-1]
    yi1, yi0 = y[index], y[index-1]
    zi1, zi0 = z[index], z[index-1]
    hi1 = xi1 - xi0

    # calculate cubic
    f0 = zi0/(6*hi1)*(xi1-x0)**3 + \
         zi1/(6*hi1)*(x0-xi0)**3 + \
         (yi1/hi1 - zi1*hi1/6)*(x0-xi0) + \
         (yi0/hi1 - zi0*hi1/6)*(xi1-x0)
    return f0


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
    r = b - np.matmul(A, x)
    return form(x[0], x[1], x[2], x[3], t)


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


plt.title('Interpolation Error')
plt.xlabel('x')
plt.ylabel('error')

x_axis = np.linspace(-np.pi, np.pi, 200)
y_axis = [0.0 for i in range(200)]
#---------------------------
for i in range(200):
    y_axis[i] = abs(np.sin(x_axis[i]) - lagrange_interpolation(x_axis[i]))
plt.plot(x_axis, y_axis, label='Polynomial')
#---------------------------
plt.plot(x_axis, abs(np.sin(x_axis)-cubic_interp1d(x_axis, x, y)), label='Splines')
#---------------------------
for i in range(200):
    y_axis[i] = abs(np.sin(x_axis[i]) - least_squares(A, b, x_axis[i]))
plt.plot(x_axis, y_axis, label='Least Squares')
#---------------------------
plt.legend()
plt.show()


