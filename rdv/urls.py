from django.contrib import admin
from . import views
from django.urls import path, include

urlpatterns = [
    path('add_rdv/', views.add_rdv, name="add_rdv"),
    path('save_rdv/', views.save_rdv, name="save_rdv"),
    path('rdv/<int:rdv_pk>', views.rdv_details, name="rdv_details"),
    path('rdv_list/', views.rdv_list, name="rdv_list"),
    path('complete_rdv/<int:rdv_pk>', views.rdv_complete, name="rdv_complete"),
    path('rdv_list/<int:rdv_pk>/delete', views.rdv_delete, name="rdv_delete"),
    ]
