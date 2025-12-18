from numpy import *
import numpy as np

fichier = open("seance-01_serpents.txt", "w")
mTransition = [[0 for j in range(101)] for i in range(101)]

echelles = [(5, 15), (12, 33), (23, 56), (35, 73), (50, 69), (59, 78), (66, 96), (71, 92)]
serpents = [(18,4),(39,20),(47,26),(53,32),(79,60),(88,70),(94,45),(98,77)]
echeserps = echelles + serpents

for i in range(101):
    for j in range(1, 7):
        if i+j<101:
            mTransition[i][i+j] += 1/6
        else:
            mTransition[i][100] += 1/6

for echeserp in echeserps:
    for j in range(1, 7):
        if echeserp[0]-j >= 0:
            mTransition[echeserp[0]-j][echeserp[0]] = 0
            mTransition[echeserp[0]-j][echeserp[1]] += 1/6
        mTransition[echeserp[0]] = [0]*101

P = mTransition
P2 = linalg.matrix_power(P,2)
P5 = linalg.matrix_power(P,5)
P6 = linalg.matrix_power(P,6)
P100 = linalg.matrix_power(P,100)

for i in range(101):
    for j in range(101):
        fichier.write(str(P100[i][j]).replace(".",",") + "\t")
    fichier.write("\n")
#fichier.close()


np.set_printoptions(precision=8)
np.set_printoptions(suppress=True)
# fichier.write(np.array2string(P100, threshold = np.inf))
fichier.close()