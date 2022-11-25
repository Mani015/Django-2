from django.shortcuts import render,redirect
from app1.models import Student
from app1.forms import Studentform

# Create your views here.
def getstudent(request):
    x=Student.objects.all()
    return render(request,'template/index.html',{'x':x})


def createstudent(request):
    form=Studentform()
    if request.method == 'POST':
        form = Studentform(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request,'template/create.html',{'form':form})


def deletestudent(request,id):
    student=Student.objects.get(id=id)
    student.delete()
    return redirect('/')
#
def updatestudent(request,id):
    student=Student.objects.get(id=id)
    if request.method == 'POST':
        form=Studentform(request.POST,instance=student)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request,'template/update.html',{'student':student})



# Using jango form for update

def updatestudent(request,id):
    student=Student.objects.get(id=id)
    form=Studentform(instance=student)
    if request.method == 'POST':
        form=Studentform(request.POST,instance=student)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request,'template/update.html',{'form':form})
