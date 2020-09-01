# Set Rules

# --> A set is an unordered collection of items. 
# --> Every set element is unique (no duplicates) and must be immutable (cannot be changed).
# --> Indexing will not work

# --> Define empty Set and set with values
s = set()
set1 = {1,2,3,4,5,6}

# --> Eliminating duplicates from a list
lst = [1,1,2,3,3,4,5,6,7,5,4]
set2 = set(lst)
print(set2)


# --> Remove element from set
set1.remove(2)
print(set1)

# --> Add element in the set
set1.add(2)
print(set1)

# --> Copy set
set2 = set1.copy()
print(set2)

# --> clear set
set2.clear()
print(set2)

# --> Some set Functions like &, -, |
set1={1,2,3,5,9}
set2={1,3,9,11}
print(set1 & set2)
print(set1 | set2)
print(set1 - set2)
print(set2 - set1)

