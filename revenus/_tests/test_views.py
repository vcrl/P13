
"""
Module permettant les tests unitaires
des vues de l'application.
"""
from django.test import TestCase, RequestFactory, Client, client
from django.contrib.auth.models import User

from django.urls import reverse, resolve
from django.core.paginator import Page
from django.contrib import auth
from ..views import revenus_annuels, revenus_mensuel
import json

class Test_Views(TestCase):
    """
    Classe principale permettant d'exécuter les tests
    unitaires de l'application.
    """
    def setUp(self):
        self.client = Client()

    def test_revenus_annuels(self):
        """
        Test de la vue "revenus_annuels"
        """
        response = self.client.get(reverse(revenus_annuels))
        self.assertEqual(response.status_code, 302)
    
    def test_revenus_annuels_login(self):
        user = User.objects.create_user(
            username = 'user',
            password = '123'
        )
        user.save()
        self.client.login(username="user", password="123")
        response = self.client.get(reverse(revenus_annuels))
        self.assertEqual(response.status_code, 200)
    
    def test_revenus_mensuel(self):
        """
        Test de la vue "revenus_mensuel"
        """
        response = self.client.get(reverse(revenus_mensuel))
        self.assertEqual(response.status_code, 302)

    def test_revenus_mensuels_login(self):
        user = User.objects.create_user(
            username = 'user',
            password = '123'
        )
        user.save()
        self.client.login(username="user", password="123")
        response = self.client.get(reverse(revenus_mensuel))
        self.assertEqual(response.status_code, 200)
