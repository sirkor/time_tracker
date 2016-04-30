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
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('activity_name', models.CharField(max_length=40)),
                ('activity_type', models.CharField(max_length=20)),
                ('activity_start', models.DateTimeField(default=datetime.datetime(2016, 4, 29, 12, 21, 18, 99236))),
            ],
        ),
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('activity_type', models.CharField(max_length=30)),
            ],
        ),
    ]
