import numpy as np

tempsMax = 48600 #  De 11h30 à minuit, il y a 13,5 heures, soit 48 600 secondes
N = 170000
lamb = 10
p = 0.9
listNbInfectes = []

for _ in range(10000):
    nbInfectes = 1
    tempsSim = 0
    while tempsSim < 48600 and nbInfectes < N:
        nbInfectes += 1
        lambdaN = 2*lamb*nbInfectes*(N-nbInfectes)*p / (N * (N-1))
        tempsSim += np.random.default_rng().exponential(scale=1/lambdaN, size=1)[0]
    listNbInfectes.append(nbInfectes)
print(np.mean(listNbInfectes))