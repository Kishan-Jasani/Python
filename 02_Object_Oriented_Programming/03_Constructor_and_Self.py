# --> How to define Constructor?
# --> We can create a constructor without parameters. But this is rarely useful.
class Mobile:
    def __init__(self):
        print("Inside constructor")
mob1=Mobile()


# --> self is not a keyword. self refers to the current object being executed.
class Shoes:
    def __init__(self,brand,price):
        print("Id of self in constructor", id(self))
        self.brand=brand
        self.price=price 
        color = "Red"   #This is a local variable, not Attribute. self.color will not print Red. It will print None.
shoe1=Shoes("Bata",399)
print("Id of shoe1 in driver code", id(shoe1))
shoe2=Shoes("Paragon",249)
print("Id of shoe2 in driver code", id(shoe2))



#Number of parameter mismatches
class Mobile1:
    def __init__(self,one,two):
        print("Inside constructor")
        

#Uncomment below 2 lines one by one. Try it out and observe the output.
#mb1=Mobile1()
#mb1=Mobile1(100,200,300)

