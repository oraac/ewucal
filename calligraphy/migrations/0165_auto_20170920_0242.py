# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-20 02:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calligraphy', '0164_remove_detectedbox_local_centroid_y'),
    ]

    operations = [
        migrations.AddField(
            model_name='detectedbox',
            name='maxor_axis_length_norm',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='detectedbox',
            name='minor_axis_length_norm',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
