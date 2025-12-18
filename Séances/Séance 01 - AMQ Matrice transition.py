# http://japprendspython.blogspot.com/2013/05/diagonalisation-dune-matrice.html

from numpy import *

P = matrix([
    [0, 1/2, 0, 1/2, 0, 0, 0, 0, 0],
    [1/3, 0, 1/3, 0, 1/3, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0],
    [1/3, 0, 0, 0, 1/3, 0, 1/3, 0, 0],
    [0, 0.25, 0, 0.25, 0, 0.25, 0, 0.25, 0],
    [0, 0, 1/3, 0, 1/3, 0, 0, 0, 1/3],
    [0, 0, 0, 1/2, 0, 0, 0, 1/2, 0],
    [0, 0, 0, 0, 1/3, 0, 1/3, 0, 1/3],
    [0, 0, 0, 0, 0, 0, 0, 0, 1]
])

P10 = linalg.matrix_power(P,10)
P100 = linalg.matrix_power(P,100)

# print(P10)
# for i in range(9):
#     for j in range(9):
#        print(str(P10[i,j]) + "\t", end="")
#    print("")

# print("\n\n\n")

# print(P100)
# for i in range(9):
#     for j in range(9):
#         print(str(P100[i,j]) + "   ", end="")
#     print("")

# print(P)
# print(linalg.eigvals(P))
# print(linalg.eig(P))
PE = linalg.eig(P)[1]
print(PE)
D = diag(linalg.eig(P)[0])
print(D)
DPower = linalg.matrix_power(D,10000)
print(DPower)

print(PE * rint(DPower) * linalg.inv(PE))
