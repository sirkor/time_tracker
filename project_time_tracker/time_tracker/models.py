from django.db import models
import datetime
from django.contrib.auth.models import User

class Activity(models.Model):
    activity_id = models.AutoField
    activity_type = models.CharField(max_length=30)


class Activities(models.Model):
    activities_id = models.AutoField
    activities_user = models.CharField(max_length=30,default='')
    activities_name = models.CharField(max_length=40)
    activities_type = models.CharField(max_length=20)
    activities_start = models.DateTimeField(default=datetime.datetime.now())
    activities_end = models.DateTimeField(default=datetime.datetime.now())
    activities_duration = models.TimeField
