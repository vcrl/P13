"""
Module permettant les tests unitaires
des urls de l'application.
"""
from django.test import SimpleTestCase
from django.urls import resolve, reverse
from ..views import services, service_delete, save_service
import re

class Test_Urls(SimpleTestCase):
    """
    Classe principale permettant d'exécuter les tests
    unitaires de l'application.
    """
    def test_services(self):
        """
        Test de l'url "services"
        """
        url = reverse('services')
        self.assertEquals(resolve(url).func, services)

    def test_service_delete(self):
        """
        Test de l'url "service_delete"
        """
        url = r'/services/\d+/delete/'
        url_to_test = '/services/1/delete/'
        self.assertTrue(re.match(url, url_to_test))

    def test_service_details(self):
        """
        Test de l'url "service_details"
        """
        url = r'/services/\d+/'
        url_to_test = '/services/1/'
        self.assertTrue(re.match(url, url_to_test))
    
    def test_save_service(self):
        """
        Test de l'url "save_service"
        """
        url = reverse('save_service')
        self.assertEquals(resolve(url).func, save_service)