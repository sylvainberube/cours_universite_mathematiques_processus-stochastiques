from scipy.stats import binom
from scipy.stats import norm
import matplotlib.pyplot as plt  
import numpy as np

def graphique_q2a():
    # Représentation graphique
    x = np.arange(0, n_lancers+1)  # Possibles nombres de réussites
    y = binom.pmf(x, n_lancers, p_succes)  # Probabilités pour chaque nombre de réussites

    plt.figure(figsize=(10, 6))
    plt.bar(x, y, color='green', label='Probabilité de réussites')
    plt.plot(k_succes, prob_exact_10_succes, 'o', color='lightgreen', label='10 réussites')  # Marquer la probabilité de 10 réussites
    plt.text(k_succes, prob_exact_10_succes, f'{prob_exact_10_succes:.4f}', ha='center', va='bottom')

    plt.title("Probabilité d'exactement 10 réussites sur 15 lancés de 3 points")
    plt.xlabel("Nombre de réussites")
    plt.ylabel("Probabilité")
    plt.xticks(x)
    plt.legend()
    plt.grid(axis='y')
    plt.show()

def graphique_q2b():
    # Représentation graphique pour la saison
    x_saison = np.arange(100, 184)  # Plage réaliste de nombres de réussites pour la visualisation
    y_saison = binom.pmf(x_saison, n_lancers_saison, p_succes)  # Probabilités pour chaque nombre de réussites

    plt.figure(figsize=(12, 7))
    plt.bar(x_saison, y_saison, color='green', label='Probabilité de réussites')
    plt.axvline(x=k_succes_min, color="green", linestyle="--", label=f"Au moins 142 réussites (Prob ≈ {prob_au_moins_142_succes:.4f})")
    plt.fill_between(x_saison, y_saison, where=(x_saison >= k_succes_min), color='lightgreen', alpha=0.5)

    plt.title("Probabilité d'au moins 180 réussites sur 284 lancés de 3 points dans une saison")
    plt.xlabel("Nombre de réussites")
    plt.ylabel("Probabilité")
    plt.legend()
    plt.grid(axis='y')
    plt.show()

# Question 2
print("Question 2")

p_succes = 0.448  # Probabilité de succès (réussite d'un lancé de 3 points)

# a)

# Paramètres
n_lancers = 15  # Nombre de tentatives (lancés de 3 points)
k_succes = 10  # Nombre de succès (lancés réussis) souhaité

# Calcul de la probabilité d'exactement 10 réussites sur 15 tentatives
prob_exact_10_succes = binom.pmf(k_succes, n_lancers, p_succes)

print(prob_exact_10_succes)
# graphique_q2a()


# b)

# Paramètres pour la saison
n_lancers_saison = 284  # Nombre de tentatives (lancés de 3 points) dans la saison
k_succes_min = 142  # Nombre minimum de succès (lancés réussis) souhaité

# Calcul de la probabilité d'au moins 180 réussites sur 284 tentatives
# On utilise la fonction de répartition cumulative et on soustrait ce résultat de 1 pour obtenir "au moins"
prob_au_moins_142_succes = 1 - binom.cdf(k_succes_min - 1, n_lancers_saison, p_succes)

# Estimation à partir de la loi normale
# On utilise l'approximation normale en calculant la moyenne et la variance de la distribution binomiale
moyenne_saison = n_lancers_saison * p_succes
ecarttype_saison = np.sqrt(n_lancers_saison * p_succes * (1 - p_succes))

# Calcul de la probabilité d'au moins 142 réussites en utilisant la distribution normale
prob_au_moins_142_succes_norm = 1 - norm.cdf(k_succes_min - 0.5, moyenne_saison, ecarttype_saison)


print(prob_au_moins_142_succes)
print(prob_au_moins_142_succes_norm)
# graphique_q2b()
