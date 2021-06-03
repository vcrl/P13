
"""
Module permettant les tests unitaires
des urls de l'application.
"""
from django.test import SimpleTestCase
from django.urls import resolve, reverse
from ..views import revenus_mensuel, revenus_annuels
import re

class Test_Urls(SimpleTestCase):
    """
    Classe principale permettant d'exécuter les tests
    unitaires de l'application.
    """
    def test_revenu_mensuel(self):
        """
        Test de l'url "revenu_mensuel"
        """
        url = reverse('revenus_mensuel')
        self.assertEquals(resolve(url).func, revenus_mensuel)

    def test_rdv_delete(self):
        """
        Test de l'url "rdv_delete"
        """
        url = reverse('revenus_annuels')
        self.assertEquals(resolve(url).func, revenus_annuels)