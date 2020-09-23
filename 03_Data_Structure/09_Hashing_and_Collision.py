#--> Hashing is the process of transforming a set of characters (key) into a shorter fixed length integer value. 
#--> This shorter fixed length integer value which represents the original set of characters (key) is known as hash value or hash. 
#--> A hash function will be used to generate the hash value from the original set of characters (key). 
#--> Various algorithms may be used to arrive at the hash function.

#--> Suppose we have a key-value pair as shown below. 
#--> Here key is the three letter abbreviation of country names and value is the corresponding country name.  
'''
            Input(Key)        Value

              ISR             Israel
              PER             Peru
              IND             India
              FJI             Fiji
              CAN             Canada
'''

#Hash values corresponding to each key can be generated as shown below:(Here, Hash Function is h(k)= k%5.  )
'''
Key(Input)     Value                Hash(Output)

ISR            Israel      (ord("I")+ord("S")+ ord("R"))%5         (73+83+82)%5    238%5    3
PER            Peru        (ord("P")+ ord("E") + ord("R"))%5       (80+69+82)%5    231%5    1
IND            India       (ord("I")+ord("N")+ ord("D"))%5         (73+78+68)%5    219%5    4
FJI            Fiji        (ord("F")+ord("J") +ord("I"))%5         (70+74+73)%5    217%5    2
CAN            Canada      (ord("C")+ord("A") +ord("N"))%5         (67+65+78)%5    210%5    0
SWE            Sweden      (ord("S")+ord("W") +ord("E"))%5         (83+87+69)%5    239%5    4
'''

#Points to Note:
#--> Hash function will always generate the same hash value (output) for a given key (input).
#--> Keys have to be unique.
#--> A given key will have only one value in the key-value pair.

#--> What is Collision?
#Can you observe something?
#--> Two keys (IND and SWE) have generated the same hash value. 
#--> That means hash function may compute same hash value for multiple keys and this is known as collision in hashing. 
#--> This occurs because the number of possibilities in input (key) is much greater than the number of possibilities in the output (hash value).

#In this example, 
#--> three letter abbreviation exists for all the countries in the world whereas the hash value can be only between 0 and 4, both inclusive.
#--> Collisions are inevitable, however number of collisions depends on the goodness of the hash function.