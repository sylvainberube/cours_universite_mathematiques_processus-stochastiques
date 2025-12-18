#!/usr/bin/python

import random
import statistics
import time
start_time = time.time()

trajets = open("Exercice -1.1 - Trajets.txt", "w")

nb_trajets = 100000
cases = [[2,4],[1,3,5],[3],[1,5,7],[2,4,6,8],[3,5,9],[4,8],[5,7,9],[9]]
gagnants = []
longueurs = []

for n in range(nb_trajets):
    trajet=[1]
    while trajet[-1] not in [3, 9]:
        trajet.append(random.choice(cases[trajet[-1]-1]))
    gagnants.append(trajet[-1])
    longueurs.append(len(trajet)-1)
    trajets.write("Trajet " + str(n+1) + " : " + str(trajet) + "\n")

nb3 = gagnants.count(3)
nb9 = gagnants.count(9)
trajets.write("\n")
trajets.write("Nombre de 3: " + str(nb3) + "/" + str(nb_trajets) + " (" + '{:.2%}'.format(nb3/(nb3+nb9)) + ")\n")
trajets.write("Nombre de 9: " + str(nb9) + "/" + str(nb_trajets) + " (" + '{:.2%}'.format(nb9/(nb3+nb9)) + ")\n")

trajets.write("\n")
min_longueur = min(longueurs)
min_index = longueurs.index(min_longueur)
trajets.write("Plus petite longueur : " + str(min_longueur) + " (" + str(min_index+1) + ")\n")
trajets.write("Quartiles des longueurs : " + str(statistics.quantiles(longueurs, n=4)) + "\n")
max_longueur = max(longueurs)
max_index = longueurs.index(max_longueur)
trajets.write("Plus grande longueur : " + str(max_longueur) + " (" + str(max_index+1) + ")\n")

trajets.write("Moyenne des longueurs : " + str(round(statistics.mean(longueurs), 2)) + "\n")
trajets.write("Mediane des longueurs : " + str(statistics.median(longueurs)) + "\n")
trajets.write("Ecart-type des longueurs : " + str(round(statistics.pstdev(longueurs), 2)) + "\n")

trajets.write("\n")
trajets.write("Nombre de trajets des longueurs indiquées\n")
for n in range(min_longueur, max_longueur+1):
    trajets.write(str(n) + "\t" + str(longueurs.count(n)) + "\n")

trajets.write("\n")
trajets.write("--- %s seconds ---" % '{:.3}'.format(time.time() - start_time))
