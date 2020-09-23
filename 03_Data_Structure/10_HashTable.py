#Now let’s understand how we can store the values in the key-value pair using the hash of its corresponding key. 
                        
# --> Hash table is a data structure that helps to map the keys to its value. 
# --> It is primarily an array which stores the reference to the actual value based on the hash. 
# --> In the hash table, hash refers to its index and the number of elements in the hash table is based on the hash function. 
# --> Thus hash table can be searched very quickly for the actual value based on the hash obtained from its key.

'''
#To begin with let’s consider hashing without collision:

        Value     Key  HashValue                                    HashTable  
          
        Israel    ISR     3                                            0        -->Canada
        Peru      PER     1                                            1        -->Peru
        India     IND     4                                            2        -->Fiji
        Fiji      FJI     2                                            3        -->Israel
        Canada    CAN     0                                            4        -->India
        
--> Here, we observe that since hash function takes a mod of 5, only possible values for hash are 0 to 4, 
--> hence the hash table can have only 5 elements.
'''

'''
#Hashing with collision:

        Value     Key  HashValue                   HashTable  
          
        Israel    ISR     3                            0        -->Canada(None)    #None represents Address here
        Peru      PER     1                            1        -->Peru(None)
        India     IND     4                            2        -->Fiji(None)
        Fiji      FJI     2                            3        -->Israel(None)
        Canada    CAN     0                            4        -->India()-->Sweden(None)  #This is LinkedList with 2 elements
        Sweden    SWE     4                                            
                
--> One of the techniques that can be used for handling collision is known as separate chaining. 
--> In this case, instead of hash table containing a reference to one value, it will maintain a reference to a linked list. 
--> When more than one key maps to the same hash, its values are added as nodes to the corresponding linked list.




#--> Now in Hashing with collision, suppose we want to find value corresponding to IND.
#--> How will you decide whether it is India or Sweden?

        HashTable  
          
            0        -->CAN,Canada(None)    #None represents Address here
            1        -->PER,Peru(None)
            2        -->FJI,Fiji(None)
            3        -->ISR,Israel(None)
            4        -->IND,India()-->SWE,Sweden(None)  #This is LinkedList with 2 elements
            
--> That means, it may not be sufficient to just store the value alone in the linked list, instead we have to store the key value pair as shown below. 
--> Here the key-value pair forms the data part of the linked list.
'''


# Operations possible on the hash table are put() and get().

# put(): This operation is used to put a key-value pair into the hash table based on the key and the hash.
# -->Algorithm Steps:-
# --> Identify the hash by applying the hash function on the given key
# --> Locate the hash in the hash table
# --> Create a new node with the given key-value pair to be linked to the hash
# --> Traverse through the linked list corresponding to the hash until its end
# --> Place the new node as the last node of the linked list



# get(): This operation is used to retrieve a value based on its key and hash.
# -->Algorithm Steps:-
# --> Identify the hash by applying the hash function on the given key
# --> Locate the hash in the hash table
# --> Search its corresponding linked list for a node with the given key
# --> When found, return its corresponding value
# --> If a node with key is not found, display "Node not found" and return


#Python dictionary is internally implemented as a HashTable.