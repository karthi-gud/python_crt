#write a py program to create a matrix with 4 rows and 4 columns using numpy library and give only multiples of 5
import numpy as np

# Create a list of multiples of 5
multiples_of_5 = [5, 10, 15, 20, 25, 30, 35, 40, 
                  45, 50, 55, 60, 65, 70, 75, 80]

# Convert list to numpy array
array = np.array(multiples_of_5)

# Reshape into 4x4 matrix
matrix = array.reshape(4, 4)

# Print the matrix
print(matrix)
