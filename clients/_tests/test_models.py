from django.test import TestCase, Client, RequestFactory
from django.urls import reverse, resolve
from django.contrib.auth.models import User
from django.contrib import auth
from ..models import Client, Race, Chien

class Test_Models(TestCase):
    def test_dog_save_in_db(self):
        chien = Chien.objects.create(nom="Kiki")
        self.assertIs(chien.nom, "Kiki")

    def test_dog_race_save_in_db(self):
        race = Race.objects.create(race="Spitz")
        chien = Chien.objects.create(nom="Jules", race=race)
        self.assertIs(chien.race, race)
        self.assertIs(chien.nom, "Jules")

    def test_client_save_in_db(self):
        race = Race.objects.create(race="Spitz")
        chien = Chien.objects.create(nom="Jules", race=race)
        client = Client.objects.create(
            prenom="Jean",
            nom="Dupont",
            num="01010101",
            adresse="Paris",
        )
        self.assertIs(chien.race, race)
        self.assertIs(chien.nom, "Jules")
        self.assertIs(client.nom, "Dupont")
        self.assertIs(client.adresse, "Paris")