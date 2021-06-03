"""
Module permettant les tests unitaires
des vues de l'application.
"""
from django.test import TestCase, RequestFactory, Client, client
from django.urls import reverse, resolve
from django.core.paginator import Page
from django.contrib import auth
from ..models import Service
from ..views import service_delete, service_details, services, save_service
import json

class Test_Views(TestCase):
    """
    Classe principale permettant d'exécuter les tests
    unitaires de l'application.
    """
    def setUp(self):
        """
        Méthode setup
        """
        self.client = Client()

    def test_services(self):
        """
        Test de la vues "services"
        """
        response = self.client.get(reverse(services))
        self.assertEqual(response.status_code, 200)
    
    def test_service_delete(self):
        """
        Test de la vue "service_delete"
        """
        service = Service.objects.create(
            prix=10.00,
        )
        service.save()
        response = self.client.get('/services/' + str(service.id) + '/delete')
        self.assertEqual(response.status_code, 302)

    def test_save_service(self):
        """
        Test de la vue "save_service"
        """
        response = self.client.get(reverse(save_service))
        self.assertEqual(response.status_code, 302)
