# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-02-17 23:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_geo_db', '0004_auto_20180211_1720'),
    ]

    operations = [
        migrations.CreateModel(
            name='GeographicRegion',
            fields=[
                ('geographic_region_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=40)),
                ('locations', models.ManyToManyField(to='django_geo_db.Location')),
            ],
        ),
    ]