# --> What happens when we pass an object as a parameter to a function? In the below code, what will be the output?

class Mobile:
    def __init__(self, price, brand):
        self.price = price
        self.brand = brand

# This def function is not inside class. We are passing Mobile object as a parameter in this function.
def change_price(mobile_obj):
    mobile_obj.price = 3000

mob1=Mobile(1000, "Apple")
change_price(mob1)
print (mob1.price)

# --> When we pass an object to a parameter, the parameter name becomes a reference variable.
# --> Recollecting the balloon example, it is like creating one more ribbon to the same balloon. 
# --> Thus there is one object with two reference variable, one the formal parameter and the actual parameter. 
# --> Thus any change made through one reference variable will affect the other as well.


# Let's think about output of below code.

class Customer:
    def __init__(self, cust_id, age):
        self.cust_id = cust_id
        self.age = age

c1=Customer(100,20)

def change(c2):
    c2=Customer(100,21)

change(c1)
print(c1.age) # will it print 20 or 21?

# --> It will print 20 because, We are creating a new customer object inside change() and hence the original customer object c1 is unaffected.