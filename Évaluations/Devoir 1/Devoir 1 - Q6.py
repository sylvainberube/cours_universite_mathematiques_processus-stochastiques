#!/usr/bin/python

import random
import statistics
import time
start_time = time.time()

fichier_q6 = open("Devoir 1 - Question 6.txt", "w")

nb_trajets = 10000
p = 0.5
longueurs = []

def lancer_piece():  # 1:face, 0:pile
    if random.random() < p:
        return 1
    return 0

for n in range(nb_trajets):
    serie_pf=[]
    # lancers 1, 2
    serie_pf.append(lancer_piece())
    serie_pf.append(lancer_piece())
    if (serie_pf[0] + serie_pf[1] == 2):
        longueurs.append(2)
        fichier_q6.write("Série " + str(n+1) + " : " + str(serie_pf) + "\n")
        continue
    # lancers 3
    serie_pf.append(lancer_piece())

    while (serie_pf[-1] + serie_pf[-2] + serie_pf[-3] < 2):
        serie_pf.append(lancer_piece())

    longueurs.append(len(serie_pf))
    fichier_q6.write("Série " + str(n+1) + " : " + str(serie_pf) + "\n")

fichier_q6.write("\n")
min_longueur = min(longueurs)
min_index = longueurs.index(min_longueur)
fichier_q6.write("Plus petite longueur : " + str(min_longueur) + " (" + str(min_index+1) + ")\n")
fichier_q6.write("Quartiles des longueurs : " + str(statistics.quantiles(longueurs, n=4)) + "\n")
max_longueur = max(longueurs)
max_index = longueurs.index(max_longueur)
fichier_q6.write("Plus grande longueur : " + str(max_longueur) + " (" + str(max_index+1) + ")\n")

fichier_q6.write("Moyenne des longueurs : " + str(round(statistics.mean(longueurs), 3)) + "\n")
fichier_q6.write("Mediane des longueurs : " + str(statistics.median(longueurs)) + "\n")
fichier_q6.write("Ecart-type des longueurs : " + str(round(statistics.pstdev(longueurs), 3)) + "\n")

fichier_q6.write("\n")
fichier_q6.write("Nombre de trajets des longueurs indiquées\n")
for n in range(min_longueur, max_longueur+1):
    fichier_q6.write(str(n) + "\t" + str(longueurs.count(n)) + "\n")

fichier_q6.write("\n")
fichier_q6.write("--- %s seconds ---" % '{:.3}'.format(time.time() - start_time))
