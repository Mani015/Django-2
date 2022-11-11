from django.shortcuts import render

# Create your views here.
def displaytemplate(request):
    data={'name':'django'}
    return render(request,"template/home.html",context=data)

def passingdata(request):
    employee={'name':'Arjun','age':25,'salary':20000}
    return render(request,"template/details.html",employee)
