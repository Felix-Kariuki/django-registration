from django.db import models
from django.db.models.fields import CharField

class User(models.Model):
    Name = models.CharField(max_length=100)
    Email = models.CharField(max_length=100)
    Phone = models.IntegerField(13)
    Password = models.CharField(max_length=150)
