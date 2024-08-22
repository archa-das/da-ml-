import numpy as np
arr1 = np.array([[2,4], [4, 5]])
print("\nDeterminant of matrix:")
print(np.linalg.det(arr1))
print("\nInverse of matrix:")
print(np.linalg.inv(arr1))
print("\nRank of matrix:")
print(np.linalg.matrix_rank(arr1))
print("\nTransform matrix into 1-D array:")
print(np.reshape(arr1,-1))
