# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-03-06 08:10
from __future__ import unicode_literals

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_auto_20190306_1035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='post',
            field=tinymce.models.HTMLField(),
        ),
    ]
