# --> We can put a lock on that data by adding a double underscore in front of it, as shown in below code.
# --> Adding a double underscore makes the attribute a private attribute. 
# --> Private attributes are those which are accessible only inside the class. 
# --> This method of restricting access to our data is called encapsulation.

# --> Encapsulation is preventing access to a data outside the class
# --> Adding a __ in front of a attribute makes it private
# --> In python, adding a __ changes the name of the attribute to _Classname__attribute

class Customer:
    def __init__(self, cust_id, name, age, wallet_balance):
        self.cust_id = cust_id
        self.name = name
        self.age = age
        self.__wallet_balance = wallet_balance  #double underscore makes this attribute a private attribute

    def update_balance(self, amount):
        if amount < 1000 and amount > 0:
            self.__wallet_balance += amount     #We can access private attribute, since it is within a class.

    def show_balance(self):
        print ("The balance is ",self.__wallet_balance)

c1=Customer(100, "Gopal", 24, 1000)
c1.__wallet_balance = 1000000   # This will not throw an error, but also not updating a value of wallet balance. It basically creates a new variable.
print(c1.__wallet_balance)      # This will throw an error, since private attribute can not accessible outside the class.



# How does encapsulation work?
# --> When we put a double underscore in front of the attribute name, python will internally change its name to _Classname__attribute.
# --> That is why we get an error when we try to access a private attribute. 
c1._Customer__wallet_balance = 1000000
print(c1._Customer__wallet_balance)
# --> We can access private Attributes with _ClassName__AttributeName same as above 2 lines.


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