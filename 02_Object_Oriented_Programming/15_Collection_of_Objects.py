# --> We can store a number of objects inside a list or a dictionary.

# --> The below example, we have a list and dictionary of mobile objects and we are iterating over collection and printing the values.
class Mobile:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

mob1=Mobile("Apple", 1000)
mob2=Mobile("Samsung", 2000)
mob3=Mobile("Apple", 3000)
mob4=Mobile("Samsung", 4000)
mob5=Mobile("Apple", 5000)


# --> List of Objects:-
list_of_mobiles=[mob1, mob2, mob3, mob4, mob5]

for mobile in list_of_mobiles:
    print (mobile.brand,mobile.price)
    

# --> Dictionary of Objects:-
mob_dict={
          "m1":mob1,
          "m2":mob2,
          "m3":mob3,
          "m4":mob4,
          "m5":mob5
          }

for key,value in mob_dict.items():
    if value.price > 3000:
        print (value.brand,value.price)
        
        
        
# --> Dictionary of List of Objects
class Customer:
    def __init__(self, cust_id, cust_name, location):
        self.cust_id = cust_id
        self.cust_name = cust_name
        self.location = location

list_of_customers = [Customer(101, 'Mark', 'US'),
                     Customer(102, 'Jane', 'Japan'),
                     Customer(103, 'Kumar', 'India')]

dict_of_customer = {}
for customer in list_of_customers:
    dict_of_customer[customer.location] = customer

print ("Customer name in India is "+dict_of_customer["India"].cust_name)

for key,value in dict_of_customer.items():
    print ("Location: "+key+", Name: "+value.cust_name+", Id: "+(str(value.cust_id)))