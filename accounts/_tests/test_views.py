from accounts.views import displayprofile
from django.test import TestCase, Client
from django.urls import reverse, resolve
from django.contrib.auth.models import User
from django.contrib import auth
from ..forms import SignUpForm, LoginForm
import json

class Test_Views(TestCase):
    def init(self):
        self.client = Client()

    def test_signup_get(self):
        response = self.client.get(reverse('signup'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/signup.html')

    def test_signup_post(self):
        response = self.client.post(reverse('signup'), {
            'username': 'pseudo',
            'email': 'test@test.fr',
            'password1': '123',
            'password2': '123'
        })

        self.assertEquals(response.status_code, 302)
        self.assertEquals(User.objects.count(), 1)

    def test_loginuser_get(self):
        response = self.client.get(reverse('loginuser'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/signin.html')

    def test_loginuser_post(self):
        self.credentials = {
            'username': 'user',
            'password': '123'
            }
        User.objects.create_user(**self.credentials)
        response = self.client.post(reverse('loginuser'), self.credentials, follow=True)
        self.assertTrue(response.context['user'].is_active)

    def test_loginuser_post_nouser(self):
        self.credentials = {
            'username': 'skslslslsqkl',
            'password': '000'
            }
        response = self.client.post(reverse('loginuser'), self.credentials, follow=True)
        self.assertTemplateUsed(response, 'accounts/signin.html')

    def test_signoutuser(self):
        self.credentials = {
            'username': 'user',
            'password': '123'
            }
        User.objects.create_user(**self.credentials)
        response = self.client.post(reverse('loginuser'), self.credentials, follow=True)
        response = self.client.post(reverse('signout'), self.credentials, follow=True)
        self.assertEquals(response.status_code, 200)
    
    def test_return_to_frontpage(self):
        response = self.client.get(reverse('frontpage'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'frontpage/index.html')
        self.assertTemplateUsed(response, 'frontpage/base.html')
        