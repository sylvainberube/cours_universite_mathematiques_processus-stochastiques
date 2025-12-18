#!/usr/bin/python

# Processus de branchement

import time
import statistics
import numpy as np
start_time = time.time()

#file_sim = open("Séance 11 - Processus de branchement - Simulation 1.txt", "w")
#file_sim = open("Séance 11 - Processus de branchement - Simulation 2.txt", "w")
file_sim = open("Séance 11 - Processus de branchement - Simulation 3.txt", "w")

nb_simulation = 10000
#prob = [0.5,0,0.5]
#prob = [1/2,1/4,1/8,1/16,1/16]
prob = [1/5,1/5,1/5,1/5,1/10,1/20,1/20]
populations = []
generations = []
descendants = []
pop_diverge = 0

for sim in range(nb_simulation):
    pop = [1]
    while (pop[-1] > 0) and (pop[-1]<1000):
        nb_descendants = 0
        nb_descendants += sum(np.random.choice(len(prob), pop[-1], p=prob))
        pop.append(nb_descendants)
        if (pop[-1]>=1000):
            pop_diverge += 1
    populations.append(pop)
    generations.append(len(pop)-2)
    descendants.append(sum(pop)-1)
    file_sim.write("[Simulation " + str(sim+1) + "] ")
    file_sim.write("generations = " + str(len(pop)-2) + " | ")
    file_sim.write("descendants = " + str(sum(pop)-1) + " | ")
    file_sim.write(str(pop) + "\n")

file_sim.write("\n")
min_gen = min(generations)
min_gen_index = generations.index(min_gen)
max_gen = max(generations)
max_gen_index = generations.index(max_gen)
file_sim.write("Min generations : " + str(min_gen) + " (" + str(min_gen_index+1) + ")\n")
file_sim.write("Max generations : " + str(max_gen) + " (" + str(max_gen_index+1) + ")\n")
file_sim.write("Deciles generations : " + str(statistics.quantiles(generations, n=10)) + "\n")
file_sim.write("Centiles generations : " + str(statistics.quantiles(generations, n=100)) + "\n")
file_sim.write("Moyenne generations : " + str(round(statistics.mean(generations), 2)) + "\n")
file_sim.write("Mediane generations : " + str(statistics.median(generations)) + "\n")
file_sim.write("Ecart-type generations : " + str(round(statistics.pstdev(generations), 2)) + "\n")

file_sim.write("\n")
min_desc = min(descendants)
min_desc_index = descendants.index(min_desc)
max_desc = max(descendants)
max_desc_index = descendants.index(max_desc)
file_sim.write("Min descendants : " + str(min_desc) + " (" + str(min_desc_index+1) + ")\n")
file_sim.write("Max descendants : " + str(max_desc) + " (" + str(max_desc_index+1) + ")\n")
file_sim.write("Deciles descendants : " + str(statistics.quantiles(descendants, n=10)) + "\n")
file_sim.write("Centiles descendants : " + str(statistics.quantiles(descendants, n=100)) + "\n")
file_sim.write("Moyenne descendants : " + str(round(statistics.mean(descendants), 2)) + "\n")
file_sim.write("Mediane descendants : " + str(statistics.median(descendants)) + "\n")
file_sim.write("Ecart-type descendants : " + str(round(statistics.pstdev(descendants), 2)) + "\n")

file_sim.write("\n")
file_sim.write("Proportion extinction : ")
file_sim.write(str(nb_simulation-pop_diverge) + "/" + str(nb_simulation))
file_sim.write(" (" + '{:.2%}'.format((nb_simulation-pop_diverge)/(nb_simulation)) + ")\n")

file_sim.write("\n")
file_sim.write("--- %s seconds ---" % '{:.3}'.format(time.time() - start_time))
