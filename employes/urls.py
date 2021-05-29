from django.contrib import admin
from . import views
from django.urls import path, include

urlpatterns = [
    path('add_employee/', views.add_employee, name="add_employee"),
    path('save_employee/', views.save_employee, name="save_employee"),
    path('employees/', views.employees, name="employees"),
    path('employees/<int:employee_pk>/delete', views.employee_delete, name="employee_delete"),
    path('employees/<int:employee_pk>/edit', views.employee_edit, name="employee_edit"),
]