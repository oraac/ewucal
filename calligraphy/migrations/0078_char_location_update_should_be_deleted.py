# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-03-06 16:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calligraphy', '0077_char_location_update'),
    ]

    operations = [
        migrations.AddField(
            model_name='char_location_update',
            name='should_be_deleted',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
