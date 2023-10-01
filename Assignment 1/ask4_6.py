import numpy as np

# array size
n = 14

# random probability
q = 0.15

# create A
#     1  2  3  4  5  6  7  8  9  0  1  2  3  4  5
A = [[0, 1, 0, 0, 0, 0, 0, 0, 1,    0, 0, 0, 0, 0],  # 1
     [0, 0, 1, 0, 1, 0, 1, 0, 0,    0, 0, 0, 0, 0],  # 2
     [0, 1, 0, 0, 0, 1, 0, 1, 0,    0, 0, 0, 0, 0],  # 3
     [0, 0, 1, 0, 0, 0, 0, 0, 0,    0, 1, 0, 0, 0],  # 4
     [1, 0, 0, 0, 0, 0, 0, 0, 0,    0, 0, 0, 0, 0],  # 5
     [0, 0, 0, 0, 0, 0, 0, 0, 0,    1, 0, 0, 0, 0],  # 6
     [0, 0, 0, 0, 0, 0, 0, 0, 0,    1, 0, 0, 0, 0],  # 7
     [0, 0, 0, 1, 0, 0, 0, 0, 0,    1, 0, 0, 0, 0],  # 8
     [0, 0, 0, 0, 1, 1, 0, 0, 0,    0, 0, 0, 0, 0],  # 9

     [0, 0, 0, 0, 0, 0, 0, 0, 0,    0, 0, 0, 0, 1],  # 11
     [0, 0, 0, 0, 0, 0, 1, 1, 0,    1, 0, 0, 0, 0],  # 12
     [0, 0, 0, 0, 0, 0, 0, 0, 1,    0, 0, 0, 1, 0],  # 13
     [0, 0, 0, 0, 0, 0, 0, 0, 0,    1, 0, 1, 0, 1],  # 14
     [0, 0, 0, 0, 0, 0, 0, 0, 0,    0, 1, 0, 1, 0]]  # 15

# create G with 0's
G = [[0]*n for i in range(n)]

# create N with 0's
N = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# Calculate N
for i in range(n):
    N[i] = 0
    for j in range(n):
        N[i] += A[i][j]

# Calculate G
for i in range(n):
    for j in range(n):
        G[i][j] = (q/n) + (A[j][i]*(1-q))/N[j]

# Print N
print('N =')
for i in range(n):
    print(N[i], end=' ')
print()

# Print G
print('G =')
for i in range(n):
    for j in range(n):
        print('{:f}'.format(G[i][j]), end=' ')
    print()
print()

#Print Summation of collumns
print('sum of columns =')
for j in range(n):
    sum = 0
    for i in range(n):
        sum += G[i][j]
    print('{:f}'.format(sum), end=' ')
print()

#G = np.array(G)

x = [1 for i in range(n)]
x = np.array(x)

condition = True
step = 1
for k in range(n):
    # Multiplying G and x
    x = np.matmul(G, x)
    #print('x =', x)

    if k < n-1:
        i = 0
        while True:
            if x[i] != 0:
                x = x/x[0]
                #print(x)
                break
            i += 1

#print('x =', x)

sum = 0
for i in range(n):
    sum += x[i]

for i in range(n):
    x[i] /= sum

# Print x
print('p =')
for i in range(n):
    print('%9.7f' % x[i], end=' ')
print()
