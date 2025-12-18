# http://japprendspython.blogspot.com/2013/05/diagonalisation-dune-matrice.html

from numpy import *

P = matrix([
    [0.60, 0.40],
    [0.25, 0.75]
])

P10 = linalg.matrix_power(P,10)

print(P10)
for i in range(2):
    for j in range(2):
       print(str(P10[i,j]) + "\t", end="")
    print("")

print(linalg.eigvals(P))
print(linalg.eig(P))

D = matrix([
    [1, 0],
    [0, 0.35]
])

A = matrix([
    [1, 1],
    [1, -0.625]
])

A_inv = linalg.inv(A)

print (A_inv)

print (A_inv * A)
