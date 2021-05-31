from employes.views import employees
from django.test import TestCase, Client, RequestFactory
from django.urls import reverse, resolve
from django.contrib.auth.models import User
from django.contrib import auth
from ..models import Employee

class Test_Models(TestCase):
    def test_employee_save_in_db(self):
        employee = Employee.objects.create(
            nom="Dupont",
            prenom="Jean",
            adresse="Paris",
            num="010101",
            rdv_number="0",
            joined="1990-01-01 00:00"
            )
        self.assertIs(employee.nom, "Dupont")
        self.assertIs(employee.prenom, "Jean")
        self.assertIs(employee.adresse, "Paris")
        self.assertIs(employee.num, "010101")
        self.assertIs(employee.rdv_number, "0")
        self.assertIs(employee.joined, "1990-01-01 00:00")