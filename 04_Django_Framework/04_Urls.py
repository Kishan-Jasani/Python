'''
urls.py:-
----------
--> To call the view function we have to specify end user in urls.py
--> urls can be used by end user to send request to our view function.


from django.contrib import admin
from django.urls import path
from testapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', views.hello_world_view),
    path('datetime/', views.date_time_view),
]



--> We can create urls.py at applications levels also and provide link of this at project level
'''