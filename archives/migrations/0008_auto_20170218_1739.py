# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-02-18 12:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('archives', '0007_auto_20170218_1657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='backup',
            name='duration',
            field=models.FloatField(editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='intrusion',
            name='duration',
            field=models.FloatField(editable=False),
        ),
    ]