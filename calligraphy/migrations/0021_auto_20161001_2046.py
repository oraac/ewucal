# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-02 03:46
#
# Goes through database and makes sure all the images are valid
#
#############################################################################################
from __future__ import unicode_literals

from django.db import migrations
import os
from django.core.files.storage import default_storage


def check_update_images(apps) -> None:
    Page = apps.get_model("calligraphy", "Page")
    pages = Page.objects.all()
    for page in pages:
        img_path = page.image
        if not default_storage.exists(str(img_path)):
            new_path = str(img_path).strip(".tiff") + ".png"
            print(new_path)
            page.image = new_path
            page.save()

def transform_data(apps, schemd_editor) -> None:
    check_update_images(apps)

class Migration(migrations.Migration):

    dependencies = [
        ('calligraphy', '0020_auto_20161001_1503'),
    ]

    operations = [ migrations.RunPython(transform_data)
    ]