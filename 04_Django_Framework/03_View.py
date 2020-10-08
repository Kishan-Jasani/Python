'''
views.py:-
----------
--> View is responsible to provide the HTTP response to user after getting HTTP request in server.
--> View hears HTTP request.
--> View sends HTTP response.

                                    ----------------
HTTP request ---------------------->|     View     |----------------------> HTTP Response
                                    ----------------
                                    

Types of Views:-
----------------
1) Function based Views
2) Class based Views     



Function based Views:-
----------------------
from django.shortcuts import render
from django.http import HttpResponse
import datetime

def hello_world_view(request):
    return HttpResponse("<h1>This is response from Django Application</h1>") 
    
def date_time_view(request):
    date=datetime.datetime.now()
    s="<h1>The current date and time at the server is: "+str(date)+"</h1>"
    return HttpResponse(s)


--> We can write below code in views.py and write {{date}} in html file.
------------------------------------------------------------------------

def matrimonial(request):
    dt=datetime.datetime.now()
    my_dict={'date':dt}
    return render(request,'Matrimonial/home.html',my_dict)                              
'''