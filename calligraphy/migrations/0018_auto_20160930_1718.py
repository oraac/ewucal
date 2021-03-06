# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-01 00:18
#
# Runs through characters and populates links to authors and works
# Attempt #2 since in the previous one I had a typo
#
################################################################
from __future__ import unicode_literals

from django.db import migrations



def add_authors_and_works(apps) -> None:
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
                    char.parent_work = work
                    char.parent_author = author
                    char.save()


def transform_data(apps, schemd_editor) -> None:
    add_authors_and_works(apps)

class Migration(migrations.Migration):

    dependencies = [
        ('calligraphy', '0017_auto_20160930_1636'),
    ]

    operations = [ migrations.RunPython(transform_data)
    ]
