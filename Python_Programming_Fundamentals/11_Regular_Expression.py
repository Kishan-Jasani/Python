# --> Regular expressions are a powerful language for matching text patterns. 
# --> This page gives a basic introduction to regular expressions themselves sufficient for our Python exercises and shows how regular expressions work in Python. 
# --> The Python "re" module provides regular expression support.

# Please use below url for detailed explanation on RegEx
# --> https://www.w3schools.com/python/python_regex.asp

import re

#Check if the string starts with "The" and ends with "Spain":
txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

if x:
    print("YES! We have a match!")  
else:
    print("No match")  
    

#Find all lower case characters alphabetically between "a" and "m":
txt = "The rain in Spain"
x = re.findall("[a-m]", txt)
print(x)

   
#Find all present elements in string   
txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)
  

#Find index of element in the string
txt = "The rain in Spain"
x = re.search("r", txt)
print("The first r character is located in position:", x.start()) 


#Split the string at every white-space character:
txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)


#Replace all white-space characters with the digit underscore
txt = "The rain in Spain"
x = re.sub("\s", "_", txt)
print(x)

