"""
Module permettant les tests unitaires
des urls de l'application.
"""
from django.test import SimpleTestCase
from django.urls import resolve, reverse
from ..views import add_client, clients, dogs, save_dog, add_race, save_race, save_client
import re

class Test_Urls(SimpleTestCase):
    """
    Classe principale permettant d'exécuter les tests
    unitaires de l'application.
    """
    # Dogs.
    def test_dogs(self):
        url = reverse('dogs')
        self.assertEquals(resolve(url).func, dogs)

    def test_save_dog(self):
        url = reverse('save_dog')
        self.assertEquals(resolve(url).func, save_dog)

    # Races.
    def test_add_race(self):
        url = reverse('add_race')
        self.assertEquals(resolve(url).func, add_race)

    def save_race(self):
        url = reverse('save_race')
        self.assertEquals(resolve(url).func, save_race)
    
    # Clients.
    def test_clients(self):
        url = reverse('clients')
        self.assertEquals(resolve(url).func, clients)

    def test_add_client(self):
        url = reverse('add_client')
        self.assertEquals(resolve(url).func, add_client)

    def test_save_client(self):
        url = reverse('save_client')
        self.assertEquals(resolve(url).func, save_client)

    def test_edit_client(self):
        url = r'/clients/\d+/edit/'
        url_to_test = '/clients/1/edit/'
        self.assertTrue(re.match(url, url_to_test))
    
    def test_delete_client(self):
        url = r'/clients/\d+/delete/'
        url_to_test = '/clients/1/delete/'
        self.assertTrue(re.match(url, url_to_test))