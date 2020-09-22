# --> We can make our static variable as a private variable by adding a double underscore in front of it. 
# --> We can also create getter and setter methods to access or modify it.

class Mobile:
    __discount = 50

    def get_discount(self):
        return Mobile.__discount

    def set_discount(self,discount):
        Mobile.__discount = discount

m1=Mobile()
print(m1.get_discount())

print(Mobile.__discount) #This will throw an error, since it is a private static variable

# --> Double Underscore converts attribute name into _class__attribute_name
print(m1._Mobile__discount) #This will give us value of static Variable. 

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