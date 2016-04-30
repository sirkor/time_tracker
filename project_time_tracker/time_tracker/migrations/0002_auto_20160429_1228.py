# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('time_tracker', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='activities',
            name='activity_end',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 29, 12, 28, 45, 900690)),
        ),
        migrations.AlterField(
            model_name='activities',
            name='activity_start',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 29, 12, 28, 45, 900646)),
        ),
    ]
