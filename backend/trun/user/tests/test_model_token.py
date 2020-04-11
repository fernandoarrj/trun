from django.contrib.auth import get_user_model
from django.db.utils import IntegrityError
from django.utils import timezone
from django.test import TestCase

from user.models import UserToken


User = get_user_model()


class UserTokenModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user('test@test.com', 'somepassword')

    def test_can_create_a_model(self):
        token = UserToken()
        token.user = self.user
        token.save()

        self.assertEqual(UserToken.objects.count(), 1)

    def test_token_has_created_field(self):
        token = UserToken()
        token.user = self.user
        token.save()

        now = timezone.now().replace(microsecond=0)
        created = token.created.replace(microsecond=0)

        self.assertEqual(created, now)

    def test_token_has_a_key(self):
        token = UserToken()
        token.user = self.user
        token.save()

        self.assertTrue(token.key)

    def test_token_key_has_length_128(self):
        token = UserToken()
        token.user = self.user
        token.save()

        self.assertEqual(len(str(token.key)), 128)

    def test_token_has_unique_key(self):
        token = UserToken()
        token.key = '123'
        token.user = self.user
        token.save()

        token = UserToken()
        token.user = self.user
        token.key = '123'
        with self.assertRaises(IntegrityError):
            token.save()

            self.assertEqual(UserToken.objects.count(), 1)
