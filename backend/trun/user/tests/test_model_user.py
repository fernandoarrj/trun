from django.contrib.auth import authenticate, get_user_model
from django.test import TestCase


User = get_user_model()


def create_user(username='test@test.com', password='somepassword',
                **extra_fields):
    user = User.objects.create_user(username=username, password=password,
                                    **extra_fields)
    return user


class UserModelTest(TestCase):

    def test_can_create_a_user(self):
        create_user()
        self.assertEqual(User.objects.count(), 1)

    def test_save_password_correctly(self):
        user = create_user()
        self.assertTrue(user.check_password('somepassword'))

    def test_can_authenticate_by_email(self):
        user = create_user(password='somepassword')

        user = authenticate(
            username='test@test.com',
            password='somepassword'
        )

        self.assertNotEqual(user, None)
