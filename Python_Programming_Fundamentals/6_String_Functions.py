# --> String accepts alphabetical, characters or alpha numerical values.
# --> Indexing works in string

# --> Define string
str1 = "kishan Jasani"
str2 = "1234"

# --> length of string
print(len(str1))

# --> Count Function
print(str1.count('i'))

# --> Replace Function
print(str1.replace('j', 'J'))


# --> Find Function
print(str1.find('a'))  #Return index of first left element

# --> startswith and endwith Function
print(str1.startswith('K'))
print(str1.endswith('i'))


# --> isdigit and isalpha Function
print(str1.isalpha())
print(str2.isalpha())
print(str1.isdigit())
print(str2.isdigit())


# --> Upper and Lower Function
print(str1.upper())
print(str1.lower())


# --> Split Function
print(str1.split('a'))

# --> Capitalize and casefold Function
print(str1.capitalize())  #Capitalize first character of string
print(str1.casefold())    #Converts strings to case folded strings for caseless matching

# --> Find Index from both sides
print(str1.index('J'))  #Throws an error if substring not found
print(str1.rindex('a')) #Find index of most right sides element

# --> islower isupper Function
print(str1.isupper())
print(str1.islower())


# --> Swapcase Function
print(str1.swapcase())  #change the case of entire string

# --> strip, lstrip and rstrip Function
str3="malayalamm"
print(str3.strip("m"))      #Removes character from both side of string, if more than one present all removes
print(str3.lstrip("m"))     #Removes character from left side of string, if more than one present all removes
print(str3.rstrip("m"))     #Removes character from right side of string, if more than one present all removes