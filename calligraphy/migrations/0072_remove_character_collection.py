# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-02-20 11:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calligraphy', '0071_auto_20170218_1727'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='character',
            name='collection',
        ),
    ]
