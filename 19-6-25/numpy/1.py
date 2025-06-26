import numpy as np
arr=np.array([1,2,3,4,5,6,7,8,9,10])
print(arr[1:5])  # Output: [2 3 4 5]
print(arr[2:])   # Output: [3 4 5 6 7 8 9 10]
print(arr[:5])   # Output: [1 2 3 4 5
print(arr[::2])  # Output: [1 3 5 7 9]
print(arr[1::2]) # Output: [2 4 6 8
print(arr[::-1]) # Output: [10  9  8  7  6  5  4  3  2  1]
print(arr[1:8:2]) # Output: [2 4 6 8]
print(arr[::3])  # Output: [1 4 7 10]
#negative slicing
print(arr[-5:-1]) # Output: [6 7 8 9]
print(arr[-3:])   # Output: [8 9 10]
print(arr[:-3])  # Output: [1 2 3 4 5 6 7]
#2d slicing
arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr_2d)
print(arr_2d[0, 1:3])  # Output: [2 3]
print(arr_2d[1:, 0])   # Output: [4 7]
print(arr_2d[:, 1])   # Output: [2 5 8]
print(arr_2d[1:, 1:])  # Output: [[5 6]
                        #          [8 9]]
print(arr_2d[::2, ::2])  # Output: [[1 3]
                          #          [7 9]]
print(arr_2d[::-1, ::-1])  # Output: [[9 8 7]
                             #          [6 5 4]
                             #          [3 2 1]]    
# Accessing elements in a 2D array
print(arr_2d[0, 0])  # Output: 1
print(arr_2d[1, 1])  # Output: 5
print(arr_2d[2, 2])  # Output: 9    
# Slicing a 2D array
print(arr_2d[0:2, 0:2])  # Output: [[1 2]
                          #          [4 5]]
print(arr_2d[1:, 1:])  # Output: [[5 6]
                        #          [8 9]]   
                        
