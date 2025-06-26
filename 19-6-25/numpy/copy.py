#view
import numpy as np
arr= np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
x=arr.view()
arr[0]=42
print(arr)
print(x)

#copy
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
x = arr.copy()
arr[0] = 42
print(arr)  # Original array after modification
print(x)    # Copied array remains unchanged
# Output:
# Original array after modification: [42  2  3  4  5  6  7  8  9 10]
#array shape
# Copied array remains unchanged: [1 2 3 4 5 6 7 8 9 10]
# Array shape
import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6]])
print("Original array shape:", arr.shape)  # Output: (2, 3)
# Reshape the array
reshaped_arr = arr.reshape(3, 2)
print("Reshaped array shape:", reshaped_arr.shape)  # Output: (3, 2)
# Array shape with 1D array
#1d to 3d array
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6,7, 8, 9, 10,11])
arr_3d = arr.reshape(1, 3, 4)
print("Original array shape:", arr.shape)  # Output: (12,)
print("Reshaped array shape:", arr_3d.shape)  # Output: (1, 3, 4)
