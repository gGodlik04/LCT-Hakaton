from django.contrib import admin
from rest_framework import routers
from django.urls import path, include
from tasks.views import *

router = routers.DefaultRouter()
router.register(r'task', TaskViewSet, basename='Task')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('Backend.api_urls'))
]

