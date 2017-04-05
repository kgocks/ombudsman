# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-29 23:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ombudsman', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='apikeygrant',
            old_name='app_link',
            new_name='app_url',
        ),
        migrations.AddField(
            model_name='apikeygrant',
            name='created',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='apikeygrant',
            name='updated',
            field=models.DateField(auto_now=True, null=True),
        ),
    ]
