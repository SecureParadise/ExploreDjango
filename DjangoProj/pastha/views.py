from django.shortcuts import render
from .models import PasthaVarity
# Create your views here.

def all_pastha(request):
    pasthas = PasthaVarity.objects.all()
    return render(request,'pastha/all_pastha.html',{'pasthas':pasthas})