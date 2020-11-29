# Multiple Indexing
#--------------------------------

import numpy as np
import pandas as pd
from numpy.random import randn

#Index Levels
outside = ['G1','G1','G1','G2','G2','G2']
inside = [1,2,3,1,2,3]
hier_index = list(zip(outside,inside))
hier_index = pd.MultiIndex.from_tuples(hier_index)
print(hier_index)

df = pd.DataFrame(np.random.randn(6,2),index=hier_index,columns=['A','B'])

#Slicing and Indexing
print(df.loc['G1'])
print(df.loc['G1'].loc[1])

#Set a name for Index
df.index.names = ['Groups','Names']
print(df)

#Get Specified value
print(df.loc['G2'].loc[2]['B'])

#Another way of slicing using cross section xs method
print(df.xs('G1'))
print(df.xs(1,level='Names'))