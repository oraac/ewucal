# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-20 01:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calligraphy', '0154_auto_20170920_0126'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detectedbox',
            name='li_threshold_bottom',
        ),
    ]