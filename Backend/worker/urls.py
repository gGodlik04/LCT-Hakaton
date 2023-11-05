from rest_framework import routers
from worker.views import *
from django.urls import path, re_path, include

router = routers.DefaultRouter()

router.register('tasks', TasksViewSet, basename='tasks')

urlpatterns = [
    path('', include(router.urls))
]
