# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-10-31 15:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('silver_extensions', '0003_auto_20181031_1515'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercustomermapping',
            name='relation_type',
            field=models.CharField(choices=[('partner', 'Partner'), ('it_admin', 'IT Admin'), ('owner', 'Owner')], max_length=8),
        ),
    ]
