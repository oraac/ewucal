# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-24 04:11
#
# Stage 2 of Data import.....  This reads c-chars.json and loads that data
#
#######################################################
import socket, json, os


HOSTNAME = socket.gethostname()
if HOSTNAME == 'bigArch':
    PAGES_DIR = "/home/dave/workspace/pycharm/fetch/grabbedBooks/"  #Maybe, need to double-check
    CHARS_DIR = "/home/dave/workspace/pycharm/fetch/chars"
else:
    PAGES_DIR = "/media/pages/"
    CHARS_DIR = "/media/chars/"

def read_cworks() -> None:
    jsonfile = open("c-chars.json", mode="r", encoding='utf-8')
    readfile = json.load(jsonfile)
    jsonfile.close()
    marks = []
    for r in readfile:
        mark = r['chi_mark']
#        auth = r['chi_author']
#        work = r['chi_work']
#        wkid = r['work_id']
#        pgid = r['page_id']
#        cord = r['xy_coordinates']
#        x1 = cord[0]
#        y1 = cord[1]
#        x2 = cord[2]
#        y2 = cord[3]
        marks.append(mark)
    marks = sorted(marks)
    x=1





read_cworks()