# numpy array

import numpy as np

import pandas as pd

# 1 x
arr_x1 = np.array([1, 2, 50, 0, 39, 90])

# 5 x 2
arr_x2 = np.array([[1,24,8,9,2], [2,6,89,12,90]])

# 3 x 2 x 2
arr_x3 = np.array([[ [1, 2, 3], [4, 5, 6] ], [[7, 8, 9], [10, 11, 12]]])

# 3D with 5 x 3 x 3
arr_x5_3_3 = np.array([
    [
        [1, 2, 3, 4, 5],
        [4, 5 ,6 ,7, 9],
        [9, 500, 90, 21 ,55]
    ],
    [
        [10, 7, 43, 8, 6],
        [81, 43, 65, 12, 6],
        [98, 23, 43, 1, 8]
    ],
    [
        [20, 89, 100, 32, 75],
        [84, 23, 54, 8, 12],
        [98, 65, 12, 43, 19]
    ]
])


print("One dimentional array: ",arr_x1)
print("Two dementinal array: \n", arr_x2)
print("3D array:\n", arr_x3)
print("3D 5_3_3:\n", arr_x5_3_3)


print("Dimensions of array")
print(arr_x1.ndim)
print(arr_x2.ndim)
print(arr_x3.ndim)
print(arr_x5_3_3.ndim)

print("500 array element: ", arr_x5_3_3[0,2,1])

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(arr[0:2, 1:4])

print("Shape of array: ")
print(arr_x1.shape)
print(arr_x2.shape)
print(arr_x5_3_3.shape)

# reading svg file
file = pd.read_csv(".data/student.csv")

file.head()

file.info()