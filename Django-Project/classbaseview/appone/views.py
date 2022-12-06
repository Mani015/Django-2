from django.shortcuts import render
from django.views.generic import ListView, DetailView
from appone.models import Student

# Create your views here.
class studentlistview(ListView):
    model=Student
# default template list_view.html
# default context_object name  is list_view


class studentdetailview(DetailView):
    model=Student
# by default template is student_detail.html
# default context_object name  is list_detail
