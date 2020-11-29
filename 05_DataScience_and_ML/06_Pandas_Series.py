import numpy as np
import pandas as pd

labels = ['a','b','c']
my_data = [10,20,30]
arr = np.array(my_data)
d= {'a':10,'b':20,'c':30}

#create a series with index starting from zero
print(pd.Series(data = my_data))

#We can specify index as labels
print(pd.Series(data = my_data, index=labels))
print(pd.Series(my_data, labels))
print(pd.Series(arr, labels))

#Create series from dictionary
print(pd.Series(d))

#Using as Index
ser1 = pd.Series([1,2,3,4],index = ['USA', 'Germany','USSR', 'Japan'])   
print(ser1)
ser2 = pd.Series([1,2,5,4],index = ['USA', 'Germany','Italy', 'Japan'])     
print(ser2)
print(ser1['Germany'])
print(ser2['Italy'])

#Sum of 2 Series:-
#--> Sum happens as per index Number
print(ser1 + ser2)