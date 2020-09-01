#--> Simple if
a=10
if(a==10):
    print("Positive Integer")
   
    
#--> If else 
b=-10
if(b>0):
    print("Positive")
else:
    print("Non Positive")
    

#--> Else-if-ladder
c=0
if(c>0):
    print("Positive")
elif(c<0):
    print("Negative")   
else:
    print("Zero")
    

#--> Nested If
num1=10
num2=20
num3=30
if(num1>num2):
    if(num1>num3):
        print("num1 is largest")
    else:
        print("num3 is largest")
elif(num2>num3):
    print("num2 is largest")
else:
    print("num3 is largest")
    
    

#--> While Loop
num=5
count=1
while(count<=num):
    print("Number is: ",count)
    count+=1

#--> While Loop
counter=0
while(counter<=9):
    if(counter%2==0):
        pass
    else:
        print(counter)
    counter+=1
    
#--> For loop
for number in 1,2,3,4,5:
    print("The current number is ",number)
for number in range(1,5):
    print ("The current number is ",number)
for number in range(1,7,2):
    print ("The current number is ",number)
for number in range(5,0,-1):
    print ("The current number is ",number)

#--> For loop
start=1
end=10
step=2   
for m in range(start,end,step):
    print("Number is: ",m)
    
    
#--> Nested loop
for i in 1,2,3:
    for j in 1,2,3:
        print(i,j)
        
#--> break statement
for i in 1,2,3,4,5,6,7:
    if(i==4):
        print("4 Found")
        break
 
    
#--> Continue statement
for i in 1,2,3,4,5,6,7:
    if(i!=4):
        continue
    else:
        print("4 Found")
        break