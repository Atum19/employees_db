# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-13 08:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0003_employee_emp_department'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='emp_active',
            field=models.BooleanField(verbose_name='IsActive'),
        ),
    ]