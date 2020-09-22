# --> Array is a data type which is of fixed capacity and can store a collection of elements. 
# --> However we can use it to implement the list data structure.

# --> For implementation we will be using list data type in python which is internally a dynamic array which can grow and shrink based on the elements added to or removed from it. 
# --> Initially, it is created with a certain capacity and based on elements getting added or removed, the capacity is increased or decreased respectively.


#Add Operation:-
# --> When an element is added to an empty list in Python, a block of memory is allocated and element is added at index position 0. 
# --> The remaining memory is considered to be reserved space which will be used later for addition or insertion of elements.
# --> How Add operation works in Python? In Python, we have append() function for add element.

#--> List.append(value)
#--> 1. When the list is initially created, it is created with a certain capacity.
#--> 2. While adding the elements, if the list is filled to the capacity,
#-->    a. Create a new list with increased capacity
#-->    b. Copy the elements of initial list to the new list
#--> 3. Add the element to the end of the existing elements in the list



#Insert Operation:-
# --> How Insert operation works in Python? In Python, we have insert() function for insert element.

#--> insert(pos, element):
#-->  1. If the list is filled to capacity
#-->     a. Create a new list with increased capacity
#-->     b. Copy the elements of initial list to the new list
#-->  2. Shift right all the existing elements from index position (pos) by 1 position
#-->  3. Insert the element at index position (pos)




#Delete Operation:-
# --> How Delete operation works in Python? In Python, we have delete() function for delete element.

#-->  delete(pos)/pop(index):
#-->   1. Shift left all the existing elements from index 
#-->      position (pos+1) by 1 position
#-->  Note: Capacity will be decreased whenever remaining number of elements fall below certain value
                
