
from django.urls import path
# Import views.py
from . import views

    # locolhost:8000/pastha

urlpatterns = [
    path('',views.all_pastha,name='pastha'),
]