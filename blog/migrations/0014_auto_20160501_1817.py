# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-01 18:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20160501_1816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='codetext',
            name='info',
            field=models.CharField(default='Text-2016-05-01 18:17:09.575246+00:00', max_length=140),
        ),
        migrations.RemoveField(
            model_name='entry',
            name='author',
        ),
        migrations.AddField(
            model_name='entry',
            name='author',
            field=models.ManyToManyField(related_name='author', to='blog.Author'),
        ),
    ]
