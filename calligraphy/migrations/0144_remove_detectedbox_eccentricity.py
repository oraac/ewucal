# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-20 00:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calligraphy', '0143_auto_20170920_0001'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detectedbox',
            name='eccentricity',
        ),
    ]
