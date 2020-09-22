# Let us say that the online shopping application wants to sell different types of phones:
# -->1. Feature phone
# -->2. Smart Phone

# --> The below are the class diagrams for both the classes:
'''
                |---------------------|            |---------------------|
                |     SmartPhone      |            |    FeaturePhone     |
                |---------------------|            |---------------------|
                |    - brand          |            |    - brand          |    
                |    - price          |            |    - price          |
                |    - camera         |            |    - camera         |
                |    - OS             |            |    - type           |
                |    - Ram            |            |                     |
                |    - battery        |            |                     |
                |---------------------|            |---------------------|
                |    __init__         |            |    __init__         |
                |    + buy    ()      |            |    + buy()          |
                |    + return()       |            |    + return()       |
                |    + exchange()     |            |    + insure()       |
                |---------------------|            |---------------------|
'''

# --> We can see that both the class have a lot in common(methods and attributes).
# --> This is because they both are ultimately phones and each is just a special type of phone. 


# --> Since both the classes are of type phone, we can create a phone class with the common attributes and methods and make these two classes inherit those attributes and behavior, as shown: 

# --> The below class diagram illustrates the inheritance relationship
'''
                            |---------------------|
                            |     Phone           |    
                            |---------------------|
                            |    - brand          |        
                            |    - price          |    
                            |    - camera         |    
                            |---------------------|
                            |    __init__         |    
                            |    + buy()          |    
                            |    + return()       |    
                            |---------------------|
                                        ^
                                        |
                                        |
                        --------------------------------------
                        |                                    |
                        |                                    |
                        |                                    |
                |---------------------|            |---------------------|
                |     SmartPhone      |            |    FeaturePhone     |
                |---------------------|            |---------------------|
                |    - OS             |            |    - type           |
                |    - Ram            |            |                     |
                |    - battery        |            |                     |
                |---------------------|            |---------------------|
                |    __init__         |            |    __init__         |
                |    + exchange()     |            |    + insure()       |
                |---------------------|            |---------------------|
'''


# --> When a class inherits from another class, then those classes are said to have an inheritance relationship. 
# --> The class which is inheriting is called the child/sub/derived class and the class which is getting inherited is called the parent/super/base class. 
# --> Inheritance is also called as "is-A" relationship.
# --> In our example, 
# --> FeaturePhone is inheriting the Phone and SmartPhone is inheriting the Phone class (SmartPhone "is-A" phone, FeaturePhone "is-A" phone). 
# --> So Phone is the parent class and FeaturePhone and SmartPhone are derived classes.


#There are three main advantages of inheritance:

# --> We can keep common properties in a single place. Thus any changes needs to be made need not be repeated.
# --> Inheritance encourages code reuse thus saving us time.
# --> If we want to add a new type of phone later on, we can simply inherit the Phone class instead of writing it from scratch.