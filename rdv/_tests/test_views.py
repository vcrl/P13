"""
Module permettant les tests unitaires
des vues de l'application.
"""
from django.test import TestCase, RequestFactory, Client, client
from django.urls import reverse, resolve
from django.core.paginator import Page
from django.contrib import auth
from ..models import RDV
from ..views import add_rdv, rdv_complete, rdv_delete, rdv_details, rdv_list
import json

class Test_Views(TestCase):
    """
    Classe principale permettant d'exécuter les tests
    unitaires de l'application.
    """
    def setUp(self):
        self.client = Client()

    def test_add_rdv(self):
        response = self.client.get(reverse(add_rdv))
        self.assertEqual(response.status_code, 200)
    
    def test_rdv_delete(self):
        rdv = RDV.objects.create(
            comment="test",
        )
        rdv.save()
        response = self.client.get('/rdv_list/' + str(rdv.id) + '/delete')
        self.assertEqual(response.status_code, 302)

    def test_rdv_complete(self):
        rdv = RDV.objects.create(
            comment="test",
        )
        rdv.save()
        response = self.client.get('/complete_rdv/' + str(rdv.id))
        self.assertEqual(response.status_code, 302)

    def test_rdv_list(self):
        response = self.client.get(reverse(rdv_list))
        self.assertEqual(response.status_code, 200)