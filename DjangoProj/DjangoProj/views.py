from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Hello,Dear !,It's Our home")
    return render(request,'websites/index.html')

def About(request):
    return HttpResponse("Hello,Dear !,You dont know about me")
def Contact(request):
    return HttpResponse("Hello,Dear !,Give me yor contact Number")


