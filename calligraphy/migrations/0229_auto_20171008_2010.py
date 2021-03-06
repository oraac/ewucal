# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-10-08 20:10
#
# Goes through and writes important datasets to disk
#
######################################################
from __future__ import unicode_literals

from django.db import migrations
import numpy as np

def build_np(boxes):
    features = np.zeros((len(boxes), 10), dtype=np.int32)
    bin_good = np.zeros(len(boxes), dtype=np.bool)
    bin_bad  = np.zeros(len(boxes), dtype=np.bool)
    for i in range(len(boxes)):
        bin_good[i] = boxes[i].inside_currated_box
        bin_bad[i]  = boxes[i].inside_orig_box
        features[i][0] = boxes[i].area_norm
        features[i][1] = boxes[i].eccentricity_norm
        features[i][2] = boxes[i].solidity_norm
        features[i][3] = boxes[i].orientation_norm
        features[i][4] = boxes[i].li_threshold_bottom_norm
        features[i][5] = boxes[i].li_threshold_top_norm
        features[i][6] = boxes[i].local_centroid_x_norm
        features[i][7] = boxes[i].local_centroid_y_norm
        features[i][8] = boxes[i].major_axis_length_norm
        features[i][9] = boxes[i].minor_axis_length_norm
    return features, bin_bad, bin_good

def do_stuff(apps, schemd_editor):
    DetectedBox = apps.get_model('calligraphy', 'DetectedBox').objects
    pages_scn = apps.get_model('calligraphy', 'Page').objects.filter(has_copyright_restrictions=True)
#    pages_web = apps.get_model('calligraphy', 'Page').objects.filter(has_copyright_restrictions=False, black_chars=False)
#    first_loop = True
#    web_ftrs = None
#    web_bin_bads = None
#    web_bin_goods = None
#    for page_web in pages_web:
#        boxes = DetectedBox.filter(parent_page=page_web)
#        if len(boxes) > 0:
#            web_ftr, web_bin_bad, web_bin_good = build_np(boxes)
#            if first_loop:
#                web_ftrs = web_ftr
#                web_bin_bads = web_bin_bad
#                web_bin_goods = web_bin_good
#                first_loop = False
#            else:
#                web_ftrs = np.append(web_ftrs, web_ftr, axis=0)
#                web_bin_bads = np.append(web_bin_bads, web_bin_bad)
#                web_bin_goods = np.append(web_bin_goods, web_bin_good)
#    np.save('web_ftrs_wht.npy', web_ftrs)
#    np.save('web_bin_bads_wht.npy', web_bin_bads)
#    np.save('web_bin_goods_wht.npy', web_bin_goods)
#    pages_web = apps.get_model('calligraphy', 'Page').objects.filter(has_copyright_restrictions=False)
#    first_loop = True
#    web_ftrs = None
#    web_bin_bads = None
#    web_bin_goods = None
#    for page_web in pages_web:
#        boxes = DetectedBox.filter(parent_page=page_web)
#        if len(boxes) > 0:
#            web_ftr, web_bin_bad, web_bin_good = build_np(boxes)
#            if first_loop:
#                web_ftrs = web_ftr
#                web_bin_bads = web_bin_bad
#                web_bin_goods = web_bin_good
#                first_loop = False
#            else:
#                web_ftrs = np.append(web_ftrs, web_ftr, axis=0)
#                web_bin_bads = np.append(web_bin_bads, web_bin_bad)
#                web_bin_goods = np.append(web_bin_goods, web_bin_good)
#    np.save('web_ftrs.npy', web_ftrs)
#    np.save('web_bin_bads.npy', web_bin_bads)
#    np.save('web_bin_goods.npy', web_bin_goods)
    first_loop = True
    scn_ftrs = None
    scn_bin_bads = None
    scn_bin_goods = None
    for page_scn in pages_scn:
        scanned_boxes = DetectedBox.filter(parent_page=page_scn)
        scn_ftr, scn_bin_bad, scn_bin_good = build_np(scanned_boxes)
#        for i in range(len(scanned_boxes)):
#            scanned_boxes[i].predict_using_good = pred_good[i]
#            scanned_boxes[i].predict_using_bad = pred_bad[i]
#            scanned_boxes[i].save()
        if first_loop:
            scn_ftrs = scn_ftr
            scn_bin_bads = scn_bin_bad
            scn_bin_goods = scn_bin_good
            first_loop = False
        else:
            scn_ftrs = np.append(scn_ftrs, scn_ftr, axis=0)
            scn_bin_bads = np.append(scn_bin_bads, scn_bin_bad)
            scn_bin_goods = np.append(scn_bin_goods, scn_bin_good)
    print("Features: " + str(len(scn_bin_bads)))
    np.save('scn_ftrs.npy', scn_ftrs)
    np.save('scn_bin.npy', scn_bin_goods)



class Migration(migrations.Migration):

    dependencies = [
        ('calligraphy', '0228_remove_detectedbox_black_chars'),
    ]

    operations = [ migrations.RunPython(do_stuff)
    ]
