# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-04 19:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20170824_1446'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='language',
            field=models.CharField(choices=[(b'en-us', 'English'), (b'pt-br', 'Portuguese')], max_length=50, null=True, verbose_name='Language'),
        ),
    ]
