#!/usr/bin/python

import time
import numpy as np
import statistics
start_time = time.time()

#file_sim = open("Exercice 3.15 - Simulation 1.txt", "w")
file_sim = open("Exercice 3.15 - Simulation 3.txt", "w")

nb_simulation = 10000
prob = [1/2, 1/4, 1/4]
#prob = [1/500]*500
liste_choix = []
liste_temps = []


for sim in range(nb_simulation):
    temps = 0
    choix = [0]*len(prob)
    while(min(choix)==0):
        temps += np.random.exponential(1)
        saveur = np.random.choice(len(prob), 1, p=prob)[0]
        choix[saveur] = choix[saveur] + 1
    liste_temps.append(temps)
    liste_choix.append(choix)

for sim in range(nb_simulation):
    file_sim.write("[Simulation " + str(sim+1) + "] ")
    file_sim.write("temps = " + str(liste_temps[sim]) + " | ")
    file_sim.write("choix = " + str(liste_choix[sim]) + " " + str(sum(liste_choix[sim])) + "\n")

file_sim.write("\n")
min_temps = min(liste_temps)
min_temps_index = liste_temps.index(min_temps)
max_temps = max(liste_temps)
max_temps_index = liste_temps.index(max_temps)
file_sim.write("Min temps : " + str(min_temps) + " (" + str(min_temps_index+1) + ")\n")
file_sim.write("Max temps : " + str(max_temps) + " (" + str(max_temps_index+1) + ")\n")
#file_sim.write("Deciles generations : " + str(statistics.quantiles(generations, n=10)) + "\n")
#file_sim.write("Centiles generations : " + str(statistics.quantiles(generations, n=100)) + "\n")
file_sim.write("Moyenne temps : " + str(round(statistics.mean(liste_temps), 2)) + "\n")
#file_sim.write("Mediane generations : " + str(statistics.median(generations)) + "\n")
file_sim.write("Ecart-type temps : " + str(round(statistics.pstdev(liste_temps), 2)) + "\n")
