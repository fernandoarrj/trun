from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models


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
