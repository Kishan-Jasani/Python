# You can define functions to provide the required functionality. Here are simple rules to define a function in Python.

#--> Function blocks begin with the keyword def followed by the function name and parentheses ( ( ) ).
#--> Any input parameters or arguments should be placed within these parentheses. You can also define parameters inside these parentheses.
#--> The first statement of a function can be an optional statement - the documentation string of the function or doc string.
#--> The code block within every function starts with a colon (:) and is indented.
#--> The statement return [expression] exits a function, optionally passing back an expression to the caller. 
#--> A return statement with no arguments is the same as return None.


def calculate_sum(num1,num2):
    result = num1 + num2
    return result

res = calculate_sum(10, 5)

print(res)