# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-01 02:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ombudsman', '0002_auto_20170329_2342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apikeygrant',
            name='app_url',
            field=models.URLField(max_length=1024, verbose_name=b'App URL'),
        ),
    ]
