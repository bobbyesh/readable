# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-09-09 00:36
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0005_auto_20160907_0131'),
    ]

    operations = [
        migrations.CreateModel(
            name='PublicDefinition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified_date', models.DateTimeField(auto_now=True, null=True)),
                ('definition', models.CharField(max_length=8000)),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Language')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PublicWord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(blank=True, max_length=600)),
                ('transliteration', models.CharField(blank=True, max_length=8000)),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Language')),
            ],
        ),
        migrations.CreateModel(
            name='UserDefinition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified_date', models.DateTimeField(auto_now=True, null=True)),
                ('definition', models.CharField(max_length=8000)),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Language')),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='api_userdefinition_owner', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserWord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(blank=True, max_length=600)),
                ('ease', models.CharField(blank=True, max_length=20)),
                ('transliteration', models.CharField(blank=True, max_length=8000)),
                ('articles', models.ManyToManyField(to='api.Article')),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Language')),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='api_userword_owner', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='definition',
            name='language',
        ),
        migrations.RemoveField(
            model_name='definition',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='definition',
            name='word',
        ),
        migrations.RemoveField(
            model_name='definition',
            name='word_type',
        ),
        migrations.RemoveField(
            model_name='word',
            name='articles',
        ),
        migrations.RemoveField(
            model_name='word',
            name='language',
        ),
        migrations.RemoveField(
            model_name='word',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='wordtype',
            name='contributor',
        ),
        migrations.RemoveField(
            model_name='wordtype',
            name='editor',
        ),
        migrations.DeleteModel(
            name='Definition',
        ),
        migrations.DeleteModel(
            name='Word',
        ),
        migrations.DeleteModel(
            name='WordType',
        ),
        migrations.AddField(
            model_name='userdefinition',
            name='word',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.UserWord'),
        ),
        migrations.AddField(
            model_name='publicdefinition',
            name='word',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.PublicWord'),
        ),
    ]