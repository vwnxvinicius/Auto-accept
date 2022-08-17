from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.test import Client

class StatusCodeTest(TestCase):
    def test_home_status_code(self):
        c = Client()
        resp = c.get('')
        self.assertEqual(resp.status_code, 200, 'Erro ao acessar a página')
    def test_clicker_status_code(self):
        c = Client()
        resp = c.get('/clicker')
        self.assertEqual(resp.status_code, 200, 'Erro ao acessar a página')
    def test_check_data_status_code(self):
        c = Client()
        resp = c.get('/check_values')
        self.assertEqual(resp.status_code, 200, 'Erro ao acessar a página')