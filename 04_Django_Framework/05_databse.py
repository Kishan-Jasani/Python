'''
How to check database connection:-
----------------------------------
>>> py manage.py shell
>>> from django.db import connection
>>> c=connection.cursor()


Migrations:-
-----------
>>> py manage.py makemigrations

>>> py manage.py sqlmigrate databaseapp 0001 (Not mandatory)

>>> py manage.py migrate
'''