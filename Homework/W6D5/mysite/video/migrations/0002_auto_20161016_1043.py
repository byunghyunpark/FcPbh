# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-16 10:43
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 10, 16, 10, 43, 17, 189312, tzinfo=utc)),
        ),
    ]