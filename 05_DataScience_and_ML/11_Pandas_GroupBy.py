import pandas as pd

# Create dataframe
data = {'Company':['GOOG','GOOG','MSFT','MSFT','FB','FB'],
       'Person':['Sam','Charlie','Amy','Vanessa','Carl','Sarah'],
       'Sales':[200,120,340,124,243,350]}
df = pd.DataFrame(data)
print(df)

#Group By Function
byComp = df.groupby('Company')
print(byComp.mean())
print(byComp.sum())
print(byComp.std())
print(byComp.count())

#Indexing
print(byComp.sum().loc['FB'])

#Describe Everything
print(byComp.describe())
print(byComp.describe().transpose())