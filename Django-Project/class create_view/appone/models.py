from django.db import models
from django.urls import reverse

# Create your models here.
class Student(models.Model):
    firstname=models.CharField(max_length=30)
    lastname=models.CharField(max_length=30)
    marks=models.FloatField()


    def get_absolute_url(self):
        return reverse('detail',args = {self.pk})
