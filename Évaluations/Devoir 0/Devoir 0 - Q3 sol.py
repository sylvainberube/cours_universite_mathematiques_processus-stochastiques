from scipy.stats import binom
from scipy.stats import norm
from scipy.stats import rv_discrete
from scipy.stats import geom
import matplotlib.pyplot as plt  
import numpy as np

def graphique_q3d():
    # Génération d'un éventail de nombres de parties pour la fonction de masse de probabilité (pmf)
    parties_range = np.arange(1, 200)
    pmf_values = geom.pmf(parties_range, p_gagner)

    # Création du graphique de la fonction de masse de probabilité avec deux couleurs pour différencier avant et après 100 parties
    plt.figure(figsize=(14, 8))

    # Barres pour les parties jusqu'à 100, inclusivement
    plt.bar(parties_range[parties_range <= 100], pmf_values[parties_range <= 100], color='skyblue', label='Probabilité avant 100 parties')
    # Barres pour les parties après 100
    plt.bar(parties_range[parties_range > 100], pmf_values[parties_range > 100], color='salmon', label='Probabilité après 100 parties')

    plt.axvline(x=100, color='red', linestyle='--', label='100 parties')
    plt.text(101, max(pmf_values)/2, f'Perte > 1000 $:\n{prob_perdre_100_parties:.2%}', color='red')

    plt.title('Probabilité de perdre au 100 parties avant un premier gain')
    plt.xlabel('Nombre de parties')
    plt.ylabel('Probabilité')
    plt.legend()
    plt.grid(axis='y')
    plt.xlim(1, 200)  # Limite ajustée pour une meilleure visualisation
    plt.show()

# Question 3
print("Question 2")

# a)
print("a)")

# Probabilités
p_gagner = 1/37
p_perdre = 36/37

# Gains: gain en cas de victoire et perte en cas de défaite
xk = np.array([350, -10])  # Gains possibles
pk = np.array([p_gagner, p_perdre])  # Probabilités correspondantes

# Définition de la distribution des gains
profit_distribution = rv_discrete(name='profit_distribution', values=(xk, pk))

# Calcul de l'espérance, de l'écart-type et de la variance
esperance_profit = profit_distribution.mean()
ecart_type_profit = profit_distribution.std()
variance_profit = ecart_type_profit ** 2

print(esperance_profit, ecart_type_profit)

# b)
print("b)")

# Nombre de parties
n_parties = 100

# Calcul de l'espérance et de la variance pour 100 parties
esperance_profit_100_parties = n_parties * esperance_profit
variance_100_parties = n_parties * variance_profit
ecart_type_100_games = variance_100_parties ** 0.5

print(esperance_profit_100_parties, ecart_type_100_games)

# c)
print("c)")

# Calcul de l'espérance (moyenne) et de l'écart-type pour le nombre de parties nécessaires pour un premier gain
esperance_parties_premier_gain, variance_parties_premier_gain = geom.stats(p_gagner, moments='mv')
ecart_type_parties_premier_gain = variance_parties_premier_gain ** 0.5

print(esperance_parties_premier_gain, ecart_type_parties_premier_gain)


# d)

print("d)")

# Calcul de la probabilité d'avoir besoin de jouer plus de 100 parties pour obtenir un premier gain
prob_perdre_100_parties = geom.sf(100, p_gagner)

print(prob_perdre_100_parties)
graphique_q3d()