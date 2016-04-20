# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-20 16:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mdirector', '0007_delivery_openings_total'),
    ]

    operations = [
        migrations.CreateModel(
            name='StatsDelivery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=100)),
                ('date', models.DateTimeField()),
                ('url', models.CharField(max_length=200, null=True)),
                ('reason', models.TextField(null=True)),
                ('type_stats', models.CharField(max_length=20)),
                ('campaign', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mdirector.Campaign')),
            ],
        ),
    ]