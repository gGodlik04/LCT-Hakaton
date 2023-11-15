from rest_framework import routers

from graphs.views import *

router = routers.DefaultRouter()
router.register('', ChartView, basename='chart')

urlpatterns = router.urls

