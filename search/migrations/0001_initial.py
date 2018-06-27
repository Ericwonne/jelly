# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-08-20 09:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Jwcinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('body', models.TextField(blank=True, null=True)),
                ('url', models.CharField(blank=True, max_length=200, null=True, unique=True)),
                ('glances', models.IntegerField(default=0)),
                ('crawltime', models.DateTimeField(auto_now=True)),
                ('download', models.IntegerField(default=0)),
                ('site', models.CharField(max_length=20)),
                ('pubtime', models.DateField(blank=True, null=True)),
            ],
            options={
                'db_table': 'jwcinfo',
            },
        ),
        migrations.CreateModel(
            name='PersonalInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('st', models.CharField(max_length=10, unique=True)),
                ('info', models.TextField()),
                ('crawltime', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'personal_info',
            },
        ),
    ]
