from django.shortcuts import render

from rest_framework import generics
from rest_framework import viewsets
from rest_framework import views
from rest_framework.response import Response


class HelloAPIView(views.APIView):
    def get(self, request):
        return Response({'title': 'Hello pedik edik!'})



