# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-22 12:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='communite',
            name='user',
        ),
        migrations.AddField(
            model_name='communite',
            name='user_name',
            field=models.CharField(max_length=64, null=True),
        ),
    ]
