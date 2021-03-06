# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-03-23 21:52
#
#  This erases resets and repopulates all of the todo chars and no-chars lists
#
#

from __future__ import unicode_literals

from django.db import migrations

def do_stuff(apps, schemd_editor) -> None:
    Page = apps.get_model('calligraphy', 'Page')
    Char = apps.get_model('calligraphy', 'Character')
    ToDrawWoBoxes = apps.get_model('calligraphy', 'ToDrawBoxesWoBoxes')
    ToDrawWBoxes  = apps.get_model('calligraphy', 'ToDrawBoxesWBoxes')
    
    ToDrawWoBoxes.objects.all().delete()
    ToDrawWBoxes.objects.all().delete()
    
    for page in Page.objects.all():
        if len(Char.objects.filter(parent_page=page)) > 0:
            ToDrawWBoxes(toCheck = page).save()
        else:
            ToDrawWoBoxes(toCheck = page).save()


class Migration(migrations.Migration):

    dependencies = [
        ('calligraphy', '0096_remove_page_image_bad'),
    ]

    operations = [ migrations.RunPython(do_stuff)
    ]
