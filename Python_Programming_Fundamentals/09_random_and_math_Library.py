# Random Library
# --> random library helps in generating random numbers. 
# --> The code given below generates a random number between x and y-1 (both inclusive) using the randrange function of the random module.

import random
x=10
y=50
print(random.randrange(x,y)) #This will print random number between 10 and 49(Both inclusive)
print(random.randint(x,y))   #This will print random number between 10 and 49(Both inclusive)


import math
print(math.ceil(10.25))     #Smallest integer greater than or equal to value
print(math.floor(10.25))    #Largest integer smaller than or equal to value
print(math.factorial(5))    #Factorial of x
print(math.fabs(27.01))    #Gives absolute value of x