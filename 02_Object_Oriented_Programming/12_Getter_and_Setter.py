#--> To have a error free way of accessing and updating private variables, we create specific methods for this.

#--> The methods which are meant to set a value to a private variable are called setter methods
#--> The methods meant to access private variable values are called getter methods
#--> The below code is an example of getter and setter methods:

class Customer:
    def __init__(self, name, age, wallet_balance):        
        self.name = name
        self.age = age
        self.__wallet_balance = wallet_balance

    def set_wallet_balance(self, amount):
        if amount < 1000 and amount > 0:
            self.__wallet_balance = amount

    def get_wallet_balance(self):
        return self.__wallet_balance

c1=Customer("Gopal", 24, 1000)
c1.set_wallet_balance(120)
print(c1.get_wallet_balance())


# --> All setter methods must accept the value to be updated as a parameter and all getter methods must not have any parameter and they must return the value.
# --> Setter methods are called as mutator methods ( as they change or mutate the value ).
# --> Getter methods are called accessor methods ( as they access the values )