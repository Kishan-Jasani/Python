# --> Tuples are immutable
# --> Indexing works in Tuples
# --> Like list, tuple can also store a sequence of elements but the value of the elements cannot be changed
# --> Tuple object does not support item assignment since tuple is immutable
# --> value of tuple cannot be change once assigned. Elements can be homogeneous or heterogeneous but they are READ-ONLY.


# --> Empty Tuple and Sample Tuple with value
empty_tuple = ()
empty_tuple = tuple()
sample_tuple = ("Welcome Drink","Veg Starter","Non-Veg Starter","Veg Main Course","Non-Veg Main Course","Dessert")
print(empty_tuple)
print(sample_tuple[3])


# --> Length of Tuple
print(len(sample_tuple))

# --> Create Tuple from string
tuple1 = tuple("Kishan")
print(tuple1)


# --> Zip Function
x = "abcde"
y = "xyz"
z= (1,2,3,4)
print(list(zip(x,y,z)))


# --> Tuple object does not support item assignment since tuple is immutable
# --> value of tuple cannot be change once assigned. Elements can be homogeneous or heterogeneous but they are READ-ONLY.
sample_tuple[3]="Changed" #It will throw an error
print(sample_tuple[3])


