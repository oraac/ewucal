# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-06 15:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calligraphy', '0100_userdid'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='has_copyright_restrictions',
            field=models.BooleanField(default=False),
        ),
    ]
