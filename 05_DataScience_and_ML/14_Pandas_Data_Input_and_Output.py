'''
#Files we will work with
#--> CSV,Excel,HTML,SQL

--> We need to install below 4 libraries
    conda install sqlalchemy
    conda install lxml
    conda install html5lib
    conda install BeautifulSoup4
'''

import numpy as np
import pandas as pd

#read CSV
df = pd.read_csv('example.csv')
print(df)

#read Excel
df = pd.read_excel('Excel_Sample.xlsx',sheetname='Sheet1')
print(df)

#read HTML
df = pd.read_html('http://www.fdic.gov/bank/individual/failed/banklist.html')
print(df[0])

#read SQL
from sqlalchemy import create_engine

engine = create_engine('sqlite:///:memory:')
df.to_sql('data', engine)
sql_df = pd.read_sql('data',con=engine)
print(sql_df)