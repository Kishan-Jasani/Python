# What is Abstraction?
'''
Abstraction in Python is the process of hiding the real implementation of an application from the user and emphasizing only on usage of it. 
For example, consider you have bought a new electronic gadget. 
Along with the gadget, you get a user guide, instructing how to use the application, but this user guide has no info regarding the internal working of the gadget.
Another example is, when you use TV remote, you do not know how pressing a key in the remote changes the channel internally on the TV. 
You just know that pressing volume key will increase the volume.
'''


# Why Do We Need Abstraction?
# --> Through the process of abstraction in Python, a programmer can hide all the irrelevant data/process of an application in order to reduce complexity and increase efficiency.


#Next, let us see how to achieve abstraction in Python programs with Example-1.

#Example-1
class Mobile:
    def __init__(self, brand, price):
        print("Inside constructor")
        self.brand = brand
        self.price = price
    def purchase(self):
        print("Purchasing a mobile")
        print("This mobile has brand", self.brand, "and price", self.price)
print("Mobile-1")
mob1=Mobile("Apple", 20000)
mob1.purchase()
print("Mobile-2")
mob2=Mobile("Samsung",3000)
mob2.purchase()

#When we invoke the purchase() on a mobile object, we don’t have to know the details of the method to invoke it. 
#This ability to use something without having to know the details of how it is working is called as abstraction.