"""
Module permettant les tests unitaires
des urls de l'application.
"""
from django.test import TestCase, RequestFactory, Client, client
from django.urls import reverse, resolve
from django.core.paginator import Page
from django.contrib import auth
from ..models import Chien, Race
from ..views import clients, save_dog, add_dog, add_race, dogs
import json

class Test_Views(TestCase):
    """
    Classe principale permettant d'exécuter les tests
    unitaires de l'application.
    """
    def setUp(self):
        race = Race.objects.create(
            race="Spitz"
        )
        chien = Chien.objects.create(
            nom = 'Jules',
            race = race
        )
        chien.save()
        self.client = Client()

    def test_clients(self):
        response = self.client.get(reverse(clients))
        self.assertEqual(response.status_code, 200)
    
    def save_dog(self):
        response = self.client.get(reverse(save_dog))
        self.assertEqual(response.status_code, 302)

    def add_dog(self):
        response = self.client.get(reverse(add_dog))
        self.assertEqual(response.status_code, 302)

    def add_race(self):
        response = self.client.get(reverse(add_race))
        self.assertEqual(response.status_code, 302)

    def dogs(self):
        response = self.client.get(reverse(dogs))
        self.assertEqual(response.status_code, 200)