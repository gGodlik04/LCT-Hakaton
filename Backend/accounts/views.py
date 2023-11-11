from rest_framework import viewsets, permissions, mixins
from rest_framework.response import Response

from accounts.serializers import UserSerializer
from .models import User


class UserView(viewsets.GenericViewSet,
               mixins.RetrieveModelMixin,
               mixins.ListModelMixin,
               mixins.UpdateModelMixin,
               mixins.CreateModelMixin):

    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [permissions.IsAuthenticated, ]
