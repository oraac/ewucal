# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-19 00:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calligraphy', '0132_auto_20170919_0003'),
    ]

    operations = [
        migrations.AddField(
            model_name='pageshavechars',
            name='x1',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pageshavechars',
            name='x2',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pageshavechars',
            name='y1',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pageshavechars',
            name='y2',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
