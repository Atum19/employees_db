# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import CreateView, UpdateView, DeleteView
from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _

from ..models.departments import Department


def departments_list(request):
    """
    Display the whole Departments List.
    """
    departments = Department.objects.all()
    departments = departments.order_by('pk')

    # paginate employees
    paginator = Paginator(departments, 5)
    page = request.GET.get('page')
    try:
        departments = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        departments = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver
        # last page of results.
        departments = paginator.page(paginator.num_pages)
    return render(request, 'dep_list.html',
                  {'departments': departments,
                   'paginator': paginator})


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
        return u'%s?status_message=%s' % (reverse('departments_list'),
                                          _(u'department added successfully!'))

    def post(self, request, *args, **kwargs):
        if request.POST.get('cancel_button'):
            return HttpResponseRedirect(
                u'%s?status_message=%s' % (reverse('departments_list'), _(u'adding canceled!')))
        else:
            return super(DepartmentAdd, self).post(request, *args, **kwargs)


class DepartmentUpdate(UpdateView):
    """
    Edit Department data.
    """
    model = Department
    form_class = DepBaseForm
    template_name = 'dep_edit.html'

    def get_object(self, queryset=None):
        return get_object_or_404(self.model, pk=self.kwargs.get('pk'))

    def get_success_url(self):
        return u'%s?status_message=%s' % (reverse('departments_list'),
                                          _(u'department updated successfully!'))

    def post(self, request, *args, **kwargs):
        if request.POST.get('cancel_button'):
            return HttpResponseRedirect(
                u'%s?status_message=%s' % (reverse('departments_list'), _(u'updating canceled!')))
        else:
            return super(DepartmentUpdate, self).post(request, *args, **kwargs)


class DepartmentDelete(DeleteView):
    """
    Delete Department data.
    """
    model = Department
    form_class = DepBaseForm
    template_name = 'dep_delete.html'

    def get_object(self, queryset=None):
        return get_object_or_404(self.model, pk=self.kwargs.get('pk'))

    def get_success_url(self):
        return u'%s?status_message=%s' % (reverse('departments_list'),
                                          _(u'department deleted successfully!'))

    def post(self, request, *args, **kwargs):
        if request.POST.get('cancel_button'):
            return HttpResponseRedirect(
                u'%s?status_message=%s' % (reverse('departments_list'), _(u'deleting canceled!')))
        else:
            return super(DepartmentDelete, self).post(request, *args, **kwargs)
