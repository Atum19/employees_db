# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from ..models.employees import Employee


def employees_list(request):
    employees = Employee.objects.all()
    employees = employees.order_by('pk')
    for el in employees:
        print '>>>>>>', el
    # employees = (
    #     {'id': 1,
    #      'emp_name': u'Lisa',
    #      'emp_active': u'Yes',
    #      'emp_department': 'HR'},
    #     {'id': 2,
    #      'emp_name': u'Erik',
    #      'emp_active': u'Yes',
    #      'emp_department': 'Tech'},
    #     {'id': 3,
    #      'emp_name': u'Peter',
    #      'emp_active': u'Yes',
    #      'emp_department': 'Finance'}
    # )
    # return render(request, 'emp_list.html', {})

    # paginate students
    paginator = Paginator(employees, 3)
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
                  {'employees': employees})

def employees_add(request):
    return HttpResponse('<h1>employees Add Form</h1>')


def employees_view(request, sid):
    return HttpResponse('<h1>View employees %s</h1>' % sid)


def employees_edit(request, sid):
    return HttpResponse('<h1>Edit employees %s</h1>' % sid)


def employees_delete(request, sid):
    return HttpResponse('<h1>Delete employees %s</h1>' % sid)
