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
--> If 100 students is messed up and we want to arrange it in ascending order.

--> Let's explore that algorithm. It is called Merge Sort and works well when the number of elements to be sorted is more.

# The strategy used in this algorithm is as follows:
--> Repeatedly divide the input unsorted list into sub-lists, such that each sublist contains only one element.
--> Repeatedly merge the sub lists to produce new sorted sub lists until there is only one sublist remaining.

--> example:-
    
    Unsorted List:               [44,84,96,4,10,12,25]
    
     Split List:               [44,84,96,4], [10,12,25]
     
    Split List again:      [44,88], [96,4], [10,12], [25]
    
    Split List again:    [44], [88], [96], [4], [10], [12], [25]
    
      Merge List:          [44,88], [4,96], [10,12], [25]
      
    Merge List again:          [4,44,88,96], [10,12,25]
    
    Merge List again:           [4,10,12,25,44,88,96]                #This is how we can get sorted list with Merging


--> The technique used in merge sort algorithm is known as Divide and Conquer.
--> It requires more memory as it divides the elements in the input list into separate right half and left half lists. 
--> This is recursively done until there is only one element left in the lists.
--> So for each right half and left half lists, separate memory is required.
'''


# Quick Sort Algorithm:-
'''
--> This sorting strategy known as Quick Sort works by picking an element in the input list as pivot and 
    partitioning the list around the pivot. 
--> Partitioning is done such that
    - the pivot is placed at its correct position in the list,
    - elements less than pivot are placed in the left partition and
    - elements greater than the pivot are kept in the right partition.
--> This is repeatedly done for each partition until all pivots are correctly placed in the list.

'''
