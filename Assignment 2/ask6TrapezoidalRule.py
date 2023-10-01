import numpy as np

#n πλήθος υποδιαστημάτων, n+1 σημεία


def f(x):
    y = np.sin(x)
    return y


def trapezoidal_rule(a, b, n):
    x = np.linspace(a, b, n+1)

    sum = 0
    for i in range(1, n):
        sum = sum + f(x[i])
    approx = ((b-a)/(2*n)) * (f(x[0]) + f(x[n]) + 2*sum)
    return approx


def error_bound(a, b, n, max):
    error = ((b - a) ** 3 / (12 * (n ** 2))) * max
    return error


approx = trapezoidal_rule(0, np.pi/2, 10)
print("approx =", approx)

e = error_bound(0, np.pi/2, 10, 1)
print("error bound =", e)

print("error =", abs(1-approx))
