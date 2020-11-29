import pandas as pd

#Create Data Frame
df = pd.DataFrame({'col1':[1,2,3,4],'col2':[444,555,666,444],'col3':['abc','def','ghi','xyz']})
print(df)

#Get a series of unique numbers
print(df['col2'].unique())

#Get a size of series of unique numbers
print(df['col2'].nunique())

#Count of values in series
print(df['col2'].value_counts())


#Selecting Data:-
print(df[df['col1']>2])
print(df[(df['col1']>2) & (df['col2']>555)])

#Applying Functions:-
def times2(x):
    return x*2

print(df['col1'].apply(times2))
print(df['col3'].apply(len))
print(df['col2'].apply(lambda x:x*2))

#Deop Column
print(df.drop('col1',axis=1,inplace=False))

#Get Column names and index
print(df.columns)
print(df.index)

#Sorting
print(df.sort_values('col2'))

#Null Check
print(df.isnull())




#Example-2
data = {'A':['foo','foo','foo','bar','bar','bar'],
     'B':['one','one','two','two','one','one'],
       'C':['x','y','x','y','x','y'],
       'D':[1,3,2,5,4,1]}

df = pd.DataFrame(data)
print(df)
print(df.pivot_table(values='D',index=['A', 'B'],columns=['C']))
print(df)