from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.test import APITestCase

from user.models import UserToken


User = get_user_model()
USER_TOKEN_URL = '/api/v1/user/token/'


class UserTokenAPITest(APITestCase):

    def setUp(self):
        self.username = 'test@test.com'
        self.password = 'somepassword'
        self.user = User.objects.create_user(
            username=self.username,
            password=self.password
        )

    def test_can_get_key_if_credentials_are_correct(self):
        data = {
            'username': self.username,
            'password': self.password,
        }

        resp = self.client.post(USER_TOKEN_URL, data)
        token = UserToken.objects.get(user=self.user)

        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(resp.data['key'], token.key)

    def test_cannot_get_key_if_credentials_are_incorrect(self):
        data = {
            'username': 'wrong_user',
            'password': 'wrong_password',
        }

        resp = self.client.post(USER_TOKEN_URL, data)

        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)
