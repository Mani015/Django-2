from django.shortcuts import render
from django.views.generic import ListView,DetailView
from appone.models import Student

# Create your views here.
class studentlistview(ListView):
    model=Student
# default template list_view.html
# default context_object name  is list_view
class studentDetailview(DetailView):
    model=Student
    # bydefault template name is detail_view.html
    # default context_object _name  is student_view
