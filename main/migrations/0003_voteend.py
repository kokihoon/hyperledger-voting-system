# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-29 17:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20171127_1836'),
    ]

    operations = [
        migrations.CreateModel(
            name='VoteEnd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isEnd', models.BooleanField()),
            ],
        ),
    ]
