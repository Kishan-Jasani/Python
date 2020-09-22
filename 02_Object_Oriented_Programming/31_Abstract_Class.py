# --> A class is called an Abstract class if it contains one or more abstract methods. 
# --> An abstract method is a method that is declared, but contains no implementation. 
# --> Abstract classes may not be instantiated, and its abstract methods must be implemented by its subclasses


#Let us assume that we have a Product class , all items being sold in our online app and extend this Product class.
# --> In an online shopping app, we only have specific types of products. We don’t have something called a Product itself. 
# --> In that sense, an object of Product class would not represent a real world object, 
# --> because a Product is just an abstract concept. While shopping, we purchase types of products, not a product itself. 
# --> Thus the best practice is not to create object of the parent class.


# --> Since we are the creator of the Product class, we know it is abstract in nature and we won’t create an instance for it. 
# --> But how can another programmer know about it? 
# --> How can we ensure that some other developer does not end up creating an object of such an abstract class?

#We can programmatically declare a class as an abstract class. An abstract class should not be instantiated.

from abc import ABCMeta     # Here, abc means Abstract Base Class and ABCMeta is inbuilt special class.
from abc import abstractmethod

class Product1(metaclass=ABCMeta):   #Metaclass defines how class should behave. Here we indicate that the product class should behave like an ABC class.
    def return_policy(self):
        pass
    
    
    
# --> If an abstract class should never be instantiated, then what is the use of such a class? 
# --> The only way we can use an abstract class is to make other classes inherit from the abstract class. 
# --> An abstract class is meant to be sub classed.


#Example:-
# --> each type of product will have its own return_policy(),
# --> so we will override the return_policy() in each of the child classes.

class Product(metaclass=ABCMeta):
    @abstractmethod
    def return_policy(self):
        pass

class Mobile(Product):
    def return_policy(self):
        print("All mobiles must be returned within 10 days of purchase")

class Shoe(Product):
    def return_policy(self):
        print("All shoes must be returned within 7 days of purchase")

class Furniture(Product):
    pass

m=Mobile()
m.return_policy()

s=Shoe()
s.return_policy()
        
# --> Since the return_policy() is overridden in each of the child classes,
# --> the parent class return_policy() is never used and hence it becomes redundant.

# --> Let us say we want to add a new type of product, say Furniture. 
# --> We can create a Furniture class and make it inherit the Product class.
# --> By mistake we have forgotten to override the return_policy() in the Furniture class. 
# --> If someone tries to find the return_policy() of furniture by invoking the method, it will invoke the redundant return_policy() of the parent.

# --> How can we ensure that all subclasses of the Product class must mandatorily override the return_policy()?
# --> If we programmatically declare our return_policy() of Product class as an abstract method, then every sub-class of Product class MUST override the abstract method. 
# --> We can make our return_policy() an abstract method with @abstractmethod tag.

# --> Even if one method is abstract, then we will get an error if we try to instantiate the class.
# --> If a method is abstract, then the Subclass must override the abstract method. Else we cannot instantiate the subclass also.

#Example:-
class Product2(metaclass=ABCMeta):
    @abstractmethod
    def return_policy(self):    #Product2 becomes abstract class because of this abstract method.
        pass

class Furniture1(Product2):
    def return_policy(self):    #Furniture1 should have return_policy() method, since it is a abstract method.
        pass
    
class Sofa(Furniture):          #If a child class overrides the abstract method, then its own child classes need not override the abstract method.
    pass

Product2()    #This will throw an error, Since abstract class can not be instantiate.
Furniture1()  #If Child class don't have abstract method in it, it will throw error while try to instantiate.
Sofa()        #It will not throw error because, If a child class overrides the abstract method, then its own child classes need not override the abstract method.



# Abstract Class - Summary:-
# --> Abstract classes should not be instantiated.
# --> An abstract class may contain 0 or many abstract methods.
# --> Usually the parent class is an abstract class.
# --> Abstract classes are meant to be inherited.
# --> If a class has an abstract method, then the class cannot be instantiated.
# --> The child class must implement/override all the abstract methods of the parent class. Else the child class cannot be instantiated.