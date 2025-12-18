import numpy as np
from fractions import Fraction


# b)

P = np.array([[0.25, 0.25, 0.25, 0.25],
              [0.40, 0.50, 0.00, 0.10],
              [0.00, 0.00, 0.60, 0.40],
              [0.00, 0.00, 0.50, 0.50]])
P5 = np.linalg.matrix_power(P, 5)
# print(P5)

prob_init = np.array([1/2, 1/3, 1/12, 1/12])
prob_X5 = prob_init @ P5
Esp = prob_X5 @ np.array([0, 1, 2, 3])
print(Esp)