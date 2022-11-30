from django.db import models

# Create your models here.
class Student(models.Model):
    Firstname=models.CharField(max_length=30)
    Lastname=models.CharField(max_length=30)
    Marks=models.FloatField()
