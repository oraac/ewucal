# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-31 19:23
#
# Goes through and makes thumbnails of all the characters.
# If a high-rez image does not exist, makes it before the thumbnail
#
#########################################################################################################
from __future__ import unicode_literals

import django.core.files.storage
from django.db import migrations, models
from PIL import Image
from pathlib import Path
import subprocess



def do_jpg_crop(char, page_img_path) -> None:
    new_char_path = str(char.image).strip("jpg") + "hi-rez.jpg"
    width = char.x2 - char.x1
    height = char.y2 - char.y1
    crop_d = str(width) + "x" + str(height) + "+" + str(char.x1) + "+" + str(char.y1)
    out_file = '-outfile ' + new_char_path
    cmnd = ['jpegtran']
    cmnd.append('-crop')
    cmnd.append(crop_d)
    cmnd.append('-outfile')
    cmnd.append(new_char_path)
    cmnd.append(page_img_path)
    print(cmnd)
    subprocess.run(cmnd)
    char.image_high_rez = new_char_path
    char.save()

def do_png_tif_crop(char, page_img_path, img_type) -> None:
    new_char_path = str(char.image).strip("jpg") + "hi-rez." + img_type
    width = char.x2 - char.x1
    height = char.y2 - char.y1
    crop_d = str(width) + "x" + str(height) + "+" + str(char.x1) + "+" + str(char.y1)
    cmnd = ['convert']
    cmnd.append('-crop')
    cmnd.append(crop_d)
    cmnd.append(page_img_path)
    cmnd.append(new_char_path)
    print(cmnd)
    subprocess.run(cmnd)
    char.image_high_rez = new_char_path
    char.save()



def make_hi_rez(char, page) -> None:
    page_img_path = str(page.image)
    page_img_type = page_img_path.split(".")[1]
    if(page_img_type == "jpg"):
        do_jpg_crop(char, page_img_path)
    else:
        do_png_tif_crop(char, page_img_path, page_img_type)




def make_thumbnails(apps) -> None:
    Character = apps.get_model('calligraphy', 'Character')
    chars = Character.objects.all()
    for char in chars:
        fileptr = char.image_high_rez
        if not bool(fileptr):
            make_hi_rez(char, char.parent_page)
        fileptr.close()
        im = Image.open(str(char.image_high_rez))
        im.thumbnail((30, 30))
        img_thumb = str(char.image).strip('jpgpntif') + 'thumb.jpg'
        img_path_thumb = Path(img_thumb)
        im.save(img_path_thumb, 'JPEG')
        im.close()
        char.image_thumb = img_thumb
        char.save()

def do_stuff(apps, schemd_editor) -> None:
    make_thumbnails(apps)

class Migration(migrations.Migration):

    dependencies = [
        ('calligraphy', '0035_auto_20161031_1405'),
    ]

    operations = [
        migrations.RunPython(do_stuff)
    ]