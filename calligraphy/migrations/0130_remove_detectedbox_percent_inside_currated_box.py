# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-18 23:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calligraphy', '0129_auto_20170918_1918'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detectedbox',
            name='percent_inside_currated_box',
        ),
    ]
