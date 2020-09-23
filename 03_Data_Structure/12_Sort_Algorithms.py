# --> We have already seen in the Binary search Algorithm, the advantage of having sorted data while searching.

# Selection Sort Algorithm:-
'''
# The algorithm you have seen in the animation is as follows:

-->Assume that we have an unsorted list.

    1. Find the smallest number and swap it with the number at the first position in the list.
    2. Find the next smallest number and swap it with the number at the second position in the list.
    3. Find the next smallest number and swap it with the number at the third position in the list.
    4. Continue doing it until you are done with the number at the last position in the list.
    5. This strategy of sorting is known as Selection Sort. 
    6. Like linear search, technique followed here is also Brute-Force.
    
# Let's see how this algorithm works.

    Unsorted List:        5, 3, 1, 2, 4
                          
        Pass 1:           1, 3, 5, 2, 4         (swapping next smallest number with the number at the first position in the list)
        
        Pass 2:           1, 2, 5, 3, 4         (swapping next smallest number with the number at the second position in the list)
        
        Pass 3:           1, 2, 3, 5, 4         (swapping next smallest number with the number at the third position in the list)
        
        Pass 4:           1, 2, 3, 4, 5         (swapping next smallest number with the number at the fourth position in the list)
        
      Sorted List:        1, 2, 3, 4, 5
'''



# Bubble Sort Algorithm:-
'''
# Let's look on below example:-
List = [1,2,3,6,5,4,7,8,9,10,11,12,15,14,13,16,17,18,19,20]

--> Selection sort algorithm will take 20 Passes to sort above list.
--> However, Bubble sort algorithm will take just 4 passes to sort above list, since only 4 elements are not sorted(4,6,13,15).

--> Example:

    Unsorted List:        [5,1,2,3,4]
    
                          [5,1,2,3,4]            #Swapping first element with second element, if element2 < element1
                          [1,5,2,3,4]            #Swapping second element with third element, if element3 < element2
       Pass1:             [1,2,5,3,4]            #Swapping third element with fourth element, if element4 < element3
                          [1,2,3,5,4]            #Swapping fourth element with fifth element, if element5 < element4
                          [1,2,3,4,5]            #This all swapping are happens in same pass. This all steps are considered as Pass1
                          
    Sorted List:          [1,2,3,4,5]
    
# In Pass1, value of variable swapped is changed to true as elements are swapped
'''


# Merge Sort Algorithm:-
'''
'''
