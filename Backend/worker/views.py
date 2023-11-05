from rest_framework.decorators import action
from rest_framework import generics, viewsets, mixins, status
from rest_framework.response import Response
from worker.models import Task
from worker.serializers import TaskSerializer


class TaskViewSet(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  mixins.DestroyModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.RetrieveModelMixin,
                  viewsets.GenericViewSet):
    serializer_class = TaskSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = Task.objects.filter(employee=user)
        return queryset

    def update(self, request, *args, **kwargs):
        task = self.get_object()
        serializer = task
        return Response(serializer)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        queryset = queryset.filter(employee=self.request.user)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, *args, **kwargs):
        task = self.get_object()
        serializer = self.get_serializer(task)
        return Response(serializer.data)
