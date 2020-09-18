# --> What happens to a balloon without the ribbon connecting it to the ground? Well, it escapes and becomes unusable.

# Example:1
class Mobile:
    def __init__(self, price, brand):
        self.price = price
        self.brand = brand

mob1=Mobile(1000, "Apple")
print(mob1.price)
# --> We are able to access the object in Example1 because we have a reference variable(mob1). 
# --> We are storing our Object in reference variable here. 
# --> This is like holding a balloon with a ribbon


# Example:2
class Mobile1:
    def __init__(self, price, brand):
        self.price = price
        self.brand = brand

Mobile1(1000, "Apple")
# --> In Example2 the Mobile1 object created is lost and unusable, Since we have not store it in reference variable.
# --> This is like a balloon without ribbon.



# --> Can one balloon have multiple ribbons?

# Example:3
class Mobile2:
    def __init__(self, price, brand):
        print ("Inside constructor")
        self.price = price
        self.brand = brand

mob1=Mobile2(1000, "Apple")
mob2=mob1
print ("Id of object referred by mob1 reference variable is :", id(mob1))
print ("Id of object referred by mob2 reference variable is :", id(mob2))
#In Example3, mob1 and mob2 are reference variables to the same object. Id of both reference variables will be same.



# --> Let's say a balloon has three ribbons connecting it. 
# --> If I change the color of the balloon tied to ribbon 1, what will be the color of the balloon tied to ribbons 2 and 3?

# Example:4
class Mobile3:
    def __init__(self, price, brand):
        self.price = price
        self.brand = brand

mob1=Mobile3(1000, "Apple")
print("Price of mobile 1 :", mob1.price)

mob2=mob1
mob2.price=3000  #We are updating price of mob2, still it will automatically update price of mob1. Because, both represents same Objects.

print("Price of mobile 1 :", mob1.price)
print("Price of mobile 2 :", mob2.price)