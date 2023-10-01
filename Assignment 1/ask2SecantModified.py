import numpy as np

tolerance = 0.5 * 10e-5


# ορίζω τη συνάρτηση f
def f(x):
    return 54*(x**6) + 45*(x**5) - 102*(x**4) - 69*(x**3) + 35*(x**2) + 16*x - 4


def secant_method(a, b):
    '''
    if f(a) * f(b) >= 0:
        print('Cannot find root')
        return
    '''
    x0 = a
    x1 = (a + b) / 2
    x2 = b

    print('--------------------------------------------------------------------------')
    print('iter \t\t x3 \t\t x2 \t\t x1 \t\t x0 \t\t f(x3)')
    print('--------------------------------------------------------------------------')

    i = 0
    while True:
        q = f(x0)/f(x1)
        r = f(x2)/f(x1)
        s = f(x2)/f(x0)

        x3 = x2 - (r*(r-q)*(x2-x1) + (1-r)*s*(x2-x0)) / ((q-1)*(r-1)*(s-1))

        print(str(i + 1) + '\t\t% 10.8f\t% 10.8f\t% 10.8f\t% 10.8f\t% 10.8f\t' % (x3, x2, x1, x0, f(x3)))

        if np.abs(x3 - x2) < tolerance:
            break

        x0 = x1
        x1 = x2
        x2 = x3

        i += 1

    print('--------------------------------------------------------------------------')
    print('Root found: ' + str(x3))
    print('Root found: ' + '%7.5f' % x3)


secant_method(-2, -1.2)  # -1.381

secant_method(-1.2, 0)  # -0.667

secant_method(0, 0.4)  # 0.205

secant_method(0.4, 1)  # 0.5

secant_method(1, 2)  # 1.176
