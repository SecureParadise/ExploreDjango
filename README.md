# 1. Create Virtual Environment

python -m venv .VirtualEnvaramentName

eg :-) python -m venv .venv

##### Activate virtual Environment
###### Windows
.venv/Scripts/activate
###### Mac/Linux
source .venv/Scripts/activate
###### deactivate :- to deactivate virtual environment

## 2. Install Django
pip install Django
### Create porject
django-admin startproject PROJECTNAME
### Run porject
python manage.py runserver

# DJANGO FLOW
![alt text](image.png)
![alt text](image-1.png)

since it is a framework,so name should be as same as in the diagram.

-->We have to create "views.py" mannualy

--> No "view.py" or nay other name

# Session 2
Create views.py in /DjamgoProj/DjamgoProj

# views.py
from django.http import HttpResponse
--> render mean to send html page, django.shorcuts is very powerful
from django.shortcuts import render

def home(request):
    # return HttpResponse("Hello,Dear !,It's Our home")
    -->after django.shortcuts render
    return render(request,'websites/index.html')
    --> websites/index.html is from templete path

def About(request):
    return HttpResponse("Hello,Dear !,You dont know about me")
def Contact(request):
    return HttpResponse("Hello,Dear !,Give me yor contact Number")

# urls.py
Import views.py
from . import views
 " . " mean from current directory

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('about/',views.About,name='about'),
    path('contact/',views.Contact,name='contact'),
]
## create folder "templates","static"

## templates directory
--> file index.html
--> css injecton:templete engine
<link rel="stylesheet" href="{% static 'style' %}">

## settings.py
import os
TEMPLETES =[
    {
        'DIRS' : ['templates'],
    }
]

#STATIC_URL = 'static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR,'static')]

## Static
--> style.cssf

# Jinja2 and web app