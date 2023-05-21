from django.db import models

import datetime
# Create your models here.
class ToDoModel(models.Model):
    username = models.CharField(max_length=100,)
    event = models.CharField(max_length=500)
    date = models.DateField(verbose_name='Date', null=True)
    time = models.TimeField(verbose_name='Time', null=True)
    createddt = models.DateTimeField(null=True)
    class Meta:
        db_table = 'ToDo'