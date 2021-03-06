# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-02-18 16:32
#
# Populates a to validate list
#
#############################################################
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion

def create_list(apps) -> None:
    ToVal = apps.get_model('calligraphy', 'ToValidateOffsets')
    for user_supp in apps.get_model('calligraphy', 'UserSuppliedPageMultiplier').objects.all():
        newToDo = ToVal(toCheck=user_supp)
        newToDo.save()


def do_stuff(apps, schemd_editor) -> None:
    create_list(apps)

class Migration(migrations.Migration):

    dependencies = [
        ('calligraphy', '0066_auto_20170218_1028'),
    ]

    operations = [
        migrations.CreateModel(
            name='ToValidateOffsets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('toCheck', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='calligraphy.UserSuppliedPageMultiplier')),
            ],
        ),
        migrations.RunPython(do_stuff)
    ]
