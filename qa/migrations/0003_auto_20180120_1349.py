# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-01-20 05:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qa', '0002_auto_20170818_1344'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='glances',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='question',
            name='glances',
            field=models.IntegerField(default=0),
        ),
    ]
