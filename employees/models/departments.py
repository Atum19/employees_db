# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Department(models.Model):

    class Meta(object):
        verbose_name = "Department"
        verbose_name_plural = "Departments"

    dp_name = models.CharField(
        max_length=256,
        blank=False,
        verbose_name="DPName")

    def __unicode__(self):
        return "%s" % self.dp_name
