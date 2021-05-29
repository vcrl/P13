from django.contrib import admin
from . import views
from django.urls import path, include

urlpatterns = [
    path('services/', views.services, name="services"),
    path('add_service/', views.add_service, name="add_service"),
    path('save_service/', views.save_service, name="save_service"),
    path('services/<int:service_pk>', views.service_details, name="service_details"),
    path('services/<int:service_pk>/delete', views.service_delete, name="service_delete"),
]