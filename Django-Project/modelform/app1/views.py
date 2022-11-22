from django.shortcuts import render
from app1.forms import projectForm
from app1.models import project

# Create your views here.

def index(request):
    return render(request, 'template/index.html')

def listprojects(request):

    x=project.objects.all()
    return render(request, 'template/listprojects.html',{'project':x})

def addproject(request):
    form=projectForm()
    if request.method == 'POST':
        form=projectForm(request.POST)
        if form.is_valid():
            form.save()
        return index(request)
    return render(request,'template/addproject',{'form':form})
