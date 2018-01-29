# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-28 12:07
from __future__ import unicode_literals

from django.db import migrations
import imagekit.models.fields
import photos.models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photoupload',
            name='image',
            field=imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to=photos.models.PhotoUpload.path_and_rename),
        ),
    ]
