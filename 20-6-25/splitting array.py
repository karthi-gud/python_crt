# splitting array into two parts
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
newarray = np.split(arr, 2)  # Splitting the array into two equal parts
print("Original array:", arr)
print("Split arrays:", newarray)
import numpy as np

arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
newarray2d = np.array_split(arr2d, 2)  # This will split into 2 parts as evenly as possible
print("Original 2D array:\n", arr2d)
print("Split 2D arrays:", newarray2d)
import numpy as np

arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
newarray2d = np.array_split(arr2d, 2, axis=1)  # Split columns into 2 parts
print("Original 2D array:\n", arr2d)
print("Split 2D arrays:", newarray2d)
#searching array where method is used
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
x=np.where(arr == 4)
print(x)  # Accessing the first element of the tuple returned by where
#searching index even
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
x = np.where(arr % 2 == 0)  # Finding indices of even numbers
print(x)
#finding index of odd numbers
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
x = np.where(arr % 2 != 0)  # Finding indices of odd numbers
print(x)
#searching index of numbers greater than 5
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
x = np.where(arr > 5)  # Finding indices of numbers greater than 5
print(x)  # Accessing the first element of the tuple returned by where3410