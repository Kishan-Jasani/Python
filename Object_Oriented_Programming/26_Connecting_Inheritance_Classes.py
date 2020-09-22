# --> To create an inheritance relationship between the classes, mention the name of the parent class in brackets as shown:

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

class FeaturePhone(Phone):      #mention the name of the parent class in brackets to create inheritance relationship
    pass

class SmartPhone(Phone):        #mention the name of the parent class in brackets to create inheritance relationship
    def __init__(self, os, ram):
        self.os = os
        self.ram = ram
        print ("Inside SmartPhone constructor")

    def buy(self):
        print ("Buying a SmartPhone")
        #print(self.__price)    #This will throw an error, Since Private attribute not inherits.

FeaturePhone(10000,"Apple","13px").buy()  #FeaturePhone Child class inherits constructor, Non private attributes and methods because child class does not have his own constructor.
SmartPhone("Android", 2).buy()  #Since the SmartPhone class has its own constructor, the Phone class constructor is not inherited


# --> When we have a inheritance relationship, the attributes and behaviors get inherited, just like a child inherits certain attributes and behaviors from its parent. 

#From a code perspective, a child class inherits below 3 Properties, If Child class don't have this(Example: FeaturePhone in above example):
# --> Constructor
# --> Non Private Attributes
# --> Non Private Methods

#If class has its own constructor,method or attribute, parent class property will not inherited.(Example: SmartPhone in above example)


# --> A child class cannot directly access the private attributes of the parent class.(Example: price attribute of Parent Class)