import numpy as np


P = np.zeros((10, 10))

for i in range(10):
    for j in range(10):
        if i==0 and j==9:
            P[i, j] = 1
            continue
        if j >= i:
            continue
        if j < i:
            P[i, j] = 1/i
            continue
# print(P)

P_t = P.transpose()
# print(P_t)

# Coefficients du système d'équations
A = P_t - np.identity(10)
for i in range(10):
    A[9,i] = 1

# Constantes du système d'équations
B = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 1])

solutions = np.linalg.solve(A, B)
print("Les solutions sont:")
for i in range(10):
    print("pi_" + str(i) + f" = {solutions[i]}")

# P100 = np.linalg.matrix_power(P, 100)
# print(P100)
