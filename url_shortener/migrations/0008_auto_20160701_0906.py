# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-01 09:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('url_shortener', '0007_auto_20160629_1146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
