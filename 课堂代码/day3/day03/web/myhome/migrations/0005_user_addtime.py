# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-12 02:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myhome', '0004_user_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='addtime',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
