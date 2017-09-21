# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-18 19:18
from __future__ import unicode_literals

from django.db import migrations

def do_stuff(apps, schemd_editor) -> None:
    Pages = apps.get_model('calligraphy', 'Page').objects
    DetectedBox = apps.get_model('calligraphy', 'DetectedBox').objects
    PagesHaveChars = apps.get_model('calligraphy', 'PagesHaveChars').objects
    for thisPage in PagesHaveChars.all():
        curPage = Pages.get(id=thisPage.haveChars.id)
        features  = DetectedBox.filter(parent_page=curPage)
        print("PageId: " + str(thisPage.haveChars.id) + " Features: " + str(len(features)))
        for feature in features:
            saveme = False
            if feature.percent_inside_currated_box >= 80:
                feature.inside_currated_box = True
                saveme = True
            if feature.percent_inside_orig_box >=80:
                feature.inside_orig_box = True
                saveme = True
            if saveme:
                feature.save(update_fields=['inside_currated_box', 'inside_orig_box'])

class Migration(migrations.Migration):

    dependencies = [
        ('calligraphy', '0128_auto_20170918_1617'),
    ]

    operations = [ migrations.RunPython(do_stuff)
    ]
