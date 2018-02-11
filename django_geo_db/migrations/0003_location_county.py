# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-02-11 17:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('django_geo_db', '0002_auto_20180211_1700'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='county',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='django_geo_db.County'),
        ),
    ]
