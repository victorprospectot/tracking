# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-28 15:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('track', '0009_urlaccount_days_tracking_available'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visitortrack',
            name='url_visited',
            field=models.TextField(db_index=True),
        ),
    ]