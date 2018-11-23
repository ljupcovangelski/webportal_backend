# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-10-31 15:15
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('silver_extensions', '0002_plansteps_step_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plansteps',
            name='step_value',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='usercustomermapping',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='silver.Customer'),
        ),
        migrations.AlterField(
            model_name='usercustomermapping',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
