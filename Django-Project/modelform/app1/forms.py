from django import forms
from app1.models import project
# meta:the meta class can be used to defined various things about the model such as the permission database
class projectForm(forms.ModelForm):
    class Meta:
        model = project
        fields ='__all__'
