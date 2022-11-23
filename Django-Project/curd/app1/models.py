from django.db import models

# Create your models here.
class Student(models.Model):
    FirstName = models.CharField(max_length=30)
    LastName = models.CharField(max_length=30)
    Marks= models.FloatField()
    standard = models.IntegerField()
