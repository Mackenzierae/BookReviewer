# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-19 22:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('belt_review', '0002_author_book_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='rating',
            field=models.IntegerField(default=None),
            preserve_default=False,
        ),
    ]