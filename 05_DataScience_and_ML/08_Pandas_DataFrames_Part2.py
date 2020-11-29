import numpy as np
import pandas as pd
from numpy.random import randn

np.random.seed(101)

#Create random data frame
df = pd.DataFrame(randn(5,4),['A','B','C','D','E'],['W','X','Y','Z'])
print(df)

#Get Condition Data Frames:-
print(df > 0)
print(df[df>0])

#Get Slice with condition
print(df['W']>0)
print(df[df['W']>0])

#Get Slice with multiple conditions
print(df[(df['W']>0) & (df['X']>0)])
print(df[(df['W']<0) | (df['X']<0)])

#How to reset Index
df.reset_index(inplace=True)
print(df)

#Add New Column
newind = 'CA NY WY OR CO'.split()
print(newind)
df['States'] = newind
print(df)

#How to set Index
df.set_index('States',inplace=True)
print(df)
