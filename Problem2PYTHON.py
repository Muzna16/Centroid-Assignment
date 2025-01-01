#Import the Python Library 'numpy' to performing the numerical operations.
import numpy as np

# Given data in Problem 2
Dx, Dy = 100, 120
N, M = 5, 4

# Compute total mass of pixel matrix U using np.sum() method
U = np.array([
    [3.2, 5.1, 1.9, 4.2, 3.5],
    [5.4, 12.2, 19.3, 15.0, 6.2],
    [4.2, 13.1, 21.3, 14.1, 7.4],
    [1.1, 7.0, 9.1, 6.5, 2.3]
])
total_mass = np.sum(U)

# Compute x and y coordinates using np.arange() method.
x_coords = np.arange(1, N+1) - 0.5     
y_coords = np.arange(1, M+1) - 0.5

# Compute weighted averages
x_c = np.sum(U * x_coords[:,] * Dx) / total_mass
y_c = np.sum(U.T * y_coords[:,] * Dy) / total_mass

print(f"Centroid: (x_c, y_c) = ({x_c}, {y_c})")