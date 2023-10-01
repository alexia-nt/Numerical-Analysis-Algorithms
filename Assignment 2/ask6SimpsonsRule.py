import numpy as np

#n πλήθος υποδιαστημάτων, n+1 σημεία


def f(x):
    #y = np.exp(-x**2)
    y = np.sin(x)
    return y


def simpsons_rule(a, b, n):
    x = np.linspace(a, b, n+1)

    sum1 = 0
    for i in range(1, int(n/2)):
        sum1 = sum1 + f(x[2*i])

    sum2 = 0
    for i in range(1, int(n/2)+1):
        sum2 = sum2 + f(x[2*i-1])

    approx = ((b-a)/(3*n)) * (f(x[0]) + f(x[n]) + 2*sum1 + 4*sum2)
    return approx


def error_bound(a, b, n, max):
    error = ((b-a)**5/(180*(n**4)))*max
    return error


approx = simpsons_rule(0, np.pi/2, 10)
print("approx =", approx)

e = error_bound(0, np.pi/2, 10, 1)
print("error bound =", e)

print("error =", abs(1-approx))

