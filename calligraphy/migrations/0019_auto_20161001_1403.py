# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-01 21:03
#
# Need to update location of images, in pages
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
    Page = apps.get_model("calligraphy", "Page")
    pages = Page.objects.all()
    for page in pages:
        img_path = page.image
        tail_path = str(img_path).split(OLD_IMAGE_DIR)[1]
        new_path = os.path.join(NEW_IMAGE_DIR, tail_path)
        page.image = new_path
        page.save()


def transform_data(apps, schemd_editor) -> None:
    if runChange:
        update_images_in_database(apps)

class Migration(migrations.Migration):

    dependencies = [
        ('calligraphy', '0018_auto_20160930_1718'),
    ]

    operations = [ migrations.RunPython(transform_data)
    ]