from rest_framework.decorators import action
from rest_framework import generics, viewsets, mixins, status
from rest_framework.response import Response
from worker.models import Task
from worker.serializers import TaskSerializer, CreateTaskSerializer


class TaskViewSet(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  mixins.DestroyModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.RetrieveModelMixin,
                  viewsets.GenericViewSet):
    def get_serializer_class(self):
        if self.action == 'list':
            return TaskSerializer
        elif self.action == 'create':
            return CreateTaskSerializer
        return TaskSerializer

    def get_queryset(self):
        queryset = Task.objects.all()
        return queryset

    def update(self, request, *args, **kwargs):
        task = self.get_object()
        serializer = task
        return Response(serializer)

    def list(self, request, *args, **kwargs):

        queryset = self.filter_queryset(self.get_queryset())
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

