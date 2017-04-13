# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models.employees import Employee
from .models.departments import Department


# Register your models here.
admin.site.register(Employee)
admin.site.register(Department)
