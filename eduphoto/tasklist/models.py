from django.db import models
from datetime import datetime
# Create your models here.
class Task(models.Model):
    given = models.DateTimeField(default=datetime.now)
    deadline = models.DateTimeField(null=True)
    description = models.CharField(max_length = 512)
    done = models.BooleanField(default=False)


class Kitten(models.Model):
    birth_date = models.DateTimeField(default=datetime.now)
    color = models.CharField(max_length = 512)
    race = models.CharField(max_length = 512)
    male = models.BooleanField(default=False)
    imya = models.CharField(max_length = 512)

    
class Photo(models.Model):
    image = models.ImageField()
    message = models.CharField()