from django.shortcuts import render
from django.views.generic import ListView,DetailView, CreateView, DeleteView
from appone.models import Student
from django.urls import reverse_lazy

# Create your views here.
class studentlistview(ListView):
    model=Student
# default template list_view.html
# default context_object name  is list_view
class studentDetailview(DetailView):
    model=Student
    # bydefault template name is detail_view.html
    # default context_object _name  is student_view

class studentcreativeview(CreateView):
    model=Student

    fields='__all__'



class studentdeleteview(DeleteView):
    model=Student
    success_url=reverse_lazy('students')
