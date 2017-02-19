# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-19 02:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0003_course_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='homework',
        ),
        migrations.AddField(
            model_name='course',
            name='homework',
            field=models.ManyToManyField(to='course.Homework'),
        ),
    ]