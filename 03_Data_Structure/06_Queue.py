# --> Queue follows First-In-First-Out (FIFO) principal:
# example:-
# --> Queue at multiplex for movie ticket.

# Operations possible on the Queues are:
# --> En-queue or add an element to the end of the queue
# --> De-queue or remove an element from the front of the queue

class Queue:
    def __init__(self,max_size):  #max_size is maximum number of element expected in the queue
        self.__max_size=max_size
        self.__elements = [None]*self.__max_size  #Elements of the queue are stored in the python List.    
        self.__rear= -1            #rear indicates the index of last element of queue. We assumes that rear it is -1 when queue created.
        self.__front = 0           #front indicates the index of first element of queue. We assumes that front it is 0 when queue created.
    
    def enqueue(self,data):
        if(self.is_full()):
            print("Queue is full!!!")
        else:
            self.__rear+=1
            self.__elements[self.__rear]=data
    
    def dequeue(self):
        if(self.is_empty()):
            print("Queue is empty!!!")
        else:
            data=self.__elements[self.__front]
            self.__front+=1
            return data

queue1=Queue(5)
#Enqueue all the required element(s).
queue1.enqueue("Tom")
queue1.enqueue("Dick")
queue1.enqueue("Harry")
queue1.enqueue("Jack")
queue1.enqueue("Maria")
#Dequeue all the required element(s).
data=queue1.dequeue()


# The functions associated with queue are:
# --> Enqueue : Adds an item to the queue. If the queue is full, then it is said to be an Overflow condition.
# --> Dequeue : Removes an item from the queue. The items are popped in the same order in which they are pushed. If the queue is empty, then it is said to be an Underflow condition.
# --> Front   : Get the front item from queue.
# --> Rear    : Get the last item from queue.
    

# enqueue (data) operation to add data in queue:-
# --> 1. Check whether queue is full. If full, display appropriate message
# --> 2. If not,
# -->    a. increment rear by one
# -->    b. Add the element at rear position in the elements array


# dequeue()
# --> 1. Check whether the queue is empty. If it is empty, display appropriate message
# --> 2. If not,
# -->    a. Retrieve data at the front of the queue
# -->    b. Increment front by 1
# -->    c. Return the retrieved data


#How to convert Queue to List:-
lst = []
for i in queue1:
    lst.append(queue1.dequeue())
    
#How to convert List to Queue:-
for i in lst:
    queue1.enqueue(i)
