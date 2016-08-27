# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-08-27 00:26
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import extras


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('city_name', models.CharField(max_length=150, null=True)),
                ('added', models.DateTimeField(editable=False, null=True)),
                ('updated', models.DateTimeField(editable=False, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('country_name', models.CharField(max_length=250, null=True)),
                ('added', models.DateTimeField(editable=False, null=True)),
                ('updated', models.DateTimeField(editable=False, null=True)),
                ('user_added', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_added_country', to=settings.AUTH_USER_MODEL)),
                ('user_updated', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_updated_country', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Definition',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('word', extras.CharNullField(blank=True, max_length=600, null=True)),
                ('definition', models.CharField(max_length=8000, null=True)),
                ('transliteration', extras.CharNullField(blank=True, max_length=8000, null=True)),
                ('total_lookups', models.IntegerField(null=True)),
                ('user_added', models.IntegerField(null=True)),
                ('archived', models.BooleanField(default=False)),
                ('added', models.DateTimeField(editable=False, null=True)),
                ('updated', models.DateTimeField(editable=False, null=True)),
                ('archived_date', models.DateTimeField(editable=False, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='DictionaryAPI',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150, null=True)),
                ('description', extras.CharNullField(blank=True, max_length=8000, null=True)),
                ('api_type', models.CharField(max_length=150, null=True)),
                ('site', models.CharField(max_length=2000, null=True)),
                ('base_url', models.CharField(max_length=2000, null=True)),
                ('api_key', models.CharField(max_length=500, null=True)),
                ('id_key', models.CharField(max_length=500, null=True)),
                ('added', models.DateTimeField(editable=False, null=True)),
                ('updated', models.DateTimeField(editable=False, null=True)),
                ('user_added', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_added_dictionary_api', to=settings.AUTH_USER_MODEL)),
                ('user_updated', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_updated_dictionary_api', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('language', models.CharField(max_length=150, null=True)),
                ('script', models.CharField(max_length=300, null=True)),
                ('added', models.DateTimeField(editable=False, null=True)),
                ('updated', models.DateTimeField(editable=False, null=True)),
                ('user_added', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_added_lang', to=settings.AUTH_USER_MODEL)),
                ('user_updated', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_updated_lang', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('region', models.CharField(max_length=300, null=True)),
                ('added', models.DateTimeField(editable=False, null=True)),
                ('updated', models.DateTimeField(editable=False, null=True)),
                ('country_region', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='country_region', to='api.Country')),
                ('user_added', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_added_region', to=settings.AUTH_USER_MODEL)),
                ('user_updated', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_updated_region', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserDefinition',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('added', models.DateTimeField(editable=False, null=True)),
                ('updated', models.DateTimeField(editable=False, null=True)),
                ('definitions', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='definitions', to='api.Definition')),
                ('user_owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_owner', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='WordType',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('word_type', models.CharField(max_length=150, null=True)),
                ('added', models.DateTimeField(editable=False, null=True)),
                ('updated', models.DateTimeField(editable=False, null=True)),
                ('user_added', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_added_wordtype', to=settings.AUTH_USER_MODEL)),
                ('user_updated', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_updated_wordtype', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='definition',
            name='dictionary_apis',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dictionary_apis', to='api.DictionaryAPI'),
        ),
        migrations.AddField(
            model_name='definition',
            name='language',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='current_lang', to='api.Language'),
        ),
        migrations.AddField(
            model_name='definition',
            name='target',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='target_lang', to='api.Language'),
        ),
        migrations.AddField(
            model_name='definition',
            name='user_contributor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_contributor', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='definition',
            name='word_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='word_type_id', to='api.WordType'),
        ),
        migrations.AddField(
            model_name='city',
            name='country_city',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='country_city', to='api.Country'),
        ),
        migrations.AddField(
            model_name='city',
            name='region_city',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='region_city', to='api.Region'),
        ),
        migrations.AddField(
            model_name='city',
            name='user_added',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_added_city', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='city',
            name='user_updated',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_updated_city', to=settings.AUTH_USER_MODEL),
        ),
    ]