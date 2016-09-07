# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-09-07 01:31
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0004_auto_20160905_1924'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='definition',
            name='contributor',
        ),
        migrations.RemoveField(
            model_name='word',
            name='user',
        ),
        migrations.AddField(
            model_name='definition',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='api_definition_owner', to=settings.AUTH_USER_MODEL),
        ),
    ]