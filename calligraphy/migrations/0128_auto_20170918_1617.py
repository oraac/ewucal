# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-18 16:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calligraphy', '0127_auto_20170918_1331'),
    ]

    operations = [
        migrations.AddField(
            model_name='detectedbox',
            name='inside_currated_box',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='detectedbox',
            name='inside_orig_box',
            field=models.IntegerField(default=False),
            preserve_default=False,
        ),
    ]
