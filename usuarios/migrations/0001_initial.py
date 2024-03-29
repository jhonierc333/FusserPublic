# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-10-26 13:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('cedula', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=50)),
                ('phone_number', models.CharField(blank=True, max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
