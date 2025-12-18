#!/usr/bin/python

# AFFAIRES À FAIRE
# Puissance de la matrice de transition

import time
start_time = time.time()

import numpy as np

fMatTrans = open("Séance 12 - Exercice 3 - Matrice P.txt", "w")
file_S = open("Séance 12 - Exercice 3 - Matrice S.txt", "w")
file_F = open("Séance 12 - Exercice 3 - Matrice F.txt", "w")

mTransition = [[0 for j in range(102)] for i in range(102)]

echelles = [(5, 15), (12, 33), (23, 56), (35, 73), (50, 69), (59, 78), (66, 96), (71, 92)]
serpents = [(18,4),(39,20),(47,26),(53,32),(79,60),(88,70),(94,45),(98,77)]
echeserps = echelles + serpents

for i in range(102):
    for j in range(1, 7):
        if i+j<101:
            mTransition[i][i+j] += 1/6
        else:
            mTransition[i][100] += 1/6
mTransition[100][101] = 1
mTransition[101][101] = 1
for echeserp in echeserps:
    for j in range(1, 7):
        if echeserp[0]-j >= 0:
            mTransition[echeserp[0]-j][echeserp[0]] = 0
            mTransition[echeserp[0]-j][echeserp[1]] += 1/6
        mTransition[echeserp[0]] = [0]*102

for i in range(102):
    for j in range(102):
        fMatTrans.write(str(mTransition[i][j]).replace(".",",") + "\t")
    fMatTrans.write("\n")
#fichier.close()

""" PT = np.array([[0. for col in range(101)] for row in range(101)])

for row in range(101):
    for col in range(101):
        PT[row,col] = mTransition[row,col]

# Il faut rendre transitoire les «faux états» (pieds des échelles et têtes des serpents)
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

# trajets.write("--- %s seconds ---" % '{:.3}'.format(time.time() - start_time)) """
