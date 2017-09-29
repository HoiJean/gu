# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-24 10:06
from __future__ import unicode_literals

from django.db import migrations
import filebrowser.fields


class Migration(migrations.Migration):

    dependencies = [
        ('socialmedia', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='image',
            field=filebrowser.fields.FileBrowseField(blank=True, default='', max_length=200),
            preserve_default=False,
        ),
    ]