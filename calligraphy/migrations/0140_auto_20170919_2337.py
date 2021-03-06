# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-19 23:37
from __future__ import unicode_literals

from django.db import migrations, connection

def do_stuff(apps, schemd_editor) -> None:
    Pages = apps.get_model('calligraphy', 'Page').objects
    HaveChars = apps.get_model('calligraphy', 'PagesHaveChars').objects
    DetectedBox = apps.get_model('calligraphy', 'DetectedBox').objects
    with connection.cursor() as cursor:
        for thisPage in HaveChars.all():
            parent_area = (thisPage.x2 - thisPage.x1)  *  (thisPage.y2 - thisPage.y1)
            norm_mult = 1 / parent_area * 2147483647
            print("PageId: " + str(thisPage.haveChars.id))
            cursor.execute("UPDATE calligraphy_detectedbox SET convex_area_norm = CAST( convex_area * %s AS int )  WHERE parent_page_id = %s", [norm_mult, thisPage.haveChars.id])

class Migration(migrations.Migration):

    dependencies = [
        ('calligraphy', '0139_detectedbox_convex_area_norm'),
    ]

    operations = [ migrations.RunPython(do_stuff)
    ]
