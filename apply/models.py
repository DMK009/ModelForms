from django.db import models

# Create your models here.
class hello(models.Model):
    FirstName=models.CharField(max_length=50)
    MiddleName=models.CharField(max_length=50)
    LastNmae=models.CharField(max_length=50)