# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-31 15:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calligraphy', '0063_charset_set_chars'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tofindmultiplier',
            name='page_id',
        ),
        migrations.DeleteModel(
            name='ToFindMultiplier',
        ),
    ]
