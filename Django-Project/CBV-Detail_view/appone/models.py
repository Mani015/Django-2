from django.db import models
from django.urls import reverse

# Create your models here.
class Student(models.Model):
    Firstname=models.CharField(max_length=30)
    Lastname=models.CharField(max_length=30)
    Marks=models.FloatField()

    def get_absolute_url(self):
        return reverse('detail', args={self.pk})
