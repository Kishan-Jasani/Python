import numpy as np

#Create an 1-D array
arr = np.arange(0,11)
print(arr)

#Indexing
print(arr[8])
print(arr[1:5])
print(arr[0:5])

#Broadcast Array
arr[0:5] = 100
print(arr)

# Broadcast Array changes main Array also... Observe output of below code
# It will affect original array, even though you stored it in different variable
# It means, the sliced array is not independent array. It is referring the same memory as main array is referring.
arr = np.arange(0,11)
slice_of_arr = arr[0:5]
slice_of_arr[:] = 99 
print(slice_of_arr)
print(arr)


#If we want copy and independent array. We need to use copy method same as below
arr_copy = arr.copy()
print(arr_copy)
arr_copy[:] = 100
print(arr_copy)
print(arr)

#Conditional Array
bool_arr = arr > 5
print(bool_arr)
print(arr[bool_arr])  #It will return only those elements from main array where condition is true in boolean array
print(arr[arr>10])


#Create a 2-D Array
arr_2d = np.array([[5,10,15],[20,25,30],[35,40,45]])
print(arr_2d)

#Indexing in 2-D Array
print(arr_2d[0])  #It will return an entire row
#Method-1
print(arr_2d[0][0])
#Method-2
print(arr_2d[2,1])


#Slicing in 2-D arrays
print(arr_2d[0:2,1:3])