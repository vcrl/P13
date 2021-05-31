from django.test import TestCase, RequestFactory, Client, client
from django.urls import reverse, resolve
from django.core.paginator import Page
from django.contrib import auth
from ..models import Employee
from ..views import employees, employee_edit, employee_delete, save_employee
import json

class Test_Views(TestCase):
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

    def test_employee_edit(self):
        employee = Employee.objects.create(
            nom="Dupont",
            prenom="Jean",
            adresse="Paris",
            num="010101",
        )
        employee.save()
        response = self.client.get('/employees/' + str(employee.id) + '/edit')
        self.assertEqual(response.status_code, 200)