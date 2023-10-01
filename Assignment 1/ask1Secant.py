import numpy as np

tolerance = 0.5 * 10e-5


# ορίζω τη συνάρτηση f
def f(x):
    return 14 * x * np.exp(x - 2) - 12 * np.exp(x - 2) - 7 * (x ** 3) + 20 * (x ** 2) - 26 * x + 12


def secant_method(a, b):
    if f(a)*f(b) >= 0:
        print('Cannot find root')
        return

    x0 = a
    x1 = b

    print('--------------------------------------------------------------------------')
    print('iter \t\t x2 \t\t x1 \t\t x0 \t\t f(x1)')
    print('--------------------------------------------------------------------------')

    i = 0
    while True:
        x2 = x1 - ((f(x1)*(x1-x0))/(f(x1)-f(x0)))

        print(str(i + 1) + '\t\t% 10.8f\t% 10.8f\t% 10.8f\t% 10.8f\t' % (x2, x1, x0, f(x2)))

        if np.abs(x2 - x1) < tolerance:
            break

        x0 = x1
        x1 = x2

        i += 1

    print('--------------------------------------------------------------------------')
    print('Root found : ' + str(x2))
    print('Root found: ' + '%7.5f' % x2)


secant_method(0, 1.1)
print('\n')
secant_method(1.1, 3)
