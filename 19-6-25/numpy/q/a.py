#write a python program to creatte an 1d array with 15 elements and reshape it into 2 dimensional arra of with 3 rows and 5 colums 
#5 rows and 3 columns and print the dimension of it
#and reshape the same array into 3d array with 5 rows and 3 columns with one element in each column
import numpy as np

# 1️⃣ Create a 1D array with 15 elements
array_1d = np.arange(1, 16)  # elements from 1 to 15
print("1D Array:")
print(array_1d)

# 2️⃣ Reshape into 2D array with 3 rows and 5 columns
array_2d_3x5 = array_1d.reshape(3, 5)
print("\n2D Array (3 rows, 5 columns):")
print(array_2d_3x5)

# 3️⃣ Reshape into 2D array with 5 rows and 3 columns
array_2d_5x3 = array_1d.reshape(5, 3)
print("\n2D Array (5 rows, 3 columns):")
print(array_2d_5x3)

# 4️⃣ Print dimension of the 5x3 array
print("\nDimension of 5x3 array:", array_2d_5x3.ndim)

# 5️⃣ Reshape into 3D array with 5 rows, 3 columns, and 1 element per column
array_3d = array_1d.reshape(5, 3, 1)
print("\n3D Array (5 rows, 3 columns, 1 element per column):")
print(array_3d)

# 6️⃣ Print dimension of 3D array
print("\nDimension of 3D array:", array_3d.ndim)
