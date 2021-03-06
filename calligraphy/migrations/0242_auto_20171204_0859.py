# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-12-04 08:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('calligraphy', '0241_boxedges'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='boxedges',
            name='edge_right',
        ),
        migrations.AddField(
            model_name='boxedges',
            name='parent_character',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='calligraphy.Character'),
        ),
        migrations.AddField(
            model_name='boxedges',
            name='quadrants',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
