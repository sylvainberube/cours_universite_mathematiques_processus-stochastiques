#!/usr/bin/python

import time
import numpy as np
from numpy.linalg import matrix_power
from fractions import Fraction
start_time = time.time()

# Exercice 2.9
e29_file = open("Exercice 2.9.txt", "w")

e29_P = np.array([[6/10,2/10,2/10],[1/6,4/6,1/6],[3/8,3/8,2/8]])
e29_X0 = np.array([0.2,0.3,0.5])
print(np.matmul(e29_X0, e29_P))

e29_P2 = matrix_power(e29_P, 2)
print(e29_P2)
print(np.matmul(e29_X0, e29_P2))

# file_F.write(str(F[row,col])+"\t")


# Exercice 2.35
e235_Pt = np.array([[0.5,0.4],[0.3,0.5]])
e235_I = np.array([[1,0],[0,1]])
print(e235_I - e235_Pt)
print(np.linalg.inv(e235_I - e235_Pt))
