
"""
Module permettant les tests unitaires
des vues de l'application.
"""
from django.test import SimpleTestCase
from django.urls import resolve, reverse
from ..views import add_employee, employee_delete, employee_edit, employees, save_employee
import re

class Test_Urls(SimpleTestCase):
    """
    Classe principale permettant d'exécuter les tests
    unitaires de l'application.
    """
    def test_add_employee(self):
        url = reverse('add_employee')
        self.assertEquals(resolve(url).func, add_employee)

    def test_employee_delete(self):
        url = r'/employees/\d+/delete/'
        url_to_test = '/employees/1/delete/'
        self.assertTrue(re.match(url, url_to_test))

    def test_employee_edit(self):
        url = r'/employees/\d+/edit/'
        url_to_test = '/employees/1/edit/'
        self.assertTrue(re.match(url, url_to_test))
    
    def test_employees(self):
        url = reverse('employees')
        self.assertEquals(resolve(url).func, employees)

    def test_save_employee(self):
        url = reverse('save_employee')
        self.assertEquals(resolve(url).func, save_employee)