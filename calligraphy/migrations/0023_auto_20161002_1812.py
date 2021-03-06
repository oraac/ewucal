# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-03 01:12
#
# Create high-rez characters and add those characters to char database
#
#############################################################################################
from __future__ import unicode_literals

from django.db import migrations
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


def make_new_char_image(page, char) -> None:
    page_img_path = str(page.image)
    page_img_type = page_img_path.split(".")[1]
    if(page.image_width < char.x2 or page.image_length < char.y2):
        print(page.image_type_httpRequest)
        page.image_type_httpRequest = str(page.image_type_httpRequest).split(" : ")[0] + " : BADCHARS" # WARNING!:  This line probably foobars this row in the database
        page.save()
    else:
        if(page_img_type == "jpg"):
            do_jpg_crop(char, page_img_path)
        else:
            do_png_tif_crop(char, page_img_path, page_img_type)

def make_high_rez(apps) -> None:
    Page = apps.get_model("calligraphy", "Page")
    Char = apps.get_model("calligraphy", "Character")
    pages = Page.objects.all()
    for page in pages:
        chars = Char.objects.filter(parent_page=page)
        for char in chars:
            make_new_char_image(page, char)

def transform_data(apps, schemd_editor) -> None:
    make_high_rez(apps)

class Migration(migrations.Migration):

    dependencies = [
        ('calligraphy', '0022_character_image_high_rez'),
    ]

    operations = [ migrations.RunPython(transform_data)
    ]
