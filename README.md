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
single urls.py is project urls.py

_--> multiple one inside a table is app's urls.py

project urls.py hit app's urls.py 
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
## By this django understand that every single apps have a templetes folder if not then there is tempaltes inside root directory

#STATIC_URL = 'static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR,'static')]

## Static
--> style.cssf

# Jinja2 and web app
--> "startproject" only one time during initilization of project

--> https://docs.djangoproject.com/en/5.0/topics/templates/
--> https://jinja.palletsprojects.com/en/3.1.x/


(.DjangoEnv) PS S:\Learning\WEB DEV\DJANGO\ParadiseExplore\DjangoProj> python manage.py startapp pastha

# settings.py
--> make aware of app to project
 -->INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
 ]

 --> these above apps are cooked in apps/file ,mean someone other have created it and we are using it

 --> add
 INSTALLED_APPS = [
    'pastha',
 ]
 --> now we have sucessfully configured a app

--> every app is a standalone app in itself,so many people prefer to have their templete inthe apps itself(most  prefareble)
/pastha/tempaltes/pastha/all_pastha.html
--> press( ctrl + ,) goto setting > search emmit>Emmet:Include Languages>Add Item "django-html" value = "html"
    --> after that we will get all django emmit html suggestation

-->also people prefer to make apps folder inside tempaltes.i.e--> templates/pastha/..

## Focus On Jinja

--> /pastha/tempaltes/pastha/all_pastha.html

### pastha/views.py
def all_pastha(request):
    return render(request,'pastha/all_pastha.html')

--> copy all the content of /DjangoProj/DjangoProj/urls.py
i.e
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('about/',views.About,name='about'),
    path('contact/',views.Contact,name='contact'),
    ..> added for app, control trasfer to pastha
    path('pastha/',include('pastha.urls')),



    path("__reload__/",include("django_browser_reload.urls")),
]

--> create pastha/urls.py
 add:

 urlpatterns = [
     path('',views.all_pastha,name='pastha'),
 ]
 --> remove admin header module inside pastha/urls.py since its not our responsibilty
 

-->create templates/layout.html

    -->layout.html is our template , we we need not to write our same html to every single page
in top of html page use 
{% load static %}

### html attribute django
load

block

block unnamed

### templete/appname/index.html
{% extends "layout.html" %}

{% block title %}
Home Page
{% endblock %}

{% block content %}

 Django 

{% endblock %}


# Tailwind CSS and  Admin pannel 

<h1> TailWind CSS Installation </h1>

pip install django-tailwind

--> for hot reloading

pip install 'django-tailwind[reload]'

## Install pip
python -m ensurepip --upgrade (works 90%)

python -m pip install --upgrade

add --> "tailwind" in 'settings.py 'INSTALLED_APPS'

--> python manage.py tailwind init
some packege will be download which thake some time
--> it will ask for name,you can skip by pressing inter or just assign name

By default name is theme

Now add 'theme',  in setings.py's 'INSTALLED_APPS' section

ADD

TAILWIND_APP_NAME = 'theme'
INTERNAL_IPS = ['127.0.01']

 -->For error handling, to run css we need nodeJS
    --> node pathe, where npm in terminal
        --> In order to handle space in path use r"windows_path"
 NPM_BIN_PATH = r"C:\Program Files\nodejs\npm.cmd"
#### python  manage.py tailwind install
--> /DjangoProj/DjangoProj/theme 
NPM_BIN_PATH = r"C:\Program Files\nodejs\npm.cmd"
is generated

In /theme/tempaltes/base.html 

line no 1 i.e {% load static tailwind_tags %} and line no 9 i.e {% tailwind_css %}

since we already have template i.e templates/layout.html , so copy and paste line no 1 to top of layout.html and 9 above body

--> Now we have to run two server one for css and one for manage.py

1) python manage.py runserver
2) python manage.py runserver tailwind
for production
2) python manage.py runserver tailwind build

INSTALLED_APPS = [
    'django_browser_reload',
]

    <h6> <-- This config. is gemerally copied --></h6>
MIDDLEWARE = [
    'django_browser_reload.middleware.BrowserReloadMiddleware',
]

# ADMIN PANEL
--> seems like old school to make compitable with every browser

--> By Injecting our own css we can modify it

--> migration talks with DataBase by  default we have db.sqlite3

--> We don't talk with db directly with django on our behalf django's orm talk with database

That ORM command is
1) python manage.py migrate

we get authnication,admin for admin pannel which fuillfilled by this migration

--> To craete super user
2) python manage.py createsuperuser



