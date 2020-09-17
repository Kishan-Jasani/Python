# --> We can create behavior in a class by adding functions in a class. 
# --> However, such functions should have a special parameter called self as the first parameter. 
# --> Such functions which describe the behavior are also called as methods. 
# --> We can invoke the methods using the dot operator as shown.
# --> Even though purchase() is accepting a parameter called self, we need not pass it when we invoke it.
# --> We can access an attribute in a method by using self. 
# --> Value of the attribute accessed inside the method is determined by the object used to invoke the method.


class Mobile:
    def __init__(self,brand,price):
        print("Inside constructor")
        self.brand=brand
        self.price=price

    def purchase (self): #we can not define method without first parameter. Generally first parameter is self but instead of self we can give other name as well.
        print("Purchasing a mobile")
        print("Brand of mobile is: "+self.brand)
        print("Price of mobile is: "+str(self.price))

mob1=Mobile("iPhone",25000)
#We can invoke methods with 3 different ways same as below
mob1.purchase()
Mobile.purchase(mob1)
Mobile("Oppo",10000).purchase()



#Function VS Methods
# --> Functions can be invoked using the name of the function and passing parameters.
# --> Methods Can be invoked only on an object, using dot operator. Without an object we cannot invoke a method.
# --> Parameters are optional in a function.
# --> A method must have at least one parameter : self
                    