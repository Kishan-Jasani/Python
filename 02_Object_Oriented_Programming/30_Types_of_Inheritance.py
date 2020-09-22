# Inheritance can come in many forms as below: 
# --> Single Level    :        Single Parent - Single Child
# --> Multi Level     :        Parent - Child - Grand Child
# --> Hierarchy       :        One Parent - Many Children
# --> Multiple        :        One Child - Many Parents


# Examples:

# --> Single Level:-
class Phone:
    pass
class SmartPhone(Phone):
    pass


# --> Multi Level:-
class Product:
    pass
class Shoes(Product):
    pass
class SportShoes(Shoes):
    pass



# Hierarchy:-
class Employee:
    pass
class GovermentEmployee(Employee):
    pass
class PrivateEmployee(Employee):
    pass




# Multiple:-
# --> When a child is inheriting from multiple parents, and if there is a common behavior to be inherited, it inherits the method in Parent class which is first in the list. 
# --> In our example, the buy() of Product is inherited as it appears first in the list.

class Prodct:
    def __init__(self):
        print ("Inside Product constructor")
    def buy(self):
        print ("Buying a Product")
class Fan:
    def __init__(self):
        print ("Inside Fan constructor")
    def buy(self):
        print ("Buying a Fan")
class AutomaticFan(Prodct,Fan): #This is how we represent multiple Inheritance.
    pass

fn=AutomaticFan()   #It will inherit from parent class which is first in list.
fn.buy()            #It will inherit from parent class which is first in list.