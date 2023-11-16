from django.shortcuts import render
from django.db.models import Count, Avg

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated

from tasks.models import Task


class ChartView(viewsets.GenericViewSet):
    queryset = Task.objects.all()
    permission_classes = [IsAuthenticated]

    @action(methods=['get'], detail=False)
    def easy_chart(self, request):
        x = Task.objects.aggregate(Avg('status'))
        return Response(x)

