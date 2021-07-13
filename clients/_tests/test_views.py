"""
Module permettant les tests unitaires
des urls de l'application.
"""
from clients.forms import NewClient, NewRace
from django.contrib.auth.models import User
from django.http import request
from django.http.response import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.models import AnonymousUser, User
from django.test import TestCase, RequestFactory, Client
from django.urls import reverse, resolve
from django.core.paginator import Page
from django.contrib import auth
from ..models import Chien, Race, Client as cust
from ..views import add_client, clients, save_client, save_dog, add_dog, add_race, dogs
from ..services import get_client, get_clients, get_clients_context, get_dogs, get_dogs_context, get_new_client_form, get_new_race_form, manage_super_context, save_client_context
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
		customer = cust.objects.create(
			nom = "Dupont",
			prenom = "Jean"
		)
		self.client = Client()
		self.factory = RequestFactory()

	def test_clients(self):
		response = self.client.get(reverse(clients))
		self.assertEqual(response.status_code, 302)

	def test_clients_login(self):
		user = User.objects.create_user(
			username = 'user',
			password = '123'
		)
		user.save()
		self.client.login(username="user", password="123")
		response = self.client.get(reverse(clients))
		self.assertEqual(response.status_code, 200)
		
	def test_get_client(self):
		customer = cust.objects.create(
			nom = "Dupont",
			prenom = "Jean"
		)
		self.assertEqual(get_client(2), customer)
	
	def test_get_clients(self):
		customers = cust.objects.all()
		self.assertQuerysetEqual(customers, customers)
	
	def save_dog(self):
		response = self.client.get(reverse(save_dog))
		self.assertEqual(response.status_code, 302)
		self.save_dog_template(response)

	def save_dog_login(self):
		user = User.objects.create_user(
			username = 'user',
			password = '123'
		)
		user.save()
		self.client.login(username="user", password="123")
		response = self.client.get(reverse(save_dog))
		self.assertEqual(response.status_code, 200)
		self.save_dog_template(response)
		response = self.client.post(reverse(save_dog))
		self.assertEqual(response.status_code, 200)
	
	def save_dog_template(self, response):
		self.assertTemplateUsed(response, 'frontpage/base.html')

	def add_dog(self):
		response = self.client.get(reverse(add_dog))
		self.assertEqual(response.status_code, 302)
		self.add_dog_template(response)
	
	def add_dog_login(self):
		user = User.objects.create_user(
			username = 'user',
			password = '123'
		)
		user.save()
		self.client.login(username="user", password="123")
		response = self.client.get(reverse(add_dog))
		self.assertEqual(response.status_code, 200)
		self.add_dog_template(response)
	
	def add_dog_template(self, response):
		self.assertTemplateUsed(response, 'frontpage/base.html')

	def add_race(self):
		response = self.client.get(reverse(add_race))
		self.assertTemplateUsed(response, 'frontpage/base.html')
		self.assertEqual(response.status_code, 302)
		self.add_race_template(response)
	
	def add_race_login(self):
		user = User.objects.create_user(
			username = 'user',
			password = '123'
		)
		user.save()
		self.client.login(username="user", password="123")
		response = self.client.get(reverse(add_race))
		self.assertTemplateUsed(response, 'frontpage/base.html')
		self.assertEqual(response.status_code, 302)
		self.add_race_template(response)
	
	def add_race_template(self, response):
		self.assertTemplateUsed(response, 'frontpage/base.html')
		self.assertTemplateUsed(response, "clients/add_race.html")

	def dogs(self):
		response = self.client.get(reverse(dogs))
		self.assertTemplateUsed(response, 'frontpage/base.html')
		self.assertEqual(response.status_code, 200)
		self.dogs_template(response)
		self.assertEqual(dogs["render"], "clients/clients.html")
	
	def dogs_login(self):
		user = User.objects.create_user(
			username = 'user',
			password = '123'
		)
		user.save()
		self.client.login(username="user", password="123")
		response = self.client.get(reverse(dogs))
		self.assertTemplateUsed(response, 'frontpage/base.html')
		self.assertEqual(response.status_code, 200)
		self.dogs_template(response)
		self.assertEqual(dogs["render"], "clients/clients.html")
	
	def dogs_template(self, response):
		self.assertTemplateUsed(response, 'frontpage/base.html')

	def test_manage_super_context_false(self):
		super_context = {
			"redirect": None,
			"render": None,
			"context": None
		}
		self.assertFalse(manage_super_context(super_context), 1)
	
	def test_save_client(self):
		response = self.client.get(reverse(save_client))
		self.assertEqual(response.status_code, 302)
	
	def test_add_client(self):
		response = self.client.get(reverse(add_client))
		self.assertEqual(response.status_code, 302)

	def test_add_client_login(self):
		user = User.objects.create_user(
			username = 'user',
			password = '123'
		)
		user.save()
		self.client.login(username="user", password="123")
		response = self.client.get(reverse(add_client))
		self.assertEqual(response.status_code, 200)
	
	def test_delete_client(self):
		customer = cust.objects.create(
			nom="Dupont",
			prenom="Jean",
			adresse="Paris",
			num="010101",
		)
		customer.save()
		response = self.client.get('/clients/' + str(customer.id) + '/delete')
		self.assertEqual(response.status_code, 302)
		response = self.client.post('/clients/' + str(customer.id) + '/delete')
		self.assertEqual(response.status_code, 302)

	def test_client_edit(self):
		customer = cust.objects.create(
			nom="Dupont",
			prenom="Jean",
			adresse="Paris",
			num="010101",
		)
		customer.save()
		response = self.client.get('/clients/' + str(customer.id) + '/edit')
		self.assertEqual(response.status_code, 302)
		response = self.client.post('/clients/' + str(customer.id) + '/edit')
		self.assertEqual(response.status_code, 302)

	def test_client_edit_login(self):
		user = User.objects.create_user(
			username = 'user',
			password = '123'
		)
		user.save()
		self.client.login(username="user", password="123")
		customer = cust.objects.create(
			nom="Dupont",
			prenom="Jean",
			adresse="Paris",
			num="010101",
		)
		customer.save()
		customer = cust.objects.create(
			nom="Dupont",
			prenom="Jean",
			adresse="Paris",
			num="010101",
		)
		customer.save()
		response = self.client.get('/clients/' + str(customer.id) + '/edit')
		self.assertEqual(response.status_code, 200)
	
	def test_get_clients_context(self):
		request = self.factory.get('/clients')
		response = get_clients_context(request)
		self.assertEqual(response["redirect"], None)
	
	def test_get_dogs_context(self):
		request = self.factory.get('/dogs')
		response = get_dogs_context(request)
		self.assertEqual(response["redirect"], None)

	def test_save_client_context(self):
		request = self.factory.get('/save_client')
		response = save_client_context(request)
		self.assertEqual(response, None)