# http://japprendspython.blogspot.com/2013/05/diagonalisation-dune-matrice.html

import numpy as np
import random

fichier = open("seance-01_amq_promenades.txt", "w", encoding='utf-8')

tentatives = 1000000     # Nombre de tentatives
succes = 0              # Nombre de succès (case 3 avant la case 9)

promenades = []         # Liste des promenades
len_promenades = []         # Liste des promenades
longueur_promenades = [0]*501

transition = [
    [0],
    [2, 4],         # Case 1
    [1, 3, 5],      # Case 2
    [3],            # Case 3
    [1, 5, 7],      # Case 4
    [2, 4, 6, 8],   # Case 5
    [3, 5, 9],      # Case 6
    [4, 8],         # Case 7
    [5, 7, 9],      # Case 8
    [9]             # Case 9
]

for i in range(tentatives):
    case = 1
    promenade = []      # Cases visitées par le pion

    while case!=3 and case!=9:
        promenade.append(case)
        case = random.choice(transition[case])
    
    if case==3:
        succes += 1

    promenade.append(case)
    promenades.append(promenade)
    len_promenades.append(len(promenade))

vmax = len(promenades[0])
vmin = len(promenades[0])
promenademax = 0
promenademin = 0

for i in range(tentatives):
    promenade = promenades[i]
    longueur_promenades[len(promenade)] += 1
    if vmax < len(promenade):
        vmax = len(promenade)
        promenademax = i
    if vmin > len(promenade):
        vmin = len(promenade)
        promenademin = i

len_promenades_np = np.array(len_promenades)
moyenne = np.mean(len_promenades_np)
ecarttype = np.std(len_promenades_np)

print("Nombre de promenades : " + str(tentatives))
print("Nombre de succès : " + str(succes))
print("Proportion de succès : " + str(succes) + " / " + str(tentatives) + " = " + str(succes/tentatives))
print("Plus petite promenade : " + str(vmin) + " (promenade #" + str(promenademin+1) + ")")
print("Plus grande promenade : " + str(vmax) + " (promenade #" + str(promenademax+1) + ")")
print("Moyenne des promenades : " + str(moyenne))
print("Écart-type des promenades : " + str(ecarttype))
fichier.write("Nombre de promenades : " + str(tentatives) + "\n")
fichier.write("Nombre de succès : " + str(succes) + "\n")
fichier.write("Proportion de succès : " + str(succes) + " / " + str(tentatives) + " = " + str(succes/tentatives) + "\n")
fichier.write("Plus petite promenade : " + str(vmin) + " (promenade #" + str(promenademin+1) + ")" + "\n")
fichier.write("Plus grande promenade : " + str(vmax) + " (promenade #" + str(promenademax+1) + ")" + "\n")
fichier.write("Moyenne des promenades : " + str(moyenne) + "\n")
fichier.write("Écart-type des promenades : " + str(ecarttype) + "\n\n")

for i in range(tentatives):
    promenade = promenades[i]
    fichier.write("Promenade " + str(i+1) + " : " + str(promenade) + "\n")
fichier.write("\n---\n\n")

for i in range(501):
    fichier.write("Longueur " + str(i) + " : " + str(longueur_promenades[i]) + "\n")

fichier.close()