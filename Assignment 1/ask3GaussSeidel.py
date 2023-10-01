import numpy as np

e = 1/2 * 10e-4


def gauss_seidel(A, b, x, xpre, n):
    condition = True
    iteration = 1

    while condition:
        # copy X array to calculate diff
        for i in range(n):
            xpre[i] = x[i]
        for i in range(n):
            # copy X array to calculate diff
            xpre[i] = x[i]
            sum = 0
            '''
            for j in range(n):
                if j!=i:
                    sum += A[i][j]*X[j]
            '''
            if i < n - 1:
                sum += A[i][i + 1] * x[i + 1]
            if i > 0:
                sum += A[i][i - 1] * x[i - 1]
            x[i] = round((1 / A[i][i]) * (b[i] - sum), 4)

        # print(iteration, ":", Xpre)
        # print(iteration, ":", X)
        print(iteration)
        iteration += 1

        max = abs(xpre[0] - x[0])
        for i in range(n):
            if abs(xpre[i] - x[i]) > max:
                max = abs(xpre[i] - x[i])

        condition = max > e

    print(iteration, ":", x)


def initialize_arrays(n):
    # create A, b, x, Xpre as array of 0s
    A = [[0] * n for i in range(n)]
    A = np.array(A)
    b = [0] * n
    b = np.array(b)
    x = [0] * n
    xpre = [0] * n

    for i in range(n):
        A[i][i] = 5

        if i != n-1:
            A[i + 1][i] = -2
            A[i][i + 1] = -2

        if i == 0 or i == n - 1:
            b[i] = 3
        else:
            b[i] = 1

    return A, b, x, xpre


# initialize arrays for n=10
A, b, x, xpre = initialize_arrays(10)
gauss_seidel(A, b, x, xpre, 10)

# initialize arrays for n=10000
A, b, x, xpre = initialize_arrays(10000)
gauss_seidel(A, b, x, xpre, 10000)
