# --> Positional Argument:- Order, Count, Type of argument should exactly match. Else, it will throw error
def func1(arg1,arg2):
    result=arg1+arg2
    return result
print(func1(10, 15))
print(func1("Kishan", "Jasani"))


# --> Keyword Argument:- Allow flexibality in the order of passing argument by mentioning argument name
def func2(arg1,arg2,arg3):
    result=arg1+arg3+arg2
    return result
print(func2(arg2="Kishan", arg1="Jasani",arg3=" "))


# --> Default Argument:- Allow to specify default value while nothing is passed for specific argument. Default argument should be last in the order.
def func3(arg1="Kishan",arg2=" Jasani"):
    result=arg1+arg2
    return result
print(func3("Kishan"))
print(func3())


# --> Variable argument count:- Allow functionality to have variable number of argument. Argument starting with '*' will have variable number of argument. It should be last in the order.
def func4(arg1,arg2,*arg3):
    result=arg1+arg2
    for i in arg3:
        result+=i
    return result
print(func4("Kishan"," ","Anilbhai"," ","Jasani"))