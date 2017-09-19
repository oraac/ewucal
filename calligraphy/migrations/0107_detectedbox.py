# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-06 03:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('calligraphy', '0106_pageshavechars'),
    ]

    operations = [
        migrations.CreateModel(
            name='DetectedBox',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', models.IntegerField()),
                ('convex_area', models.IntegerField()),
                ('eccentricity', models.FloatField()),
                ('extant', models.FloatField()),
                ('x1', models.IntegerField()),
                ('y1', models.IntegerField()),
                ('x2', models.IntegerField()),
                ('y2', models.IntegerField()),
                ('major_axis_length', models.FloatField()),
                ('minor_axis_length', models.FloatField()),
                ('orientation', models.FloatField()),
                ('solidity', models.FloatField()),
                ('local_centroid_x', models.FloatField()),
                ('local_centroid_y', models.FloatField()),
                ('parent_page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='calligraphy.Page')),
            ],
        ),
    ]