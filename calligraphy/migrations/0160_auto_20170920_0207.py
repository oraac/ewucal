# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-20 02:07
from __future__ import unicode_literals

from django.db import migrations, connection

def do_stuff(apps, schemd_editor) -> None:
    with connection.cursor() as cursor:
        cursor.execute("UPDATE calligraphy_detectedbox SET local_centroid_x_norm = CAST( local_centroid_x / ( x2 - x1 ) * 2147483647 AS int )")

class Migration(migrations.Migration):

    dependencies = [
        ('calligraphy', '0159_detectedbox_local_centroid_x_norm'),
    ]

    operations = [ migrations.RunPython(do_stuff)
    ]
