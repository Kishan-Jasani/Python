List1 = ['a','b','c','d','e']
List2 = ['f','g','h']

# find length of list
print(len(List1))

# Concatenate two Lists
print(List1 + List2) 

# List slicing
print(List1[1:3])   #last index will not print
print(List1[-4:-2]) #last index will not print in reverse index as well
print(List1[1:-2])  #last index will not print in mixed index as well

# add element in the list at last position
List1.append('f')       #O(1)
print(List1)

# add element in the list at specific position
List1.insert(3, 'g')    #O(n)
print(List1) 

# remove element in the list at specific position with index
List1.pop(3)            #O(n)
print(List1) 

# remove element in the list with giving value as input
List1.remove('f')       #O(n)
print(List1) 

# Find index of the element
print(List1.index('c')) #O(n)

# Sort List
List1.sort()
print(List1)

# Reverse List
List1.reverse()
print(List1)

# Extend List
List1.extend(['1','2'])
print(List1)

# Count element
print(List1.count('a'))

# Copy List
List3 = List1.copy()
print(List3)

# Clear List
List3.clear()
print(List3)

# Max/Min/Sum Value
List4 = [1,2,3,4,5]
print(max(List4))
print(min(List4))
print(sum(List4))
