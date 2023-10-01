import numpy as np

tolerance = 0.5 * 10e-5


# ορίζω τη συνάρτηση f
def f(x):
    return 14*x*np.exp(x-2) - 12*np.exp(x-2) - 7*(x**3) + 20*(x**2) - 26*x + 12


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

        c = (a+b)/2

        i += 1

    print('--------------------------------------------------------------------------')
    print('Root found: ' + str(c))
    print('Root found: ' + '%7.5f' % c)


bisection_method(0, 1.1)
print('\n')
bisection_method(1.1, 3)
