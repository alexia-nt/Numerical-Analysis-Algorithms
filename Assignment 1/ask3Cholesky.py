import numpy as np
from math import sqrt


def cholesky_decomposition(M):
    A = np.copy(M)
    n = A.shape[0]
    R = np.zeros_like(A)

    for k in range(n):
        if A[k, k] < 0:
            return

        R[k, k] = sqrt(A[k, k])
        R[k, k + 1:] = A[k, k + 1:] / R[k, k]
        for j in range(k + 1, n):
            A[j, j:] = A[j, j:] - R[k, j] * R[k, j:]  # ?

    return R.transpose()


A_list = [[4, -2, 2], [-2, 2, -4], [2, -4, 11]]
A = np.array(A_list)

L = cholesky_decomposition(A)

print('L=')
print(L)

print('\nεπαλήθευση Α=:')
print(np.matmul(L, L.transpose()))
