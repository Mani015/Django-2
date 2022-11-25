from django import forms
from app1.models import Student

class Studentform(forms.ModelForm):
    class Meta:
        model=Student
        fields='__all__'
