# Dictinary Rules

# --> Keys are unique within a dictionary while values may not be.
# --> There is no particular order of items in dictionary. Indexing will not work
# --> values of a dictionary can be of any type.
# --> keys must be of an immutable data type such as strings, numbers, or tuples.

# --> Define Empty dictionary
dict = {}

# --> Dictionary with values
dict1 = {1:"one", 2:"two", 3:"three", 4:"four", 5:"five"}

# --> Length of dictionary
print(len(dict1))

# --> Print value with key as input parameter
print(dict1[1])
print(dict1.get(3))

# --> In Function
print(1 in dict1)
print("one" in dict1)

# --> Items, Keys, values
print(dict1.items())
print(dict1.keys())
print(dict1.values())

# --> Update in dictinary
dict1[5]="Five"
print(dict1[5])

#For Loop with dictionary
for i in dict1.keys():
    print(i)
for j in dict1.values():
    print(j)
for m,n in dict1.items():
    print(m,n)
    
# --> pop function in dictionary
print(dict1.pop(2))
print(dict1)  

 
# --> Clear dictionary
dict1.clear()
print(dict1)