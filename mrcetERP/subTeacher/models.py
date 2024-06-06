from django.db import models
# Create your models here.
class STsignin(models.Model):
    mail=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    password1=models.CharField(max_length=50)
class STLogIn(models.Model):
    user_mail=models.CharField(max_length=100)
    user_password=models.CharField(max_length=50)
    