from django import forms


class Studentform(forms.Form):
    Firstname=forms.CharField(max_length=30)
    Lastname=forms.CharField(max_length=30)
    Rollno=forms.IntegerField()
    
