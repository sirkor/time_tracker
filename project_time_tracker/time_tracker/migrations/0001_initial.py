# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Activities',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('add_date', models.DateTimeField(default=datetime.datetime(2016, 5, 22, 18, 33, 15, 811684))),
                ('activities_user', models.CharField(max_length=30)),
                ('activities_name', models.CharField(max_length=40)),
                ('activities_type', models.CharField(max_length=20)),
                ('activities_start', models.DateTimeField(default=datetime.datetime(2016, 5, 22, 18, 33, 15, 811883))),
                ('activities_end', models.DateTimeField(default=datetime.datetime(2016, 5, 22, 18, 33, 15, 811932))),
                ('activities_duration', models.DurationField()),
                ('new', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-add_date'],
            },
        ),
    ]
