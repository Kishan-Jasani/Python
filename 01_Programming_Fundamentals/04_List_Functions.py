# Here are some other common list methods.
#    -->list.append(elem) -- adds a single element to the end of the list. Common error: does not return the new list, just modifies the original.
#    -->list.insert(index, elem) -- inserts the element at the given index, shifting elements to the right.
#    -->list.extend(list2) adds the elements in list2 to the end of the list. Using + or += on a list is similar to using extend().
#    -->list.index(elem) -- searches for the given element from the start of the list and returns its index. Throws a ValueError if the element does not appear (use "in" to check without a ValueError).
#    -->list.remove(elem) -- searches for the first instance of the given element and removes it (throws ValueError if not present)
#    -->list.sort() -- sorts the list in place (does not return it). (The sorted() function shown later is preferred.)
#    -->list.reverse() -- reverses the list in place (does not return it)
#    -->list.pop(index) -- removes and returns the element at the given index. Returns the rightmost element if index is omitted (roughly the opposite of append()).

#--> Empty List
List=[]

#--> List with values
List1 = ['a','b','c','d','e']
List2 = ['f','g','h']

#--> find length of list
print(len(List1))

#--> Concatenate two Lists
print(List1 + List2) 

#--> List slicing
print(List1[1:3])   #last index will not print
print(List1[-4:-2]) #last index will not print in reverse index as well
print(List1[1:-2])  #last index will not print in mixed index as well

#--> add element in the list at last position
List1.append('f')       #O(1)
print(List1)

#--> add element in the list at specific position
List1.insert(3, 'g')    #O(n)
print(List1) 

#--> remove element in the list at specific position with index
List1.pop(3)            #O(n)
print(List1) 

#--> remove element in the list with giving value as input
List1.remove('f')       #O(n)
print(List1) 

#--> Find index of the element
print(List1.index('c')) #O(n)

#--> Sort List
List1.sort()
print(List1)

#--> Reverse List
List1.reverse()
print(List1)

#--> Extend List
List1.extend(['1','2'])
print(List1)

#--> Count element
print(List1.count('a'))

#--> Copy List
List3 = List1.copy()
print(List3)

#--> Clear List
List3.clear()
print(List3)

#--> Max/Min/Sum Value
List4 = [1,2,3,4,5]
print(max(List4))
print(min(List4))
print(sum(List4))

#--> List inside list
lst = [1,2,3,['a','b'],4,5]
print(lst[3])
print(lst[3][0])


# --> Zip Function
x = [1,2,3]
y = ['x','y','z']
print(list(zip(x,y)))


#Known Size and unknown element
list1 = [None]*5
list2 = ["Hey"]*5
print(list1,list2)