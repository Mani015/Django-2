from django.shortcuts import render
from app1 import forms

# Create your views here.

def studentdetails(request):
    form=forms.studentform()
    if request.method == 'POST':
        form=forms.studentform(request.POST)
        if form.is_valid():
            print('form is valid')
            print('firstname',form.cleaned_data['firstname'])
            print('lastname',form.cleaned_data['lastname'])
            print('rollno',form.cleaned_data['rollno'])
    return render(request, 'template/student.html',{'form':form})
