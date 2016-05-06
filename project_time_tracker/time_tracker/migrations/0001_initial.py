# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activities',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('activities_user', models.CharField(max_length=30)),
                ('activities_name', models.CharField(max_length=40)),
                ('activities_type', models.CharField(max_length=20)),
                ('activities_start', models.DateTimeField(default=datetime.datetime(2016, 5, 6, 14, 2, 21, 547447))),
                ('activities_end', models.DateTimeField(default=datetime.datetime(2016, 5, 6, 14, 2, 21, 547490))),
                ('activities_duration', models.DurationField()),
            ],
        ),
    ]
