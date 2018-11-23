# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-10-04 09:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('va_saas', '0004_auto_20181004_0931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companypagelanding',
            name='footer_facebook',
            field=models.URLField(max_length=600),
        ),
        migrations.AlterField(
            model_name='companypagelanding',
            name='footer_instagram',
            field=models.URLField(max_length=600),
        ),
        migrations.AlterField(
            model_name='companypagelanding',
            name='footer_logo',
            field=models.URLField(max_length=600),
        ),
        migrations.AlterField(
            model_name='companypagelanding',
            name='footer_text',
            field=models.CharField(max_length=600),
        ),
        migrations.AlterField(
            model_name='companypagelanding',
            name='footer_twitter',
            field=models.URLField(max_length=600),
        ),
        migrations.AlterField(
            model_name='companypagelanding',
            name='footer_youtube',
            field=models.URLField(max_length=600),
        ),
        migrations.AlterField(
            model_name='companypagelanding',
            name='landing_header',
            field=models.CharField(max_length=600),
        ),
        migrations.AlterField(
            model_name='companypagelanding',
            name='landing_image',
            field=models.URLField(max_length=600),
        ),
        migrations.AlterField(
            model_name='companypagelanding',
            name='landing_text',
            field=models.CharField(max_length=600),
        ),
    ]
