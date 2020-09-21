# --> If class A owns class B, then class A is said to aggregate class B. 
# --> This is also commonly known as "has-A" relationship. 
# --> For example, in our shopping app, a Customer has an Address. 
# --> First let us look at the Customer class and Address class independently. 

# Customer has a Address-
'''
                |---------------------|
                |     Customer        |    
                |---------------------|
                |    - name           |     
                |    - age            |    
                |    - address        |    # Here address independently represents another class
                |---------------------|    # But, address is also one of the attribute of Customer
                |    __init__         |    # This is called 'has-A' or 'Aggregation' relationship between class.
                |    + view_detail()  |   
                |    + updt_detail()  |    
                |---------------------|
                        <>                 # This is how we can represent Aggregation relation in class diagram.
                        |                  # If Customer has a address, Then diamond symbol should be on Customer side.
                        |                  # because, the Customer aggregates the Address.
                        |
                |---------------------|
                |     Address         |    
                |---------------------|
                |    - door_no        |     
                |    - street         |    
                |    - pin_code       |    
                |---------------------|
                |    __init__         |    
                |    + view_address() |   
                |    + updt_addres()  |    
                |---------------------|
'''

# Note: 
# --> In class diagram, aggregation is represented by a line connecting the classes and a diamond symbol in the class which aggregates the other class. 
# --> In the above example, the Customer aggregates the Address and hence the diamond symbol is near the Customer class


# Example:-
class Customer:
    def __init__(self, name, age, phone_no, address):
        self.name = name
        self.age = age
        self.phone_no = phone_no
        self.address = address      # This is how we can make other class as a attribute of this class.

    def view_details(self):
        print (self.name, self.age, self.phone_no)
        # See below line, This is how we can access details of other class who is in 'has-A' relationship with this class. 
        print (self.address.door_no, self.address.street, self.address.area, self.address.pincode)

    def update_details(self,add):
        self.address = add

class Address:
    def __init__(self, door_no, street, area, pincode):
        self.door_no = door_no
        self.street = street
        self.area = area
        self.pincode = pincode

    def update_address(self):
        pass


add1=Address(123,"5th Lane","TXS",56001)
add2=Address(567,"6th Lane","BBD",82006)

cus1=Customer("Jack",24,1234567890,add1) # This is how we can make other class as a parameter of this class.

cus1.view_details()
cus1.update_details(add2)       # This is how we can update address.
cus1.view_details()         