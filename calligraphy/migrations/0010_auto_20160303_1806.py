# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-04 02:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calligraphy', '0009_remove_character_char_work'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='author_dynesty',
            new_name='dynesty',
        ),
        migrations.RenameField(
            model_name='author',
            old_name='author_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='character',
            old_name='char_image',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='character',
            old_name='char_mark',
            new_name='mark',
        ),
        migrations.RenameField(
            model_name='page',
            old_name='page_bookid',
            new_name='book_id',
        ),
        migrations.RenameField(
            model_name='page',
            old_name='page_image',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='page',
            old_name='page_pageid',
            new_name='page_id',
        ),
        migrations.RenameField(
            model_name='page',
            old_name='page_transcript',
            new_name='transcript',
        ),
        migrations.RenameField(
            model_name='work',
            old_name='work_author',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='work',
            old_name='work_id',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='work',
            old_name='work_title',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='work',
            old_name='work_transcript',
            new_name='transcript',
        ),
    ]