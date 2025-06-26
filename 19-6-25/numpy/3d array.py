#accessing 3d array elements
import numpy as np

# Create a 3D array
array_3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

# Accessing elements
print("Element at (0, 0, 0):", array_3d[0, 0, 0])  # Output: 1
print("Element at (1, 1, 1):", array_3d[1, 1, 1])  # Output: 11
print("Element at (0, 1, 2):", array_3d[0, 1, 2])  # Output: 6
