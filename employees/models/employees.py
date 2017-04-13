# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Employee(models.Model):

    class Meta(object):
        verbose_name = u"Employee"
        verbose_name_plural = u"Employees"

    emp_name = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=u"Name")

    emp_active = models.BooleanField(
        blank=False,
        verbose_name=u"IsActive")

    emp_department = models.ForeignKey("Department",
                                       verbose_name=u"DPName",
                                       blank=False,
                                       null=True,
                                       on_delete=models.PROTECT)

    def __unicode__(self):
        return u"%s" % self.emp_name
        # return u"%s %s" % (self.first_name, self.last_name)
