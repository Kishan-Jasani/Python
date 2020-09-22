# Method Overloading:
# --> Method Overloading is the class having methods that are the same name with different arguments.
# --> Arguments different will be based on a number of arguments and types of arguments.
# --> It is used in a single class.
# --> It is also used to write the code clarity as well as reduce complexity.

#Example-

class Human:

    def sayHello(self, name=None):
    
        if name is not None:
            print('Hello ' + name)
        else:
            print('Hello ')
        

# Create instance
obj = Human()
    
# Call the method without parameter
obj.sayHello()          
    
# Call the same method with a parameter
obj.sayHello('Guido')

# --> In above example, we are calling a method 2 times. Once with parameter and Once without parameter. This is called Method Overloading.