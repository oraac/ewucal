# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-10-27 00:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calligraphy', '0233_detectedbox_parent_char'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detectedbox',
            name='parent_char',
        ),
    ]