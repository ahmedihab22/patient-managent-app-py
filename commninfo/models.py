from django.db import models
from django.contrib.auth.models import User
from django import utils

# Create your models here.
class patients(models.Model):
    id = models.IntegerField(primary_key=True,unique=True)
    username = models.CharField(max_length=100,blank=True)
    FirstName = models.CharField(max_length=100,blank=True)
    LastName = models.CharField(max_length=100,blank=True)
    Email = models.TextField(max_length=100,blank=True)
    password = models.IntegerField(blank=True)
    confpassword = models.IntegerField(blank=True)
    dateofbirth = models.DateField()

