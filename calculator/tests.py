import json

from django.test import TestCase
from unittest.mock import patch, MagicMock

from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from rest_framework.test import APIRequestFactory, force_authenticate, APITestCase

from .factory import resultFactory
from .models import result
from calculator.views import func
from .serializers import serializeResult
from dataCluster.views import cluster
from calculator import views
import pytest

# Create your tests here.

@pytest.fixture
def input_value():
    input = 39
    return input

def test_divisible_by_3(input_value):
    assert input_value % 3 == 0

class ResgisterTestCase(APITestCase):
    def test_registeration(self):
        data = {"username":"apurva12345","password":"qwerty12345","email":"abc@abcd.in"}
        response = self.client.post('/api/register',data)
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)
        #data = {"username":"apurva12345","password":"qwerty12345","email":"abc1235@abc.in"}
        #response = self.client.post('/api/register',data)
        #elf.assertEqual(response.status_code,status.HTTP_400_BAD_REQUEST)
        
        
class LoginTestCase(APITestCase):
    fixtures = ['../shadowfax/user.json','../shadowfax/test.json']
    url = '/calc'
    def setUp(self):
        self.user = User.objects.create_user(username="apurva12",password="qwerty123")
        self.token = Token.objects.create(user=self.user)
        self.api_authentication()

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token "+ self.token.key)
    
    def test_auth(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code,status.HTTP_200_OK)
    
    def test_calc(self):
        data = {"num1":4,"num2":2}
        response = self.client.delete(self.url,data)
        self.assertEqual(float(response.content.decode("utf-8")),2.0)
    def test_calc_mock(self):
        with patch('calculator.views.requests.get') as mocked_get:
            mocked_get.return_value = 'good'
            data = {"num1":4,"num2":2}
            response = self.client.post(self.url,data)
            mocked_get.assert_called_with('https://jsonplaceholder.typicode.com/todos/1')
            self.assertEqual(response.content.decode("utf-8"),'good')

    '''def tearDown():
        self.result.delete()'''