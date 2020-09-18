#Why we need Encapsulation(Privacy)?
# Refer below scenarios


#Let's think about scenario of bank where customer can deposit amount till 1000. Refer below code.
class Customer:
    def __init__(self, cust_id, name, age, wallet_balance):
        self.cust_id = cust_id
        self.name = name
        self.age = age
        self.wallet_balance = wallet_balance

    def deposit_balance(self,amount):
        if amount <= 1000 and amount > 0:
            self.wallet_balance += amount

    def show_balance(self):
            print("The balance is :",self.wallet_balance)
            
#Example-1
c1=Customer(100, "Gopal", 24, 1000)
c1.deposit_balance(500)
c1.show_balance()
# deposit_method works as expected in Example-1.


#Example-2
c2=Customer(100, "Gopal", 24, 1000)
c2.wallet_balance = 10000000000
c2.show_balance()
# In Example-2, anyone can update wallet_balance Attributes of class, without entering into deposit_balance method. 
# What do you think? Is it Safe for any bank?
# Don't you think, Safety is required here?

# Similarly, Locking and privacy is essential in most of the real life scenarios. That is why Encapsulation comes in to picture.