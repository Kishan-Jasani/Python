'''
How to create Project:-
-----------------------
django-admin startproject ProjectName


How to run server:-
--------------------
py manage.py runserver
python manage.py runserver


How to change Port Number:-
-----------------------------
py manage.py runserver 8888
python manage.py runserver 8888


how to start Application:-
-------------------------
py manage.py startapp ApplicationName
python manage.py startapp ApplicationName


Folder Structure of Django Applicaton:-
---------------------------------------
firstProject
    -----manage.py
    -----db.sqlite3
    -----firstProject
                -----__pycache__
                -----__init__.py
                -----asgi.py
                -----settings.py
                -----settings.py
                -----urls.py
                -----wsgi.py
    -----testApp
                -----migrations
                            -----__init__.py
                -----__init__.py
                -----admin.py
                -----apps.py
                -----models.py
                -----tests.py
                -----views.py
                
                
                
                
                
Steps to follow:-
------------------
1) Start Project
--> django-admin startproject ProjectName

2) Go inside ProjectName folder
---> cd ProjectName

3) create template folder in our main project folder, inside template folder create folder with name as Application name, 
   Put all html files (template files) there. 

4) create static folder inside main project and add images and css folder inside static folder
    create new list with name STATICFILES_DIRS = []
    {%load static%} after <!DOCTYPE html>
    <img src="{%static "images/4553fb4cf80f13c52e56002f7180e13c.png" %}">
    <link rel="stylesheet" href="{%static "css/design.css" %}">

5) Start Application
--> py manage.py startapp AppName

6) Add AppName inside INSTALLED_APPS list in settings.py
--> INSTALLED_APPS = ['AppName']

7) import os and Add tempate folder path inside settings.py and add TEMPLATE_DIR inside DIRS list.
--> TEMPLATE_DIR = os.path.join(BASE_DIR,'templates')
--> 'DIRS': [TEMPLATE_DIR]

8) import HttpResponse and define view function inside view.py
--> from django.http import HttpResponse
--> def matrimonial(request):
        dt=datetime.datetime.now()
        my_dict={'date':dt}
        return render(request,'Matrimonial/home.html',my_dict)

9) define url pattern inside urls.py
--> urlpatterns = [ path('matrimonial/', views.matrimonial),]

10) Run server

11) Send Request




Methods to learn-
-----------------
1) How to change Port number?
--> py manage.py runserver 8888

2) How to defile url patterns at application level?
--> create urls.py at application level
--> import include
--> urlpatterns = [ path('testapp1/', include('testapp1.urls')),]    

3) How to use dynamic content in html files?
--> def matrimonial(request):
        dt=datetime.datetime.now()
        my_dict={'date':dt}
        return render(request,'Matrimonial/home.html',my_dict)
--> mention {{date}} inside html file

4) {%  %} --> Jinja2



For Database connection:-
-------------------------
1)define model class by extending models.Model inside models.py
2)py manage.py makemigrations
3)py manage.py sqlmigrate databaseapp 0001 (Not mandatory)
4)py manage.py migrate
5)register table inside admin.py
6)create user

Create User:-
-------------
py manage.py createsuperuser
'''