import numpy as np
import scipy.stats as stats
import math


# b)
lambda_valeur = 1

P = np.zeros((7, 7))

for i in range(7):
    for j in range(7):
        if i > j+1:
            continue
        if i==0 and j==0:
            P[i, j] = stats.poisson.pmf(0, lambda_valeur) + stats.poisson.pmf(1, lambda_valeur)
            continue
        if j!=6:
            P[i, j] = stats.poisson.pmf(j-i+1, lambda_valeur)
            continue
        if j==6:
            P[i, j] = 1-stats.poisson.cdf(j-i, lambda_valeur)
# print(P)


# e)
P4 = np.linalg.matrix_power(P, 4)
# print(P4)


# f)
P2 = np.linalg.matrix_power(P, 2)
P3 = np.linalg.matrix_power(P, 3)

prob = 0
quotient = 0
for i in range(4, 7):
    for j in range(3):
        prob += P3[0,j] * P2[j,i]
for j in range(3):
    quotient += P3[0,j]

prob = prob/quotient
# print(prob)


# g)

Q = np.zeros((7, 7))
for i in range(7):
    for j in range(7):
        Q[i,j] = P[i,j]
Q[6,5] = 0
Q[6,6] = 1
# print(Q)

Q35 = np.linalg.matrix_power(Q, 35)
print(Q35[0,6])