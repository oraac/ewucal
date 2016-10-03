# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-03 01:04
#
# Just adds high_rez character image field
#
#############################################################################################
from __future__ import unicode_literals

import django.core.files.storage
from django.db import migrations, models



class Migration(migrations.Migration):

    dependencies = [
        ('calligraphy', '0021_auto_20161001_2046'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='image_high_rez',
            field=models.ImageField(blank=True, storage=django.core.files.storage.FileSystemStorage(), upload_to=''),
        ),
    ]
