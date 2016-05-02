# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('time_tracker', '0003_auto_20160429_1236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activities',
            name='activities_end',
            field=models.DateTimeField(default=datetime.datetime(2016, 5, 2, 9, 57, 5, 571622)),
        ),
        migrations.AlterField(
            model_name='activities',
            name='activities_start',
            field=models.DateTimeField(default=datetime.datetime(2016, 5, 2, 9, 57, 5, 571579)),
        ),
    ]
