'''
--> The problem is divided into smaller sub-problems, 
    then by reusing the solutions of these sub-problems, 
    we will be able to arrive at the solution of the actual problem.
    
    
    Expressions1:-        23 + 23 = 46
    
    Expressions2:-        23 + 23 + 23 =69
    
    Expressions3:-        23 + 23 + 23 + 23 + 23 = ?
                          -------   ------------
                             46   +    69     =   115
                             
                             
--> Lets understand this with fibonacci series example:-
    
Question:- F(n) = F(n-1) + F(n-2), If F(0)=0 and F(1)=1, what is F(4)?
    
                               F(4)=3
                                 |
                        --------------------
                        |                  |
                     F(3)=2              F(2)=1
                        |                  |
                --------------        ----------------   
                |            |        |              |
             F(2)=1        F(1)=1   F(1)=1         F(0)=0 
                |
        ------------------
        |                |
     F(1)=1            F(0)=0
       
'''