import json

from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from session.models import Session
from Event.models import Event
from session.tests import CreateTestSession

class CreateTestEvent(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User(username="testuser", email="testemail@test.com")
        self.user.is_staff = True
        self.user.set_password('secret')
        self.user.save()

    def test_create_event(self):
        self.assertTrue(self.client.login(username="testuser", password="secret"))
        url = 'http://127.0.0.1:8000/api/event/create'
        data2={
            'name':'denem1',
            'start_date':'2020-06-15',
            'end_date':'2020-07-17',
            'timezone':'Iran',
            'session_id':Session.pk
        }
        response = self.client.post(url,data2,format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_event(self):
        url='http://127.0.0.1:8000/api/event/create'
        response=self.client.get(url)
        self.test_create_event()
        self.assertEqual(len(json.loads(response.content)["result"]),1)

