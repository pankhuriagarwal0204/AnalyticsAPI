# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-02-11 05:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('archives', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='intrusion',
            name='neutralized_datetime',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='intrusion',
            name='non_human_intrusion_datetime',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='intrusion',
            name='verified_datetime',
            field=models.DateTimeField(null=True),
        ),
    ]