# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-08-22 06:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bigapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicesdata',
            name='course_start_time',
            field=models.TimeField(max_length=100),
        ),
    ]
