# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-11 15:06
#
#
# This is a redo of 0112 because I accidentally threw away the box width
#
#
#############################################################################################

from __future__ import unicode_literals

from django.db import migrations

from django.db import migrations

def do_stuff(apps, schemd_editor) -> None:
    Pages = apps.get_model('calligraphy', 'Page').objects
    HaveChars = apps.get_model('calligraphy', 'PagesHaveChars').objects
    DetectedBox = apps.get_model('calligraphy', 'DetectedBox')
    for thisPage in HaveChars.all():
        curPage = Pages.get(id=thisPage.haveChars.id)
        print(str(curPage.image))
        for box in DetectedBox.objects.filter(parent_page=curPage.id):
            box.delete()



class Migration(migrations.Migration):

    dependencies = [
        ('calligraphy', '0115_detectedbox_inside_orig_box'),
    ]

    operations = [ migrations.RunPython(do_stuff)
    ]
