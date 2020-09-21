# --> Private variables cannot be accessed outside the class. This is true even in aggregation. 
# --> The owning class cannot access the private attributes of the aggregated class directly.

class Customer:
    def __init__(self, name, age, phone_no, address):
        self.name = name
        self.age = age
        self.phone_no = phone_no
        self.address = address

    def view_details(self):
        print (self.name, self.age, self.phone_no)    
        print (self.address.__door_no, self.address.__street, self.address.__pincode)
        
    def view_details1(self):
        print (self.name, self.age, self.phone_no)    
        print (self.address._Address__door_no, self.address._Address__street, self.address._Address__pincode)

class Address:
    def __init__(self, door_no, street, pincode):
        self.__door_no = door_no
        self.__street = street
        self.__pincode = pincode

    def update_address(self):
        pass

add1=Address(123, "5th Lane", 56001)
cus1=Customer("Jack", 24, 1234, add1)

cus1.view_details()      #This will throw an error, since Address is a private attribute
cus1.view_details1()    #This will give an output, because we have change attribute name into _Class__AttributeName


# Don't you have a question?
# --> Since we know that the name of the variable changes when we make it private, we can access it using its modified name as shown in above code.
# --> So, if private variable can be accessed outside the class and can be modified, then what is the advantage of making it private?
# --> Note: Languages like Java, C#, etc do not allow access of private variable outside the class

# Encapsulation - Just a caution sign !
'''
Any lock can be broken by a determined thief. 
Similarly, just because you make your code private, does not mean it is not accessible to other developers. 
When a developer sees a private variable, it’s a gentleman's agreement not to access it directly. 
It is used to only prevent accidental access.

Thus in python encapsulation is more like a caution sign than a lock. 
A caution sign is there so that you don’t accidentally break a rule. 
But if you still want to break it you can, with consequence ;)
''' 