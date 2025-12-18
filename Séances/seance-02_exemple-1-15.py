import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Définir les bornes pour x et y
x = np.linspace(0, 1, 100)
y = np.linspace(0, 1, 100)

# Créer une grille de points pour x et y
X, Y = np.meshgrid(x, y)

# Calculer les valeurs de Z en fonction de X et Y
Z = 6 * X * Y * (2 - X - Y)

# Créer un graphique en 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Tracer la surface
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='viridis', edgecolor='none')

# Titres et labels
ax.set_title('Surface 3D de f(x, y) = 6xy(2 - x - y)')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Afficher le graphique
plt.show()