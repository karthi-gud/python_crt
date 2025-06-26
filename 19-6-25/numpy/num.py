import numpy as np

# Creating Array Objects of Different Dimensions

# 0D Array (Scalar)
Array = np.array(10)
print(Array)
print(type(Array))
print(Array.ndim)
print()

# 1D Array
Array1 = np.array([12, 24, 36, 48, 60])
print(Array1)
print(type(Array1))
print(Array1.ndim)
print()

# 2D Array
Array2 = np.array([[10, 20], [30, 40], [50, 60]])
print(Array2)
print(type(Array2))
print(Array2.ndim)
print()

# 3D Array
Array3 = np.array([[[10, 20, 30], [40, 50, 60], [70, 80, 90]]])
print(Array3)
print(type(Array3))
print(Array3.ndim)
print()

# Additional information about arrays
print("=== Additional Array Information ===")
print("Array shapes:")
print(f"Array (0D): {Array.shape}")
print(f"Array1 (1D): {Array1.shape}")
print(f"Array2 (2D): {Array2.shape}")
print(f"Array3 (3D): {Array3.shape}")
print()

print("Array sizes:")
print(f"Array (0D): {Array.size}")
print(f"Array1 (1D): {Array1.size}")
print(f"Array2 (2D): {Array2.size}")
print(f"Array3 (3D): {Array3.size}")