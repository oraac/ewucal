# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-19 23:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calligraphy', '0141_remove_detectedbox_convex_area'),
    ]

    operations = [
        migrations.AddField(
            model_name='detectedbox',
            name='eccentricity_norm',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
