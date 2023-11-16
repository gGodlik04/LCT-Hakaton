from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticated
from .models import TaskTypeModel, AgentPointModel
from .serializers import AgentPointSerializer, TaskTypeSerializer


class AgentPointViewSet(viewsets.GenericViewSet,
                        mixins.ListModelMixin,
                        mixins.DestroyModelMixin,
                        mixins.CreateModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin):
    
    permission_classes = [IsAuthenticated, ]
    queryset = AgentPointModel.objects.all()
    serializer_class = AgentPointSerializer


class TaskTypeViewSet(viewsets.GenericViewSet,
                      mixins.ListModelMixin,
                      mixins.CreateModelMixin,
                      mixins.RetrieveModelMixin):
    permission_classes = [IsAuthenticated, ]
    queryset = TaskTypeModel.objects.all()
    serializer_class = TaskTypeSerializer
