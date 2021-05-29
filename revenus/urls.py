from django.contrib import admin
from . import views
from django.urls import path, include

urlpatterns = [
    path('revenus/mensuels', views.revenus_mensuel, name="revenus_mensuel"),
    path('revenus/annuels', views.revenus_annuels, name="revenus_annuels"),
]