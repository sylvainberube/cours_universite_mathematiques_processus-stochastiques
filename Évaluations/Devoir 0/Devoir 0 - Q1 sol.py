from scipy.stats import norm
import numpy as np
import matplotlib.pyplot as plt             

def graphique_q1a():
    # Préparation des données pour le graphique
    x = np.linspace(moyenne - 4*ecarttype, moyenne + 4*ecarttype, 1000)
    y = norm.pdf(x, moyenne, ecarttype)

    # Création du graphique
    plt.figure(figsize=(10, 6))

    # Courbe de la distribution normale
    plt.plot(x, y, label="Distribution de QI", color="green")

    # Zone sous la courbe pour QI < 75
    plt.fill_between(x, y, where=(x<75), color="green", alpha=0.5, label=f"QI < 75 (Prob = {prob_inf_75:.4f})")

    plt.title("Probabilité d'avoir un QI inférieur à 75")
    plt.xlabel("Quotient Intellectuel")
    plt.ylabel("Densité de probabilité")
    plt.legend()

    plt.grid(True)
    plt.show()

def graphique_q1b():
    # Préparation des données pour le graphique
    x = np.linspace(moyenne - 5*ecarttype, moyenne + 5*ecarttype, 1000)
    y = norm.pdf(x, moyenne, ecarttype)

    # Création du graphique
    plt.figure(figsize=(10, 6))

    # Courbe de la distribution normale
    plt.plot(x, y, label="Distribution de QI", color="green")

    # Zone sous la courbe pour QI > 160
    plt.fill_between(x, y, where=(x>160), color="green", alpha=0.5, label=f"QI > 160 (Prob = {prob_sup_160:.8f})")

    plt.title("Probabilité d'avoir un QI supérieur à 160")
    plt.xlabel("Quotient Intellectuel")
    plt.ylabel("Densité de probabilité")
    plt.legend()

    plt.grid(True)
    plt.show()

def graphique_q1c(qi_top_2_pourcent):
    # Préparation des données pour le graphique
    x = np.linspace(moyenne - 4*ecarttype, moyenne + 4*ecarttype, 1000)
    y = norm.pdf(x, moyenne, ecarttype)

    # Réutilisation des données pour le graphique
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, label="Distribution de QI", color="green")
    plt.fill_between(x, y, where=(x>qi_top_2_pourcent), color="green", alpha=0.5, label="Top 2%")
    plt.axvline(x=qi_top_2_pourcent, color="green", linestyle="--", label=f"QI ≈ {qi_top_2_pourcent:.1f}")

    plt.title("QI nécessaire pour être dans le top 2%")
    plt.xlabel("Quotient Intellectuel")
    plt.ylabel("Densité de probabilité")
    plt.legend()
    plt.grid(True)
    plt.show()

# QUESTION 1
print("Question 1")

# Moyenne (espérance) et écart-type pour la distribution du QI
moyenne = 100
ecarttype = 15


# a)

# Probabilité d'avoir un QI inférieur à 75
prob_inf_75 = norm.cdf(75, moyenne, ecarttype)

print("a)")
print(prob_inf_75)
# graphique_q1a()

# b)

# Probabilité d'avoir un QI supérieur à 160
prob_sup_160 = 1 - norm.cdf(160, moyenne, ecarttype)
un_sur_x = 1 / prob_sup_160
un_sur_x_arrondi = round(un_sur_x)

print("b)")
print(prob_sup_160)
print(un_sur_x_arrondi)
# graphique_q1b()

# c)

# Calcul du QI correspondant au top 2%
# Utilisation de la fonction ppf (inverse de la fonction de répartition) pour obtenir le seuil
# Le top 2% correspond à 1 - 0.02 = 0.98 percentile
qi_top_2_pourcent = norm.ppf(0.98, moyenne, ecarttype)
qi_top_2_pourcent_arrondi = round(qi_top_2_pourcent, 1)

print("c)")
print(qi_top_2_pourcent_arrondi)
graphique_q1c(qi_top_2_pourcent)