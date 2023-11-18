import numpy as np

# numpy -> for array and matrix manipulation

l = [1,2,3,4,5]
print(np.array(l))
print(type(np.array(l)))

print(np.asarray(l))

print(np.array([[1,2,3],[4,5,6]]))

arr1 = np.array([[1,2,3],[4,5,6]])
print(arr1.ndim)          # To check dimension

print(np.matrix(l))    # By default 2 dimension
m = np.matrix(l)
print(np.asanyarray(l))
print(np.asanyarray(m))
# np.asanyarray converts any type into array but not matrix because matrix is a sub-class of array
# For example : list will be converted into array whereas matrix will be not

arr = np.array(l)
a = arr     # This operation is called shallow copy, we are giving a refernce and new data is not created in the memory. Orignal data will be affected
print(a)
a[0] = 10      
print(a)


b = np.copy(arr)     # This is called deep copy, where new memory is created for the data and it will not affect the original array(here, arr)
b[0] = 23
print(b)


# More function to create different type of arrays : 
# fromfunction() method takes function as an argument and returns an array
print(np.fromfunction(lambda i,j : i==j , (3,3)))   # This will apply this function for 3*3 matrix

print(np.fromfunction(lambda i,j : i*j , (3,3)))

# fromiter() method iterates and returns an array. It takes 2 arguments, variable and datatype
iterable = (i*i for i in range(5))
print(np.fromiter(iterable,float))

# fromstring
print(np.fromstring('23,45,67',sep=","))

# arr.size gives the total number of elements
print(arr.size)

print(arr1.shape)    # It gives the dimension of matrix like 2X2,3X3 etc

print(arr.dtype)