# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2016-11-04 09:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pootle_app', '0012_set_directory_tp'),
    ]

    operations = [
        migrations.AddField(
            model_name='directory',
            name='tp_path',
            field=models.CharField(blank=True, db_index=True, max_length=255, null=True),
        ),
    ]