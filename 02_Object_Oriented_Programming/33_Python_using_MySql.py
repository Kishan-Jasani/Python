# --> Database programming with Python is very easy. 
# --> You just need 8 lines of code to insert a record into a database table from Python. 
# --> Take a look!

#https://lex.infosysapps.com/en/viewer/web-module/lex_auth_012999418611122176829?collectionId=lex_auth_01278069079858380860&collectionType=Course&viewMode=START

import mysql.connector

#Establishing a connection
con = mysql.connector.connect(host="sql12.freemysqlhosting.net",user="sql12367431",passwd="pNfdgreQmZ",database="sql12367431")

#Execute a query
cur = con.cursor()
#cur.execute("Insert into Employee (emp_id,emp_name,emp_designation,salary) values (1043290,'Manoj','Systems Engineer',29000)")
cur.execute("select * from Employee")


#Use the result of query
print(cur.rowcount)

#Clean up resources
cur.close()
con.commit()
con.close()




# MongoDB
#https://lex.infosysapps.com/en/viewer/web-module/lex_auth_012887542735896576661?collectionId=lex_auth_01278069079858380860&collectionType=Course&viewMode=START 


from pymongo import MongoClient
conn=MongoClient('mongodb://localhost:27017/')
db=conn['ETA']
col=db['student']
