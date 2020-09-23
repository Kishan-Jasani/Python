# --> A linked list consists of a group of nodes which together represent a sequence or a list. 
# --> Each node will have a data part which holds the actual data and an address part which holds the link to the next node. 
# --> The first node in the list is known as head node and the last node is known as tail node. 
# --> Unlike array, in linked list, the nodes need not be stored in contiguous memory locations.


class Node:
    def __init__(self,data):        #data to be stored in the node.
        self.__data=data            #Data part of the node
        self.__next=None            #Address/Link part of the node
        
    def get_data(self):
        return self.__data

    def set_data(self,data):
        self.__data=data

    def get_next(self):
        return self.__next

    def set_next(self,next_node):
        self.__next=next_node

        
item_node = Node("Sugar")           #Create node with data as Sugar and address as None.
print(item_node.get_data())       





# --> To link the nodes and create a linked list, let’s create a new class, LinkedList with two attributes, head and tail both initialized to None as shown below.

class LinkedList:
    def __init__(self):
        self.__head=None
        self.__tail=None
    def get_head(self):
        return self.__head
    def get_tail(self):
        return self.__tail
    
    def add(self,data):
        new_node=Node(data)
        if(self.__head is None):
            self.__head=self.__tail=new_node
        else:
            self.__tail.set_next(new_node)
            self.__tail=new_node
    
    def display(self):
        temp=self.__head
        while(temp is not None):
            print(temp.get_data())
            temp=temp.get_next()
    def insert(self,data,data_before):
        new_node=Node(data)
        if(data_before==None):
            new_node.set_next(self.__head)
            self.__head=new_node
            if(new_node.get_next()==None):
                self.__tail=new_node

        else:
            node_before=self.find_node(data_before)
            if(node_before is not None):
                new_node.set_next(node_before.get_next())
                node_before.set_next(new_node)
                if(new_node.get_next() is None):
                    self.__tail=new_node
            else:
                print(data_before,"is not present in the Linked list")

    def find_node(self,data):
        temp=self.__head
        while(temp is not None):
            if(temp.get_data()==data):
                return temp
            temp=temp.get_next()
        return None

    def delete(self,data):
        node=self.find_node(data)
        if(node is not None):
            if(node==self.__head):
                if(self.__head==self.__tail):
                    self.__tail=None
                self.__head=node.get_next()
            else:
                temp=self.__head
                while(temp is not None):
                    if(temp.get_next()==node):
                        temp.set_next(node.get_next())
                        if(node==self.__tail):
                            self.__tail=temp
                        node.set_next(None)
                        break
                    temp=temp.get_next()
        else:
            print(data,"is not present in Linked list") 
            
biscuit_list=LinkedList()
biscuit_list.add("Goodday")
biscuit_list.add("Bourbon")
biscuit_list.add("Hide&Seek")
biscuit_list.add("Nutrichoice")
biscuit_list.display()


# Display algorithm of LinkedList:-
# --> display()
# --> 1. Call the head node as temp
# --> 2. While temp is not None,
# -->    a. Display temp’s data
# -->    b. Make the next node as temp



# Add algorithm of LinkedList:-
# --> add(data)
# --> 1. Create a new node with the data
# --> 2. If the linked list is empty (head node is not referring to any other node), 
# -->    make the head node and the tail node refer to the new node
# --> 3. Otherwise,
# -->    a. Make the tail node’s link refer to new node
# -->    b. Call the new node as tail node



# Insert algorithm of LinkedList:-
# --> insert(data,data_before)
# --> 1. Create a new node with the given data
# --> 2. If the data_before is None,
# -->     a. Make the new node's link refer to head node 
# -->     b. Call the new node as head node
# -->     c. If the new node's link is None, make it the tail node
# --> 3. Else
# -->     a. Find the node with data_before, once found consider it as node_before
# -->     b. Make the new node’s link refer to node_before’s link.
# -->     c. Make the node_before’s link refer to new node
# -->    d. If new node’s link is None, make it the tail node
# --> 4. If node with data_before is not found, display appropriate error message



# Delete algorithm of LinkedList:-
# --> delete(data):
# --> 1. Find the node with the given data. If found,
# -->    a. If the node to be deleted is head node, make the next node as head node
# -->       1. If it is also the tail node, make the tail node as None
# -->    b. Otherwise,
# -->       1. Traverse till the node before the node to be deleted, call it temp
# -->       2. Make temp’s link refer to node’s link.
# -->       3. If the node to be deleted is the tail node, call the temp as tail node
# -->       4. Make the node's link as None
# --> 2. If the node to be deleted is not found, display appropriate error message
