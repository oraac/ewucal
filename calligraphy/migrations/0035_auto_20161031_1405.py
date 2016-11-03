# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-18 02:59
#
# Goes through and tries to find character multiplier values
# Note:  I run this a second time because I did not store resulting values for later analysis
#
#########################################################################################################
from __future__ import unicode_literals

import django.core.files.storage
from django.db import migrations, models
from PIL import Image
from PIL.ImageChops import difference
from PIL.ImageOps import autocontrast
from PIL.ImageOps import grayscale
from ..models import Page, Character


class char_dat(object):
    def __init__(self, coords: [str], img: Image, char: Character):
        self.x1 = int(coords[0])
        self.y1 = int(coords[1])
        self.x2 = int(coords[2])
        self.y2 = int(coords[3])
        self.img = img
        self.char = char

class page_dat(object):
    def __init__(self, x_size: int, y_size: int, img: Image, page: Page):
        self.x = x_size
        self.y = y_size
        self.img = img
        self.page = page

class wobble(object):
    def __init__(self, x_mult: float, y_mult: float, best_diff: int):
        self.x_mult = x_mult
        self.y_mult = y_mult
        self.best_diff = best_diff

def search_with_value(page: page_dat, chars: [char_dat], mult: float, max_x: int, max_y: int) -> wobble:
    histodiff_sum = 0
    best_diff_sum = 9999999999999999999999999999999999999999999999999999999999999
    max_wobble = mult * 1.1
    wobinc = (max_wobble - mult) / 10
    curx = mult
    cury = mult
    bestx = None
    besty = None
    
    while(curx < max_wobble and int(max_x * (curx + wobinc)) < page.x):
        curx += wobinc
        while(cury < max_wobble and int(max_y * (cury + wobinc)) < page.y):
            cury += wobinc
            histodiff_sum = 0
            for char in chars:
                x1 = int(curx * char.x1)
                y1 = int(cury * char.y1)
                x2 = int(curx * char.x2)
                y2 = int(cury * char.y2)
                page_char = page.img.crop([y1, x1, y2, x2])
                page_charr = autocontrast(page_char.resize([char.img.width, char.img.height], Image.BOX))
                page_diff = difference(page_charr, char.img).histogram()
                histo_sum = 0
                inc = 0
                for diff in page_diff:
                    inc += 1
                    histo_sum += diff * inc
                histodiff_sum += histo_sum
            if histodiff_sum < best_diff_sum:
                best_diff_sum = histodiff_sum
                bestx = curx
                besty = cury
    return wobble(bestx, besty, best_diff_sum)

def set_new_coords(chars: [char_dat], mult: wobble) -> None:
    for char in chars:
        mchar = char.char
        mchar.x1 = int(mult.x_mult * char.x1)
        mchar.y1 = int(mult.y_mult * char.y1)
        mchar.x2 = int(mult.x_mult * char.x2)
        mchar.y2 = int(mult.y_mult * char.y2)
        mchar.save()


def perform_search(PageMultiplier, page: page_dat, chars: [char_dat], max_x: int, max_y: int, min_width: int) -> None:
    scale_max = float(0)
    if(float(page.x) / float(max_x) < float(page.y) / float(max_y)):
        scale_max = float(page.x) / float(max_x)
    else:
        scale_max = float(page.y) / float(max_y)
    scale_cur = scale_max / 4 
    scale_inc = (scale_max - scale_cur) / 1000
    
    difflast = 0

    best_result = 999999999999999999999999999999999999999999999999999999999999999999999
    best_scale = wobble(0,0,0)
    while scale_cur < scale_max:
        scale_cur += scale_inc
        search_results = search_with_value(page, chars, scale_cur, max_x, max_y)
        if(search_results.best_diff < 99999999):
            print(search_results.best_diff)
            PageMultiplier(parent_page=page.page, match_score=search_results.best_diff, x_mult=search_results.x_mult, y_mult=search_results.y_mult).save()
        if (search_results.best_diff < best_result):
            best_result = search_results.best_diff
            best_scale = search_results
            print('----------->' + str(best_scale.best_diff) + ' : ' + str(best_scale.x_mult) + ' : ' + str(best_scale.y_mult))
    set_new_coords(chars, best_scale)



def find_search_space(PageMultiplier, page: page_dat, chars: [char_dat]) -> None:
    max_x = 0
    max_y = 0
    min_width = 9999999999
    for char in chars:
        if (max_x < char.x2):
            max_x = char.x2
        if (max_y < char.y2):
            max_y = char.y2
        if (min(char.x2 - char.x1, char.y2, char.y1) < min_width):
            min_width = min(char.x2 - char.x1, char.y2, char.y1)
    perform_search(PageMultiplier, page, chars, max_x, max_y, min_width)

def correct_coords(apps, page: Page, chars: Character) -> None:
    PageMultiplier = apps.get_model('calligraphy', 'PageMultiplier')
    print(str(page.image))
    p_img = grayscale(Image.open(str(page.image)))
    mypage = page_dat(page.image_width, page.image_length, p_img, page)
    mychars = []
    for char in chars:
        coords = str(char.image).split('(')[1].split(')')[0].split(',')
        charimg = autocontrast(grayscale(Image.open(str(char.image))))
        mychars.append(char_dat(coords, charimg, char))
    find_search_space(PageMultiplier, mypage, mychars)


def fix_coordinates(apps) -> None:
    Page = apps.get_model("calligraphy", "Page")
    Char = apps.get_model("calligraphy", "Character")
    pages = Page.objects.all()
    for page in pages:
        if page.i_valid_transform is False:
            chars = Char.objects.filter(parent_page=page)
            if len(chars) > 0:
                correct_coords(apps, page, chars)



def do_stuff(apps, schemd_editor) -> None:
    fix_coordinates(apps)

class Migration(migrations.Migration):

    dependencies = [
        ('calligraphy', '0034_character_image_thumb'),
    ]

    operations = [
        migrations.RunPython(do_stuff)
    ]