import numpy as np

tolerance = 0.5 * 10e-5


# ορίζω τη συνάρτηση f
def f(x):
    return 14 * x * np.exp(x - 2) - 12 * np.exp(x - 2) - 7 * (x ** 3) + 20 * (x ** 2) - 26 * x + 12


# ορίζω την 1η παράγωγο της συνάρτησης f
def f_deriv(x):
    return 14 * x * np.exp(x - 2) + 2 * np.exp(x - 2) - 21 * (x ** 2) + 40 * x - 26


# ορίζω την 2η παράγωγο της συνάρτησης f
def f_2nd_deriv(x):
    return 14 * x * np.exp(x - 2) + 16 * np.exp(x - 2) - 42 * x + 40


def newton_raphson_method(a, b):
    if f(a)*f(b) >= 0:
        print('Cannot find root')
        return

    if f(a) * f_2nd_deriv(a) > 0:
        x0 = a
    elif f(b) * f_2nd_deriv(b) > 0:
        x0 = b

    print('--------------------------------------------------------------------------')
    print('iter \t\t x1 \t\t x0 \t\t f(x1)')
    print('--------------------------------------------------------------------------')

    i = 0
    while True:
        x1 = x0 - (f(x0)/f_deriv(x0))

        print(str(i + 1) + '\t\t% 10.8f\t% 10.8f\t% 10.8f\t' % (x1, x0, f(x1)))

        if np.abs(x1 - x0) < tolerance:
            break

        x0 = x1

        i += 1

    print('--------------------------------------------------------------------------')
    print('Root found : ' + str(x1))
    print('Root found: ' + '%7.5f' % x1)


newton_raphson_method(0, 1.1)
print('\n')
newton_raphson_method(1.1, 3)
