# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-28 16:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calligraphy', '0060_auto_20170128_1624'),
    ]

    operations = [
        migrations.RenameField(
            model_name='charset',
            old_name='set_has_problems',
            new_name='set_valid',
        ),
    ]
