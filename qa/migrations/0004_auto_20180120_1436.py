# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-01-20 06:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('qa', '0003_auto_20180120_1349'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='aswerer',
            new_name='answerer',
        ),
    ]
