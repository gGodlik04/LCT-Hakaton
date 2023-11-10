from directories.views import TaskTypeViewSet, AgentPointViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('agent_points', AgentPointViewSet, basename='agent points')
router.register('task_types', TaskTypeViewSet, basename='task types')

urlpatterns = router.urls

