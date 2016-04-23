# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-22 06:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calligraphy', '0013_auto_20160405_0846'),
    ]

    def import_data(apps, schemd_editor) -> None:
        Char = apps.get_model("calligraphy", "Character")
        Page = apps.get_model("calligraphy", "Page")
        chars = Char.objects.all()
        for char in chars:
            #     var sWidth = 820;
            #     var sHeight = (sWidth * size[1]) / size[0] + 40;
            parent_page = char.parent_page
            width_ratio = parent_page.image_width / 820
            height_ratio = width_ratio * parent_page.image_length / parent_page.image_width
            char.newx1 = int(char.x1 * width_ratio)
            char.newy1 = int(char.y1 * height_ratio)
            char.newwidth = int((char.x2 - char.x1) * width_ratio)
            char.newheight = int((char.y2 - char.y1) * height_ratio)
            char.save()

    operations = [
        migrations.AddField(
            model_name='character',
            name='newheight',
            field=models.IntegerField(blank=True, default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='character',
            name='newwidth',
            field=models.IntegerField(blank=True, default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='character',
            name='newx1',
            field=models.IntegerField(blank=True, default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='character',
            name='newy1',
            field=models.IntegerField(blank=True, default=0),
            preserve_default=False,
        ),
        migrations.RunPython(import_data)
    ]
