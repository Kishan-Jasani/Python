# --> In real life objects interact with other objects. 
# --> For example, a Customer object buys a mobile object. Therefore, it must be true in OOP as well. 
# --> So far, we have been creating classes and objects which don’t interact with other objects. 
# --> Now we will take a look at how to create objects which have some relationship with other objects.


# --> In your opinion what is the best way to describe the relationship between these two classes?
'''
                ---------------                ---------------
                |   Customer  |                |   Address   |
                ---------------                ---------------
                
                A. Customer is an address
                B. Address is a Customer
                C. Customer has an Address
                D. Address has a Customer
'''
'''
                ---------------                ---------------
                |   Product   |                |   Mobile    |
                ---------------                ---------------
                
                A. Product is a Mobile
                B. Mobile is a Product
                C. Product has a Mobile
                D. Mobile has a Product
'''
'''
                ---------------                ---------------
                |   Customer  |                |   Address   |
                ---------------                ---------------
                
                A. Customer can have only one address
                B. Customer can have many addresses
                C. Address can have only one customer
                D. Address can have many customers
'''
'''
                ---------------                ---------------
                |   Customer  |                |   Address   |
                ---------------                ---------------
                
                A. Customer has an Address. But if the Customer is no more, then the Address will also be no more
                B. Customer has an Address. If the Customer is no more, still the Address can continue to exist              
'''
'''
                ---------------                ---------------
                |   College   |                |  Department |
                ---------------                ---------------
                
                A. College has a department and if the College is closed, then the department also gets closed
                B. College has a department and if the College is closed the department still continues to run            
'''




# Types of Relationships:-

# --> Inheritance - When one object is a type of another object
# --> Example - Mobile is a Product

# --> Aggregation - When one object owns another object, but they both have independent life cycle
# --> Example - Customer has an Address. Even if the Customer is no more, there may be other customers in that address. So Address continues to exist even after a customer is no more

# --> Composition - When one object owns another object, but they both have same life cycle
# --> Example - College has a department. If the college closes, the department is also closed.