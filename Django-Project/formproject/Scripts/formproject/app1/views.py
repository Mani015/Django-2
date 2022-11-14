from django.shortcuts import render
from . import forms

# Create your views here.
def student(request):
    form=forms.Studentform()
    return render(request,'template/entry.html',{'form':form})
