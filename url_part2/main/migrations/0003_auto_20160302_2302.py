# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-03-02 23:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20160302_2248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='private',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='url',
            name='short',
            field=models.CharField(default='a4bed1fc-27eb-4402-aec8-b6b5225769ed', max_length=255),
        ),
    ]