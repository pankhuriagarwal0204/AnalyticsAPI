# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-02-18 05:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('archives', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='morcha',
            name='units',
            field=models.ManyToManyField(related_name='units', to='archives.Device'),
        ),
    ]