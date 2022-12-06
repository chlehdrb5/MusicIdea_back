from django.test import TestCase, Client
# Create your tests here.
from user.models import User


class UserTestClass(TestCase):
    def test_signup(self):
        client = Client()
        response = client.post('/user/signup', {'name': 'test1', 'password': 'tester123'})
        self.assertEqual('test1', response.json()['user'])
