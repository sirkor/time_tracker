# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('time_tracker', '0004_auto_20160502_0957'),
    ]

    operations = [
        migrations.AddField(
            model_name='activities',
            name='activities_user',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='activities',
            name='activities_end',
            field=models.DateTimeField(default=datetime.datetime(2016, 5, 2, 10, 5, 10, 91821)),
        ),
        migrations.AlterField(
            model_name='activities',
            name='activities_start',
            field=models.DateTimeField(default=datetime.datetime(2016, 5, 2, 10, 5, 10, 91779)),
        ),
    ]
