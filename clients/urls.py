from django.contrib import admin
from . import views
from django.urls import path, include

urlpatterns = [
    # Clients.
    path('add_client/', views.add_client, name="add_client"),
    path('save_client', views.save_client, name="save_client"),
    path('clients/', views.clients, name="clients"),
    path('clients/<int:client_pk>/delete', views.client_delete, name="client_delete"),
    path('clients/<int:client_pk>/edit', views.client_edit, name="client_edit"),
    # Animaux.
    path('add_dog/', views.add_dog, name="add_dog"),
    path('dogs/', views.dogs, name="dogs"),
    path('save_dog/', views.save_dog, name="save_dog"),
    path('add_race/', views.add_race, name="add_race"),
    path('save_race/', views.save_race, name="save_race"),
]