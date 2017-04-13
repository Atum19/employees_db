# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-13 05:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dp_name', models.CharField(max_length=256, verbose_name='DPName')),
            ],
            options={
                'verbose_name': 'Department',
                'verbose_name_plural': 'Departments',
            },
        ),
    ]
