# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-05-21 10:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0006_auto_20180520_1508'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='phone_number',
            field=models.CharField(max_length=20),
        ),
    ]
