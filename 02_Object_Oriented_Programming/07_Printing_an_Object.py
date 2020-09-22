# --> For a more readable output when printing an object we can use the inbuilt special __str__ method. 
# --> This method MUST return a string and this string will be used when the object is printed. 
# --> This is useful in debugging as we can print the values of the attributes.

#Example1:
class Shoe:
    def __init__(self, price, material):
        self.price = price
        self.material = material

s1=Shoe(1000, "Canvas")
print(s1) #Observe the result in console. Is it Readable?

# What can we do for Readable output? Refer Example2.


#Example2:
class Shoe1:
    def __init__(self, price, material):
        self.price = price
        self.material = material

    def __str__(self):
        return "A pair of shoe with price Rs. " + str(self.price) + " and material of shoe is " + self.material

s2=Shoe1(1000, "Canvas")
print(s2) #Observe the result in console. Is it Readable?



#Example3:
class Shoe2:
    def __init__(self, price, material):
        self.price = price
        self.material = material
    def __repr__(self):
        return "A pair of shoe with price Rs. " + str(self.price) + " and material of shoe is " + self.material

s3=Shoe2(1000, "Canvas")
print(s3)