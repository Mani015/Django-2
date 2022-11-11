from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.

def python(request):
    return HttpResponse("<h1>python is general purpose programming </h>")

def showdatetime(request):
    dt=datetime.datetime.now()
    s=("<h1>display current dateandtime: </h1>",dt)
    return HttpResponse(s)
 
