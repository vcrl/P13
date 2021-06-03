
"""
Module permettant les tests unitaires
des urls de l'application.
"""
from django.test import SimpleTestCase
from django.urls import resolve, reverse
from ..views import rdv_list, rdv_complete, rdv_delete, add_rdv
import re

class Test_Urls(SimpleTestCase):
    """
    Classe principale permettant d'exécuter les tests
    unitaires de l'application.
    """
    def trst_add_rdv(self):
        url = reverse('add_rdv')
        self.assertEquals(resolve(url).func, add_rdv)

    def test_rdv_delete(self):
        url = r'/rdv_list/\d+/delete/'
        url_to_test = '/rdv_list/1/delete/'
        self.assertTrue(re.match(url, url_to_test))

    def test_rdv_complete(self):
        url = r'/rdv_list/\d+/complete/'
        url_to_test = '/rdv_list/1/complete/'
        self.assertTrue(re.match(url, url_to_test))
    
    def test_rdv_list(self):
        url = reverse('rdv_list')
        self.assertEquals(resolve(url).func, rdv_list)