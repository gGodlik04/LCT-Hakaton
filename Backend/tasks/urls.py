from rest_framework import routers

from tasks.views import *
from django.urls import path, include

router = routers.DefaultRouter()
router.register('task', TaskViewSet, basename='task')

urlpatterns = [
    path('', include(router.urls)),
    path('', MixTasksAPIView.as_view(), name='send tasks to workers')
]
