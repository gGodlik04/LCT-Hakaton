from rest_framework.decorators import action
from rest_framework import viewsets, mixins, status, views
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from tasks.models.tasks import Task
from tasks.serializers import TaskSerializer, CreateTaskSerializer


class TaskViewSet(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  mixins.DestroyModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.RetrieveModelMixin,
                  viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated, ]

    def get_serializer_class(self):
        if hasattr(self.request, 'method'):
            if self.request.method == 'GET':
                return TaskSerializer
            elif self.request.method == 'POST':
                return CreateTaskSerializer
            elif self.request.method == 'PUT':
                return TaskSerializer

    def get_queryset(self):
        queryset = Task.objects.all()
        return queryset

    def update(self, request, *args, **kwargs):
        task = self.get_object()
        serializer = task

        return Response(serializer)

    def list(self, request, *args, **kwargs):
        user = self.request.user
        queryset = self.get_queryset()

        if user.is_manager_user():
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data, status.HTTP_200_OK)
        else:
            queryset = self.filter_queryset(self.get_queryset())
            queryset = queryset.filter(employee=user)
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data, status.HTTP_200_OK)

    @action(methods=['get'], detail=False)
    def employee(self, request):
        user = self.request.user
        queryset = self.filter_queryset(self.get_queryset())

        if user.is_worker_user():
            queryset = queryset.filter(employee=user)
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        user = self.request.user

        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            if user.is_manager_user():
                self.perform_create(serializer)
                return Response('task created! status 200', status=status.HTTP_201_CREATED)
            else:
                return Response('you have no rights for that', status=status.HTTP_401_UNAUTHORIZED)

        return Response(status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, *args, **kwargs):
        task = self.get_object()
        serializer = self.get_serializer(task)
        return Response(serializer.data)

    @action(methods=['patch'], detail=True)
    def favorite(self, request, pk=None):

        task = self.get_object()
        data = {'favorite': request.data['favorite']}
        serializer = TaskSerializer(task, data=data, partial=True)

        if serializer.is_valid():
            self.perform_update(serializer)
            return Response(f'favorite was updated {data}', status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['patch'], detail=True)
    def status(self, request, pk=None):

        task = self.get_object()
        data = {'status': request.data['status']}
        serializer = TaskSerializer(task, data=data, partial=True)
        if serializer.is_valid():
            self.perform_update(serializer)
            return Response(f'status was updated {data} ', status.HTTP_200_OK)

