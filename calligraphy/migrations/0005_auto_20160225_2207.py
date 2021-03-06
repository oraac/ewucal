# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-26 06:07
#
# Walks through the chars on disk, and adds non-json ones to database
#
################################################
from __future__ import unicode_literals

from django.db import migrations
import socket
import os
from stat import S_ISDIR

HOSTNAME = socket.gethostname()
if HOSTNAME == 'bigArch':
    CHAR_DIR = "/home/dave/workspace/pycharm/media/chars/"
else:
    CHAR_DIR = "/media/chars/"


def add_chars_from_filesystem(apps) -> None:
    Page = apps.get_model("calligraphy", "Page")
    Char = apps.get_model("calligraphy", "Character")
    for book in os.listdir(CHAR_DIR):
        fpath = os.path.join(CHAR_DIR, book)
        if S_ISDIR(os.stat(fpath).st_mode):
            if S_ISDIR(os.stat(fpath).st_mode):
                for img in os.listdir(fpath):
                    if img.endswith('.jpg'):
                        filepath = os.path.join(fpath, img)
                        imgs = img.split('(')
                        pagenum = imgs[0]
                        coords = imgs[1].strip(').jpg').split(',')
                        x1 = int(coords[0])
                        y1 = int(coords[1])
                        x2 = int(coords[2])
                        y2 = int(coords[3])
                        page = Page.objects.filter(page_bookid=int(book), page_pageid=int(pagenum))[0]
                        chrs = Char.objects.filter(parent_page=page, x1=x1, y1=y1, x2=x2, y2=y2)
                        if len(chrs) == 0:
                            chr = Char(parent_page=page, x1=x1, y1=y1, x2=x2, y2=y2, char_image=filepath)
                            chr.save()

def import_data(apps, schemd_editor) -> None:
    add_chars_from_filesystem(apps)


class Migration(migrations.Migration):

    dependencies = [
        ('calligraphy', '0004_auto_20160225_2013'),
    ]

    operations = [ migrations.RunPython(import_data)
    ]
