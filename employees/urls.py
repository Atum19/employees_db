from django.conf.urls import include, url
from django.contrib import admin
import debug_toolbar   # add this

# from views import students, groups, exams, contact_admin, journal
# from employees import views
from views import employees

urlpatterns = [
    # Students urls
    # url(r'^$', views.students_list, name='home'),
    url(r'^__debug__/', include(debug_toolbar.urls)),   # added this line

    url(r'^$', employees.employees_list, name='home'),
    # url(r'^students/$', students.students_list, name='home'),

    url(r'^employees/add/$', employees.employees_add, name='employees_add'),

    url(r'^employees/(?P<sid>\d+)/view/$', employees.employees_view, name='employees_view'),

    url(r'^employees/(?P<sid>\d+)/edit/$', employees.employees_edit, name='employees_edit'),

    url(r'^employees/(?P<sid>\d+)/delete/$', employees.employees_delete, name='employees_delete'),



    # Contact Admin Form
    # url(r'^admin/', include(admin.site.urls)),
    # url(r'^contact-admin/$', contact_admin.contact_admin, name='contact_admin'),
    # url(r'^contact-admin/$', contact_admin.ContactView.as_view(), name='contact_admin'),
]
