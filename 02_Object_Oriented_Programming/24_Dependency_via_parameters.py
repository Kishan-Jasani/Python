# Dependency Via Formal parameter-
# --> Sometimes a class may depend on another class for some of its use. 
# --> This is not a strict relationship and hence won’t appear in the class diagram. 
# --> For example, in the below code, the Customer class depends on a payment object for purchasing. 
# --> Here payment is a local variable and not an attribute.

class Customer:
    def __init__(self, name, age, phone_no):
        self.name = name
        self.age = age
        self.phone_no = phone_no

    def purchase(self, payment):
        if payment.typ == "card":
            print ("Paying by card")
        elif payment.typ == "e-wallet":
            print ("Paying by wallet")
        else:
            print ("Paying by cash")

class Payment:
    def __init__(self, typ):
        self.typ = typ

payment1=Payment("card")
c=Customer("Jack",23,1234)

c.purchase(payment1)






# Dependency Via Local Object-
# --> Apart from an object being passed as a parameter to the method, we can also create an object locally inside a method. 
# --> This again is a weaker dependency which does not reflect in the class diagram.
# --> Also, sometimes we may access the static values of another class directly in our method. 
# --> This again is a weaker relationship.

#Object creation
class Customer1:
    def __init__(self, name,cust_type,bill):
        self.name = name
        self.bill = bill
        self.cust_type=cust_type
    def calulate_bill(self):
        tax1=Tax(self.cust_type)
        final_bill=self.bill*tax1.tax_details(self.cust_type)
        return final_bill
class Tax:
    def __init__(self,cust_type):
        self.cust_type=cust_type
    def tax_details(self,cust_type):
        if(cust_type=="Student"):
            return 5
        else:
            return 10
cust1=Customer1("Maddy","Student",100)
print(cust1.calulate_bill())


#Usage of static
class CustomerCare:
    helpline=111000
class Customer2:
    def call_support(self):
        print("Calling ",CustomerCare.helpline)
Customer2().call_support()
