# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-17 15:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('calligraphy', '0051_character_collection'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pagemultiplier',
            name='parent_page',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='calligraphy.Page'),
        ),
    ]
