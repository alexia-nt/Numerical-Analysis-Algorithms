import numpy as np

tolerance = 0.5 * 10e-5


# ορίζω τη συνάρτηση f
def f(x):
    return 54*(x**6) + 45*(x**5) - 102*(x**4) - 69*(x**3) + 35*(x**2) + 16*x - 4


# ορίζω την 1η παράγωγο της συνάρτησης f
def f_deriv(x):
    return 324*(x**5) + 225*(x**4) - 408*(x**3) - 207*(x**2) + 70*x + 16


# ορίζω την 2η παράγωγο της συνάρτησης f
def f_2nd_deriv(x):
    return 1620*(x**4) + 900*(x**3) - 1224*(x**2) - 414*x + 70


def newton_raphson_method(a, b):
    '''
    if f(a) * f(b) >= 0:
        print('Cannot find root')
        return
    '''
    if f(a) * f_2nd_deriv(a) > 0:
        x0 = a
    elif f(b) * f_2nd_deriv(b) > 0:
        x0 = b
    # ορίζω αυθαίρετα x0 = b για την περίπτωση που δεν μπούμε στο if ούτε στο elif παραπάνω
    else:
        x0 = b

    print('--------------------------------------------------------------------------')
    print('iter \t\t x1 \t\t x0 \t\t f(x1)')
    print('--------------------------------------------------------------------------')

    i = 0
    while True:
        x1 = x0 - 1 / ((f_deriv(x0)/f(x0)) - 1/2*(f_2nd_deriv(x0)/f_deriv(x0)))

        print(str(i + 1) + '\t\t% 10.8f\t% 10.8f\t% 10.8f\t' % (x1, x0, f(x1)))

        if np.abs(x1 - x0) < tolerance:
            break

        x0 = x1

        i += 1

    print('--------------------------------------------------------------------------')
    print('Root found: ' + str(x1))
    print('Root found: ' + '%7.5f' % x1)


newton_raphson_method(-2, -1)  # -1.381

newton_raphson_method(-1, 0)  # -0.667

newton_raphson_method(0.1, 0.4)  # 0.205

newton_raphson_method(0.4, 0.7)  # 0.5

newton_raphson_method(0.9, 2)  # 1.176

