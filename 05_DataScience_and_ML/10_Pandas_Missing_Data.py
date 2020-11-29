import numpy as np
import pandas as pd

#Create data frame using dictionary
d={'A':[1,2,np.nan],'B':[5,np.nan,np.nan],'C':[1,2,3]}
df = pd.DataFrame(d)
print(df)

#Drop a column(axis=0 which is default) or row(axis=1) where one or more value is nan
# Below operation will not affect main data Frame since default inplace value is False
print(df.dropna(inplace=False))
print(df.dropna(axis=1,inplace=False))

#Set a threshold for minimum NA values
print(df.dropna(thresh=2))

#Fill NA values
print(df.fillna('Fill Value'))

#Set Mean value for NA value in particular column
print(df['A'].fillna(value=df['A'].mean()))