#array iterating 1d
import numpy as np
arr=np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
for x in arr:
    print(x)
#array iterating 2d
import numpy as np
arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
for x in arr_2d:
    print(x)
#iteration with 3d array
import numpy as np
arr_3d= np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
for x in arr_3d:
    print(x)
#perform slicing for 4,5,6
import numpy as np
arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
sliced_arr = arr_2d[1, 0:3]  # Slicing to get elements 5 and 6
print("Sliced elements (5, 6):", sliced_arr)
#joining 2d arrays ----> concanatation
import numpy as np
arr1 = np.array([[1, 2, 3], [4, 5, 6]])
arr2 = np.array([[7, 8, 9], [10, 11, 12]])
joined_arr = np.concatenate((arr1, arr2), axis=0)  # Joining along rowscheck the axis
print("Joined 2D Array:")
print(joined_arr)

