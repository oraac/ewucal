# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-01 22:03
# Need to update location of images, in chars
#
# This is important because it standardizes the database between all server implementations we have
#
#####################################################
from __future__ import unicode_literals

from django.db import migrations
import socket
import os

HOSTNAME = socket.gethostname()
if HOSTNAME == 'bigArch':
    runChange = True
else:
    runChange = False

OLD_IMAGE_DIR = "/home/dave/workspace/pycharm/media/"
NEW_IMAGE_DIR = "/media/"


def update_images_in_database(apps) -> None:
    Char = apps.get_model("calligraphy", "Character")
    chars = Char.objects.all()
    for char in chars:
        img_path = char.image
        tail_path = str(img_path).split(OLD_IMAGE_DIR)[1]
        new_path = os.path.join(NEW_IMAGE_DIR, tail_path)
        char.image = new_path
        char.save()


def transform_data(apps, schemd_editor) -> None:
    if runChange:
        update_images_in_database(apps)


class Migration(migrations.Migration):

    dependencies = [
        ('calligraphy', '0019_auto_20161001_1403'),
    ]

    operations = [ migrations.RunPython(transform_data)
    ]
