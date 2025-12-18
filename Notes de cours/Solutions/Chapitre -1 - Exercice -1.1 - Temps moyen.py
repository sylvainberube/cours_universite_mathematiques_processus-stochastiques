#!/usr/bin/python

import time
start_time = time.time()

import numpy as np

file_P = open("Exercice -1.1 - Matrice P.txt", "w")
file_S = open("Exercice -1.1 - Matrice S.txt", "w")
file_F = open("Exercice -1.1 - Matrice F.txt", "w")

# Création de la matrice de transition 102 x 102
#  - Lignes 0 à 100 : état représentant les 101 cases du jeu
#  - Ligne 101 : état où l'on va à la fin du jeu
mat_P = np.array([
            [0,1/2,0,1/2,0,0,0,0,0],
            [1/3,0,1/3,0,1/3,0,0,0,0],
            [0,0,1,0,0,0,0,0,0],
            [1/3,0,0,0,1/3,0,1/3,0,0],
            [0,1/4,0,1/4,0,1/4,0,1/4,0],
            [0,0,1/3,0,1/3,0,0,0,1/3],
            [0,0,0,1/2,0,0,0,1/2,0],
            [0,0,0,0,1/3,0,1/3,0,1/3],
            [0,0,0,0,0,0,0,0,1],
        ])

# print(mat_P)

for row in range(9):
    for col in range(9):
        file_P.write(str(mat_P[row,col])+"\t")
    file_P.write("\n")

mat_PT = np.array([
            [0,1/2,0,1/2,0,0,0,0,0],
            [1/3,0,0,0,1/3,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [1/3,0,0,0,1/3,0,1/3,0,0],
            [0,1/4,0,1/4,0,1/4,0,1/4,0],
            [0,0,0,0,1/3,0,0,0,0],
            [0,0,0,1/2,0,0,0,1/2,0],
            [0,0,0,0,1/3,0,1/3,0,0],
            [0,0,0,0,0,0,0,0,0],
        ])

mat_S = np.linalg.inv(np.identity(9)-mat_PT)
# print(mat_S)

for row in range(9):
    for col in range(9):
        file_S.write(str(mat_S[row,col])+"\t")
    file_S.write("\n")

# Création de la matrice F, où f_{i,j} représente la probabilité d'atteindre l'état j
#   étant donné que X_0=i
mat_I = np.identity(9)
mat_F = np.array([[0. for col in range(9)] for row in range(9)])
for row in range(9):
    for col in range(9):
        mat_F[row,col] = (mat_S[row,col] - mat_I[row,col]) / mat_S[col,col]
# print(mat_F)

for row in range(9):
    for col in range(9):
        file_F.write(str(mat_F[row,col])+"\t")
    file_F.write("\n")

# Espérance de la durée du jeu
# print(sum([mat_S[0,k] for k in range(9)]))

# # trajets.write("--- %s seconds ---" % '{:.3}'.format(time.time() - start_time))
