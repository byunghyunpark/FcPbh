# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-16 12:59
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0002_auto_20161016_1043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 10, 16, 12, 59, 10, 346909, tzinfo=utc)),
        ),
    ]
