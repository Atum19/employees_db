from django.conf.urls import include, url

import debug_toolbar   # for debug mode

from views import employees

urlpatterns = [
    url(r'^__debug__/', include(debug_toolbar.urls)),

    url(r'^$', employees.employees_list, name='home'),

    url(r'^employees/add_form/$', employees.EmployeeAdd.as_view(), name='employees_add'),

    url(r'^employees/(?P<pk>\d+)/view/$', employees.EmployeeDetail.as_view(), name='employees_view'),

    url(r'^employees/(?P<pk>\d+)/edit/$', employees.EmployeeUpdate.as_view(), name='employees_edit'),

    url(r'^employees/(?P<pk>\d+)/delete/$', employees.EmployeeDelete.as_view(), name='employees_delete'),

    url(r'^employees/search_names/$', employees.EmployeeSearchList.as_view(), name='employees_search'),
]
