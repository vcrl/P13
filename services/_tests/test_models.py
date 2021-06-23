"""
Module permettant les tests unitaires
des urls de l'application.
"""
from employes.views import employees
from django.test import TestCase, Client, RequestFactory
from django.urls import reverse, resolve
from django.contrib.auth.models import User
from django.contrib import auth
from ..models import Service

class Test_Models(TestCase):
    """
    Classe principale permettant d'exécuter les tests
    unitaires de l'application.
    """
    def test_service_save_in_db(self):
        """
        Test de l'enregistrement du model
        Service
        """
        service = Service.objects.create(
            prix = 10.00,
            )
        self.assertIs(service.prix, 10.00)