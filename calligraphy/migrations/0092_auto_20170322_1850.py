# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-03-22 18:50
#
# adjust coordinates for all characters
#
######################################################################

from __future__ import unicode_literals

from django.db import migrations

def fix_coordinates(apps) -> None:
    Chars_back = apps.get_model('calligraphy', 'Character_orig')
    Chars =      apps.get_model('calligraphy', 'Character')
    CharSet =    apps.get_model('calligraphy', 'CharSet')
    
    for charset in CharSet.objects.all():
        for ochar in charset.set_chars_orig.all():
            char = Chars.objects.get(id=ochar.id)
            char.x1 = int(ochar.x1 * charset.set_offset_x)
            char.x2 = int(ochar.x2 * charset.set_offset_x)
            char.y1 = int(ochar.y1 * charset.set_offset_y)
            char.y2 = int(ochar.y2 * charset.set_offset_y)
            char.save()
            

def do_stuff(apps, schemd_editor) -> None:
    fix_coordinates(apps)

class Migration(migrations.Migration):

    dependencies = [
        ('calligraphy', '0091_remove_charset_set_chars'),
    ]

    operations = [ migrations.RunPython(do_stuff)
    ]
