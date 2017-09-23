# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-19 00:12
from __future__ import unicode_literals

from django.db import migrations


def do_stuff(apps, schemd_editor) -> None:
    Pages = apps.get_model('calligraphy', 'Page').objects
    HaveChars = apps.get_model('calligraphy', 'PagesHaveChars').objects
    Characters = apps.get_model('calligraphy', 'Character').objects
    DetectedBox = apps.get_model('calligraphy', 'DetectedBox')
    for thisPage in HaveChars.all():
        curPage = Pages.get(id=thisPage.haveChars.id)
        chars = Characters.filter(parent_page=curPage.id)
        print("PageId: " + str(thisPage.haveChars.id) + " Features: " + str(len(chars)))
        x_1 = 9999999999
        x_2 = 0
        y_1 = 9999999999
        y_2 = 0
        for char in chars:
            if x_1 > char.x1:
                x_1 = char.x1
            if y_1 > char.y1:
                y_1 = char.y1
            if x_2 < char.x2:
                x_2 = char.x2
            if y_2 < char.y2:
                y_2 = char.y2
        thisPage.x1 = x_1
        thisPage.x2 = x_2
        thisPage.y1 = y_1
        thisPage.y2 = y_2
        thisPage.save(update_fields=['x1', 'x2', 'y1', 'y2'])
    

class Migration(migrations.Migration):

    dependencies = [
        ('calligraphy', '0133_auto_20170919_0012'),
    ]

    operations = [ migrations.RunPython(do_stuff)
    ]