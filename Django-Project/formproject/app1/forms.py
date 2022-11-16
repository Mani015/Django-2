from django import forms
from django.core import validators


class studentform(forms.Form):
    GENDER=[('male','MALE'),('female','FEMALE')]
    # firstname = forms.CharField(widget=forms.TextInput)
    # firstname = forms.CharField(required=False)
    firstname = forms.CharField(required=False)
    lastname = forms.CharField()
    rollno = forms.IntegerField()
    gender=forms.CharField(widget=forms.Select(choices=GENDER))
    password=forms.CharField(widget=forms.PasswordInput)


    def clean_firstname(self):
        firstname = self.cleaned_data['firstname']
        if len(firstname)>10:
            raise forms.ValidationError('the maximum lenght of the firstname below 10 characters')
        return firstname

    def clean_lastname(self):
        lastname = self.cleaned_data['lastname']
        if len(lastname)>10:
            raise forms.ValidationError('the maximum lenght of the lastname below 10 characters')
        return lastname
