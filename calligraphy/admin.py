from django.contrib import admin

from . import models


class CAuthor(admin.ModelAdmin):
    list_display = ('id', 'author_name', 'author_dynesty')


class CWork(admin.ModelAdmin):
    list_display = ('work_id', 'work_title', 'work_author', 'work_transcript')


class CPage(admin.ModelAdmin):
    list_display = ('id', 'page_image', 'page_transcript', 'parent_work')


class CCharacter(admin.ModelAdmin):
    list_display = ('id', 'char_mark', 'x1', 'y1', 'x2', 'y2', 'char_image', 'parent_page')

admin.site.register(models.Author, CAuthor)
admin.site.register(models.Work, CWork)
admin.site.register(models.Page, CPage)
admin.site.register(models.Character, CCharacter)
