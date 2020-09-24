'''
--> Analysis of algorithms is all about estimating the amount of computing resources needed 
    to execute a given algorithm before implementing it as a program. 
--> It is also referred as algorithm complexity.

--> The most common resource that is estimated using analysis of algorithms is the computation time 
    i.e., how fast the algorithm performs and what affects its run time.
    
    
--> To find out the growth rate of an algorithm, we will be using worst case analysis (Big-O notation). This is one of the analysis categories that can be used to identify the growth rate.

    Notation name                     Meaning and usage

                                --Represents the maximum computation time an algorithm requires for any problem size
    Big-O notation              --Represented by ‘O’. Also called upper bound
    (worst case)                --Worst Case is used to express goodness of an algorithm


--> Computation of Big-O is done using a method called as step count method.

-->    O(1)   <   O(log n)     <  O(n)     <   O(n*log n)    <    O(n*n)    <     O(2^n)    <     O(n!)
    Excellent    Excellent        Good            Fair              Bad          Horrible        Horrible
'''