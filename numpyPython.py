import numpy as np

np_array1 = np.array([1,2,3,4,5])

# this is 1-Dimensional array

print(np_array1)
print(type(np_array1))
print(np_array1.shape)

np_array2 = np.array([(1,2,3,4,5), (6,7,8,9,10)], dtype = "float")
# this is 2-Dimensional array with float type

print(np_array2)
print(type(np_array2))
print(np_array2.shape)

np_zeros_array = np.zeros((4,5))
# this will create array of zero values
print(np_zeros_array)

np_ones_matrix = np.ones((4,5))
# this will create matrix of one values
print(np_ones_matrix)

np_value_matrix = np.full((2,3), 4)
# this will create matrix of specified value values
print(np_value_matrix)

np_identity_matrix = np.eye(3)
# this will create identity matrix
print(np_identity_matrix)

np_random_matrix = np.random.random((2,3))
# this will create matrix of random values, this will give matrix of random float values
print(np_random_matrix)

np_random_int_matrix = np.random.randint(20, 50, (2,3))
# this will create matrix of random values of integer type with the given range
print(np_random_int_matrix)

list = [2, 4, 6, 8, 10]
np_listToArray = np.asarray(list)
# to convert a list to numpy array 
print(np_listToArray)

# analysing an numpy array 

np_array_analyze = np.random.randint(20, 100, (5,5))
print("\n\n",np_array_analyze)

# to get rows and columns of matrix
print(np_array_analyze.shape)

# to get the number of elements in numpy matrix
print(np_array_analyze.size)

# to get the datatype of numpy matrix
print(np_array_analyze.dtype)

# mathematical operations in numpy array

np_matrix1 = np.random.randint(10, 20, (3,3))
np_matrix2 = np.random.randint(30, 40, (3,3))

print("\n\n")
print(f"{np_matrix1}\n{np_matrix2}")

# method 1

print("\n\nmatrix addation\n")
print(np_matrix1 + np_matrix2)
print("\n\nmatrix substraction\n")
print(np_matrix1 - np_matrix2)
print("\n\nmatrix product\n")
print(np_matrix1 * np_matrix2)
print("\n\nmatrix division\n")
print(np_matrix1 / np_matrix2)

# mathod 2

np_matrix3 = np.random.randint(10, 20, (3,3))
np_matrix4 = np.random.randint(30, 40, (3,3))

print("\n\n")
print(f"{np_matrix3}\n{np_matrix4}")

print(f"addation : \n {np.add(np_matrix3, np_matrix4)}")
print(f"substraction : \n {np.subtract(np_matrix3, np_matrix4)}")
print(f"product : \n {np.multiply(np_matrix3, np_matrix4)}")
print(f"division : \n {np.divide(np_matrix3, np_matrix4)}")

# numpy array manipulation

# to find transpose 

np_matrix_manipulate = np.random.randint(10, 20, (2,3))
print(np_matrix_manipulate)

# first way to find transpose 

np_matrix_transpose1 = np.transpose(np_matrix_manipulate)
print(f"\n\ntranspose of matrix : \n{np_matrix_transpose1}")

# second way to find transpose 
np_matrix_transpose2 = np_matrix_manipulate.T
print(f"\n\ntranspose of matrix : \n{np_matrix_transpose2}")

# reshaping the matrix 
np_matrix_before_reshape = np.random.randint(20, 50, (2,6))
print(f"\n\nmatrix before reshape : \n{np_matrix_before_reshape}")

np_matrix_after_reshape = np_matrix_before_reshape.reshape(1, 12)
print(f"\n\nmatrix after reshape : \n{np_matrix_after_reshape}")