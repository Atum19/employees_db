# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.generic import CreateView
from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _

from ..models.departments import Department


class DepBaseForm(ModelForm):
    class Meta:
        model = Department
        fields = "__all__"


class DepartmentAdd(CreateView):
    """
    Add Department data.
    """
    model = Department
    form_class = DepBaseForm
    template_name = 'dep_add.html'

    def get_success_url(self):
        return u'%s?status_message=%s' % (reverse('home'),
                                          _(u'department added successfully!'))

    def post(self, request, *args, **kwargs):
        if request.POST.get('cancel_button'):
            return HttpResponseRedirect(
                u'%s?status_message=%s' % (reverse('home'), _(u'adding canceled!')))
        else:
            return super(DepartmentAdd, self).post(request, *args, **kwargs)
