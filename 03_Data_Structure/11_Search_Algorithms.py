#Linear Search Algorithm:-
'''
--> It's one of the simplest search algorithms which searches through 
    a list of elements in a sequential manner starting from the first element in the list. 
--> The technique used in this algorithm is known as Brute-Force.
--> Brute-Force is a trial and error technique in which we keep trying through all the possibilities 
    until the solution is found or until we have exhausted all the possibilities.
--> If we want to find name Parth from the list of 10 students, It will take a maximum of 10 guesses
'''




#Binary Search Algorithm:-
'''
--> If we want to find name Rahul from the list of 100 students. In How many guesses can you find him out? 
--> It will take a maximum of 100 guesses, if we use linear search algorithm
--> But with Binary Search Algorithm we will find Rahul in a maximum of 7 guesses!!!
--> List should be Sorted is the pre-condition of using Binary search algorithm.

i.e. Assume that the students are standing in increasing order of their student Id.

1, 2, 3, ...................................................................................99, 100    (1st guess)
                                                51, 52, ....................................99, 100    (2nd guess)
                                                                    76, 77, ................99, 100    (3rd guess)
                                                                               89, 90, .....99, 100    (4th guess)
                                                                                       95.......100    (5th guess)
                                                                                            98..100    (6th guess)
                                                                                                100    (7th guess)
                                                                                                
--> First Sort the list either Ascending or descending Order.
--> Here, we are selecting a middle number from list and comparing whether the selected number is 
    less than expected number or greater than expected number.
--> If, expected number is greater than selected number,
    We will find from elements which is in either right or left side of selected number accordingly.
'''