from django.shortcuts import render
from app1.models import employee
# Create your views here.

def empdetail(request):
    emp= employee.objects.all()
    empDict = {'empdata':emp}
    return render(request, 'template/detail.html',empDict)
