# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-09-04 06:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20160904_0600'),
    ]

    operations = [
        migrations.AlterField(
            model_name='word',
            name='article',
            field=models.ManyToManyField(to='api.Article'),
        ),
    ]
