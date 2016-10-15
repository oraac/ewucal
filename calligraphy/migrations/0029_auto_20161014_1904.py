# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-15 02:04
#
# Go through pages deemed invalid and correct discrepancies with extensions
#
###########################################################
from __future__ import unicode_literals

from django.db import migrations
from os.path import isfile
from os import remove
from ..models import Character


def correct_transform_judgement(apps) -> None:
    Page = apps.get_model("calligraphy", "Page")
    Char = apps.get_model("calligraphy", "Character")
    pages = Page.objects.all()
    for page in pages:
        page_img_type = str(page.image).split('.')[1]
        chars = Char.objects.filter(parent_page=page)
        if(len(chars) > 0):
            good_transform = True
            for char in chars:
                char_hirez = Character.get_image(char).split('.')[0] + '.hi-rez.' + page_img_type
                if(not isfile(char_hirez)):
                    good_transform = False;
            page.i_valid_transform = good_transform
            page.save()
            if good_transform:
                for char in chars:
                    char.image_high_rez = Character.get_image(char).split('.')[0] + '.hi-rez.' + page_img_type
                    char.save()
            else:
                for char in chars:
                    char_hirez = Character.get_image(char).split('.')[0] + '.hi-rez.' + page_img_type
                    if isfile(char_hirez):
                        remove(char_hirez)
                        
                    

def do_stuff(apps, schemd_editor) -> None:
    correct_transform_judgement(apps)

class Migration(migrations.Migration):

    dependencies = [
        ('calligraphy', '0028_auto_20161011_1935'),
    ]

    operations = [ migrations.RunPython(do_stuff)
    ]
