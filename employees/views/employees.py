# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.views.generic.detail import DetailView
from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _

from ..models.employees import Employee


def employees_list(request):
    """
    Display the whole Employees List.
    """
    employees = Employee.objects.all()
    employees = employees.order_by('pk')

    # paginate employees
    paginator = Paginator(employees, 10)
    page = request.GET.get('page')
    try:
        employees = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        employees = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver
        # last page of results.
        employees = paginator.page(paginator.num_pages)
    return render(request, 'emp_list.html',
                  {'employees': employees,
                   'paginator': paginator})


class BaseForm(ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"


class EmployeeDetail(DetailView):
    """
    Display single Employee data.
    """
    template_name = 'emp_view.html'

    def get_object(self, queryset=None):
        return get_object_or_404(Employee, pk=self.kwargs.get("pk"))

    def post(self, request, *args, **kwargs):
        if request.POST.get('back_button'):
            return HttpResponseRedirect(reverse('home'))


class EmployeeUpdate(UpdateView):
    """
    Edit Employee data.
    """
    model = Employee
    form_class = BaseForm
    template_name = 'emp_edit.html'

    def get_object(self, queryset=None):

        return get_object_or_404(self.model, pk=self.kwargs.get('pk'))

    def get_success_url(self):
        return u'%s?status_message=%s' % (reverse('home'),
                                          _(u'employee updated successfully!'))

    def post(self, request, *args, **kwargs):
        if request.POST.get('cancel_button'):
            return HttpResponseRedirect(
                u'%s?status_message=%s' % (reverse('home'), _(u'updating canceled!')))
        else:
            return super(EmployeeUpdate, self).post(request, *args, **kwargs)


class EmployeeAdd(CreateView):
    """
    Add Employee data.
    """
    model = Employee
    form_class = BaseForm
    template_name = 'emp_add.html'

    def get_success_url(self):
        return u'%s?status_message=%s' % (reverse('home'),
                                          _(u'employee added successfully!'))

    def post(self, request, *args, **kwargs):
        if request.POST.get('cancel_button'):
            return HttpResponseRedirect(
                u'%s?status_message=%s' % (reverse('home'), _(u'adding canceled!')))
        else:
            return super(EmployeeAdd, self).post(request, *args, **kwargs)


class EmployeeDelete(DeleteView):
    """
    Delete Employee data.
    """
    model = Employee
    form_class = BaseForm
    template_name = 'emp_delete.html'

    def get_object(self, queryset=None):
        return get_object_or_404(self.model, pk=self.kwargs.get('pk'))

    def get_success_url(self):
        return u'%s?status_message=%s' % (reverse('home'),
                                          _(u'employee deleted successfully!'))

    def post(self, request, *args, **kwargs):
        if request.POST.get('cancel_button'):
            return HttpResponseRedirect(
                u'%s?status_message=%s' % (reverse('home'), _(u'deleting canceled!')))
        else:
            return super(EmployeeDelete, self).post(request, *args, **kwargs)


class EmployeeSearchList(ListView):
    """
    Display Employees List pages filtered by the search query.
    """
    paginate_by = 10
    model = Employee
    template_name = 'emp_search.html'

    def __init__(self, *args, **kwargs):
        super(EmployeeSearchList, self).__init__(*args, **kwargs)
        self.search_name = None  # we need to have the same searching data for two different requests

    @staticmethod
    def get_data(name, page):
        if name:
            elem_lst = Employee.objects.filter(emp_name__startswith=name)
        else:
            elem_lst = Employee.objects.all()
        paginator = Paginator(elem_lst, 10)
        try:
            emp_lst = paginator.page(page)
        except PageNotAnInteger:
            emp_lst = paginator.page(1)
        except EmptyPage:
            emp_lst = paginator.page(paginator.num_pages)
        return emp_lst

    def get_context_data(self, **kwargs):
        context = super(EmployeeSearchList, self).get_context_data(**kwargs)

        page = self.request.GET.get('page') or 1
        search_name = self.request.GET.get('search_name')
        if search_name:
            if page:
                context['employee_list'] = self.get_data(search_name, page)
                context['search_name'] = search_name
        elif page:
            context['employee_list'] = self.get_data(self.search_name, page)
        return context

    def post(self, request):
        if request.POST.get('back_button'):
            return HttpResponseRedirect(reverse('home'))
