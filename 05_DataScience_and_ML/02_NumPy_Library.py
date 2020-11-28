'''
#NumPy Library:-

--> Linear Algebric Library For Python
--> All Libraries rely on NumPy
--> It is incredibly Fast
--> 1-D Vectors or 2-D Metrix
'''

import numpy as np

#Creating 1-D Array
my_list = [1,2,3]
arr = np.array(my_list)
print(arr)

#Creating 2-D Array
my_list1 = [[1,2,3],[4,5,6],[7,8,9]]
arr1 = np.array(my_list1)
print(arr1)

#Creating 1-D array with arange function
print(np.arange(0,11,2))

#Creating 1-D and 2-D arrays with all zeroes
print(np.zeros(3))
print(np.zeros((4,3)))

#Creating 1-D and 2-D arrays with all Ones
print(np.ones(3))
print(np.ones((4,3)))

#Divide into 10 equal parts between 0 to 10 and make array
print(np.linspace(0,5,10))

#Create an Identity Matrix
print(np.eye(3))

#Generate random array with size as input (All Positive values)
print(np.random.rand(5))
print(np.random.rand(4,4))

#Generate random array with size as input (Both Positive and Negative values)
print(np.random.randn(5))
print(np.random.randn(4,4))

#Generate random number between 1 to 99
print(np.random.randint(1,100))

#Generate 5 random numbers between 0 to 99 and make array
print(np.random.randint(1,100,5))

#make array of integer from 0 to 24
arry = np.arange(0,25)

#Convert 1-D Array into 2-D Array
print(arry.reshape(5,5))

#Find Max and Min number in Array
print(arry.max())
print(arry.min())

#Find Index of Max and Min number in Array
print(arry.argmax())
print(arry.argmin())

#Find the size of the array
print(arry.shape)

#Find Datatype of the Array
print(arry.dtype)