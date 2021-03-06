import secrets

from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

from rest_framework.authtoken.models import Token


User = get_user_model()


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValidationError('This field is required')

        user = User.objects.create(email=self.normalize_email(email),
                                   **extra_fields)
        user.set_password(password)
        user.save()
        return user


class User(AbstractBaseUser):
    email = models.EmailField()

    objects = UserManager()

    USERNAME_FIELD = 'email'


class UserToken(Token):
    key = models.CharField(max_length=128, primary_key=True,
                           unique=True)

    def generate_key(self):
        return secrets.token_hex(64)
