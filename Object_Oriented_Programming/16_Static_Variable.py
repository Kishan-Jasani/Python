# --> Let us assume that in our online shopping app, we want to provide a limited 50% flat off on all mobile phones.

# --> How can we write our code so that all mobile objects get a 50% off? 
# --> One solution is to create a discount attribute and hard code the value as 50%

# --> However, the solution of hardcoding the value in the attribute is not a good one. 
# --> For example, since this is a limited time discount we should be able to programmatically enable and disable the discount using functions.
# --> For that we can create a different function for enable and disable discount.


# Lets see, what is Static Variable?
# --> We can create shared attributes by placing them directly inside the class and not inside the constructor. 
# --> And since this attribute is not owned by any one object, we don’t need the self to create this attribute. 
# --> Such variables which are created at a class level are called static variables. Here discount is a static value.
# Example
class Mobile:
    discount = 50
    def __init__(self, price, brand):
        self.price = price
        self.brand = brand
    def purchase(self):
        total = self.price - self.price * Mobile.discount / 100  #We can see here static variable is accessible with class name.
        print (self.brand, "mobile with price", self.price, "is available after discount at", total)
def enable_discount():
    Mobile.discount = 50    #We can update the static value using the class name. 
def disable_discount():
    Mobile.discount = 0     #We can update the static value using the class name. 

mob1=Mobile(20000, "Apple")
mob1.purchase()
disable_discount()
mob1.purchase()

# --> Now that we have created static variables, we can access them using the Class name itself. 
# --> Static variable belong to the class and not an object. Hence we don’t need self to access static variables.
# --> We can update the static value using the class name. 
# --> Static variables belong to the class and hence it is incorrect to access them or update them using the reference variable or self. 
# --> Doing so may cause unexpected consequences in the code and should be refrained from.