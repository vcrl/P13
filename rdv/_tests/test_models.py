"""
Module permettant les tests unitaires
des vues de l'application.
"""
from employes.views import employees
from django.test import TestCase, Client, RequestFactory
from django.urls import reverse, resolve
from django.contrib.auth.models import User
from django.contrib import auth
from ..models import RDV

class Test_Models(TestCase):
    """
    Classe principale permettant d'exécuter les tests
    unitaires de l'application.
    """
    def test_rdv_save_in_db(self):
        rdv = RDV.objects.create(
            comment="Test",
            completed="1990-01-01 00:00",
            date="1990-01-01 00:00"
            )
        self.assertIs(rdv.completed, "1990-01-01 00:00")
        self.assertIs(rdv.date, "1990-01-01 00:00")
        self.assertIs(rdv.comment, "Test")