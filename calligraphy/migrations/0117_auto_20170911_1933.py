# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-11 19:33
from __future__ import unicode_literals

from django.db import migrations


def do_stuff(apps, schemd_editor) -> None:
    print("Do nothing")



class Migration(migrations.Migration):

    dependencies = [
        ('calligraphy', '0116_auto_20170911_1506'),
    ]

    operations = [ migrations.RunPython(do_stuff)
    ]
