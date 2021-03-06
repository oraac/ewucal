# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-15 20:10
from __future__ import unicode_literals

from django.db import migrations
from django.db import migrations, models
from PIL import Image
import subprocess as sub
from os import path
from os import remove

def make_thumbnails(apps) -> None:
    Character = apps.get_model('calligraphy', 'Character')
    Page = apps.get_model('calligraphy', 'Page')
    chars = Character.objects.all()
    for char in chars:
        imName = str(char.image_high_rez)
        if not path.isfile(imName):
            myPage = Page.objects.get(id=char.parent_work.id)
            pageImg = Image.open(str(myPage.image))
            croppedImg = pageImg.crop([char.x1, char.y1, char.x2, char.y2])
            croppedImg.save(imName, format='PNG', optimize=True)
        im = Image.open(imName)
        height = int(float(char.x2 - char.x1) / float(char.y2 - char.y1) * 200)
        img_thumb = im.resize((200, height), Image.BOX)
        img_thumb_name = str(char.image).strip('jpgpntif') + 'thumb.jpg'
        img_png_name = img_thumb_name.strip('jpg') + 'png'
        if path.isfile(img_png_name):
            remove(img_png_name)
        if path.isfile(img_thumb_name):
            remove(img_thumb_name)
        img_thumb.save(img_thumb_name, format='JPEG', optimize=True)
        img_thumb.close()
        char.image_thumb = img_thumb_name
        char.image_thumb_y = 200
        char.image_thumb_x = height
        char.save()

def do_stuff(apps, schemd_editor) -> None:
    make_thumbnails(apps)

class Migration(migrations.Migration):

    dependencies = [
        ('calligraphy', '0041_auto_20161114_2001'),
    ]

    operations = [  migrations.RunPython(do_stuff)
    ]
