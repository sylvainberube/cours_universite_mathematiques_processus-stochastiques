import numpy as np
import sympy as sp

# Définir la variable symbolique
p = sp.symbols('p')

# Définir l'équation
equation = (1 + 2*p - p**2) / (2*p**2 - p**3) - 25

# Résoudre l'équation
solutions = sp.solve(equation, p)

# Obtenir les solutions numériques
solutions_num = [sp.N(sol) for sol in solutions]

# Filtrer et afficher les solutions avec une partie imaginaire très petite
tolerance = 1e-10
solutions_reelles = [sol.evalf() for sol in solutions_num if abs(sol.as_real_imag()[1]) < tolerance and 0 <= sol.evalf().as_real_imag()[0] <= 1]

# Conserver uniquement la partie réelle des solutions
parties_reelles = [sol.as_real_imag()[0] for sol in solutions_reelles]

print(parties_reelles)


p = 0.5
n = 1000
resultats_N = []

for _ in range(n):
    lancers = []
    for _ in range(3):
        lancer = 'face' if np.random.rand() < p else 'pile'
        lancers.append(lancer)
    if lancers[0] == 'face' and lancers[1] == 'face':
        resultats_N.append(2)
        continue
    N = 3
    while lancers.count('face') < 2:
        lancers[0] = lancers[1]
        lancers[1] = lancers[2]
        lancers[2] = 'face' if np.random.rand() < p else 'pile'
        N += 1
    resultats_N.append(N)

print(f"Le plus grand nombre de lancers requis est {max(resultats_N)}")

esperance_N = np.mean(resultats_N)

print(f"Espérance empirique de N après {n} tentatives : {esperance_N}")