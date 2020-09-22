# --> Even though the child class may override the methods of the parent class, it might still decide to use the parent class overridden method. 
# --> To invoke anything belonging to the parent class, the child class needs to use the super() function, as shown below:

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
    def buy(self):
        super().buy()   #This is how we can use overridden method of Parent Class with Super() function.
        print ("Buying a FeaturePhone") 
    
class SmartPhone(Phone):
    def __init__(self, price, brand, camera, os, ram):
        super().__init__(price, brand, camera)   #This is how we can inherit Parent constructor from Super function, even though child has its own constructor.
        self.os = os
        self.ram = ram
        print ("Inside smartphone constructor")
        
s1=FeaturePhone(20000, "Apple", 13)
s1.buy()

s2=SmartPhone(20000, "Samsung", 12, "Android", 2)
print(s2.os)
print(s2.brand)


# --> To access the parent class constructor we can use super(). 
# --> Thus, the data is passed to the child class constructor, from there the data is sent to the parent class constructor and thus the attributes of the parent class get inherited.
# --> super() function can be used to access the constructor or methods of the parent class, but not the attributes. 
# --> Also super() function can be used only inside a class and not outside it.

# --> For example, refer SmartPhone class above.