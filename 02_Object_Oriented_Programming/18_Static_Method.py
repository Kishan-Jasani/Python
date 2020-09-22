# --> Since static variable is object independent, we need a way to access the getter setter methods without an object. 
# --> This is possible by creating static methods. Static methods are those methods which can be accessed without an object. 
# --> They are accessed using the class name.
from builtins import staticmethod

# There are two rules in creating such static methods:
# --> The methods should not have self
# --> @staticmethod must be written on top of it

class Shoes:
    __discount = 50
    def __init__(self, price, brand):
        self.price = price
        self.brand = brand

    def purchase(self):
        total = self.price - self.price * Shoes.__discount / 100
        print ("Total is ",total)
    
    @staticmethod
    def get_discount():   #No need to write Self here as a first parameter, if @staticmethod is written on top of this method.
        return Shoes.__discount
    
    @staticmethod
    def set_discount(discount):   #No need to write Self here as a first parameter, if @staticmethod is written on top of this method.
        Shoes.__discount = discount

print(Shoes.get_discount()) #We can access static methods directly using the class name, even without creating objects.




# Please Find Complete Solution here.
class Mobile:
    __discount = 50
    def __init__(self, price, brand):
        self.price = price
        self.brand = brand

    def purchase(self):
        total = self.price - self.price * Mobile.__discount / 100
        print (self.brand, "mobile with price", self.price, "is available after discount at", total)

    @staticmethod
    def enable_discount():  #No need to write Self here as a first parameter, if @staticmethod is written on top of this method.
        Mobile.set_discount(50)

    @staticmethod
    def disable_discount(): #No need to write Self here as a first parameter, if @staticmethod is written on top of this method.
        Mobile.set_discount(0)

    @staticmethod
    def get_discount():     #No need to write Self here as a first parameter, if @staticmethod is written on top of this method.
        return Mobile.__discount

    @staticmethod
    def set_discount(discount): #No need to write Self here as a first parameter, if @staticmethod is written on top of this method.
        Mobile.__discount = discount

mob1=Mobile(20000, "Apple")
mob2=Mobile(30000, "Apple")
mob3=Mobile(5000, "Samsung")

Mobile.disable_discount()
mob1.purchase()
Mobile.enable_discount()
mob2.purchase()
Mobile.disable_discount()
mob3.purchase()