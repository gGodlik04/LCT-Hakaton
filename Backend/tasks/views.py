from rest_framework.decorators import action
from rest_framework import generics, viewsets, mixins, status, views
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from tasks.models import Task
from tasks.serializers import TaskSerializer, CreateTaskSerializer


class MixTasksAPIView(views.APIView):

    def get(self, request):

        return Response({'text': 'created'}, status.HTTP_200_OK)

    def post(self,request):
        pass


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
            elif self.request.method == 'UPDATE':
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
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)

        if user.is_worker_user():
            queryset = queryset.filter(employee=user)
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)

        return Response(serializer.data)

    def create(self, request, *args, **kwargs):

        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            self.perform_create(serializer)
            return Response('task created! status 200', status=status.HTTP_201_CREATED)

    def retrieve(self, request, *args, **kwargs):
        task = self.get_object()
        serializer = self.get_serializer(task)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        pass
