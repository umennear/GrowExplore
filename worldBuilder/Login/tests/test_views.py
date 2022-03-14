from django.test import TestCase, Client
##from django.urls import reverse
##from budget.models import Project, Category, Expense
import json

class TestViews(TestCase):
    def test_mainPage_GET(self):
       client = Client()
       response = client.get('/')
       self.assertEquals(response.status_code, 200)
       self.assertTemplateUsed(response, 'homepage.html')
    def test_login_GET(self):
           client = Client()
           response = client.get('/login/')
           self.assertEquals(response.status_code, 200)
           self.assertTemplateUsed(response, 'login.html')
    def test_register_GET(self):
           client = Client()
           response = client.get('/register/')
           self.assertEquals(response.status_code, 200)
           self.assertTemplateUsed(response, 'register.html')
