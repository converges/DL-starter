'''
Github: https://github.com/converges/DL-starter/
Author: An
'''
''' Exercise 04: Python Programming
Find a solution of a linear equation.
'''

import numpy as np

# 1: Find the zero of the matrix. A(_x) = B
A = np.array([[2,1,1,1,1], [1,2,1,1,1], [1,1,2,1,1], [1,1,1,2,1], [1,1,1,1,2]])
B = np.array([1,2,3,4,5])

x = np.linalg.solve(A, B)
print(f"A =\n{A}\n")
print(f"B =\n{B}\n")
print(f"The solution of Ax = B is {x}.")
# Done.