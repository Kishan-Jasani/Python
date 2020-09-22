# --> How to define a Class?
class Mobile:
    pass


# --> How to create an Object?
Mobile()        #Line1
Mobile()        #Line2
Mobile()        #Line3
mob1 = Mobile() #Line4
mob2 = Mobile() #Line5
mob3 = Mobile() #Line6
# --> We can not access values of Line 1,2 and 3 anywhere, Since we have not stored objects into Variables.
# --> To access the Object we need to store it into Variable same as Line 4,5 and 6.



# Look a like Object:-
# --> If two objects look the same and have the same values, can we treat it as a single object?
# --> Each object is unique and independent of other object. Just like every person, including twins, are unique, so is every object.
# --> All objects have an internal unique id (just like aadhar or green card number). We can check this using the inbuilt id(). 
# --> The below code will display the unique number associated with the object.
print(id(mob1))
print(id(mob2))
# --> You will find in the Console that both mob1 and mob2 objects have different Id.


# Attributes of an object:-
mob1.price=20000
mob1.brand="Apple"
mob2.price=3000
mob2.brand="Samsung"
mob2.color = "black"
print(mob1.brand,mob1.price)
print(mob2.brand,mob2.price,mob2.color)

# Update Attributes:-
mob2.color = "Red"
print(mob2.color)


# Variables VS Attributes VS reference Variable
variable1 = 5           #variable1 is Variable
mob2.color = "Green"    #mob2 is reference variable and color is Attributes
# --> The value of an attribute can be assigned to another variable. 
var = mob2.color


# --> How do we create attributes in a class?
class Shoes:
    #This is Constructor
    def __init__(self,brand,price):  #Brand and Price are Parameters here
        self.brand=brand             #brand is Attribute here
        self.price=price             #price is Attribute here
        
#This is Objects
shoe1=Shoes("Woodland",2000)
shoe2=Shoes("Adidas",2500)
