# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-15 03:57
#
# Goes round and makes sure characters all have a parent work and parent author
#
##############################################################
from __future__ import unicode_literals

from django.db import migrations


def add_missed_auth_works(apps) -> None:
    Author = apps.get_model("calligraphy", "Author")
    Work = apps.get_model("calligraphy", "Work")
    Page = apps.get_model("calligraphy", "Page")
    Char = apps.get_model("calligraphy", "Character")
    authors = Author.objects.all()
    for author in authors:
        works = Work.objects.filter(author=author)
        for work in works:
            pages = Page.objects.filter(parent_work=work)
            for page in pages:
                chars = Char.objects.filter(parent_page=page)
                for char in chars:
                    save_me = False
                    if char.parent_work is None:
                        char.parent_work = work
                        save_me = True
                    if char.parent_author is None:
                        char.parent_author = author
                        save_me = True
                    if save_me:
                        char.save()
                    
def do_stuff(apps, schemd_editor) -> None:
    add_missed_auth_works(apps)

class Migration(migrations.Migration):

    dependencies = [
        ('calligraphy', '0029_auto_20161014_1904'),
    ]

    operations = [ migrations.RunPython(do_stuff)
    ]
