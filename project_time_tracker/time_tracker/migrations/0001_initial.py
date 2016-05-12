# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import datetime


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Activities',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('activities_user', models.CharField(max_length=30)),
                ('activities_name', models.CharField(max_length=40)),
                ('activities_type', models.CharField(max_length=20)),
                ('activities_start', models.DateTimeField(default=datetime.datetime(2016, 5, 12, 10, 21, 9, 1147))),
                ('activities_end', models.DateTimeField(default=datetime.datetime(2016, 5, 12, 10, 21, 9, 1189))),
                ('activities_duration', models.DurationField()),
                ('new', models.ForeignKey(to=settings.AUTH_USER_MODEL, default='')),
            ],
        ),
    ]
