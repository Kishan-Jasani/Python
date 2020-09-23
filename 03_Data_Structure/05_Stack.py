# --> Stack follows Last-In-First-Out (LIFO) principal:
# example:-
# --> Undo-Redo operation in any application.
# --> Lift

# Operations possible on the stack are:
# --> Push or insert an element to the top of the stack
# --> Pop or remove an element from top of the stack

class Stack:
    def __init__(self,max_size):  #max_size is maximum number of element expected in the stack
        self.__max_size=max_size
        self.__elements = [None]*self.__max_size  #Elements of the Stack are stored in the python List.    
        self.__top= -1            #top indicates the index of top most element of stack. We assumes that top is -1 when the stack is created.
    
    def push(self,data):
        if(self.is_full()):
            print("The stack is full!!")
        else:
            self.__top+=1
            self.__elements[self.__top]=data

    def pop(self):
        if(self.is_empty()):
            print("The stack is empty!!")
        else:
            data= self.__elements[self.__top]
            self.__top-=1
            return data
        
stk = Stack()
stk.push("A")
stk.push("B")
stk.push("C")
stk.pop()

# The functions associated with stack are:
# --> empty() – Returns whether the stack is empty.
# --> size()  – Returns the size of the stack.
# --> top()   – Returns a reference to the top most element of the stack.
# --> push(g) – Adds the element ‘g’ at the top of the stack.
# --> pop()   – Deletes the top most element of the stack.     
       
        
# push(data) algorithm for add element to the top of the stack:
# --> 1. Check whether the stack is full. If full, display appropriate message
# --> 2. If not,
# -->    a. increment top by one
# -->    b. Add the element at top position in the elements array


# pop algorithm for remove an element from top of the stack:
# --> 1. Check whether the stack is empty. If empty, display appropriate message
# --> 2. If not,
# -->    a. Retrieve data at the top of the stack
# -->    b. Decrement top by 1
# -->    c. Return the retrieved data



#How to convert Stack to List:-
lst=[]
for i in stk:
    lst.append(stk.pop())
    
#How to convert List to Stack:-
for i in lst:
    stk.push(i)
    