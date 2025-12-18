import random

tentatives = 10000     # Nombre de simulations
succes = 0             # Nombre de succès (case 3 avant la case 9)

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

    while case!=3 and case!=9:
        case = random.choice(transition[case])

    if case==3:
        succes += 1

print(str(succes) + " / " + str(tentatives))
print(succes/tentatives)