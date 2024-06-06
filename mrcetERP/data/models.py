from django.db import models


# Create your models here.
class Student(models.Model):
    std_id = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    branch = models.CharField(max_length=50, default='')
    year = models.IntegerField(default=0)
    subject_marks = models.TextField(default='')  

class Faculty(models.Model):
    name=models.CharField(max_length=50)



