# --> Let us say we want to assign a unique number to each mobile object. 
# --> The first object should be given a number 1000 and subsequent objects should have that value increased by 1. 
# --> We can accomplish this by using a combination of static and instance variables as shown below:

class Mobile:
    counter = 1000
    def __init__(self, price, brand):
        self.price = price
        self.brand = brand
        self.mobile_id = Mobile.counter
        Mobile.counter += 1

mob1=Mobile(20000, "Apple")
mob2=Mobile(30000, "Apple")
mob3=Mobile(5000, "Samsung")

print("mobile_id for mob1 is", mob1.mobile_id)
print("mobile_id for mob2 is", mob2.mobile_id)
print("mobile_id for mob3 is", mob3.mobile_id)

print("Current value of counter is", Mobile.counter)



#Summary of Static Variables and static methods.
# --> Static attributes are created at class level.
# --> Static attributes are accessed using ClassName.
# --> Static attributes are object independent. We can access them without creating instance (object) of the class in which they are defined.
# --> The value stored in static attribute is shared between all instances(objects) of the class in which the static attribute is defined.