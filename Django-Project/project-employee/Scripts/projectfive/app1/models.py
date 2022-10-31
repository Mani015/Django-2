from django.db import models


# Create your models here.
class  employee(models.Model):
    FirstName = models.CharField(max_length=30)
    LastName = models.CharField(max_length=30)
    salary = models.IntegerField()
