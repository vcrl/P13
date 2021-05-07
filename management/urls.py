from django.contrib import admin
from . import views
from django.urls import path, include

urlpatterns = [
    # Clients.
    path('add_client/', views.add_client, name="add_client"),
    path('save_client', views.save_client, name="save_client"),
    path('clients/', views.clients, name="clients"),
    # Animaux.
    path('add_dog/', views.add_dog, name="add_dog"),
    path('dogs/', views.dogs, name="dogs"),
    path('save_dog/', views.save_dog, name="save_dog"),
    path('add_race/', views.add_race, name="add_race"),
    path('save_race/', views.save_race, name="save_race"),
    # RDV.
    path('calendar/', views.calendar, name="calendar"),
    path('services/', views.services, name="services"),
    path('add_rdv/', views.add_rdv, name="add_rdv"),
    # Services.
    path('add_service/', views.add_service, name="add_service"),
    path('save_service/', views.save_service, name="save_service"),
    path('services/<int:service_pk>', views.service_details, name="service_details"),
    path('services/<int:service_pk>/delete', views.service_delete, name="service_delete"),
]