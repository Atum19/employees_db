from django.conf.urls import include, url

import debug_toolbar   # for debug mode

from views import employees, departments

urlpatterns = [
    url(r'^__debug__/', include(debug_toolbar.urls)),

    # employees part
    url(r'^$', employees.employees_list, name='home'),

    url(r'^employees/add_form/$', employees.EmployeeAdd.as_view(), name='employees_add'),

    url(r'^employees/(?P<pk>\d+)/view/$', employees.EmployeeDetail.as_view(), name='employees_view'),

    url(r'^employees/(?P<pk>\d+)/edit/$', employees.EmployeeUpdate.as_view(), name='employees_edit'),

    url(r'^employees/(?P<pk>\d+)/delete/$', employees.EmployeeDelete.as_view(), name='employees_delete'),

    url(r'^employees/search_names/$', employees.EmployeeSearchList.as_view(), name='employees_search'),

    # departments part
    url(r'^departments/$', departments.departments_list, name='departments_list'),

    url(r'^departments/add_form/$', departments.DepartmentAdd.as_view(), name='departments_add'),

    url(r'^departments/(?P<pk>\d+)/edit/$', departments.DepartmentUpdate.as_view(), name='departments_edit'),

    url(r'^departments/(?P<pk>\d+)/delete/$', departments.DepartmentDelete.as_view(), name='departments_delete'),
]
