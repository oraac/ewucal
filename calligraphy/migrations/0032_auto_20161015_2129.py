# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-16 04:29
#
# use jpegtran to make all jpeg images match the collorspace of parent image
#
###################################################################
from __future__ import unicode_literals

from django.db import migrations
from PIL import Image
import subprocess

def fix_colorspace(apps) -> None:
    Page = apps.get_model("calligraphy", "Page")
    Char = apps.get_model("calligraphy", "Character")
    pages = Page.objects.all()
    for page in pages:
        if not "RGB" in str(Image.open(str(page.image)).mode):  # Page is grayscale
            chars = Char.objects.filter(parent_page=page)
            if(len(chars) > 0):
                for char in chars:
                    charname = str(char.image)
                    tmpcharname = charname.strip(".jpg") + "t.jpg"
                    cmnd = ['jpegtran']
                    cmnd.append('-optimize')
                    cmnd.append('-grayscale')
                    cmnd.append('-outfile')
                    cmnd.append(tmpcharname)
                    cmnd.append(charname)
                    subprocess.run(cmnd)
                    cmnd2 = [ 'mv', '-f', tmpcharname, charname]
                    subprocess.run(cmnd2)

def do_stuff(apps, schemd_editor) -> None:
    fix_colorspace(apps)

class Migration(migrations.Migration):

    dependencies = [
        ('calligraphy', '0031_page_i_transform_type_new'),
    ]

    operations = [ migrations.RunPython(do_stuff)
    ]
