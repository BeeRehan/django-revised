from operator import mod
from xml.parsers.expat import model
from django.db import models

# Create your models here.
class TodoList(models.Model):
    task = models.CharField(max_length=200)
    status = models.BooleanField(default=False)