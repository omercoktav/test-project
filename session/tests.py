import json

from django.contrib.auth.models import User
from django.test import Client

from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase,APIClient

import session
from session.models import Session

class CreateTestSession(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User(username="testuser", email="testemail@test.com")
        self.user.is_staff = True
        self.user.set_password('secret')
        self.user.save()
    def test_create_session(self):
        self.assertTrue(self.client.login(username="testuser", password="secret"))
        url = 'http://127.0.0.1:8000/api/session/create'
        data={
            'name':'ahmet2',
            'start_date':'2020-05-26',
            'end_date':'2020-05-29',
            'speaker':'mustafa'
        }
        response = self.client.post(url,data,format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_session_list(self):
        self.test_create_session()
        url="http://127.0.0.1:8000/api/session/list"
        response=self.client.get(url)
        print(len(json.loads(response.content)['results']))
        self.assertTrue(len(json.loads(response.content)['results']) == 1)

    def test_session_UpdateDelete(self):
        self.assertTrue(self.client.login(username="testuser", password="secret"))
        session1=Session.objects.create(name="asdasd",start_date="2020-05-20",end_date="2020-05-25",speaker="mehmet")
        url=reverse('session:delete',kwargs={"slug":session1.slug})
        response=self.client.delete(url)
        self.assertEqual(204,response.status_code)