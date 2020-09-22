# --> Sometimes a child may not want to use what it has inherited from the parent. 
# --> The same holds true for OOP as well. 
# --> If the child class does not want to use a method inherited from the parent class then it may create its own method with the same name.
# --> When the child has a method with the same name as that of the parent, it is said to override the parent’s method. 
# --> This is called as Method Overriding. 
# --> Method overriding is also called as Polymorphism.

#Example-
class Phone:
    def __init__(self, price, brand, camera):
        print ("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print ("Buying a phone")

    def return_phone(self):
        print ("Returning a phone")

class FeaturePhone(Phone):
    pass

class SmartPhone(Phone):
    def buy(self):
        print ("Buying a smartphone")

s=SmartPhone(20000, "Apple", 13)

s.buy()


#In above example, 
# --> SmartPhone(Child class) is using constructor of Phone(Parent Class), 
# --> But SmartPhone(Child class) is using its own buy() method, even if same method is present in Phone(parent Class) also.
# --> This is called Method Overriding or Polymorphism.

# Methods with same name is present in both child as well as parent class, called Method Overriding or Polymorphism.