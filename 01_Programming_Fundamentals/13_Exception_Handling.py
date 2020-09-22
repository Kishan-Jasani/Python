#Example1
def calculate_expenditure(list_of_expenditure):
    total=0
    try:
        for expenditure in list_of_expenditure:
            total+=expenditure
        print("Total:",total)
        avg=total/num_values
        print("Average:",avg)
    except ZeroDivisionError:
        print("Divide by Zero error")
    except TypeError:
        print("Wrong data type")
    except:
        print("Some error occured")
list_of_values=[100,200,300,"400",500]
num_values=0
calculate_expenditure(list_of_values)



#Example2 - Finally block
balance=1000
amount="300Rs"
def take_card():
    print("Take the card out of ATM")
try:
    if balance>=int(amount):
        print("Withdraw")
    else:
        print("Invalid amount")

except TypeError:
    print("Type Error Occurred")
except ValueError:
    print("Value Error Occurred")
except:
    print("Some error Occurred")
finally:
    take_card()





# --> ZeroDivisionError :- When a value is divideo by zero
num_list=[]
total=10
avg=total/len(num_list)
print(avg)


# --> TypeError :- When we try to do an operation with incompatible data types
total=10
total+="20"


# --> NameError :- When we try to access a variable which is not defined
avg=total/10      #total is not defined


# --> IndexError :- When we try to access an index value which is out of range
num_list=[1,2,3,4]
value=num_list[4]


# --> ValueError :- When we use a valid data type for an argument of a built-in function but passes an invalid value for it
value="A"
num=int(value) #string is a valid data type for int() but the value “A” is invalid, as "A" can't be converted into int.