import numpy as np

P = np.array([[1/6, 2/6, 3/6],
              [3/7, 2/7, 2/7],
              [4/11, 5/11, 2/11]])


# c)
P4 = np.linalg.matrix_power(P, 4)
# print(P4)

ligne = P[0, :]
colonne = P4[:, 1]
prob = np.dot(ligne, colonne)
# print(prob)


# d)
P5 = np.linalg.matrix_power(P, 5)
# print(P5)


# e) 1
# Coefficients du système d'équations
A = np.array([[-5/6, 3/7, 4/11],
              [2/6, -5/7, 5/11],
              [1, 1, 1]])

# Constantes du système d'équations
B = np.array([0, 0, 1])

solutions = np.linalg.solve(A, B)
# print("Les solutions sont:")
# print(f"pi_1 = {solutions[0]}")
# print(f"pi_2 = {solutions[1]}")
# print(f"pi_3 = {solutions[2]}")


# e) 2
# Trouver les valeurs propres et les vecteurs propres
valeursPropres, vecteursPropres = np.linalg.eig(P)

# Créer la matrice diagonale à partir des valeurs propres
D = np.diag(valeursPropres)
D_infini = np.array([[1, 0, 0],
                 [0, 0, 0],
                 [0, 0, 0]])

# La matrice des vecteurs propres est déjà donnée par numpy
A = vecteursPropres

# Calculer l'inverse de la matrice des vecteurs propres
A_inv = np.linalg.inv(A)

print(A)
print(D)
#print(Dinf)
#print(A_inv)
#print(A @ D_infini @ A_inv)
