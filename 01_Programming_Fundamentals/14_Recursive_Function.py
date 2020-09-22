# --> Suppose we want to find the total weight of a human tower which has 5 people standing at the bottom level. 
#     Assume that each person weighs 50 kg and there will always be odd number of men at the base level. 
#     We can solve this problem recursively. Have a look.

def human_tower(no_of_people_at_bottom):
    if(no_of_people_at_bottom==1):  #Termination Condition
        return 1*50
    else:
        return (no_of_people_at_bottom*50) + human_tower(no_of_people_at_bottom-2)   #Recursive Function call
    
print(human_tower(51))





# --> Find factorial of number
import math
def factorial(num):
    if(num==1 or num==0):
        return 1
    else:
        return num * factorial(num-1)

print(factorial(7))
print(math.factorial(7))



# Example:-3
def fun(number):
    if(number<2):
        return 1
    elif(number/2==2):
        return fun(number-1)
    else:
        return (number-1)*fun(number-1)

print(fun(7))