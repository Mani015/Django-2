from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def function(requst):
    return HttpResponse("<h1>This is my firstproject successfully done</h1>")

def name(request):
    return HttpResponse('this is seocnd function')
