from django.http import HttpResponse
from django.shortcuts import render
from . models import  Place
from .models import Members

# Create your views here.
def demo(request):
    #fetching data from database

    obj=Place.objects.all()
    obj1=Members.objects.all()
    return render(request, "index.html", {'result': obj, 'result1': obj1})
    #return HttpResponse("<h1>hellooo")
    #name="athira"

#def addition(request):
   # a=int(request.GET['num1'])
    #b=int(request.GET['num2'])
    #res=a+b
    #return render(request,'result.html',{'result':res})
