from django.shortcuts import render,redirect
from app1.models import Student
from app1.forms import studentforms


# Create your views here.
def getstudent(request):
    x=Student.objects.all()
    return render(request,'template/student.html',{'x':x})




def createStudent(request):
    form=studentforms()
    if request.method == 'POST':
        form=studentforms(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request, 'template/index.html', {'form': form})
