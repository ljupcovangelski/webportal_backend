# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-10-30 14:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('silver_extensions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='plansteps',
            name='step_name',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
    ]