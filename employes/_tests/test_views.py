"""
Module permettant les tests unitaires
des vues de l'application.
"""
from django.test import TestCase, RequestFactory, Client, client
from django.contrib.auth.models import User

from django.urls import reverse, resolve
from django.core.paginator import Page
from django.contrib import auth
from ..models import Employee
from ..views import add_employee, employees, employee_edit, employee_delete, save_employee
import json

class Test_Views(TestCase):
    """
    Classe principale permettant d'exécuter les tests
    unitaires de l'application.
    """
    def setUp(self):
        employee = Employee.objects.create(
            nom="Dupont",
            prenom="Jean",
            adresse="Paris",
            num="010101",
        )
        employee.save()
        self.client = Client()

    def test_employees(self):
        response = self.client.get(reverse(employees))
        self.assertEqual(response.status_code, 302)
    
    def test_employees_login(self):
        user = User.objects.create_user(
            username = 'user',
            password = '123'
        )
        user.save()
        self.client.login(username="user", password="123")
        response = self.client.get(reverse(employees))
        self.assertEqual(response.status_code, 200)
    
    def test_delete_employee(self):
        employee = Employee.objects.create(
            nom="Dupont",
            prenom="Jean",
            adresse="Paris",
            num="010101",
        )
        employee.save()
        response = self.client.get('/employees/' + str(employee.id) + '/delete')
        self.assertEqual(response.status_code, 302)

    def test_delete_employee_login(self):
        user = User.objects.create_user(
            username = 'user',
            password = '123'
        )
        user.save()
        self.client.login(username="user", password="123")
        employee = Employee.objects.create(
            nom="Dupont",
            prenom="Jean",
            adresse="Paris",
            num="010101",
        )
        employee.save()
        response = self.client.get('/employees/' + str(employee.id) + '/delete')
        self.assertEqual(response.status_code, 302)

    def test_employee_edit(self):
        employee = Employee.objects.create(
            nom="Dupont",
            prenom="Jean",
            adresse="Paris",
            num="010101",
        )
        employee.save()
        response = self.client.get('/employees/' + str(employee.id) + '/edit')
        self.assertEqual(response.status_code, 302)
    
    def test_employee_edit_login(self):
        employee = Employee.objects.create(
            nom="Dupont",
            prenom="Jean",
            adresse="Paris",
            num="010101",
        )
        employee.save()
        user = User.objects.create_user(
            username = 'user',
            password = '123'
        )
        user.save()
        self.client.login(username="user", password="123")
        response = self.client.get('/employees/' + str(employee.id) + '/edit')
        self.assertEqual(response.status_code, 200)

    def test_add_employee(self):
        response = self.client.get(reverse(add_employee))
        self.assertEqual(response.status_code, 302)
    
    def test_add_employee_login(self):
        user = User.objects.create_user(
            username = 'user',
            password = '123'
        )
        user.save()
        self.client.login(username="user", password="123")
        response = self.client.get(reverse(add_employee))
        self.assertEqual(response.status_code, 200)

    def test_save_employee(self):
        response = self.client.post(reverse(save_employee))
        self.assertEqual(response.status_code, 302)
