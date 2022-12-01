from django.shortcuts import render

# from django.views import View
# from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView
from appone.models import Student
# Create your views here.

# class birthdaywishes(View):
#     def get(self,request):
#         return HttpResponse('<b><h1>appy birthaday python</h1></b>')


class studentlistview(ListView):
    model=Student

class studentDetailView(DetailView):
    model=Student

class studentCreateView(CreateView):
    model=Student
    fields = '__all__'
