# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-02-18 06:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('archives', '0005_auto_20170218_1135'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='weaksignal',
            name='duration',
        ),
    ]
