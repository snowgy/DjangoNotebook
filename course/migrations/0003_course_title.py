# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-19 02:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='title',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
