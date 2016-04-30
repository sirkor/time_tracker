# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('time_tracker', '0002_auto_20160429_1228'),
    ]

    operations = [
        migrations.RenameField(
            model_name='activities',
            old_name='activity_name',
            new_name='activities_name',
        ),
        migrations.RenameField(
            model_name='activities',
            old_name='activity_type',
            new_name='activities_type',
        ),
        migrations.RemoveField(
            model_name='activities',
            name='activity_end',
        ),
        migrations.RemoveField(
            model_name='activities',
            name='activity_start',
        ),
        migrations.AddField(
            model_name='activities',
            name='activities_end',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 29, 12, 36, 36, 154023)),
        ),
        migrations.AddField(
            model_name='activities',
            name='activities_start',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 29, 12, 36, 36, 153975)),
        ),
    ]
