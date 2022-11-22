from django.db import models

# Create your models here.
class project(models.Model):
    startdate=models.DateField()
    enddate=models.DateField()
    location=models.CharField(max_length=30)
    budget=models.IntegerField()
    company=models.CharField(max_length=30)
