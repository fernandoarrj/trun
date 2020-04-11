from django.contrib.auth import authenticate
from django.utils.translation import ugettext_lazy as _

from rest_framework import generics
from rest_framework.exceptions import ParseError
from rest_framework.response import Response

from user.models import UserToken


class UserTokenObtainKeyView(generics.CreateAPIView):

    def post(self, request, *args, **kwargs):
        username = request.data['username']
        password = request.data['password']

        user = authenticate(
            username=username,
            password=password,
        )

        if user:
            token, __ = UserToken.objects.get_or_create(user=user)
            return Response({'key': token.key})
        msg = {'detail': _('Wrong credentials.')}
        raise ParseError(detail=msg)
