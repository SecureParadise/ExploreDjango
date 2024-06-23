from django.shortcuts import render

# Create your views here.

def all_pastha(request):
    return render(request,'pastha/all_pastha.html')