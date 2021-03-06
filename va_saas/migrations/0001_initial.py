# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-09-05 12:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyPageAbout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('features_header', models.CharField(max_length=20)),
                ('features_text', models.CharField(max_length=20)),
                ('features_image', models.URLField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='CompanyPageAboutSteps',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('step_header', models.CharField(max_length=20)),
                ('step_details', models.CharField(max_length=20)),
                ('belongs_to_page', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='va_saas.CompanyPageAbout')),
            ],
        ),
        migrations.CreateModel(
            name='CompanyPageContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='CompanyPageFeature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feature_image', models.URLField(max_length=20)),
                ('feature_header', models.CharField(max_length=20)),
                ('feature_details', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='CompanyPageFeaturesList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_page', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='va_saas.CompanyPageContent')),
            ],
        ),
        migrations.CreateModel(
            name='CompanyPageLanding',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header_logo', models.URLField(max_length=20)),
                ('landing_header', models.CharField(max_length=20)),
                ('landing_text', models.CharField(max_length=20)),
                ('footer_logo', models.URLField(max_length=20)),
                ('footer_text', models.CharField(max_length=20)),
                ('footer_facebook', models.URLField(max_length=20)),
                ('footer_twitter', models.URLField(max_length=20)),
                ('footer_youtube', models.URLField(max_length=20)),
                ('footer_instagram', models.URLField(max_length=20)),
                ('company_page', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='va_saas.CompanyPageContent')),
            ],
        ),
        migrations.CreateModel(
            name='CompanyPageLoggedIn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('footer_text', models.CharField(max_length=20)),
                ('support_email', models.CharField(max_length=20)),
                ('company_page', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='va_saas.CompanyPageContent')),
            ],
        ),
        migrations.CreateModel(
            name='CompanyPagePricing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pricing_header', models.CharField(max_length=20)),
                ('pricing_details', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='CompanyPageSignup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('terms_text', models.CharField(max_length=20)),
                ('company_page', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='va_saas.CompanyPageContent')),
            ],
        ),
        migrations.AddField(
            model_name='companypagefeature',
            name='belongs_to_list',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='va_saas.CompanyPageFeaturesList'),
        ),
        migrations.AddField(
            model_name='companypageabout',
            name='company_page',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='va_saas.CompanyPageContent'),
        ),
    ]
