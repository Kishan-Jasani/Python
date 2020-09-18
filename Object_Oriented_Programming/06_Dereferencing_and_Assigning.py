# Reference variable - Summary
'''
1. Reference variables hold the objects
2. We can create objects without reference variable as well
3. An object can have multiple reference variables
4. Assigning a new reference variable to an existing object does not create a new object
'''


# --> Can we take one of the multiple ribbons of balloon 1 and tie it to another balloon?
# --> What will happen to the first balloon? Will it be lost?

# Example:1
class Mobile:
    def __init__(self, price, brand):
        self.price = price
        self.brand = brand

mob1=Mobile(1000, "Apple")

mob2=mob1
mob2=Mobile(2000," Samsung") #Line1
mob2.price=3000              

print(" Mobile ", "    Id","       Price")
print("  mob1  ", id(mob1), mob1.price)
print("  mob2  ", id(mob2), mob2.price)
# Observe the output her. You will see, Id and Price of both elements will be different, since we are assigning another object in mob2 at Line1.
# If you will comment Line1, Id and price of mob1 and mob2 will be same.



# Let's try below question.
# How many Objects and Reference variables in below code.
class Table:                 #Line1
    def __init__(self):      #Line2
        self.no_of_legs=4    #Line3
        self.glass_top=None  #Line4
        self.wooden_top=None #Line5
dining_table=Table()         #Line6
back_table=Table()           #Line7
front_table=back_table       #Line8
back_table=dining_table      #Line9

# Answer is, 2 Objects and 3 Reference Variables.
# Objects             >> Line6 and Line7
# Reference variables >> Line6, Line7 and Line8. 
# Line 9 changes the reference of back_table and makes it refer the object created in Line 6.