from django.db import models
import datetime
from django.contrib.auth.models import User


class Activities(models.Model):
    new = models.ForeignKey(User)
    activities_user = models.CharField(max_length=30)
    activities_name = models.CharField(max_length=40)
    activities_type = models.CharField(max_length=20)
    activities_start = models.DateTimeField(default=datetime.datetime.now())
    activities_end = models.DateTimeField(default=datetime.datetime.now())
    activities_duration = models.DurationField()

    def __str__(self):
        return self.activities_name
