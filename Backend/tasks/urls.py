from rest_framework import routers

from tasks.views import *

router = routers.DefaultRouter()
router.register('task', TaskViewSet, basename='task')

urlpatterns = router.urls
