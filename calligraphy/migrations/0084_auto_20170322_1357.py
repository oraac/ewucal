# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-03-22 13:57
#
#
# Goes through and stores all the origional character data inside a table so we can manipulate the current table without fear
#
#
from __future__ import unicode_literals

from django.db import migrations


def backup_table(apps) -> None:
    Chars_back = apps.get_model('calligraphy', 'Character_orig')
    for char in apps.get_model('calligraphy', 'Character').objects.all():
        Chars_back(              id = char.id,
                                 author_name = char.author_name,
                                 parent_work_name = char.parent_work_name,
                                 supplied_by = char.supplied_by,
                                 parent_page = char.parent_page,
                                 parent_author = char.parent_author,
                                 parent_work = char.parent_work,
                                 mark = char.mark,
                                 x1 = char.x1,
                                 y1 = char.y1,
                                 x2 = char.x2,
                                 y2 = char.y2,
                                 image = char.image,
                                 image_width = char.image_width,
                                 image_height = char.image_height).save()


def do_stuff(apps, schemd_editor) -> None:
    backup_table(apps)

class Migration(migrations.Migration):

    dependencies = [
        ('calligraphy', '0083_character_orig'),
    ]

    operations = [ migrations.RunPython(do_stuff)
    ]
