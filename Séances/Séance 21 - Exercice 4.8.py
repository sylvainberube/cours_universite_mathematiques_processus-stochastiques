import numpy as np
import matplotlib.pyplot as plt

# Définir les fonctions dérivées
def df_dt(f, h):
    return 0.1 * h - f

def dg_dt(f, g):
    return f - 0.2 * g

def dh_dt(g, h):
    return 0.2 * g - 0.1 * h

# Paramètres de la méthode d'Euler
t0, tf = 0, 15  # Intervalle de temps
dt = 0.01  # Pas de temps
n = int((tf - t0) / dt)  # Nombre de pas de temps

# Initialisation des solutions
t = np.linspace(t0, tf, n)
f = np.zeros(n)
g = np.zeros(n)
h = np.zeros(n)

# Conditions initiales
f[0], g[0], h[0] = 1, 0, 0

# Méthode d'Euler
for i in range(1, n):
    f[i] = f[i-1] + dt * df_dt(f[i-1], h[i-1])
    g[i] = g[i-1] + dt * dg_dt(f[i-1], g[i-1])
    h[i] = h[i-1] + dt * dh_dt(g[i-1], h[i-1])

# Tracer les solutions
plt.plot(t, f, label='f(t)')
plt.plot(t, g, label='g(t)')
plt.plot(t, h, label='h(t)')
plt.xlabel('t')
plt.ylabel('Solutions')
plt.legend()
plt.show()