from django.contrib import admin
from django.urls import path, re_path

from api.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('api/hello/', HelloAPIView.as_view(), name='test'),
]

