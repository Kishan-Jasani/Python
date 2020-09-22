# --> A lot of things can go wrong in verbal communication.
# --> To ensure that programmers all over understand each other properly, we need a common way of representing a class. This is called as a class diagram.

# --> Unlike the complex engineering diagrams, a class diagram is quite simple. 
# --> It has four parts: the name of the class, the list of attributes, the list of methods and access specifiers.

'''
                |---------------------|
                |     Employee        |    # Class Name
                |---------------------|
                |    - emp_id         |    #Attribute    
                |    - emp_name       |    #Attribute
                |    - salary         |    #Attribute
                |---------------------|
                |    __init__         |    #Method
                |    + display()      |    #Method
                |    + update_salary()|    #Method
                |---------------------|
'''

# --> In a class diagram,Attributes and Methods have + and - sign which is called Access specifier. 
# --> – sign indicates private access and + indicates public access.


# --> We can create private methods by adding a double underscore in front of it, just like private attributes. 
# --> Also, if a method has both leading and trailing double underscores ( like __init__, __str__, etc) it indicates that it is a special built-in method. 
# --> As per coding convention, we are not supposed to create our own methods with both leading and trailing underscores.