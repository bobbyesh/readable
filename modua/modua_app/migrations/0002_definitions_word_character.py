# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-29 02:04
from __future__ import unicode_literals

from django.db import migrations
import extras


class Migration(migrations.Migration):

    dependencies = [
        ('modua_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='definitions',
            name='word_character',
            field=extras.CharNullField(blank=True, max_length=600, null=True),
        ),
    ]
