"""
URL configuration for DjangoProj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# This is main project 
# urls.py

from django.contrib import admin
from django.urls import path,include
# Import views.py
from . import views
# " . " mean from current directory

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('about/',views.About,name='about'),
    path('contact/',views.Contact,name='contact'),
    path('pastha/',include('pastha.urls')),


# This path is for hot reloading, auto reloading, always at last, since it send zip and it is a heavy path
    path("__reload__/",include("django_browser_reload.urls")),
]
