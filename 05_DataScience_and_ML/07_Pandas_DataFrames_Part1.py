import numpy as np
import pandas as pd
from numpy.random import randn

np.random.seed(101)

#Create random data frame
df = pd.DataFrame(randn(5,4),['A','B','C','D','E'],['W','X','Y','Z'])
print(df)

#Selecting Colums
print(df['W'])
print(df[['W','Z']])

#Selecting rows
print(df.loc['C'])
print(df.iloc[2])
print(df.loc[['C','D']])
print(df.iloc[[2,3]])

#Get a value using Indexing
print(df.loc['B','Y'])
print(df.loc[['B','C'],['Y','Z']])

#Types
print(type(df['W']))
print(type(df))

#Add New Colums
df['New'] = df['W'] + df['X']
print(df)

#Remove Column (Axis will be 1 while removing Column)
df.drop('New',axis=1)                 #This will not affect main Data Frame. 
df.drop('New',axis=1,inplace=True)    #This will affect main Data Frame also. 

#Remove Row (Axis will be 0 while removing Row. No need to pass Axis because default value of axis is 0)
df.drop('E')                        #This will not affect main Data Frame. 
df.drop('E',inplace=True)           #This will affect main Data Frame also. 

#To check Data Frame Size
print(df.shape)

