#!/usr/bin/python

# AFFAIRES À FAIRE
# Puissance de la matrice de transition

import time
start_time = time.time()

import numpy as np

fMatTrans = open("Exercice -1.3 (matTrans).txt", "w")
file_S = open("Exercice -1.3 - Matrice S.txt", "w")
file_F = open("Exercice -1.3 - Matrice F.txt", "w")

# Création de la matrice de transition 102 x 102
#  - Lignes 0 à 100 : état représentant les 101 cases du jeu
#  - Ligne 101 : état où l'on va à la fin du jeu
matTrans = np.array([[0. for col in range(102)] for row in range(102)])

# Ajout des probabilités liées au dé
for row in range(102):
    for col in range(row+1, min(row+7,100)):
        matTrans[row,col] = 1/6
# Ajout des probabilités liées à l'atteinte de la case 100
for i in range(1,7):
    matTrans[100-i,100] = (7-i)/6
# Ajout des probabilités liées à la case 101
matTrans[100,101] = 1
matTrans[101,101] = 1
# Ajout des probabilités liées aux serpents et échelles
serpents = [(18,4),(39,20),(47,26),(53,32),(79,60),(88,70),(94,45),(98,77)]
echelles = [(5, 15), (12, 33), (23, 56), (35, 73), (50, 69), (59, 78), (66, 96), (71, 92)]
serpentsechelles = serpents + echelles
for serpentechelle in serpentsechelles:
    for i in range(1,7):
        if (serpentechelle[0]-i >= 0):
            matTrans[serpentechelle[0]-i,serpentechelle[0]] = 0
            matTrans[serpentechelle[0]-i,serpentechelle[1]] = 1/6
# Rendre matTrans inversible (en annuler les cases des bases des serpents et des échelles)
for serpentechelle in serpentsechelles:
    matTrans[serpentechelle[0],serpentechelle[0]] = 1
    for i in range(1,7):
        if serpentechelle[0]+i <= 100:
            matTrans[serpentechelle[0],serpentechelle[0]+i] = 0

#print(matTrans)

for row in range(102):
    for col in range(102):
        fMatTrans.write(str(matTrans[row,col])+"\t")
    fMatTrans.write("\n")

PT = np.array([[0. for col in range(101)] for row in range(101)])

for row in range(101):
    for col in range(101):
        PT[row,col] = matTrans[row,col]

# Il nous faut rendre transitoire les «faux états» (pieds des échelles et têtes des serpents)
for serpentechelle in serpentsechelles:
    PT[serpentechelle[0],serpentechelle[0]] = 0

S = np.linalg.inv(np.identity(101)-PT)
#print(S)

for row in range(101):
    for col in range(101):
        file_S.write(str(S[row,col])+"\t")
    file_S.write("\n")

# Création de la matrice F, où f_i,j représente la probabilité d'atteindre l'état j
#   étant donné qu'elle débute à l'état i
mI = np.identity(101)
F = np.array([[0. for col in range(101)] for row in range(101)])
for row in range(101):
    for col in range(101):
        F[row,col] = (S[row,col] - mI[row,col]) / S[col,col]
print(F)
for row in range(101):
    for col in range(101):
        file_F.write(str(F[row,col])+"\t")
    file_F.write("\n")


# Espérance de la durée du jeu
print(sum([S[0,k] for k in range(101)]))

# trajets.write("--- %s seconds ---" % '{:.3}'.format(time.time() - start_time))
