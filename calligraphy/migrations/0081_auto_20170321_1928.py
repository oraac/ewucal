# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-03-21 19:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calligraphy', '0080_auto_20170306_1721'),
    ]

    operations = [
        migrations.AlterField(
            model_name='char_location_update',
            name='x1',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='char_location_update',
            name='x2',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='char_location_update',
            name='y1',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='char_location_update',
            name='y2',
            field=models.IntegerField(blank=True),
        ),
    ]
