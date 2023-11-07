from django.contrib.auth import login
from django.contrib.auth.models import AnonymousUser

from rest_framework import viewsets, permissions, mixins
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from accounts.serializers import UserSerializer
from .models import User


class UserView(viewsets.GenericViewSet, mixins.RetrieveModelMixin):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def retrieve(self, request, *args, **kwargs):
        pass

    def list(self):
        pass
