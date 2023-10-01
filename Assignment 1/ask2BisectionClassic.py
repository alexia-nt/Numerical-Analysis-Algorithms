import numpy as np

tolerance = 0.5 * 10e-5


# ορίζω τη συνάρτηση f
def f(x):
    return 54*(x**6) + 45*(x**5) - 102*(x**4) - 69*(x**3) + 35*(x**2) + 16*x - 4


def bisection_method(a, b):
    if f(a)*f(b) >= 0:
        print('Cannot find root')
        return

    print('--------------------------------------------------------------------------')
    print('iter \t\t a \t\t\t b \t\t\t c \t\t\t f(c)')
    print('--------------------------------------------------------------------------')

    c = (a+b)/2

    i = 0
    while (b-a)/2 >= tolerance:
        print(str(i + 1) + '\t\t% 10.8f\t% 10.8f\t% 10.8f\t% 10.8f\t' % (a, b, c, f(c)))

        if f(a) * f(c) < 0:
            b = c
        else:
            a = c

        c = (a + b) / 2

        i += 1

    print('--------------------------------------------------------------------------')
    print('Root found: ' + str(c))
    print('Root found: ' + '%7.5f' % c)


bisection_method(-2, -1)  # -1.381

bisection_method(-1, 0)  # -0.667 cannot find root

bisection_method(0, 0.4)  # 0.205

bisection_method(0.4, 0.7)  # 0.5

bisection_method(0.7, 2)  # 1.176
