# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-02 10:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Community', '0008_auto_20180102_0951'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='requestcommunitycreation',
            name='user',
        ),
        migrations.AddField(
            model_name='requestcommunitycreation',
            name='email',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='requestcommunitycreation',
            name='requestedby',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
